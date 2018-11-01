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
        
def no_e():
    with open("words.txt") as file:
        linecount= 0
        count = 0
        for line in file:
            linecount+=1
            if not 'e' in line:  
                count +=1
        print(f"%{(count/linecount)*100}")
        
def avoids(word,str):
    for l in str:
        for i in range(len(word)):
             if l == word[i]:
                 return False
                
    else:
        return True
def count_avoids(word,str):
    word = input("word:")
    str = input("letters:")
if __name__=="__main__":
    avoids("toll", 't')