# coding: utf-8
from Transaction import Transaction
from PayrollDatabase import PayrollDatabase
from PaymentClassification import HourlyClassification
from TimeCard import TimeCard


class TimeCardTransaction(Transaction):

    def __init__(self, _date, hours, empid):
        self._date = _date
        self.hours = hours
        self.empid = empid

    def execute(self):
        emp = PayrollDatabase.get_emp(self.empid)
        if not emp:
            raise Exception('not found emp')
        classification = emp.get_payment_classification()
        if isinstance(classmethod, HourlyClassification):
            time_card = TimeCard(self._date, self.hours)
            classification.add_time_card(time_card)
