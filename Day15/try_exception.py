#3대 에러
##1.컴파일 에러:문법오류(실행전 오류) <--컴파일러가 잡아줌. 빨간줄 <=====미리잡아줘서 안잡아줘도됨
##2.런타임 에러:실행중 오류 <--예: 정수를 입력하는 곳인데 str 입력하기. ============> 얘만 잡으면됨 = 예외처리구문
##3. 컨텍스트 에러:사람만 알 수 있는 오류(테스터가 있는 이유) <--예: 게임 버그 <======테스터가 잡아줄거라 내가 안잡아도됨.

#예외처리구문(Try-Except 구문): try->except->else->finally 순은 지켜야댐
## 정의: 예외(Exception)는 프로그램 실행 중에 발생하는 예기치 않은 상황이나 오류를 의미함. 예외 처리(Exception Handling)는
######## 이러한 예외 상황을 감지하고, 프로그램을 안전하게 종료하거나 문제를 해결하기 위해 정의된 방식으로 처리하는 기술입니다.
# try: 예외가 발생할 가능성이 있는 구문
# except: 예외가 발생하면 실행되는 구문
#else: 예외가 실행되지 않으면 실행되는 구문
#finally: 예외가 발생하든 발생하지 않든 무조건 실행되는구문
try:
    num = int(input("숫자 입력:"))
    print(f"결과:{10/num}")
except ValueError:
    print("숫자를 넣으세요")
except ZeroDivisionError:
    print("0넣지 마세요")
else: #except을 어떤것도 거치지 않으면
    print("에러 안남")
finally: #except과 상관없이 항상.
    print("코드끝!")


# 에러가 발생할 수 있는 경우 (주요 에러) ######## 갑자기: 아래 Error들은 Error 부모 Class의 하위 클래스들
## ValueError: type은 맞는데 값이 다른경우
## IndexError: 리스트,튜플 등
## KeyError: 딕셔너리
## AttributeError: 딕셔너리에서 item
## ZeroDivisionError: 숫자/0으로 나누려고할때
## TypeError: 연산대상의 type이 적절하지 않을 때

"""

except ValueError:
    print("숫자를 넣으세요")
except ZeroDivisionError:
    print("0넣지 마세요")
    
이걸

except Exception: 으로 묶을 수 있음


"""