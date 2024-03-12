import sys
city_num = int(sys.stdin.readline()) # 4
city_len = list(map(int,sys.stdin.readline().split())) # 2 3 1 
oil_cost = list(map(int,sys.stdin.readline().split())) # 5 2 4 1 

oil_min = oil_cost[0]
min_cost = city_len[0] * oil_cost[0]

for i in range(1,city_num-1):
  if oil_cost[i] < oil_min:
    oil_min = oil_cost[i]
  min_cost += oil_min * city_len[i]
print(min_cost)

# 처음엔 기름을 무조건 넣어야하므로 넣고 그 후에는 작은 기름값을 계속 바꿔주며 계산
