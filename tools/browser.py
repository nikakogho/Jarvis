from .plugin import Skill
from playwright.sync_api import sync_playwright

class BrowserSkill(Skill):
    """
    Skill to open URLs or perform simple browser actions.
    Supports:
      - browser open <URL>
      - browser close
    """

    def __init__(self):
        self.playwright = None
        self.browser = None

    def can_handle(self, command: str) -> bool:
        cmd = command.strip().lower()
        return cmd.startswith("browser ")

    def run(self, command: str) -> str:
        parts = command.split(" ", 2)
        if len(parts) < 2:
            return "Usage: browser open <URL> | browser close"

        action = parts[1].lower()

        if action == "open":
            if len(parts) != 3:
                return "Usage: browser open <URL>"

            url = parts[2]
            # Start Playwright if needed
            if not self.playwright:
                self.playwright = sync_playwright().start()
                self.browser = self.playwright.chromium.launch(headless=False)

            page = self.browser.new_page()
            page.goto(url)
            return f"Opened browser to {url}"

        elif action == "close":
            if not self.browser:
                return "No browser is currently open."
            self.browser.close()
            self.playwright.stop()
            self.browser = None
            self.playwright = None
            return "Browser closed."

        else:
            return f"Unknown browser action '{action}'. Supported: open, close."
