import random
#함수정의,매개변수
def rolling_dice(pip,reapt):
    for r in range(reapt):
        n=random.randint(1,pip)
        print(r, n)

#함수호출
rolling_dice(6,5) #인수, 인자 

