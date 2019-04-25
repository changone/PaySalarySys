# encoding=utf-8
from PayrollDatabase import PayrollDatabase

class DeleteEmployeeTransaction(object):

    def delete_employee_transaction(self, emp_id):
        PayrollDatabase.del_emp(emp_id)
