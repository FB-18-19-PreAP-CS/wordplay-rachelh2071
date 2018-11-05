for num in range(10,100):
    for diff in range(1,100):
        if str(num)[0]== str(num+diff)[1] and str(num+diff)[0]== str(num)[1]:
            print(num,diff)
