# TODO.md

- [X] **Phase 1: Repository & Dev Diary**
  - [X] Initialize Git repo with `README.md` and `DEV_DIARY.md`
  - [X] Add `.gitignore` file
  - [X] Create folder structure:
    - `.venv/`
    - `tools/`
    - `agents/`
    - `scripts/`
  - [X] Perform initial commit of skeleton
  - [X] Push to GitHub (manual or via `gh` CLI)

- [ ] **Phase 2: Core LLM-chat CLI**
  - [ ] Create & activate Python 3.11 virtual environment (`.venv`)
  - [ ] Install dependencies:
    - `openai` (or `azure-openai`)
    - `langchain`
    - CLI framework (`typer` or `click`)
  - [ ] Scaffold `chat.py` CLI with context persistence
  - [ ] Implement `/shell` skill with Python `subprocess`
  - [ ] Test basic conversation and shell execution

- [ ] **Phase 3: Plugin Architecture & Skills**
  - [ ] Define plugin interface (`can_handle(input)`, `run(input)`)
  - [ ] Develop browser control plugin (using Playwright or Pyppeteer)
  - [ ] Develop email automation plugin (IMAP/SMTP or Microsoft Graph API)
  - [ ] Integrate MCPS as a plugin within the architecture
  - [ ] Develop calendar/task plugin (Outlook or Google Calendar integration)

- [ ] **Phase 4: Scheduling & Persistence**
  - [ ] Integrate Windows Task Scheduler or Power Automate flows
  - [ ] Design persistent storage (SQLite database or JSON logs) for context and task history
  - [ ] Implement `status.py` to report pending and completed jobs
  - [ ] Test scheduled tasks and ensure state persists across restarts

- [ ] **Phase 5: Full Agentic Loop & Extensibility**
  - [ ] Implement event loop (file‐watcher, calendar/event triggers, email triggers)
  - [ ] Build interactive GUI or web dashboard (Electron or Flask)
  - [ ] Write `CONTRIBUTING.md` with plugin development guidelines and code standards
  - [ ] Perform final release: tag version, update `DEV_DIARY.md`, publish documentation
