import os
import json
from pathlib import Path

import typer
from openai import OpenAI

from tools.plugin import Skill
from tools.shell import ShellSkill

app = typer.Typer()
HISTORY = Path.home() / ".jarvis_history.json"

# --- Plugin setup: only ShellSkill for now ---
skills: list[Skill] = [
    ShellSkill(),
]

def load_history() -> list[dict]:
    if HISTORY.exists():
        return json.loads(HISTORY.read_text())
    return []

def save_history(history: list[dict]) -> None:
    HISTORY.write_text(json.dumps(history, indent=2, ensure_ascii=False))

@app.command()
def chat(message: str):
    """
    Send MESSAGE to Jarvis.  
    First, check if any skill can handle it;  
    if not, fall back to the LLM.
    """
    # 1) Try skills
    for skill in skills:
        if skill.can_handle(message):
            output = skill.run(message)
            typer.echo(output)
            return

    # 2) Otherwise, go to the LLM
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
    """
    (Alias) Run a shell command via the ShellSkill.
    """
    shell = ShellSkill()
    # ensure prefix matches can_handle logic
    output = shell.run(f"shell {cmd}")
    typer.echo(output)

if __name__ == "__main__":
    app()
