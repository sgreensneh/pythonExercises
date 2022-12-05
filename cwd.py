import cwd
from pathlib import Path
sony = cwd.Path() / "S_green"
sony.mkdir(exist_ok=True)
print(sony.exists())