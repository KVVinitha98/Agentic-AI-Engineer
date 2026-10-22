# Initial project: LangChain + Ollama

A small Python example that sends a prompt to a local Ollama model through
LangChain and prints the model's summary.

## Requirements

- Python 3.15 or newer
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) installed and running
- The `gemma3:270m` model available in Ollama

Pull the model before running the application:

```powershell
ollama pull gemma3:270m
```

## Setup

From this directory, install the project dependencies:

```powershell
uv sync
```

Run the example:

```powershell
uv run langchain-course
```

The example creates a LangChain prompt from a generic developer profile,
passes it to the local `gemma3:270m` model with Ollama, and prints the
generated summary. No hosted API key is required.
