import subprocess
from .plugin import Skill

class ShellSkill(Skill):
    def can_handle(self, command: str) -> bool:
        return command.startswith("shell ")

    def run(self, command: str) -> str:
        _, arg = command.split(" ", 1)
        res = subprocess.run(arg, shell=True, capture_output=True, text=True)
        return res.stdout or res.stderr
