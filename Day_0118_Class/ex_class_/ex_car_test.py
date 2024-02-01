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



#-----------------------------------------------
# 자율 주행 자동차 클래스 생성
# 상속 적용하기
class AutoCar(Car):
    def __init__(self, wheel, color, number, kind):
        # 부모 객체 생성
        super().__init__( wheel, color, number,kind)

    def autodrive(self):
        print(f'{self.number} 차가 자율주행하고 있다.')

tesla = AutoCar('가','가', '가','가')

tesla.autodrive()


# 자율 비행자동차 클래스 생성
# 상속 적용하기

class FlyingAutoCar(AutoCar):
    def __init__(self,wheel,color,number,kind,fly):
        super().__init__(wheel,color,number,kind)
        self.fly=fly
    def flyingautodrive(self):
        print(f'{self.number} 차가 {self.fly}날개로 자율비행하고 있다.')


tesla2=FlyingAutoCar('넥센','검정',1001,'가',"엄준식")

tesla2.flyingautodrive()


#34.2.2 인스턴스를 만들 떄 값 받기

class person:
    def __init__(self,name,age,address):
        self.hello='안녕하세요'
        self.name=name
        self.age=age
        self.address=address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello,self.name) )


maria=person('마리아','20','서울시 서초구 반포동')
maria.greeting()

print(maria.name)
print(maria.age)
print(maria.address)

maria=person('마리아','20','서울시 서초구 반포동')
print(maria)


# 34.3 비공개 속성 사용하기

# __를 사용하여 표현한다.
# 클래스 바깥에서 접근하려고 하면 에러가 발생한다.

class wa:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet

    def pay(self,amount):
        if amount>self.__wallet:
            print("돈이 모자라네...")
            return
        self.__wallet-=amount
        print('이제 {0}원 남았네요'.format(self.__wallet))

maria=wa('마리아',20,'서울시 서초구 반포동',10000)
maria.pay(3000)



#연습 문제: 능력치와 '베기'가 출력되게 만들라

class Knight:
    def __init__(self,health,mana,armor):
        self.health=health
        self.mana=mana
        self.armor=armor

    def slash(self):
        print('베기')

x=Knight(542.4,210.3,38)
print(x.health,x.mana,x.armor)
x.slash()



#심사문제:게임 캐릭터 클래스 만들기, 애니 클래스를 작성하여 티버 스킬의 피해량이 출력되게 만드시오

class Annie:
    def __init__(self,health,mana,ability_power):
        self.health=health
        self.mana=mana
        self.ability_power=ability_power

    def tibbers(self,ability_power):
        print(f'티버의 피해량은 {ability_power}*0.65)+400입니다.')

health,mana,ability_power= map(float,input().split())

x=Annie(90,180,290)
x.tibbers()

