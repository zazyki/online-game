def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def sendPos(n1, n2):
    return str(str(n1)+","+str(n2))
 