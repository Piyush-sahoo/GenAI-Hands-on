## What I Understood

Through this Unit 2 hands-on project, I gained a clear understanding of how text-generation models work, especially for short creative tasks like email subject optimization.
I learned how decoder-only architectures such as GPT-2 generate new text by predicting the next token based on context.
This assignment helped me understand concepts like sampling, temperature, and model randomness, which directly influence the creativity and variation of generated subject lines.
I also realized that even small generative models can produce useful outputs when the prompt is short and well-structured.

## What I Implemented

As part of this assignment, I implemented an Email Subject Line Optimizer using the Hugging Face text-generation pipeline.
I provided a single subject line as input and generated five different variations using GPT-2.
The implementation included:

Loading the GPT-2 model

Using temperature-based sampling to control creativity

Running the generator multiple times to produce unique outputs

Printing and comparing the results to identify the best subject line

This practical experiment helped me see how generative AI can assist in marketing, communication, and content writing tasks.

## Challenges Faced

During the implementation, I faced a few challenges such as:

Import and version issues while installing the Transformers library

Model loading delays due to missing cached files

Occasional long or incomplete generations that required adjusting parameters like max_length

Understanding how temperature and randomness influence consistency vs creativity

These challenges gave me real-world experience in handling generative models and tuning their outputs for better results.

## Tools Used

Python

Hugging Face Transformers library

VS Code / Jupyter Notebook

GPT-2 (decoder-only text-generation model)