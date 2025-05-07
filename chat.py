import os, json
from pathlib import Path
import subprocess
import typer
from openai import OpenAI

app = typer.Typer()
HISTORY = Path.home() / ".jarvis_history.json"

def load_history():
    return json.loads(HISTORY.read_text()) if HISTORY.exists() else []

def save_history(h):
    HISTORY.write_text(json.dumps(h, indent=2, ensure_ascii=False))

@app.command()
def chat(message: str):
    """Send MESSAGE to Jarvis and print the response."""
    history = load_history()
    history.append({"role": "user", "content": message})

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history,
    )
    reply = resp.choices[0].message.content
    typer.echo(reply)

    history.append({"role": "assistant", "content": reply})
    save_history(history)

@app.command("shell")
def run_shell(cmd: str):
    """Run a shell command and return stdout/stderr."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    typer.echo(result.stdout or result.stderr)

if __name__ == "__main__":
    app()
