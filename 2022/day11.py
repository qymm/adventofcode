#https://adventofcode.com/2022/day/11

import sys
import math
import operator
import string

if __name__ == "__main__":

    operatorlookup = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
    }

    monkeys = []
    itm = []
    oper = []
    coe = []
    test = []
    res = []
    count = []

    def inspec (item, monke):

        monke.update({"count":monke.get("count")+1})

        op = monke.get("opr")[0] #find operation

        if monke.get("opr")[1] == "self":
            item = op(item,item) #exponential
        else:
            item = op(item,monke.get("opr")[1]) #apply coefficient
        #item = math.floor(item / 3)

        if item % monke.get("test") == 0:
            return item, monke.get("true")
        else:
            return item, monke.get("false")

    with open(sys.argv[1]) as file:
        chunks = file.read().split("\n\n")
        chunks = [x.strip().split("\n") for x in chunks]
        for chunk in chunks:
            items = [int(i.strip(",")) for i in chunk[1].strip().split(" ")[2:]]
            #print (chunk[2][23])
            if any(map(str.isdigit, chunk[2])):
                coeff = int("".join(filter(str.isdecimal, chunk[2])))
            else:
                coeff = "self"
            #print(items)
            chunkyMonkey = {
                "items":items,
                "opr":(operatorlookup.get(chunk[2][23]),coeff),
                "test": int("".join(filter(str.isdecimal, chunk[3]))),
                "true": int("".join(filter(str.isdecimal, chunk[4]))),
                "false": int("".join(filter(str.isdecimal, chunk[5]))),
                "count":0
            }
            itm.append(items)
            oper.append(operatorlookup.get(chunk[2][23]))
            coe.append(coeff)
            test.append(int("".join(filter(str.isdecimal, chunk[3]))))
            res.append((int("".join(filter(str.isdecimal, chunk[4]))),int("".join(filter(str.isdecimal, chunk[5])))))
            count.append(0)
            monkeys.append (chunkyMonkey)

        for r in range(10000):
            print("starting cycle",r)
            for i,monke in enumerate(monkeys):
                #print("starting monkey",i)
                #print(itm[i])
                for x,item in enumerate(itm[i]):
                    #print("starting item",item, x)
                    count[i] += 1
                    temp = itm[i][x]
                    if coe[i] == "self":
                        op = operator.pow
                        temp = op(temp,2)
                    else:
                        op = oper[i]
                        temp = op(temp,coe[i])

                    temp = temp % math.lcm(*test)
                    #temp = math.floor(temp/3)

                    if temp % test[i] == 0:
                        itm[res[i][0]].append(temp)
                    else:
                        itm[res[i][1]].append(temp)
                    #print(x,i)
                itm[i].clear()


        count.sort()
        print(count)
        print(math.prod(count[-2:]))