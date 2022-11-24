
input_money = int(input("돈을 입력하세요. >>"))

count = []

# 큰 단위의 화폐부터 차례대로 확인하기
coin_list = [10000, 5000, 1000, 500, 100, 50, 10]

for coin in coin_list:
    count.append(input_money // coin)
    input_money %= coin # coin_list 만큼 한번씩 나누기

print(f"10,000원 통화 : {count[0]}개")
print(f"5,000원 통화 : {count[1]}개")
print(f"1,000원 통화 : {count[2]}개")
print(f"500원 통화 : {count[3]}개")
print(f"100원 통화 : {count[4]}개")
print(f"50원 통화 : {count[5]}개")
print(f"10원 통화 : {count[6]}개")