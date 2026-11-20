import json
import subprocess
import sys
import tempfile
from pathlib import Path

command = ['preflight.py', 'examples']
def check(arguments, code):
    result = subprocess.run([sys.executable, *arguments, "--json"], capture_output=True, text=True)
    assert result.returncode == code, result.stderr
    return json.loads(result.stdout)["findings"]

assert check(command, 1) == ['small.jpg: resize to 1080x1920']
with tempfile.TemporaryDirectory() as folder:
    target = Path(folder) / "good.jpg"
    target.write_bytes(Path('examples/good.jpg').read_bytes())
    command[1] = str(target)
    assert check(command, 0) == []
