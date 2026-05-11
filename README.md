# improvement
📝 My Personal Code Lab - A place to experiment, learn, and share knowledge about software development and more.

## 🚀 Technologies
- Python 3.12
- FastAPI
- Transformers (Hugging Face)
- PyTorch
- Ruff
- pre-commit
- uv (Optional)

## 🛠️ Installation

### Option 1: Using uv (recommended)

```bash
git clone https://github.com/felipemrz0/improvement.git
cd improvement
uv sync
```
### Option 2: Using pip

```bash
git clone https://github.com/felipemrz0/improvement.git
cd improvement

python -m venv .venv
```
Windows PowerShell
```bash
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Linux / macOS
```bash
source .venv/bin/activate
pip install -r requirements.txt
```
## 🚀 Quick Start

Using uv
```bash
uv run app.py
```
or:
```bash
uv run uvicorn app.main:app --reload
```
Using activated virtual environment
```bash
python app.py
```
or:
```bash
uvicorn app.main:app --reload
```

## 🧪 Development

Run Ruff:
```bash
uv run ruff check
uv run ruff format
```

Run pre-commit hooks:
```bash
uv run pre-commit run --all-files
```