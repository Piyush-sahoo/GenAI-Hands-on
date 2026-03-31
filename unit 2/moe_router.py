import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# You can override via .env: GROQ_MODEL=your_preferred_supported_model
BASE_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
VALID_CATEGORIES = {"technical", "billing", "sales", "general", "tool_use"}

MODEL_CONFIG = {
    "technical": {
        "model": BASE_MODEL,
        "system_prompt": (
            "You are a senior technical support engineer. "
            "Be precise, structured, and code-focused. "
            "Ask for logs only when necessary and provide step-by-step fixes."
        ),
        "temperature": 0.7,
    },
    "billing": {
        "model": BASE_MODEL,
        "system_prompt": (
            "You are a billing support specialist. "
            "Be empathetic, policy-driven, and clear about charges, refunds, and invoices. "
            "Avoid technical jargon unless needed."
        ),
        "temperature": 0.7,
    },
    "sales": {
        "model": BASE_MODEL,
        "system_prompt": (
            "You are a sales specialist. "
            "Understand customer goals, recommend suitable plans, and explain value clearly. "
            "Keep responses persuasive but honest."
        ),
        "temperature": 0.7,
    },
    "general": {
        "model": BASE_MODEL,
        "system_prompt": (
            "You are a helpful general support assistant. "
            "Be friendly, concise, and practical."
        ),
        "temperature": 0.7,
    },
    "tool_use": {
        "model": BASE_MODEL,
        "system_prompt": (
            "You are a tool-enabled assistant. "
            "When tool data is provided, explain it clearly and briefly."
        ),
        "temperature": 0.2,
    },
}


def _create_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Missing GROQ_API_KEY. Add it to your .env file.")
    return Groq(api_key=api_key)


def _normalize_category(raw: str) -> str:
    cleaned = raw.strip().lower()
    cleaned = cleaned.replace("-", "_").replace(" ", "_")
    cleaned = cleaned.replace(".", "").replace("`", "")
    if cleaned in VALID_CATEGORIES:
        return cleaned
    return "general"


def _keyword_fallback(user_input: str) -> str:
    text = user_input.lower()

    technical_keywords = [
        "error",
        "bug",
        "exception",
        "crash",
        "python",
        "api",
        "stack trace",
        "indexerror",
        "code",
    ]
    billing_keywords = [
        "charged",
        "charge",
        "invoice",
        "refund",
        "billing",
        "payment",
        "subscription",
        "receipt",
    ]
    sales_keywords = [
        "pricing",
        "plan",
        "trial",
        "upgrade",
        "features",
        "demo",
        "buy",
        "quote",
    ]
    tool_keywords = ["bitcoin", "btc", "crypto price", "current price"]

    if any(keyword in text for keyword in tool_keywords):
        return "tool_use"
    if any(keyword in text for keyword in technical_keywords):
        return "technical"
    if any(keyword in text for keyword in billing_keywords):
        return "billing"
    if any(keyword in text for keyword in sales_keywords):
        return "sales"
    return "general"


def route_prompt(user_input: str) -> str:
    """Classify the user request into one category name only."""
    client = _create_client()

    routing_system_prompt = (
        "You are a strict intent router.\n"
        "Classify the user text into exactly one category from this set:\n"
        "[technical, billing, sales, general, tool_use].\n"
        "Use tool_use only for live/factual price lookup requests (e.g., Bitcoin price).\n"
        "Return ONLY the category word. No punctuation, no explanation."
    )

    response = client.chat.completions.create(
        model=BASE_MODEL,
        temperature=0,
        max_tokens=8,
        messages=[
            {"role": "system", "content": routing_system_prompt},
            {"role": "user", "content": user_input},
        ],
    )

    raw_category = response.choices[0].message.content or ""
    category = _normalize_category(raw_category)

    if category not in VALID_CATEGORIES:
        return _keyword_fallback(user_input)

    # Guardrail in case the model returns unknown text.
    if category == "general" and raw_category.strip().lower() not in VALID_CATEGORIES:
        return _keyword_fallback(user_input)

    return category


def mock_fetch_bitcoin_price() -> str:
    """Bonus tool-use mock function."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    mocked_price = 68420.55
    return f"Bitcoin (BTC) mock spot price: ${mocked_price:,.2f} as of {now}."


def _ask_expert(category: str, user_input: str) -> str:
    config = MODEL_CONFIG.get(category, MODEL_CONFIG["general"])
    client = _create_client()

    response = client.chat.completions.create(
        model=config["model"],
        temperature=config["temperature"],
        messages=[
            {"role": "system", "content": config["system_prompt"]},
            {"role": "user", "content": user_input},
        ],
    )

    return (response.choices[0].message.content or "").strip()


def process_request(user_input: str) -> str:
    """Orchestrator:
    1) route prompt
    2) select expert configuration
    3) call expert model or tool
    4) return final response
    """
    category = route_prompt(user_input)

    if category == "tool_use":
        tool_data = mock_fetch_bitcoin_price()
        tool_context = (
            f"User asked: {user_input}\n"
            f"Tool output: {tool_data}\n"
            "Answer in a concise support style."
        )
        return _ask_expert("tool_use", tool_context)

    return _ask_expert(category, user_input)


if __name__ == "__main__":
    print("Smart Customer Support Router (MoE) - type 'exit' to quit")
    while True:
        user_query = input("\nYou: ").strip()
        if user_query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            intent = route_prompt(user_query)
            answer = process_request(user_query)
            print(f"Routed to: {intent}")
            print(f"Assistant: {answer}")
        except Exception as exc:
            print(f"Error: {exc}")
