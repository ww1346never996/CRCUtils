# 16进制转2进制
def set16To2(code16):
    return list(map(int, bin(int(code16, 16))[2:].zfill(8)))


# 读取低位寄存器
def getRegLow(reg):
    return reg[8:16]


# 异或计算
def XORList(reg, regLo, codeList):
    parList = []
    for i in range(len(regLo)):
        parNum = regLo[i] ^ codeList[i]
        parList.append(parNum)
    reg = reg[0:8] + parList
    return reg


# 移位计算
def moveSet(reg):
    for i in range(8):
        parList = []
        if reg[15] == 0:
            for j in range(1):
                reg.insert(0, reg.pop())
        else:
            for k in range(1):
                reg.insert(0, reg.pop())
            reg[0] = 0
            AList = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            for l in range(len(reg)):
                parNum = reg[l] ^ AList[l]
                parList.append(parNum)
            reg = parList
    return reg


# 计算CRC码流程
def calculateCRC(code, reg):
    code16List = []
    i = 0
    while i < len(code):
        code16p = code[i: i + 2]
        code16List.append(code16p)
        i += 2
    for i in range(len(code16List)):
        code2 = set16To2(code16List[i])
        regLo = getRegLow(reg)
        reg = XORList(reg, regLo, code2)
        reg = moveSet(reg)
    reg = reg[8:16] + reg[0:8]
    return reg
