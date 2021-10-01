def mean(dataList):
    if len(dataList) == 0:
        return 0
    else:
        theSum = 0
        for dataValue in dataList:
            theSum += dataValue
        meanValue = theSum / len(dataList)
        return meanValue

def median(dataList):
    n = len(dataList)
    if n == 0:
        return 0
    elif n % 2 == 1:
        return dataList[n // 2]
    else:
        medianValue = (dataList[n // 2] + dataList[(n // 2) -1]) / 2
        return medianValue

def mode(dataList):
    if len(dataList) == 0:
        return 0
    else:
        freqOfMostAppearing = 0
        tmpCounter = 0
        modeValue = None
        alreadyVisited = []
        for dataValue in dataList:
            if dataValue not in alreadyVisited:
                alreadyVisited.append(dataValue)
                
                for element in dataList:
                    if element == dataValue:
                        tmpCounter += 1
                if tmpCounter > freqOfMostAppearing:
                    modeValue = dataValue
                    freqOfMostAppearing = tmpCounter
                elif tmpCounter == freqOfMostAppearing:
                    modeValue = (modeValue + dataValue) / 2
                
                tmpCounter = 0
        
        return modeValue
                

def main():
    data = [1, 2, 3, 3, 4, 4, 5, 8, 9, 10]
    print("Data is :", data)
    print("Mean Of Data is : ", mean(data))
    print("Median Of Data is : ", median(data))
    print("Mode Of Data is : ", mode(data))

if __name__ == "__main__":
    main()


