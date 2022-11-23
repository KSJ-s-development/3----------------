list1 = input("숫자를 3개 입력하세요.(숫자는 스페이스로 구분) >> ").split()

list1.sort()

print(f"가장 작은 수 : {list1[0]}")
print(f"중간 크기 수 : {list1[1]}")
print(f"가장 큰 수 : {list1[2]}")