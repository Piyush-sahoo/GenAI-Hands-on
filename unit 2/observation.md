# Unit 2 Observation Report

**Student Details:**
* **Name:** Abhishrut Kaushik
* **Section:** A
* **SRN:** PES2UG23CS023
* **Course:** GenAI Hands-on Unit 2

## 1. Notebook Coverage
* **1_LangChain_Foundation.ipynb:** Covers setup, tokens, temperature, prompt templates, output parsers, and LCEL chaining.
* **2_Prompt_Engineering.ipynb:** Covers prompt structure, CO-STAR, zero-shot, few-shot, and advanced prompt templates.
* **3_Advanced_Prompting.ipynb:** Covers Chain of Thought, Tree of Thoughts, and Graph of Thoughts.
* **4_RAG_and_Vector_Stores.ipynb:** Covers embeddings, cosine similarity, FAISS, RAG pipeline, and indexing algorithms.
* **Assignment_MOE.ipynb:** Covers Mixture of Experts routing, specialized prompts, orchestration, and tool-use extension.

## 2. LangChain Foundation
* LangChain acts as a framework layer sitting between the code and the model provider.
* It standardizes model access, making it easier to swap providers later without rewriting raw API logic.
* Tokens are the basic units read by the model, rather than full words.
* The context window dictates how much the model can remember in a single interaction.
* API keys must be loaded securely using tools like dotenv or getpass.
* A temperature of 0.0 makes the model focused, while 1.0 makes it creative.

## 3. Prompts, Roles, and LCEL
* Prompts can be heavily structured by role, template, and parser rather than just being raw text.
* System messages provide strong control over model behavior and personality.
* LCEL (LangChain Expression Language) connects the pipeline and acts like Unix piping for LLM workflows.
* The standard LCEL pipeline flows cleanly as: `template | llm | parser`.

## 4. Prompt Engineering and In-Context Learning
* Vague prompts yield generic answers, while structured prompts add context, constraints, and instructions for controlled outputs.
* The CO-STAR framework results in better clarity, less ambiguity, and consistent formatting.
* Few-shot prompting provides examples to help the model imitate patterns and match the desired tone.

## 5. Advanced Prompting: CoT, ToT, and GoT
* **Chain of Thought (CoT):** Best for linear, step-based problems where the model benefits from showing intermediate reasoning.
* **Tree of Thoughts (ToT):** Useful for generating multiple possible strategies and judging to select the best one.
* **Graph of Thoughts (GoT):** Ideal for merging several perspectives or branches into a stronger final answer.

## 6. RAG, Embeddings, and Vector Search
* Embeddings convert text into vectors mathematically to measure semantic similarity.
* RAG (Retrieval-Augmented Generation) acts like an open-book test, reducing hallucination by grounding answers in external data rather than relying only on memory.
* Cosine similarity measures the semantic closeness between vectors, explaining why concepts like "cat" and "dog" score closer than "cat" and "car".

## 7. Indexing and Mixture of Experts
* Brute-force similarity search (Flat) is often too expensive at scale.
* FAISS indexing algorithms (Flat, IVF, HNSW, PQ) optimize the tradeoffs between speed, accuracy, and memory efficiency.
* A Mixture of Experts (MoE) system uses a router to direct questions to the correct specialized expert behavior rather than simply retrieving documents.

## 8. Final Reflection
* Good GenAI systems are built as pipelines rather than relying on single prompts.
* Prompt quality directly dictates output quality.
* Reasoning structure is essential for complex tasks.
* Retrieval ensures freshness and heavily grounds the model's knowledge.
* Routing specializes behavior without needing to alter the underlying base model.