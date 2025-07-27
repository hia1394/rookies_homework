import statistics

num = [10,20,30,40,50]

print(f"평균: {statistics.mean(num)}")
print(f"최댓값: {max(num)}")
print(f"최솟값: {min(num)}")
print(f"표준편차: {statistics.stdev(num):.2f}")