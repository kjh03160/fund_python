with open('test.txt', 'r') as file:
    file2 = open('text2.txt', 'w')

    length = len(file.readlines())
    file.seek(0, 0)                 # 위에서 다 읽어버렸기 때문에 다시 처음으로 되돌려야함

    for i in range(length):
        str = file.readline()

        if i % 2 == 0:
            file2.write(str)

    file2.close()