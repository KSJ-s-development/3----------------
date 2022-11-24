# 입력받을 숫자 갯수 입력 받고 그만큼 숫자를 입력받는다
# 입력받은 숫자들 중 가장 큰 수 출력

# 입력받을 숫자 갯수 입력 받고 그만큼 숫자를 입력받는다
n = int(input("몇개의 숫자를 입력하시겠습니까? >> "))

# 숫자 입력받기
list1 = []
for i in range(n):
    data = int(input(f"입력 No.{i+1} >> "))
    list1.append(data)

list1.sort()
# 입력받은 숫자들 중 가장 큰 수 출력
print(f"가장 큰 수 : {list1[-1]}")