"""

class HighSchool:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.grade = c
        self.classes = []

    def addClass(self):
        self.classes.append(input("추가할 과목을 입력하세요"))

    def removeClass(self):
        self.classes.remove(input("제거할 과목을 입력하세요"))

class Classes:
    def __init__(self, a, b, c, d):
        self.name = a
        self.mid = b
        self.fin = c
        self.activity = d

    def calScore(self):
        return self.mid + self.fin + self.activity

"""
class Course:
    def __init__(self, title, midterm, final, performance):
        self.title = title
        self.midterm = midterm
        self.final = final
        self.performance = performance


    def intro(self):
        print(f"{self.title}")

    def getGrade(self):
        print(f"과목명 : {self.title}")
        # 반영 비율 4:4:2
        total = self.midterm * 0.4 + self.final * 0.4 + self.performance * 0.2
        if total >= 90 and total <= 100:
            print('A')
        elif total >= 80 and total < 90:
            print('B')
        elif 70 <= total < 80:
            print('C')
        elif total >= 60 and total <= 70:
            print('D')
        else:
            print('F')

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def enroll(self):
        title = input("과목이름")
        mid = int(input("중간 점수"))
        fin = int(input("기말 점수"))
        perf = int(input("수행 점수"))

        self.courses.append(Course(title,mid,fin,perf))

    def checkScore(self):
        if len(self.courses) == 0:
            print("등록된 과목이 없습니다")
            return
        else:
            for i in self.courses:
                i.getGrade()

    def dropCorses(self):
        if len(self.courses) == 0:
            print("등록된 과목이 없습니다")
            return
        else:
            for index,item in enumerate(self.courses): #몇번짼지 알려주는 함수 enumerate
                print(f'{index}. \n')
                item.intro()
            delete = int(input("삭제할 과목번호:"))
            del self.courses[delete]

    def checkCourses(self):
        print(self.courses)


kyle = Student("kyle",11,4)
