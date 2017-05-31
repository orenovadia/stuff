from abc import ABCMeta, abstractmethod

import re


class Rule(metaclass=ABCMeta):
    @abstractmethod
    def applies(self, code_str: str) -> bool:
        pass

    def apply(self, code_str: str) -> str:
        pass


class RegexRule(Rule):
    def __init__(self, pattern):
        super().__init__()
        self._pattern = re.compile('^' + pattern)

    def applies(self, code_str: str) -> bool:
        return bool(self._pattern.match(code_str))

    def apply(self, code_str: str) -> str:
        return self._pattern.sub('', code_str, count=1)
