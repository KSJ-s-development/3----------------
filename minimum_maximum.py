# 첫번째 줄 입력
n, m = map( int, input("row, column >> ").split() )

li = list()

for i in range(n):
    row = list(map(int, input(">> ").split()))
    li.append(min(row))

print(f"작은 수 중 큰 값 : {max(li)}")
