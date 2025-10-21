"""
    初始化学生类
    设置学生各科目成绩
    输出各科目成绩内容
"""
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = {"语文":0,"数学":0,"英语":0}
    # 设置成绩
    def setGrade(self,course,grade):
        self.grade[course] = grade
    def getGrade(self):
        return self.grade
    def print(self):
        print(f"姓名{self.name} 年龄 {self.age} 的各科成绩：")
        for e in self.grade:
            print(f"科目{e} 分数{self.grade[e]}")

liu = Student("小刘",18)
shen = Student("小沈",22)
liu.setGrade("数学",88)
liu.setGrade("英语",89)
shen.setGrade("语文",96)
print(liu.grade)
print(shen.grade)
