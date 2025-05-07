## [v0.2.0] – 2025-05-07
- Created Python venv and installed dependencies  
- Scaffolded `chat.py` CLI with OpenAI + context persistence  
- Added `/shell` skill (via `subprocess`)  
- Verified basic chat and shell execution work  

## [v0.3.0] – 2025-05-07
- Created `tools/plugin.py` with abstract base class `Skill`
- Moved shell logic into `tools/shell.py` as `ShellSkill`
- Updated `chat.py` to load skills from `tools/` and delegate before falling back to LLM

## [v0.3.2] – 2025-05-07
- Refactored `BrowserSkill` to start Playwright manually (no `with` block)
- Stored `playwright` & `browser` as instance attributes to keep them alive
- Added `browser close` action
- Added `repl` command to `chat.py` for a persistent interactive session  
- Moved skill instantiation (ShellSkill, BrowserSkill) into REPL so browser stays open  
