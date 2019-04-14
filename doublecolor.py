tp = [int(i) for i in input().split()]
tt = []
tt.append([tp[0]-1,tp[1]])
tt.append([tp[0],tp[1]-1])
for i in range(2,tp[0]+tp[1]):
    temp = []
    for k in tt:
        for j in range(2):
            if j == 0 and k[j] - i >= 0:
                temp.append([k[j] - i,k[1]])
            elif j == 1 and k[j] - i >= 0:
                temp.append([k[0],k[1] - i])
    if not temp:
        print(len(tt))
        break
    tt = temp.copy()