# Jarvis

A modular, LLM-driven automation framework for Windows 11:

* interactive “chat + agent” CLI called Jarvis
* plugins for shell, GUI, email, browser, calendar, etc.
* scheduler integration (Task Scheduler / Power Automate)
* easy to extend via Python/Node “skills"

---

## Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/nikakogho/Jarvis.git
   cd Jarvis
   ```

2. Create and activate a Python 3.11 virtual environment:

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```cmd
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API key(s):

   ```env
   OPENAI_API_KEY=your_openai_key_here
   LLM_PROVIDER=openai
   ```

---

## Usage

### 1. Shell commands

Run one-off shell commands via the `shell` alias:

```cmd
python chat.py shell "dir"
```

### 2. Interactive REPL

Start a persistent Jarvis session (REPL mode), which keeps skills like Browser or Robot alive:

```cmd
.venv\Scripts\activate
python chat.py repl
```

At the `Jarvis>` prompt, you can run any supported skill or ask the LLM directly:

```text
Jarvis> shell echo "Hello from Jarvis!"
Jarvis> browser open https://www.google.com
Jarvis> What's the weather today?
Jarvis> exit
```

---

## Adding Skills

Drop new skill modules under `tools/` implementing the `Skill` interface and register them in `chat.py`.

---

## Contributing

See `CONTRIBUTING.md` for guidelines on writing and registering new skills, coding standards, and submitting PRs.
