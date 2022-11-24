# inp_cost = input("")
inp_cost = 1260

count = 0

coin_types = [500,100,50,10]

for cost in coin_types:
    count += (inp_cost // cost) # 갯수
    inp_cost %= cost # 코스트계산


print(count)    
