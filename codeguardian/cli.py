import argparse
import os
from .core import analyze_file
from .llm import generate_suggestions


def main():
    parser = argparse.ArgumentParser(description="Run CodeGuardian analysis")
    parser.add_argument("file", help="Python source file to analyze")
    args = parser.parse_args()

    issues = analyze_file(args.file)
    if not issues:
        print("No issues found.")
        return

    print("Issues detected:\n" + "\n".join(f"- {issue}" for issue in issues))

    with open(args.file, "r", encoding="utf-8") as f:
        source = f.read()

    suggestion = generate_suggestions(issues, source)
    if suggestion:
        print("\nAI Suggestions:\n" + suggestion)


if __name__ == "__main__":
    main()
