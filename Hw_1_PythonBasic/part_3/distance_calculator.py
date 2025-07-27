import math

point1 = (0,0)
point2 = (3,4)

n1 = (point1[0] - point2[0])**2
n2 = (point1[1] - point2[1])**2

print(f"점1: ({point1[0]},{point1[1]})")
print(f"점2: ({point2[0]},{point2[1]})")
print(f"두 점 사이의 거리: {(math.sqrt(n1+n2))}")