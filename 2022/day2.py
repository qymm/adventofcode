#https://adventofcode.com/2022/day/2

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        games = [(l.strip()[:1],l.strip()[-1:]) for l in file]
        
        total = 0
        #PART 1
        for (i,j) in games:
            subtotal = 0
            
            #points for throw you make
            subtotal += ord(j) - 87 

            diff = (ord(j)-ord(i)-23+2)%3
            if diff == 2:
                subtotal += 3
                #print ("draw")
            elif diff == 1:
                subtotal += 0
                #print ("loser")
            elif diff == 0:
                subtotal += 6
                #print ("winner")
            total += subtotal

        print (total)

        #PART 2
        total = 0
        for (i,j) in games:
            subtotal = 0
            match j:
                case 'Z':
                    subtotal += 6
                    formula = ((ord(i)-65+1)%3)+1
                    subtotal += formula
                    #print("win",i," = ",formula)
                case 'Y':
                    subtotal += 3
                    formula = ((ord(i)-65)%3)+1
                    subtotal += formula
                    #print("draw",i," = ",formula)
                case 'X':
                    subtotal += 0
                    formula = ((ord(i)-65+2)%3)+1
                    subtotal += formula
                    #print("lose",i," = ",formula)
            total += subtotal
        
        print(total)

