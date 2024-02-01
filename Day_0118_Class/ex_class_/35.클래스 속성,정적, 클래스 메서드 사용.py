#----------------
# class person:
#     bag=[]
#
#     def put_bag(self,stuff):
#         self.bag.append(stuff)



# self대신 다른 것을 사용해보자

# class person:
#     bag = []
#
#     def put_bag(self, stuff):
#         person.bag.append(stuff)


class person:
    bag = []

    def put_bag(self, stuff):
        person.bag.append(stuff)

james=person()
james.put_bag('책')

maria=person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)


#비공개 클래스 속성 사용하기

class Knight:
    __item_limit=10

    def print_item_limit(self):
        print(Knight.__item_limit)


x=Knight()
x.print_item_limit()

# print(Knight.__item_limit)  #클래스 바깥에서는 접근 불가능

# 35.2 정적 메서드 사용하기

#class 클래스이름:
 # @staticmethod
 # def 메서드(매개변수1,매개변수2):
 #     코드

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def multi(a, b):
        print(a * b)

Calc.add(10,20)  #클래스에서 바로 메서드 호출 클래스이름.메서드()
Calc.multi(10,20)

# 35.3 클래스 메서드 사용하기

# class 클래스 이름:
#     @classmethod
#     def 메서드(cls,매개변수1,매개변수2):
#         코드


# 사람 클래스 people을 만들고 인스턴스가 몇개 만들어졌는지 출력하는 메서드를 만들기

class people:
    count=0
    def __init__(self):
        people.count+=1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))

james=people()
maria=people()

people.print_count()

#35.5

#날짜 클래스 만들기

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year,month,day=map(int,date_string.split('-'))
        return month <=12 and day <=31