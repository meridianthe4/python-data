class NewEmployee:
    count = 10  # static variable
    def __init__(self, name="John", basic=5000):
        NewEmployee.count += 1
        self._empid = NewEmployee.count
        self._name = name
        self._basic = basic
    
    @property
    def name(self):
        return self._name
    
    @property
    def basic(self):
        return self._basic
    
    @basic.setter
    def basic(self, value):
        if value <= 0:
            raise ValueError("Salary cannot be -ve or zero")
        else:
            self._basic = value
            
    def calculate_salary(self):
        hra = self._basic * 0.4
        da = self._basic * 0.15
        return self._basic + hra + da
    
    def __str__(self):
        return f"Employee [Id: {self._empid}, Name: {self._name},Salary: {self.calculate_salary()}]"
    
    def __repr__(self):
        return f"NewEmployee({repr(self._name)}, {self._basic})"
    
    def test(self):
        print(self._basic)
        print(self._name)
        print(repr(self._name))
        
    @staticmethod
    def count_employees():
        return NewEmployee.count
    
    @classmethod
    def set_count(cls, value):
        cls.count = value