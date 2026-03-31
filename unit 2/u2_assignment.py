import os
from groq import Groq
from dotenv import load_dotenv

# 1. Setup - Loads your API key from the .env file
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Define Your Experts
# We use different System Personas to simulate specialized experts.
MODEL_CONFIG = {
    "technical": {
        "system_prompt": "You are a Senior Software Engineer. Provide rigorous, code-focused, and precise solutions. Include code snippets where applicable.",
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.5
    },
    "billing": {
        "system_prompt": "You are a Billing Support Specialist. Be empathetic and professional. Focus on financial accuracy and company policy regarding refunds and subscriptions.",
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.3
    },
    "general": {
        "system_prompt": "You are a helpful and friendly general assistant. Keep answers concise and polite.",
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.7
    }
}

# 3. The Router (The Core Task)
def route_prompt(user_input):
    """
    Analyzes the user input and returns ONLY the category name.
    """
    routing_instructions = (
        "Classify the following user query into exactly one of these categories: "
        "[technical, billing, general]. "
        "Return ONLY the category name as a single word. Do not include punctuation."
    )
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": routing_instructions},
            {"role": "user", "content": user_input},
        ],
        model="llama-3.3-70b-versatile",
        temperature=0,  # Zero temperature ensures consistent routing logic
    )
    
    # Clean the output to ensure it matches our dictionary keys
    category = response.choices[0].message.content.lower().strip()
    
    # Fallback safety check
    if category not in MODEL_CONFIG:
        return "general"
    return category

# 4. The Orchestrator
def process_request(user_input):
    """
    Step 1: Route the request.
    Step 2: Initialize the correct expert.
    Step 3: Generate the final response.
    """
    # Identify the expert
    category = route_prompt(user_input)
    print(f"\n[SYSTEM LOG]: Routing to {category.upper()} expert...")
    
    # Fetch settings for that specific expert
    config = MODEL_CONFIG[category]
    
    # Call the Expert
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": config["system_prompt"]},
            {"role": "user", "content": user_input},
        ],
        model=config["model"],
        temperature=config["temperature"],
    )
    
    return response.choices[0].message.content

# --- Main Execution Block ---
if __name__ == "__main__":
    print("--- Smart Customer Support Router Active ---")
    
    test_queries = [
        "My python script is throwing an IndexError on line 5.",
        "I was charged twice for my subscription this month.",
        "Tell me a joke about robots."
    ]
    
    for query in test_queries:
        print(f"\nUSER: {query}")
        final_answer = process_request(query)
        print(f"EXPERT RESPONSE: {final_answer}")
        print("-" * 50)