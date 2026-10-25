# Generative AI Internship — Task 1: Text Generation

## 1. Objective

The objective of this task is to explore text generation using Generative AI by creating diverse prompts, generating text outputs, and evaluating their quality.

## 2. Project Overview

This project contains 20 text-generation prompts covering artificial intelligence, education, programming, cybersecurity, robotics, and other technology-related topics.

The project includes:
- 20 text-generation prompts.
- 20 generated text samples saved as plain text files.
- An evaluation summary of the generated outputs.
- A Python inference script demonstrating text generation.

## 3. Model and Generation Method

### Generated Samples

- **Platform:** Google Gemini website
- **Method:** Manual prompt submission through the Gemini interface.
- **Number of prompts:** 20
- **Output format:** Plain text (`.txt`)

Each prompt was entered into Gemini manually, and its generated response was saved as a text file.

The exact Gemini model version used for these samples should be verified from the original conversation or interface.

Official source: https://gemini.google.com/

Applicable terms:
- https://policies.google.com/terms
- https://policies.google.com/terms/generative-ai

### Python Inference Demonstration

The `Generate.py` file demonstrates a separate, programmatic text-generation workflow using the Gemini API.

This script was not used to generate the 20 manually collected samples.

- **Model specified in the script:** `gemini-2.0-flash`
- **Official API documentation:** https://ai.google.dev/gemini-api/docs
- **API terms:** https://ai.google.dev/terms

The API model specified in the script should not be assumed to be the model used for the manually generated samples.

## 4. Project Structure

```text
GAI-1-Textgeneration/
├── README.md
├── Prompts.txt
├── Generate.py
├── Evaluation summary.txt
└── generated_samples/
    ├── 1-20.txt
    ├── 2-20.txt
    ├── 3-20.txt
    ├── ...
    └── 20-20.txt
```

The filenames and folder name shown above should match the actual files in the repository.

## 5. Running the Inference Script

The Python script provides an example of generating text through the Gemini API.

Running it requires:
- Python.
- Internet access.
- The `google-genai` Python package.
- A valid Gemini API key.

Install the required package:

```bash
pip install google-genai
```

Set the `GEMINI_API_KEY` environment variable with your API key, then run:

```bash
python Generate.py
```

The script sends a sample prompt to the specified model and prints the generated response.

**Note:** Running the script requires API access. An API key is not required to use the Gemini website or to view the 20 existing text samples.

Never commit API keys or other secrets to the repository.

## 6. Evaluation

The `Evaluation summary.txt` file contains a qualitative assessment of the generated responses, focusing on coherence, relevance, readability, strengths, and observed limitations.

The evaluation should reflect the actual generated samples and should not claim quantitative measurements that were not performed.

## 7. Conclusion

This project explores text generation using Gemini across 20 educational and technical prompts. It includes the generated outputs, a qualitative evaluation, and a separate Python inference demonstration.
