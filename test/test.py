import subprocess
import sys
from pathlib import Path

test_file = Path(__file__).resolve()
app_path = test_file.parent.parent / "app.py"

output = subprocess.check_output([sys.executable, str(app_path)], text=True).strip()
assert output == "Hello, world!", f"unexpected output: {output!r}"
print('Test passed')
