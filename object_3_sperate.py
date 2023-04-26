#클래스 선언
class Student:
    
    count = 0
    
    def __init__(self,name,korean,math,english,science):#생성자
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        
    def get_sum(self):
        return self.math+self.korean+self.english+self.science
     
    def get_average(self):
        return self.get_sum()/4
        
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
 #학생 리스트를 선언       
students = [
   Student(name="윤인성", korean=87, math=98, english=88, science=95),
   Student(name="연하진", korean=87, math=98, english=88, science=95),
   Student(name="구지연", korean=87, math=98, english=88, science=95),
   Student(name="나선주", korean=87, math=98, english=88, science=95)
]

isinstance(students, Student)

#학생을 한명씩 반복
print("이름", "총점", "평균",sep="\t")
for student in students:
    #출력
    print(student.to_string())

print("총 인원 {}명".format(Student.count))