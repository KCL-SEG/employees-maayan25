"""Employee pay calculator."""

import abc


class Employee:
    def __init__(self, name, salary, commission):
        self.name = name
        self.salary = salary
        self.commission = commission

    def get_pay(self):
        salary= self.salary.salary
        commission = self.commission.get_commission()
        return salary + commission

    def __str__(self):
        salary_str = self.salary.get_str()
        commission_str = self.commission.get_str()
        pay_str = f"{self.name} works on a {salary_str}{commission_str}.  Their total pay is {self.get_pay()}."
        return pay_str


class Salary(abc.ABC):
    def __init__(self):
        pass

    def get_salary(self):
        pass

    def get_str(self):
        pass


class HourlySalary(Salary):
    def __init__(self, rate, hours):
        super().__init__()
        self.rate = rate
        self.hours = hours
        self.salary = self.get_salary()

    def get_salary(self):
        salary = self.rate * self.hours
        return salary

    def get_str(self):
        pay_str = f"contract of {self.hours} hours at {self.rate}/hour"
        return pay_str


class MonthlySalary(Salary):
    def __init__(self, salary):
        self.salary = salary

    def get_pay(self):
        return self.salary

    def get_str(self):
        pay_str = f"monthly salary of {self.salary}"
        return pay_str


class Commission(abc.ABC):
    def get_commission(self):
        pass

    def get_str(self):
        pass


class NoCommission(Commission):
    def __init__(self):
        self.commission = 0

    def get_commission(self):
        return self.commission

    def get_str(self):
        commission_str = ""
        return commission_str


class Bonus(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def get_commission(self):
        return self.bonus

    def get_str(self):
        pay_str = f" and receives a bonus commission of {self.get_commission()}"
        return pay_str


class Contracts(Commission):
    def __init__(self, rate_com, contracts):
        self.rate_com = rate_com
        self.contracts = contracts

    def get_commission(self):
        return self.rate_com * self.contracts

    def get_str(self):
        pay_str = f" and receives a commission for {self.contracts} contract(s) at {self.rate_com}/contract"
        return pay_str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000), NoCommission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100), NoCommission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), Contracts(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), Contracts(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), Bonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(30, 120), Bonus(600))