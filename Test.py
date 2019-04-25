# encoding=utf-8

import unittest
from AddEmployeeTransaction import AddHourlyEmpTransaction, AddSalariedEmpTransaction
from PayrollDatabase import PayrollDatabase
from DeleteEmployeeTransaction import DeleteEmployeeTransaction

class TestAddEmployee(unittest.TestCase):

    def test_add_employee(self):
        add_hourly_emp = AddHourlyEmpTransaction(1, '张三', '深圳')
        add_hourly_emp.execute()

        add_salarie_emp = AddSalariedEmpTransaction(2, '李四', '湖南')
        add_salarie_emp.execute()

        emp = PayrollDatabase.get_emp(1)
        self.assertEqual('张三', emp.name)
        emp2 = PayrollDatabase.get_emp(2)
        self.assertEqual('李四', emp2.name)

    def test_del_employee(self):
        del_emp_transaction = DeleteEmployeeTransaction()
        del_emp_transaction.delete_employee_transaction(1)
        with self.assertRaises(KeyError):
            PayrollDatabase.get_emp(1)
