#Book 제목, 작가, 가격 + 인트로함수
class Book:
    def __init__(self,a,b,c):
        self.title = a
        self.author = b
        self.price = c

    def intro(self):
        print(f"이 책의 제목은 {self.title}이며, 작가는 {self.author}, 가격은 {self.price}원입니다.")

book1 = Book("집에가서","자고싶다",23000)
book1.intro()

# 서점class 지점, booklist + 함수(책 도입하기)
class BookStore:
    def __init__(self,a):
        self.branch = a
        self.bookList = [] ## 여기는 초기화 단계에서는 변수로 정의할 필요가 없었던것.

    def buyBook(self,a):
        self.bookList.append(a) #self.bookList가 []<-리스트.

    def showBookList(self):
        for i in self.bookList: #이때 i 는 Book <<을 우리가 넣어줘서. 근데 python이라서 걍 넘어가는데 다른언어는 오류뜸. 오류를 방지하려면 if 로 case를 나눠주는게 정석.
            i.intro()

sinchon = BookStore("교보신촌")
sinchon.buyBook(Book('집에가고싶다','김해인',23000))
sinchon.buyBook(Book('진심 그만하고 싶다','이해인',40000))
sinchon.showBookList()
