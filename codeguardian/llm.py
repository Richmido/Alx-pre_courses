import os
from typing import List

try:
    import openai
except ImportError:  # pragma: no cover - openai optional
    openai = None

SYSTEM_PROMPT = (
    "You are an experienced Python code reviewer. "
    "Given a list of issues and the code, propose improvements and patches."
)


def generate_suggestions(issues: List[str], code: str) -> str:
    """Return suggestions from OpenAI if API key is set."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not openai:
        return "OpenAI not configured."

    openai.api_key = api_key
    message = {
        "role": "user",
        "content": "Issues:\n" + "\n".join(issues) + "\n\nCode:\n" + code,
    }
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, message],
        )
    except Exception as e:  # pragma: no cover - network errors
        return f"OpenAI request failed: {e}"

    return resp.choices[0].message["content"].strip()
