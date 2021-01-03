# class
class A_class():
    def __init__(self):
        print("A_Class 입니다.")

    def stock(self):
        print("키움증권입니다.")
        return "키움"

aa = A_class()
result = aa.stock()
print(result)

# self
class B_class():
    def __init__(self):
        print("B_Class 입니다.")
        self.student_name = "손채건"
    def name(self):
        print("%s" % self.student_name)

B_class().name()
print(B_class().student_name)

# 상속
class Parent():
    def __init__(self):
        print("부모 클래스!")
        self.money = 1000000000;

class Child_1(Parent):
    def __init__(self):
        super().__init__()
        print("첫번째 자식입니다.")
        print(self.money)

class Child_2(Parent):
    def __init__(self):
        print("두번째 자식입니다.")

Child_1()
Child_2()