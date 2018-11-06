tdl = [[0]*2 for i in range(100)]
for num in range(10,110):
    for diff in range(1,100):
        if str(num)[0]== str(num+diff)[1] and str(num+diff)[0]== str(num)[1]:
            tdl[num-11][0] = num
            tdl[num-11][1] = diff
#print(tdl)

for i in range(len(tdl)):
    count = 0
    agediff = tdl[i][1]
    for i in range(len(tdl)):
        if agediff == tdl[i][1] and agediff !=0:
            count+=1
    if count == 7:
        print(agediff)
#for num in range(10,120):
#    for diff in range(1,100):
#        if str(num)[0]== str(num+diff)[1] and str(num+diff)[0]== str(num)[1]:
#            print(num,diff)

