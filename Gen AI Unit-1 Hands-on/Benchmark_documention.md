## What I Understood
Through this Unit 1 hands-on, I gained a clear understanding of how different transformer architectures behave differently across various NLP tasks. I learned that encoder-only models like BERT and RoBERTa are mainly designed for language understanding tasks such as masked language modeling and question answering. In contrast, encoder–decoder models like BART are capable of text generation but require proper fine-tuning to produce coherent outputs.
This assignment also helped me understand the importance of model architecture, training objectives, and tokenizer differences in determining a model’s performance.

## What I Implemented
As part of this assignment, I implemented a model benchmarking experiment where I compared three transformer models—BERT, RoBERTa, and BART—across three different tasks: text generation, masked language modeling, and question answering.
I executed each experiment using the Hugging Face pipeline API and carefully observed how each model behaved when forced to perform tasks they were not primarily designed for. Based on the results, I documented observations and filled an observation table to explain the successes and failures from an architectural perspective.

## Challenges Faced

During the implementation, I faced issues related to model compatibility and tokenizer differences, such as using the correct mask token for different models.
I also encountered environment-related warnings while running the notebook in VS Code.
These challenges helped me understand practical issues that arise while working with real-world AI libraries.


## Tools Used
Python
Hugging Face Transformers library
VS Code

