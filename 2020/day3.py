from file_in import load

def process_input(l):
    o=[]
    l = load(l)
    for n in l:
        temp = n.strip("\n")
        o.append(temp)
    return o

def translate (xmove, ymove, text):
    trees = 0
    xpos = 0
    ypos = 0
    distance = len(text)
    width = len(text[0])

    while ypos < distance:
        if i[ypos][xpos%width] == '#':
            trees += 1
        ypos += ymove
        xpos += xmove
    return trees


if __name__ == "__main__":

    i = process_input('input3.txt')

    first = translate (1,1,i)
    second = translate (3,1,i)
    third = translate (5,1,i)
    fourth = translate (7,1,i)
    fifth = translate (1,2,i)
    result = first * second * third * fourth * fifth


    print (result)