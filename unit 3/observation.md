# Unit 3 Observations

## 1) 1_Advanced_RAG_and_Retrieval.ipynb

### Key understanding
- Dense retrieval handles semantic matches better than strict keyword matching.
- BM25 is strong for lexical overlap and proper terms.
- Hybrid retrieval with RRF balances sparse and dense strengths.
- ColBERT-style late interaction improves fine-grained matching behavior.

### Output highlights
- Query-wise rankings were printed for Dense, BM25, and Hybrid methods.
- Hybrid ranking placed the most relevant neural-learning and BM25-related docs at top positions for corresponding queries.
- End-to-end retrieval plus response generation cells executed successfully.

## 2) 2_Reranking_and_Query_Expansion.ipynb

### Key understanding
- Two-stage retrieval is practical: bi-encoder for recall, cross-encoder for precision.
- Query expansion improves candidate quality when query wording is weak.
- Multi-query union retrieval increases coverage of relevant documents.
- Full pipeline structure is: Expansion -> Hybrid Retrieval -> Re-ranking -> Generation.

### Output highlights
- Stage 1 and Stage 2 scores clearly showed reranking impact.
- HyDE and Multi-Query cells executed with fallback because Gemini API requests returned ChatGoogleGenerativeAIError in this environment.
- Full pipeline runs produced grounded outputs from retrieved context even when fallback generation was used.

## 3) 3_Generation_Enhancement.ipynb

### Key understanding
- LoRA reduces trainable parameters significantly while preserving adaptation capability.
- Precision choices (FP32/FP16/BF16/INT8/INT4) trade accuracy vs memory and speed.
- Quantization can provide large compression with bounded reconstruction error.
- MoE routing enables specialization and efficiency by selecting expert subsets.

### Output highlights
- Parameter-count and memory-comparison outputs were generated successfully.
- Quantization demos produced expected compression/error tables.
- MoE router and expert invocation cells ran successfully with expert-specific responses.

## 4) Unit3_Assignment.ipynb

### Key understanding
- Assignment requirements were implemented in parts:
  - Part 1: Corpus setup
  - Part 2: HybridRetriever with BM25 rank, SBERT rank, and RRF score
  - Part 3: Cross-encoder reranking
  - Part 4: Multi-query expansion
  - Part 5: End-to-end advanced_rag pipeline
  - Part 6: Naive vs Advanced comparison experiment

### Output highlights
- The comparison dataframe executed successfully.
- Observed comparison in this run:
  - Query 1: Naive and Advanced top docs were same
  - Query 2: Naive and Advanced top docs differed
  - Query 3: Naive and Advanced top docs were same
- Final sample query cell executed and returned a fallback extractive answer due to Gemini API unavailability.

