# Zero-Shot Metrical Poetry Generation with Open Language Models: a Quantitative Analysis

This is the official repository for our paper published in ICCC'24.

This repository contains a number of poems that were generated by prompting two open Large Language Models (LLM). We prompted Llama2's (Touvron et al. 2023) 7B and 70B parameter models (quantized versions). We employed Erato (Agirrezabal, Gonçalo Oliveira, and Ormazabal, 2023) for analysing the generated text.

The repository is structured as follows:

  - `code`: Code to calculate the values from the Agirrezabal and Gonçalo Oliveira (2024) article.
  - `dataset`: The generated poems. There are two subdirectories here: `topic_defined` and `topic_undefined`. Inside them, you can find several files:
    - `context_test.py`: This is the script that was used to prompt the model
    - `prompts.txt`: This is a list of different prompts used
    - `topics.txt`: (If defined) This is a list of different topics used
    - Directories `responses` and `responses7b`: The results for the 70B and 7B models, respectively. In these folder, you will find the following files:
      - `promptX.txt`: This contains a prompt and a number at the end. Please ignore this last number, as it was not used for prompting, but just to index each prompt within a group (1-10).
      - `responseX.txt`: The response that corresponds to `promptX.txt`, which was returned by the LLM.
      - `responseX_clean.txt`: The cleaned text, where unnecessary information was removed using regular expressions (Check prompts subsection in Agirrezabal and Gonçalo Oliveira (2024)).
      - `responseX_clean.txt.analysis`: Analysis returned by Erato, in JSON format, which corresponds to the cleaned text.
  - `dataset_groups`: This directory contains the same information as `dataset`, but it is organized in groups for the simplicity of analysis. It also includes the group analyses, where the overlap between poems is calculated. This was employed to analyze the diversity of the generated poems (Table 5 in the article).

# Citation:

Agirrezabal, Manex, and Hugo Gonçalo Oliveira. "Zero-Shot Metrical Poetry Generation with Open Language Models: a Quantitative Analysis.", in Proceedings of the International Conference on Computational Creativity ICCC'24, Jönkoping, Sweden, 2024. [link to paper](https://computationalcreativity.net/iccc24/papers/ICCC24_paper_164.pdf)

Agirrezabal, Manex, Hugo Gonçalo Oliveira, and Aitor Ormazabal. "Erato: Automatizing poetry evaluation." EPIA Conference on Artificial Intelligence. Cham: Springer Nature Switzerland, 2023. [link to paper](https://link.springer.com/chapter/10.1007/978-3-031-49011-8_1)
