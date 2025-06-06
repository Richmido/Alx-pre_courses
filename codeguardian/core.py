import ast
from typing import List


def analyze_file(path: str) -> List[str]:
    """Analyze a Python file and return a list of issues."""
    issues: List[str] = []
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        issues.append(f"Syntax error: {e}")
        return issues

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            arg_count = len(node.args.args)
            if arg_count > 5:
                issues.append(
                    f"Function '{node.name}' has {arg_count} arguments at line {node.lineno}."
                )
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == 'eval':
                issues.append(f"Use of eval detected at line {node.lineno}.")

    for lineno, line in enumerate(source.splitlines(), 1):
        if 'TODO' in line:
            issues.append(f"TODO comment at line {lineno}.")

    return issues
