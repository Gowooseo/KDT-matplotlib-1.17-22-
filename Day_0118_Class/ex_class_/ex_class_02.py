#
# 자동차 클래스
# 클래스이름:car
# 클래스속성: 바퀴,색상,차번호,차종류,제조사(클래스속성)
#           12,빨강,차번호,세단,현대
#           12,빨강,차번호,세단,현대
# 클래스 기능: 주행,정지,후진
#--------------------------------------
class Car:
    # 클래스 속성
    maker='현대'

    # 생성자 메서드=> 객체 즉, 인스턴스 생성 메서드

    def __init__(self,wheel,color,number,kind):
        #힙 영역에 저장
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind

    # 객체 즉, 카 인스턴스 메서드
    def driving(self,where,who):
        print(f'{where}에 {self.number} 차가 드라이빙하고 있다.')
    def stop(self,place):
        print(f'{self.number} 차가 {place}에 정지 한다.')

    def back(self):
        print(f'{self.number} 차가 후진하고 있다.')


# 자동차 인스턴스 생성

#-----------------------------------------------
myCar=Car(19,'red','1111','세단')
secondcar=Car(20,'hotpink','7777','SUV')





#---------------------------------------------
# 사랑 클래스
# 클래스이름:Love
# 클래스속성:kind,platonic,agape, (클래스속성)
# 클래스 기능: 금융치료하기,,깻잎뗴주기,같이 아프기
#             대신죽어주기, 희생하기
#---------------------------------------------------
# class Love:
#     pass
#
#     def __init__(self,kind,platonic,agape):
#         self.kind = kind
#         self.platonic = platonic
#         self.agape = agape
#
#     def money(self,who,what):
#         print(f'{who}에게 {what}으로 금융치료한다.')
#
#     def GivingPerillaleaves(self,who):
#         print(f'{who}에게 깻잎을 까준다.')
#
#     def cosicking(self,who):
#         print(f'{who}와  같이 아픈다.')
#
#     def sacrifice(self,who):
#         print(f'{who}를 대신하여 희생한다.')
#
#
#
# myLove=(1,)


#---------------------------------------------------------
# 계산기 클래스
# 클래스이름:Calc
# 클래스속성: 브랜드,종류,색상,크기,가격,
# 클래스기능: 덧셈,뺄셈,곱셈,나눗셈
# - 데이터 => 속성 또는 기능에서 매개변수
#----------------------------------------------------------
class Calc:
    #클래스 변수
    maker='casio'
    _size=(7,15)

    # 객체 즉 인스턴스 생성 메서드
    def __init__(self,kind,color,price,info):
        self.kind=kind
        self.color=color
        self.__size=(7,15)  # 비공개 속성 __ 속성명 : 클래스 밖에서 속성을 읽거나 쓰기 불가
        self.price=price
        self.__info=info    # 인스턴스 생성 시 계산기에 각인되는 정보
        self.data=0

    #비공개 인스턴스 속성 읽기/쓰기 메서드
    def getInfo(self):
        return self.__info
    def setInfo(self,info):
         self.__info=info

    #비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    #=> 속성 읽기/쓰기 방식으로 동작하도록 설정

    @property   #선택 사항
    def info(self):
        return self.__info
    @info.setter
    def info(self,info):
        self.__info=info


    #덧셈 기능
    def plus(self,nums):
        self.data +=nums
    def minus(self,nums):
        self.data -=nums
    def multi(self,nums):
        self.data *= nums
    def div(self,nums):
        if not nums:
            return '0으로 나눌 수 없습니다.'
        self.data=self.data/nums

    def result(self):
        return self.data
#-----------------------------------------------
# Calc 클래스로 인스턴스 생성 => 합에 생성: 인스턴스 변수 + 클래스 변수
#----------------------------------------------
c1=Calc('공학용','블랙',10000,'홍길동계산기')

# 인스턴스 속성 읽기=> 공개 속성만 읽기 가능
print(c1.data,c1.color,c1.kind)
# 인스턴스 속성 변경=> 공개 속성만 읽기 가능
c1.color='빨강색'
#인스턴스 비공개 속성 읽기 ==> 전용에 메서드 getter/setter 통해서 읽기/쓰기
print(c1.getInfo(),c1.info)
# 인스턴스 속성 변경  ==> 전용에 메서드 getter/setter 통해서 변경
c1.setInfo("내꺼")
c1.info='내꺼야~~~~~'
#-----------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인이 가능
                                #인스턴스 변수나 메서드 사용 불가능!!
                                # self 값이 없음
#----------------------------------------------
print(Calc.maker)


#인스턴스 메서드에 접근 불가!!
#print(Calc.plus(10,2))

#-----------------------------------------------
# 자율 주행 자동차 클래스 생성
# 상속 적용하기
# 자율 비행자동차 클래스 생성
# 상속 적용하기
def autoCar(Car):
    def autodrive(self):
        print(f'{self.number} 차가 자율주행하고 있다.')
        super().__init__(self,)
