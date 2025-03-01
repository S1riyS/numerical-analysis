from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
