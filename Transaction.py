# encoding=utf-8

from abc import ABCMeta, abstractmethod


class Transaction(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass
