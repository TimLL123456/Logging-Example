# UV tutoral

## Getting Started


<details>
  <summary>Extra Information</summary>

### UV python list
Select python version to install
```bash
>>> uv python list

cpython-3.14.0b4-windows-x86_64-none                 <download available>
cpython-3.14.0b4+freethreaded-windows-x86_64-none    <download available>
cpython-3.13.5-windows-x86_64-none                   <download available>
...
```

### UV python install
Select python version to install
```bash
>>> uv python install 3.13

Installed Python 3.13.5 in 4.76s
 + cpython-3.13.5-windows-x86_64-none
```

### Pin a specific Python version for project
```bash
uv python pin 3.13
```

Make sure your pyproject.toml's requires-python setting is compatible, for example:
```text
[project]
requires-python = ">=3.12"
```

### Create a virtual environment with a specific Python version
```bash
uv venv --python 3.11.6
```

</details>

### 1. Install UV
```bash
pip install uv
```

### 2. Initialize a New Project
* Create a new Python project with all configuration files and a virtual environment

* This creates:
  - .gitignore
  - .python-version
  - main.py
  - pyproject.toml
  - README.md
  - uv.lock

```bash
uv init my-project
cd my-project
```

### 3. Install Packages
* Add the `rich` package as a dependency

```bash
>>> uv add rich

Using CPython 3.12.3 interpreter at: C:\Users\miniconda3\python.exe
Creating virtual environment at: .venv
Resolved 5 packages in 46ms
Installed 4 packages in 263ms
 + markdown-it-py==3.0.0
 + mdurl==0.1.2
 + pygments==2.19.2
 + rich==14.0.0
```

### 4. Create a Python script using `rich`
* Create a file named main.py with the following content:

`main.py`
```python
from rich.console import Console

console = Console()
console.print("[bold magenta]Hello, Rich![/bold magenta]")
console.print("This text is [green]green[/green] and this is [red]red[/red].")
```

### 5. Run the script inside the uv environment

```bash
uv run python main.py
# or 
uv run --python 3.13 python your_script.py
```