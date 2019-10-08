from random import randint

print("구구단을 외자~ 구구단을 외자~")

chance = 5
while True:
    a = randint(1, 9)
    b = randint(1, 9)
    print("Computer : \n%d * %d" % (a, b))
    answer = int(input("답 : "))

    if chance == 0:
        print("GG")
        break

    if answer == a * b:
        chance -= 1
        print("%d번만 더 맞추시면 됩니다." % chance)
        print("Player : ")
        a, b = map(int, input().split(","))
        print("%d * %d" % (a, b))
        print("답 : %d" % (a * b))
    else:
        print("You Lose!")
        break

a()