from file_in import load

def process_input(l):
    lower=[]
    upper=[]
    letter=[]
    password=[]
    l = load(l)
    for n in l:
        colon = n.find(":")
        dash = n.find("-")
        i = n[0:dash]
        lower.append(int(i))
        i = n[dash+1:colon-2]
        upper.append(int(i))
        i = n[colon-1:colon]
        letter.append(i)
        i = n[colon+1:len(n)-1]
        i = i.strip()
        password.append(i)
        
    return lower, upper, letter, password

if __name__ == "__main__":

    count = 0
    count2 = 0

    i = process_input('input2.txt')
    for n in range(0,len(i[3])):
        l = i[0][n]
        u = i[1][n]
        letter = i[2][n]
        p = i[3][n]
        if p.count(letter) >= l and p.count(letter) <= u:
            count += 1
        if (p[l-1] == letter and p[u-1] != letter) or (p[l-1] != letter and p[u-1] == letter):
                count2 += 1
    
    print(count)
    print(count2)
