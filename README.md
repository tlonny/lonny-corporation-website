# Lonny Corporation website generator

### Installation

```bash
# Set up a virtualenv
python -m venv .venv

# Point to the virtualenv python with direnv
echo "PATH_add .venv/bin" > .envrc

# Install the dependency (there is one)
pip install -r requirements.txt

# Build the website
python -m script.build

# Host the website
python -m http.server -d build
```
