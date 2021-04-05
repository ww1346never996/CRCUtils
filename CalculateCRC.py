import CRCUtils as CRCut

reg = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
code = input("请输入需要进行CRC校验的报文：")
# 计算CRC码
CRC = CRCut.calculateCRC(code, reg)
# 转为16进制
print(hex(int(''.join([str(t) for t in CRC]), 2))[2:].zfill(4))
