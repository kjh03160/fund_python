from random import randint

number_list= []
for i in range(100):
    random_number = randint(0, 100)
    # while random_number in number_list:
    #     random_number = randint(0, 100)
    number_list.append(random_number)

print("A = %s" % number_list)
print(len(number_list))
average = sum(number_list) / len(number_list)
print(average)

from random import randint

number_list2 = []
while len(number_list2) < 100 :
    random_number2 = randint(0, 100)
    number_list2.append(random_number2)

print(number_list2)
print(len(number_list2))
average = sum(number_list2) / len(number_list2)
print(average)