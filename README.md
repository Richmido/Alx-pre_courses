# CodeGuardian Prototype

This repository contains a minimal prototype of **CodeGuardian**,
an AI-assisted code review tool. It scans Python files for simple
issues and can optionally query the OpenAI API to suggest fixes.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Set your `OPENAI_API_KEY` environment variable to enable
   AI-powered suggestions.
3. Run the analysis:
   ```bash
   python -m codeguardian.cli path/to/file.py
   ```

## InternAI Quickstart

InternAI is a lightweight demo API to manage internship applications. It
uses FastAPI and provides a simple CV scoring endpoint.

### Running the server

```bash
pip install -r requirements.txt
python -m internai
```

Submit an application with a form field `name`, `mission_id` and a CV file
named `cv` using an HTTP client or `curl`. Retrieve all candidates at
`/candidates`.
