from day4 import validateData

if __name__ == "__main__":

    assert validateData(["byr:1919"]) == False, "Birthdate too early."
    assert validateData(["byr:2003"]) == False, "Birthdate too late."

    assert validateData(["iyr:2009"]) == False, "Issuedate too early."
    assert validateData(["iyr:2021"]) == False, "Issuedate too late."

    assert validateData(["eyr:2009"]) == False, "Expired."
    assert validateData(["eyr:2031"]) == False, "Expiration date too far in future."

    assert validateData(["hgt:1"]) == False, ""
    assert validateData(["hgt:1cm"]) == False, ""
    assert validateData(["hgt:1000cm"]) == False, ""
    assert validateData(["hgt:19823in"]) == False, ""
    assert validateData(["hgt:in"]) == False, ""
    assert validateData(["hgt:2in"]) == False, ""
    assert validateData(["hgt:2IN"]) == False, ""
    assert validateData(["hgt:20nin"]) == False, ""

    assert validateData(["hcl:#00000"]) == False, ""
    assert validateData(["hcl:000000"]) == False, ""
    assert validateData(["hcl:#abcdef"]) == True, ""
    assert validateData(["hcl:#bcdefg"]) == False, ""
    assert validateData(["hcl:#######"]) == False, ""

    assert validateData(["ecl:ambe"]) == False, ""
    assert validateData(["ecl:bl"]) == False, ""
    assert validateData(["ecl:GRY"]) == False, ""
    assert validateData(["ecl:grnn"]) == False, ""
    assert validateData(["ecl:other"]) == False, ""
    assert validateData(["ecl:blue"]) == False, ""

    assert validateData(["pid:1234567890"]) == False, ""
    assert validateData(["pid:a12345678"]) == False, ""
    assert validateData(["pid:000000000123456789"]) == False, ""
    assert validateData(["pid:000000001"]) == True, ""
    assert validateData(["pid:100000000"]) == True, ""