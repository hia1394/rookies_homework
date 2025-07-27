list1 = [2,4,6,8,10]
list2 = [1,3,5,7,12]

ans1 = all(i%2==0 for i in list1)
ans2 = any(j>10 for j in list1)
ans3 = all(k%2==0 for k in list2)
ans4 = any(l>10 for l in list2)

print(f"모든 숫자가 짝수인가? {(ans1)}")
print(f"하나라도 10보다 큰 수가 있는가? {(ans2)}")
print(f"모든 숫자가 짝수인가? {(ans3)}")
print(f"하나라도 10보다 큰 수가 있는가? {(ans4)}")