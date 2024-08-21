def min(*numbers):
    min_value=numbers[0]
    max_value=numbers[0]
    for number in numbers:
        if min_value>number:
            min_value=number
        if max_value<number:
            max_value=number
    return  min_value,max_value
#튜플 자료형 ()
result=min(8,2,45,6,7,9)
print(result)
a,b=min(67,45,23,89,120,23)
print("최솟값:",a, "최댓값:",b)