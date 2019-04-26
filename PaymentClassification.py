# encoding=utf-8
from abc import ABCMeta, abstractmethod


class PaymentClassification(metaclass=ABCMeta):
    """
    薪水计算类
        按小时计算
        底薪加提成
        按月直接计算薪水
    """
    @abstractmethod
    def calculate_pay(self):
        pass


class HourlyClassification(PaymentClassification):

    def calculate_pay(self):
        pass

    def add_time_card(self, time_card):
        self.time_card = time_card


class SalariedClassification(PaymentClassification):
    def calculate_pay(self):
        pass


class CommissionedClassification(PaymentClassification):
    def calculate_pay(self):
        pass


