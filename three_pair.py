with open("words.txt") as file:
    for line in file:
        if len(line) >=6:
            for i in range(len(line)-6):
                if line[i] == line[i+1] and line[i+2] == line[i+3] and line[i+4]==line[i+5]:
                    print(line)
