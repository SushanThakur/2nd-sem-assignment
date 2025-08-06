class Student:
    def __init__(self, name, reg_no, marks):
        self.name = name
        self.reg_no = reg_no
        self.marks = marks  
    
    def getPercent(self):
        total = sum(self.marks)
        percent = (total / 500) * 100
        print(f'Total Percentage = {percent:.2f}%')  
    
    def getResult(self):
        print(f'Name = {self.name}')
        print(f'Reg. Number = {self.reg_no}')
        for i, mark in enumerate(self.marks, start=1):
            print(f'Mark {i} = {mark}')
        

marks = [10, 20, 40, 50, 90]
st1 = Student("Ram", "1001", marks)

st1.getPercent()
st1.getResult()

