num_list = []

for _ in range(9):
    num_list.append(int(input()))

TF = False    

for i in range(9):
    
    num_list_temp = num_list.copy()
    del num_list_temp[i]
    for k in range(8):
        num_list_temp1 = num_list_temp.copy()

        del num_list_temp1[k]

        if sum(num_list_temp1) == 100:
            TF = True
            break

    if TF:
        break

num_list_temp1.sort()

for i in num_list_temp1:
    print(i)
        
