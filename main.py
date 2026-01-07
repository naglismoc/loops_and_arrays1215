import random
import time

# num = 12
#       0 1 2 3  4 5 6 7
nums = [3,5,9,78,5,0,7,20,9]
print(nums)
print(nums[0])
print(nums[1])
print(nums[7])
print(len(nums))
nums.append(60)
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.remove(9)#pasalins 4ta elementa, nes jo reiksme 9, pasalins tik viena
print(nums)
nums.insert(3, 30)
print(nums)
nums[3] = 9
print(nums)
print(nums.index(9))
nums[nums.index(9)] = 30
print(nums)

#             0              1            2          3
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius"]
print(vardai)
print(vardai[1])

belekas = [1, True, 'jo']

arr2d = [
    #0  1  2
    [2, 5, 6],# 0
    [84, 8, 3],# 1
    [7, 5, 9] # 2
]
print(arr2d)
print(arr2d[1][2])

#             0  1  2  3  4  5  6  7  8  9 indexai
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####################### PIRMAS PARAMETRAS INCLUSSIVE, JĮ IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO #################
####################### Multidimensiniose masyvuose galioja tos pacios taiykles ######################################
# my_numbers[pradzia:galas:zingsnis]
print(my_numbers) #atspausdins viską
print(my_numbers[6]) #atspausdins viena elementa
print(my_numbers[0:4]) #nuo iki
print(my_numbers[4:8])
print(my_numbers[7:])#nuo, iki galo
print(my_numbers[:4])# nuo pradzios iki nurodytos pozicijos
print(my_numbers[-2]) #antra pozicija nuo galo
print(my_numbers[-5:]) #nuo 5tos pozicijos nuo galo iki galo
print(my_numbers[:-5]) # nuo pradzios iki penktos nuo galo
print(my_numbers[2:-5]) #nuo 2os pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2]) #nuo 6tos nuo galo iki 2os nuo galo
print(my_numbers[-8:4]) #teoriskai veikia, bet neapsikraukit :D
print(my_numbers[:])#nuo pradzios iki galo
new_arr = my_numbers[:]# padaro kopiją
print(my_numbers[0:10:2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::3]) #kas trecias elementas
print(my_numbers[1::2]) #nuo pirmo elemento iki galo kas antras
print(my_numbers[3:7:2])
print(my_numbers[2:-2:2])
print(my_numbers[-8:8:2]) #nuo 8to nuo galo iki 8to nuo pradzios kas antras (nereiks tokiu, teoriskai imanoma)
print(my_numbers[::-1]) # visi elementai nuo galo, reverse
print(my_numbers[::-2]) #visi elementai nuo galo kas antras
print(my_numbers[5::-2]) #nuo 5 iki galo(tiksliau pradzios, nes einam atbulai ;) )
print(my_numbers[8:2:-2]) # nuo 8tos iki 2os, kas antras. 2a pozicija exclusive
print(my_numbers[-2:2:-2]) # nuo antros nuo galo iki antros pozicijos, kas antras atbulai

#             0              1            2          3        4
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius", "Jonas",'Vikrotas']
print(vardai)
for i in vardai:
    print(i)
print("--------")
for vyriskis in vardai:
    print(vyriskis)
print("--------")
for vyriskis in vardai:
    print(vardai[0])

print(range(0,4))

for i in range(0,4):
    print(i)

for i in range(4):
    print("labas")
print("--------")

for i in range(4):
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')
print("--------")

for i in range(len(vardai)):
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')
print("--------")

for i, vardas in enumerate(vardai):
    print(i, vardas)

names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
]
print(len(names))
# select name from names where length(name) < 5;
for name in names: # du identacijos lygiai
    if len(name) < 5:
        print(name)
for i, name in enumerate(names): #naudojame kai reikia pasiekti elemento poziciją ir elementą
    if i % 10 == 0:
        print(i, name)

print("-----------------------------------")
arr2d = [
    [1, 4, 10], # 0
    [3, 5, 8], # 1
    [1, 2, 3], # 2
    [5, 10, 5], # 3
]
print(arr2d)
total_sum = 0
total_count = 0
for row in arr2d:
    print(row)
    total_sum += sum(row)
    total_count += len(row)
# print(total_sum / (len(arr2d) * len(arr2d[0])))
print(total_sum / total_count)

total_sum = 0
total_count = 0
for row in arr2d:
    for cell in row:
        total_sum += cell
        total_count += 1
print(total_sum / total_count)

total_sum = 0
total_count = 0
for row in arr2d:
    for cell in row:
        if cell > 3:
            total_sum += cell
            total_count += 1
print(total_sum / total_count)
print("------------------------------------------")
for i in range(10):
    if i  == 5:
        continue
    print(i)

print("------------------------------------------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print("------------------------------------------")
for i in range(10):
    if i == 5:
        break
    print(i)


for name in names:
    if name == "Patrick":
        print(name)
        break
    else:
        print("looking...")

for name in names:
    if len(name) < 8:
        continue
    letter1 = name[0] * len(name)
    new_name = letter1 + name[1:]
    new_name = new_name.upper()
    print(new_name)

print("-------------------------------")
for name in names:
    if len(name) >= 8:
        letter1 = name[0] * len(name)
        new_name = letter1 + name[1:]
        new_name = new_name.upper()
        print(new_name)

count = 0
while True:
    count+= 1
    if count >= 5:
        break
    print(count)
print("----------------------------")
count = 0
should_continue = True
while should_continue:
    count += 1
    if count >= 5:
        should_continue = False
    print(count)

# print("----------------------------")
# count = 0
# while count < 20: #bet cia jau veikia kaip for ciklas, tai geriau ir naudokit for
#     count+= 1
#     print(count)

print("----------------------------")
while True:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        break

print("----------------------------")
start_time = time.time()
count = 0
for i in range(10000):
    while True: #0,1666666666666667
        dice = random.randint(1,6)
        count +=1
        # print(dice)
        if dice == 6:
            break
print(f'meciau {count} kartu, kol iskrito 1000000 6tu. tikimybe yra {10000 / count}')
end_time = time.time()
print(f'paskaiciavimams prireikė {(end_time - start_time)  } sekundžių')