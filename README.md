# AI Trading Agent

Simple AI trading agent scaffolded for development.

[![Live on Railway](https://img.shields.io/badge/deploy-railway-blue?logo=railway)](https://ai-trading-agent-production-48a0.up.railway.app/)


## Prerequisites
- Python 3.10+ recommended

## Setup
Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
Start the agent:

```bash
make run
```

## UI (Streamlit)

Quick demo UI (Streamlit):

```bash
source .venv/bin/activate
streamlit run ui.py
```

Deploy on Railway: add the `web` start command in Railway to match `Procfile`:

```
web: streamlit run ui.py --server.port $PORT --server.address 0.0.0.0
```

## Tests
Run tests with:

```bash
make test
```
