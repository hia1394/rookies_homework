list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [i for i in list1 if i%2==0]
list3 = [j**2 for j in list2]

print(f"원본 리스트: {list1}")
print(f"짝수들: {list2}")
print(f"짝수의 제곱: {list3}")
