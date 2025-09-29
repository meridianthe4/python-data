class Employee:
    # ini directly
    # def __init__(self,empid,name,basic):
    #     self._empid = empid
    #     self._name = name
    #     self._basic = basic
    
    
    def __init__(self,empid = 100,name = 'AAA',basic = 10000):
        self._empid = empid
        self._name = name
        self._basic = basic
    
    
    def calculate_salary(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da
    
    def __str__(self):
        return f'Employee Details ID: {self._empid} , Name : {self._name} , Salary : {self._basic}'
    
    def __repr__(self):
        # return f'Employee (ID : {self._empid} , Name : {repr(self._name)} , Salary : {self._basic} )'
        # return f'Employee (ID : {self._empid} , Name : (self._name) , Salary : {self._basic} )'
         return f"Employee({self._empid!r}, {self._name!r}, {self._basic!r})"
     
    '''Property for Name only
        like a getter method
        read only
    '''
    @property
    def name(self):
        return self._name
    
    
    '''
    For basic 
    it will have readf and write
    '''
    @property
    def basic(self):
        return self._basic

    @basic.setter
    def basic(self,value):
        if value<= 0:
            raise ValueError('Salary can not be zero')
        
    
class NewEmployee:
    count = 0
    def __init__(self,name = 'AAA',basic = 10000):
        NewEmployee.count += 1
        self._empid = NewEmployee.count
        self._name = name
        self._basic = basic
        
    def calculate_salary(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da
    
    def __str__(self):
        return f'Employee Details ID: {self._empid} , Name : {self._name} , Salary : {self._basic}'
    
    @staticmethod
    def show_employee_count():
        print("Employee Count : " , NewEmployee.count)
        
    @classmethod
    def set_count(cls):
        cls.count = 100
    