# __slots__限制对象属性访问
# 限制属性范围 不能额外添加
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    __slots__ = ("name", "age")

s = Student('',0)
s.name = '张三'
s.age = 20
s.score = 0