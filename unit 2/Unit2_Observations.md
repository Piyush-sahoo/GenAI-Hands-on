Unit 2 Observations & Notes
Generative AI Concepts & LangChain

This unit introduced the practical foundations of building applications using Large Language Models. Through the notebooks and assignment, I explored LangChain workflows, prompt engineering techniques, reasoning strategies, Retrieval-Augmented Generation (RAG), and the Mixture of Experts (MoE) architecture.

1. LangChain Foundation
Why LangChain

LangChain acts as a standard interface between code and different LLM providers. Without it, switching models would require rewriting API logic. With LangChain, only the model configuration needs to change.

Observation: LangChain simplifies LLM integration and makes applications provider-agnostic.

Tokens & Context

LLMs process tokens instead of words. Tokens represent parts of words, spaces, or symbols.

Observations:

Cost is based on number of tokens.

Models have context limits.

Long inputs can cause early context to be forgotten.

Temperature Experiment

Two models were tested:

Temperature = 0 → consistent and deterministic

Temperature = 1 → creative and varied

Observation:
Temperature controls randomness in output. Lower values improve consistency, while higher values increase creativity.

Prompt Templates & LCEL

Prompt templates allow structured inputs. LCEL (LangChain Expression Language) connects components into a pipeline.

Observation:
LCEL simplifies building pipelines:
Input → Prompt → Model → Parser → Output.

Conclusion: LCEL improves modularity and scalability of LLM applications.

2. Prompt Engineering Basics
Role Prompting (System / User)

System messages control behavior and tone.

Observation:
Changing the system role can completely alter the personality and tone of the response.

Structured Prompt vs Lazy Prompt

A simple prompt produced generic output, while a structured prompt controlled:

tone

length

content

format

Observation:
Ambiguity leads to generic responses. Structured prompts improve precision.

Hallucination vs Missing Context

When instructions lack detail, the model fills gaps using probability.

Observation:
Hallucinatory details often result from incomplete instructions.

Zero-Shot vs Few-Shot Prompting
Zero-shot

Model answers based only on prior training.

Few-shot

Providing examples improved:

structure

tone

pattern matching

Observation:
Few-shot prompting guides the model using patterns from examples.

Dynamic Few-Shot Prompting

Using example templates helps the model match tone and style.

Observation:
Providing curated examples improves consistency and professional tone.

3. Advanced Prompting
Chain of Thought (CoT)

Prompting the model to “think step by step” improved reasoning accuracy.

Observation:

Direct answers may skip logic.

Step-by-step reasoning improves correctness.

Conclusion: CoT enhances logical reasoning by generating intermediate steps.

Tree of Thoughts (ToT)

Multiple solutions were generated and evaluated before selecting the best.

Observation:

Exploring multiple solutions improves decision quality.

A judging step helps select sustainable solutions.

Graph of Thoughts (GoT)

Different ideas were generated and combined into one refined output.

Observation:

Combining multiple perspectives produces richer and more creative outputs.

Comparison
Method	Best For
Simple Prompt	facts & summaries
CoT	logic & reasoning
ToT	decision making
GoT	creative synthesis
4. RAG & Vector Stores
Embeddings

Text is converted into vectors representing meaning.

Observation:
Similar words have vectors that are closer together.

Cosine Similarity

Similarity between vectors is measured using cosine similarity.

Observation:

Cat & Dog → high similarity

Cat & Car → lower similarity

This mathematical similarity enables semantic search.

FAISS Vector Store

Documents were converted into embeddings and stored in FAISS for fast retrieval.

Observation:
Vector databases enable semantic search instead of keyword search.

RAG Pipeline

Pipeline:

User Query → Retrieve Relevant Documents → Inject Context → Generate Answer

Observation:

RAG retrieves facts before answering.

Prevents hallucinations.

Provides grounded responses.

Indexing Algorithms

Different FAISS indexing methods balance speed, accuracy, and memory.

Index	Key Idea	Benefit
Flat	brute force	perfect accuracy
IVF	clustering	faster search
HNSW	graph search	very fast retrieval
PQ	compression	reduced memory

Observation:
Large-scale vector search requires optimized indexing.

5. Assignment: Mixture of Experts (MoE) Router
Concept

Instead of one general AI, specialized experts handle different tasks.

Experts created:

Technical expert

Billing expert

General support expert

Router Function

The router classifies user intent and selects the appropriate expert.

Observation:
Routing improves relevance by matching queries with domain-specific expertise.

Expert Responses

Different system prompts created domain-specific tone and responses.

Technical → precise & code-focused

Billing → empathetic & policy-driven

General → friendly & informative

Orchestration Flow

User Query → Router → Expert Selection → Expert Response

Observation:
MoE architecture improves accuracy, clarity, and user experience.

Bonus: Tool Routing

Queries like cryptocurrency price can be routed to tools instead of LLM responses.

Observation:
Tool routing enables real-time data integration.

Final Learning Outcomes

Through this unit, I learned how modern AI applications are built using structured workflows and intelligent routing.

Key Skills Gained

✔ Prompt engineering & structured prompting
✔ Reasoning enhancement using CoT, ToT, and GoT
✔ Building RAG pipelines
✔ Understanding embeddings & vector search
✔ Implementing Mixture of Experts architecture
✔ Orchestrating LLM workflows using LangChain

Final Conclusion

Unit 2 demonstrated how advanced prompt engineering, retrieval mechanisms, and expert routing can significantly enhance the accuracy, reliability, and usability of LLM-powered applications. Instead of relying on a single general-purpose model, modern AI systems combine structured prompting, external knowledge retrieval, and specialized expert routing to deliver intelligent and context-aware responses.