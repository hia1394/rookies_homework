list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

print(f"리스트1: {list1}\n리스트2: {list2}")

num = list(set(list1)&set(list2))
n_list = list1+list2 

for i in num:
    n_list.remove(i)
print(f"병합된 리스트: {n_list}")
print(f"공통 요소: {num}")