numbers = [1,2,3,4,5,6,7,8,9,10]

anw1 = list(map(lambda i:i**2, numbers ))
anw2 = list(filter(lambda j:j>5, numbers))
anw3 = list(map(lambda k:k**2, anw2))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {anw1}")
print(f"5보다 큰 수들: {anw2}")
print(f"5보다 큰 수들의 제곱{anw3}")