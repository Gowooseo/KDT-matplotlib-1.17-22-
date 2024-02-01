#  클래스 만들기

a=int(10)
b=list(range(10))
c=dict(x=10,y=20)
b.append(20)
print(b)

#파이썬에서는 자료형도 클래스이다.

class person:
    def greeting(self):
        print('Hello')




#인스턴스에 할당

james=person()    #인스턴스 생성(인스턴스=만든 클래스)
james.greeting()  # 인스턴스에 할당


# 메서드 안에서 메서드 호출
class person:
    def greeting(self):
        print('Hello')
    def greeting(self):
        print('Hello')

