from abc import ABC, abstractmethod

class Skill(ABC):
    @abstractmethod
    def can_handle(self, command: str) -> bool: ...
    
    @abstractmethod
    def run(self, command: str) -> str: ...
