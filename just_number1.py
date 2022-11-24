
# n, k = 17, 4

n, k = map(int, input("값 입력 >>").split())

count = 0
is_on = True

while is_on:
    if n == 1:
        print(f"{count}번 실행")
        count = 0
        is_on = False # n = 1일때 정지
    else : # n != 1일때
        count+=1
        if n % k == 0 : # n 나누기 k 가 0일때
            n /= k
        else : # n / k != 0
            n -= 1 # k로 나눠 떨어질 수 있게 n값에 -1 주기


