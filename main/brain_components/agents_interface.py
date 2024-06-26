from abc import ABC, abstractmethod


class Agents(ABC):
    @abstractmethod
    def run(self, **kwargs):
        pass
