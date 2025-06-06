import os
import tempfile
from codeguardian.core import analyze_file


def test_analyze_file_detects_issues():
    source = "def bad_function(a,b,c,d,e,f):\n    eval('1+1')\n    # TODO: fix later\n"
    with tempfile.NamedTemporaryFile('w+', delete=False, suffix='.py') as f:
        f.write(source)
        fname = f.name
    try:
        issues = analyze_file(fname)
    finally:
        os.unlink(fname)
    assert any('has 6 arguments' in i for i in issues)
    assert any('Use of eval' in i for i in issues)
    assert any('TODO comment' in i for i in issues)
