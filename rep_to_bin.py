def lookup_table_creater(BASE):
    table = {}
    for digit in range(BASE):
        if digit <= 9: representation = str(digit)
        else: representation = chr(digit + 96)
        table[representation] = digit

    return table

def repToDecimal(rep, BASE):
    table = lookup_table_creater(BASE)
    
    if "-" == rep[0]:
        sign = -1
        rep = rep[1:]
    else:
        sign = 1

    decimalEquivalent = 0
    for index, digitRep in enumerate(rep[::-1]):
        decimalEquivalent += table[digitRep] * (BASE ** index)

    return decimalEquivalent * sign

if __name__ == "__main__":
    BASE = int(input("Enter The Base:\t"))
    while BASE < 1:
        print("Base must be greater than equal to 1")
        BASE = int(input("Enter The Base:\t"))
    rep = input("Enter The Representation :\t")
    print("Decimal Equivalent :\t", repToDecimal(rep, BASE))
    
