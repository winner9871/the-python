def table_creater():
    table = {}
    for value in range(16):
        if value <= 9:
            table[str(value)] = bin(value)[2:].zfill(4)
        else:
            table[chr(value + 55)] = bin(value)[2:]
    return table


if __name__ == "__main__":
    table = table_creater()
    HEXrepresentation = input("Enter HEX value :\t").strip().upper()
    
    if HEXrepresentation[0] == "-":
        binaryEquivalent = "-"
    else:
        binaryEquivalent = ""

    for digit in HEXrepresentation:
        binaryEquivalent += table[digit]

    print(f"({HEXrepresentation})_16 binaryEquivalent : ({binaryEquivalent})_2")

