# encoding=utf-8
from abc import ABCMeta


class PaymentSchedule(metaclass=ABCMeta):
    """
    支付薪水时间表
        一周支付一次
        一月支付一次
        两周支付一次
    """
    pass


class WeeklySchedule(PaymentSchedule):
    pass


class MonthlySchedule(PaymentSchedule):
    pass


class BiweeklySchedule(PaymentSchedule):
    pass
