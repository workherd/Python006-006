#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Employee(object):
    """1111111所有员工的基类"""
    empCount = 0

    def __init__(self, name, salary):
        # 类的构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        # 类方法
        print("total employee ", Employee.empCount)

    def displayEmployee(self):
        print("name :", self.name, ", salary :", self.salary)

class Tlls(Employee):
    pass

e1 = Tlls('e1', 1000)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__subclasses__:", Employee.__subclasscheck__(Tlls))