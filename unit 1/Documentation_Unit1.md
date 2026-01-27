# Unit 1 – Generative AI Hands-On Documentation

## 1. Overview

This document summarizes my understanding and implementation of Unit 1 concepts
related to Generative AI using Hugging Face transformers.

---

## 2. What I Understood (Conceptual Learning)

- Generative AI models have different architectures such as Encoder-only,
  Decoder-only, and Encoder-Decoder.
- BERT and RoBERTa are encoder-based models mainly designed for understanding tasks
  like classification and masked language modeling.
- BART is an encoder-decoder model, making it more suitable for text generation
  and sequence-to-sequence tasks.
- Hugging Face pipelines simplify model usage by abstracting tokenization,
  model loading, and inference.

---

## 3. Hands-On Experiments (Benchmark Task)

I performed a benchmark comparison between BERT, RoBERTa, and BART using three tasks:

### a) Text Generation

- BERT and RoBERTa failed to generate meaningful text.
- BART was able to generate limited but coherent text.

### b) Fill-Mask

- BERT and RoBERTa performed well due to Masked Language Modeling training.
- BART showed weaker performance for this task.

### c) Question Answering

- All models gave partial or inconsistent answers as they were not fine-tuned
  for Question Answering tasks.

---

## 4. Mini Project Implemented

### Project Title: Customer Review Sentiment Analyzer

**Description:**  
A simple application that classifies customer reviews as Positive or Negative
using a pre-trained transformer model.

**Model Used:**

- distilbert-base-uncased-finetuned-sst-2-english

**Tools & Libraries:**

- Python
- Hugging Face Transformers

---

## 5. Observations

- Pre-trained models can be directly used without fine-tuning for real-world tasks.
- Model architecture plays a significant role in determining task performance.
- Sentiment analysis models perform well on short, opinion-based text.

---

## 6. Conclusion

This unit helped me understand the importance of model architecture and how
Hugging Face pipelines enable rapid development of NLP applications.
