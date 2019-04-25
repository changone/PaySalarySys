# encoding=utf-8



class PayrollDatabase(object):

    emp_dict = dict()
    emp_association_dict = dict()

    @classmethod
    def add_employee(cls, emp_id, employee):
        cls.emp_dict[emp_id] = employee

    @classmethod
    def get_emp(cls, emp_id):
        return cls.emp_dict[emp_id]

    @classmethod
    def del_emp(cls, emp_id):
        cls.emp_dict.pop(emp_id)



