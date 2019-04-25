# encoding=utf-8
from abc import ABCMeta


class PaymentMethod(metaclass=ABCMeta):
    """
    支付方式
        支票邮寄，
        支票寄存在出纳处随时取，
        直接存入银行账号
    """
    pass


class HoldMethod(PaymentMethod):
    """ 支票寄存在出纳处供随时支取 """
    pass


class MailMethod(PaymentMethod):
    """ 邮寄方式 """
    pass


class BankMethod(PaymentMethod):
    """ 存入银行账号 """
    pass
