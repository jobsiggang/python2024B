menu={"짬뽕":4000, "짜장면":6000,"탕수육":10000}
print(menu)
selected=input("메뉴를 선택하세요:")
if selected in menu:
    print(f"{selected}의 가격은{menu[selected]}입니다") #짜장면의 가격은 6000원입니다
else :
    menu[selected]=20000
    print(f"{menu}가 갱신되었습니다.")