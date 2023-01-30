//수정필요
//1번문제 록 페스티벌

num = int(input())

for _ in range(num):

  num_list = list(map(int,input().split()))

  cost = list(map(int,input().split()))

  result_list = []
  print(cost)
  for i in range(0,num_list[0] - num_list[1] + 1):
    result_list.append(sum(cost[i:i + num_list[1]])/num_list[1])
    print(sum(cost[i:i + num_list[1]]))

  print(result_list)
