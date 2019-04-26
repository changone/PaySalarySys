# encoding=utf-8

class Employee(object):

    def __init__(self, emp_id, name, address):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.payment_classification = None
        self.payment_schedule = None
        self.payment_method = None

    def set_payment_classification(self, classification):
        self.payment_classification = classification

    def set_payment_schedule(self, schedule):
        self.payment_schedule = schedule

    def set_payment_method(self, method):
        self.payment_method = method

    def get_payment_classification(self):
        return self.payment_classification

    def get_payment_schedule(self):
        return self.payment_schedule

    def get_payment_method(self):
        return self.payment_method

