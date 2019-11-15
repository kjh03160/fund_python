instr, outstr = "", ""
count, i = 0, 0

instr = input("문자열을 입력하세요 : ")
count = len(instr)

for i in range(count):
    outstr += instr[count - i - 1]

print(outstr)
