
#def read_file():
#    
#    with open("words.txt") as file: #file is name of variable
#        count_the = 0
#        for line in file:
#            for word in line.strip().split(): #line.split() splits line on spaces
#                if "the" in word.lower():  #line.strip() removes new line character
#                    count_the +=1
#        print(count_the)
#if __name__=="__main__":
#    read_file()
def at_least():
    with open("words.txt") as file: #file is name of variable
        count_the = 0
        for line in file:
            for word in line.strip().split(): #line.split() splits line on spaces
                if len(word)>=20:  #line.strip() removes new line character
                    count_the +=1
        print(count_the)
def has_no_e(word):
    '''
>>> has_no_e('texas')
False
>>> has_no_e('longhorn')
True
>>> has_no_e('UTEP')
False
'''
    if 'e' in word.lower():
        return False
    else:
        return True
def no_e():
    with open("words.txt") as file:
        linecount= 0
        count = 0
        for line in file:
            linecount+=1
            if not 'e' in line:  
                count +=1
        print(f"{(count/linecount)*100:.3f}%")
        
def avoids(word,str):
    '''
>>> avoids('Texas','tpr')
False
>>> avoids('Texas','lmn')
True
>>> avoids('Longhorn','LHN')
False
>>> avoids('truffle','dre')
False
'''
    for l in str:
        for i in range(len(word)):
             if l.lower() == word[i].lower():
                 return False
                
    else:
        return True
def count_avoids():
    str = input('forbidden letters:')
    with open("words.txt") as file: #file is name of variable
        avoid = 0
        for line in file:
            for letter in line.strip().split():
                if avoids(line,str):
                    avoid+=1
                    
    print(avoid)
def uses_only(word,str):
    count = 0
    for i in range(len(word)):
        if word[i].lower() in str:
            count+=1
    if count == len(word):
        return True
    else:
        return False
def words_with_only(str):
    pass
if __name__=="__main__":
    import doctest
    doctest.testmod()
    count_avoids()
