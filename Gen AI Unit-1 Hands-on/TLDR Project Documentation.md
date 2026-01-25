## Summarization Pipeline

The project uses the Hugging Face `summarization` pipeline to convert long text into a short and meaningful summary.
This pipeline simplifies the process by handling tokenization, model inference, and text generation internally.
It allows summarization to be implemented with minimal code.


## Model Used

The model used for summarization is `sshleifer/distilbart-cnn-12-6`.
It is a distilled version of the BART model trained on the CNN/DailyMail dataset for news summarization.
The model is optimized for speed and works efficiently on CPU while maintaining good summarization quality.

## Why distilbart-cnn-12-6

The distilbart model was chosen because it provides a balance between performance and speed.
It is suitable for summarizing long news articles and producing concise TL;DR outputs.
Since it is a lightweight model, it can be easily executed on local machines without GPU support.

## Working of the Summarizer

The summarizer first encodes the input article to understand its context.
It then decodes the most important information to generate a shorter version of the text.
The model primarily follows an extractive approach by selecting key sentences from the input.


## Limitations

The distilbart summarizer may produce outputs that closely resemble the original text.
This behavior occurs because the model focuses on extracting important sentences rather than heavily paraphrasing the content.
It performs best when the input text is long and detailed.
