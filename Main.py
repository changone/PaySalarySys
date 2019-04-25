# encoding=utf-8
from AddEmployeeTransaction import AddHourlyEmpTransaction

class Main(object):

    def add_emp(self):
        transaction = AddHourlyEmpTransaction(1, '张三', '深圳')
        transaction.execute()

