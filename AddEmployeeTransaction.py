# encoding=utf-8
from PayrollDatabase import PayrollDatabase
from Employee import Employee
from Paymethod import HoldMethod
from Transaction import Transaction
from abc import ABCMeta, abstractmethod
from PaymentClassification import HourlyClassification, SalariedClassification, CommissionedClassification
from PaymentSchedule import WeeklySchedule, MonthlySchedule, BiweeklySchedule
from Paymethod import HoldMethod, BankMethod, MailMethod


class AddEmployeeTransaction(Transaction, metaclass=ABCMeta):

    def __init__(self, emp_id, emp_name, address):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.address = address

    def execute(self):
        payment_classification = self.get_classification()
        payment_schedule = self.get_schedule()
        payment_method = self.get_paymethod()
        employee = Employee(self.emp_id, self.emp_name, self.address)
        employee.set_payment_classification(payment_classification)
        employee.set_payment_schedule(payment_schedule)
        employee.set_payment_method(payment_method)
        PayrollDatabase.add_employee(employee.emp_id, employee)

    @abstractmethod
    def get_classification(self):
        pass

    @abstractmethod
    def get_schedule(self):
        pass

    @abstractmethod
    def get_paymethod(self):
        pass


class AddHourlyEmpTransaction(AddEmployeeTransaction):

    def __init__(self, emp_id, emp_name, address):
        super(AddHourlyEmpTransaction, self).__init__(emp_id, emp_name, address)

    def get_classification(self):
        return HourlyClassification()

    def get_schedule(self):
        return WeeklySchedule()

    def get_paymethod(self):
        return BankMethod()


class AddSalariedEmpTransaction(AddEmployeeTransaction):

    def __init__(self, emp_id, emp_name, address):
        super(AddSalariedEmpTransaction, self).__init__(emp_id, emp_name, address)

    def get_classification(self):
        return SalariedClassification()

    def get_schedule(self):
        return MonthlySchedule

    def get_paymethod(self):
        return BankMethod()

class AddCommissionedEmpTransaction(AddEmployeeTransaction):

    def __init__(self, emp_id, emp_name, address):
        super(AddCommissionedEmpTransaction, self).__init__(emp_id, emp_name, address)

    def get_classification(self):
        return CommissionedClassification()

    def get_schedule(self):
        return BiweeklySchedule()

    def get_paymethod(self):
        return HoldMethod()
