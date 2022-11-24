n, m, k = map(int, input("몇개입력 받을지, 몇번 더할지, 몇번 중복가능한지 >> ").split())
data = list(map(int, input("입력 >> ").split()))

# n, m, k = 5,8,3
# data = [2,4,5,4,6]

if len(data) > n:
    # 입력받은값 초과 처리
    is_on = True
    while is_on:
        if len(data) <= n : # 길이가 같거나 작아지면 정지
            is_on = False
        else :
            del data[-1] # 끝에거 삭제

data.sort(reverse=True) # 데이터정렬, 큰수->작은수 순으로

count = 0
result = 0
for i in range(m): # 몇번 더할지
    # 몇번 중복
    if count < (k-1) : 
        result += data[0] #제일 큰수
        count +=1
    else : # count가 k-1이랑 같거나 커지면
        result += data[1] #그다음 큰 수 
        count = 0 

print(f"result : {result}")