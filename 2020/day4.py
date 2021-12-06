from file_in import load, checkHex

def process_input(l):
    l = load(l)

    listOfPassports=[]
    tempPassport = []
    for n in enumerate(l):
        #print ("New line!")
        if n[1] != "\n":
            #tempPassport += [ entries.split(":", 1)[0] for entries in n[1].split() ]
            tempPassport += [ entries for entries in n[1].split() ]
            #print ("Added new headers/entries to this passport!")
        if n[1] == "\n" or n[0] == len(l) - 1:
            listOfPassports.append (tempPassport)
            tempPassport = []
            #print ("New passport!")
    return listOfPassports

def isValidHeaders(passport):
    passportHeaders = [ header.split(":", 1)[0] for header in passport]
    #staticValidation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    # Commenting out proper code for the user's hack
    staticValidation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for header in staticValidation:
        if header not in passportHeaders:
            return False
    return True

def validateData(passport):
    for entry in passport:
        header = entry.split(":",1)[0]
        data = entry.split(":",1)[1]
        if header == "byr":
            if not ( int(data) >= 1920 and int(data) <= 2002 ):
                return False
        elif header == "iyr":
            if not ( int(data) >= 2010 and int(data) <= 2020 ):
                return False
        elif header == "eyr":
            if not ( int(data) >= 2020 and int(data) <= 2030):
                return False
        elif header == "hgt":
            if ( data.lower().endswith("cm")):
                if not ( data.lower().split("cm",1)[0].isnumeric() ):
                    return False
                elif not ( int(data.lower().split("cm",1)[0]) >= 150 and int(data.lower().split("cm",1)[0]) <= 193 ):
                    return False
            elif (data.lower().endswith("in")):
                if not ( data.lower().split("in",1)[0].isnumeric() ):
                    return False
                elif not ( int(data.lower().split("in",1)[0]) >= 59 and int(data.lower().split("in",1)[0]) <= 76 ):
                    return False
            else:
                return False
        elif header == "hcl":
            if not ( data[0] == "#" ):
                return False
            if not ( len(data) == 7 ):
                return False
            if not ( checkHex(data[1:]) ):
                return False
        elif header == "ecl":
            eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if data not in eyeColors:
                return False
        elif header == "pid":
            if not ( len(data) == 9 and data.isnumeric() ):
                return False
        elif header == "cid":
            pass
    return True
                    
if __name__ == "__main__":

    i = process_input('input4.txt')
    validCount = 0

    for passport in i:
        if isValidHeaders(passport) and validateData(passport):
            validCount += 1
            print ("Found valid")
        else:
            print ("Found invalid")

    print ("Valid count: " + str(validCount))