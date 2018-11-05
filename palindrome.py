def palindrome():
    for num in range(100000,1000000):
        if str(num)[len(str(num))-1] ==str(num)[len(str(num))-4] and str(num)[len(str(num))-2] ==str(num)[len(str(num))-3]:
            if str(num+1)[len(str(num+1))-1] ==str(num+1)[len(str(num+1))-5] and str(num+1)[len(str(num+1))-2] ==str(num+1)[len(str(num+1))-4]:
                if str(num+2)[len(str(num+2))-2] ==str(num+2)[len(str(num+2))-5] and str(num+2)[len(str(num+2))-3] ==str(num+2)[len(str(num+2))-2]:
                    if str(num+3)[len(str(num+3))-1] ==str(num+3)[len(str(num+3))-6] and str(num+3)[len(str(num+3))-2] ==str(num+3)[len(str(num+3))-5]and str(num+3)[len(str(num+3))-3] ==str(num+3)[len(str(num+3))-4]:
                        print(num)
                        
if __name__ == '__main__':
    palindrome()
