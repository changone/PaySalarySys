# coding: utf-8
from abc import ABCMeta, abstractmethod


class TimeCard(object):

    def __init__(self, _date, hours):
        self._date = _date
        self.hours = hours

