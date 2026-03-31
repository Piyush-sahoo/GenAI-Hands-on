# Observations (Student Notes)

## 1) Introduction & Setup

- I learned that Hugging Face is like a big hub where we can download ready‑made AI models instead of training from scratch.
- The `transformers` library is the bridge that lets us load and use those models easily.
- `pipeline()` hides all the complicated steps (tokenization → model → readable output), so we can focus on results.

## 2) Imports & Utilities

- Imported `pipeline`, `set_seed`, and `GPT2Tokenizer` for text generation and tokenization.
- Imported `nltk` and `os` for classic NLP tasks and file handling.

## 3) Loading Course Material

- Set the file path to `unit 1.txt`.
- Read the file using a `try/except` block, which is good because it avoids crashing if the file is missing.
- Printed the first 500 characters to verify the data looks correct.

## 4) Generative AI: Fast vs. Standard Models

- Set a seed with `set_seed(42)` to make outputs reproducible.
- When I changed the seed to `45`, the generated text changed, which shows how the seed controls randomness.
- Used the same prompt for both models so the comparison is fair.
- `distilgpt2` generates faster but sometimes drifts or repeats.
- `gpt2` feels more coherent, but output can be very long.
- I saw warnings about `max_length` vs `max_new_tokens` and truncation. The code still works, but it could be cleaned up.

### Distilled vs. Normal Models (Student View)

- A distilled model is like a smaller, compressed version of a bigger model. It learns from the bigger one, so it runs faster and uses less memory.
- A normal (full) model usually gives better quality and more consistent output, but it is slower and heavier.
- In this notebook, `distilgpt2` is the distilled model and `gpt2` is the normal model.
- My takeaway: use distilled models for speed and quick experiments, and normal models when quality matters more.

## 5) NLP Fundamentals: Tokenization

- Loaded `GPT2Tokenizer` to break a sentence into tokens.
- Printed both tokens and their numeric IDs to see how text becomes numbers.

## 6) NLP Fundamentals: POS Tagging

- Downloaded required NLTK resources (`punkt`, `averaged_perceptron_tagger_eng`).
- Tagged words in the sentence to see their grammar roles (noun, verb, adjective, etc.).
- There was an extra `nltk.download('punkt_tab')` line; it seems unusual and may not be needed.

## 7) NLP Fundamentals: Named Entity Recognition (NER)

- Used a BERT model fine‑tuned for NER.
- Extracted entities from the first paragraph and filtered for high confidence.
- Saw a warning about unused weights, which is expected for this type of model load.

## 8) Advanced: Summarization

- Compared a fast summarizer (`distilbart-cnn-12-6`) and a quality summarizer (`bart-large-cnn`).
- The fast summary was shorter and sometimes cut off, while the quality model gave a more complete summary.
- Model downloads were large, so the first run can be slow.

## 9) Advanced: Question Answering

- Used a QA model to answer two questions from the course text.
- The model returned direct answers extracted from the context.

## 10) Advanced: Fill‑Mask (Masked Language Modeling)

- Used `bert-base-uncased` to predict the missing word in a sentence.
- The model suggested multiple possible words with confidence scores.
- Warnings about unused weights are expected for masked‑LM initialization.

## 11) POS Tags Output (Student Explanation)

- `('Transformers', 'NNS')`: “Transformers” is tagged as **NNS** (plural noun).
- `('revolutionized', 'VBD')`: “revolutionized” is **VBD** (past‑tense verb).
- `('NLP', 'NNP')`: “NLP” is **NNP** (proper noun, singular).
- `('.', '.')`: the period is tagged as punctuation.
