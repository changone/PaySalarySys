# encoding=utf-8
from abc import ABCMeta


class PaymentClassification(metaclass=ABCMeta):
    """
    薪水计算类
        按小时计算
        底薪加提成
        按月直接计算薪水
    """


    pass


class HourlyClassification(PaymentClassification):
    pass


class SalariedClassification(PaymentClassification):
    pass


class CommissionedClassification(PaymentClassification):
    pass


