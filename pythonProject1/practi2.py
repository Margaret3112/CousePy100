# v = int(input("Возраст "))
# s = input("Пол ")
# l = int(input("Рост "))
# w = int(input("Вес "))
v, s, l, w = 30, 'Мужчина', 180, 80
age = [list(range(19,25)), list(range(25,35)),list(range(35,45)), list(range(45,55)), list(range (55,65))]
age1=age[0]
age2=age[1]
age3=age[2]
age4=age[3]
age5=age[4]

d = age[-1]
print(d)
if w > age1[-1]:
    imt = w/((l/100)**2)
    del_imt = (imt - age1[-1]) * (1.6 ** 2)
    print(del_imt)
elif ("Мужчина" in s) and (v in age2):
    imt = w/((l/100)**2)
    print(imt)
if ("Мужчина" in s) and (v in age2):
    imt = w/((l/100)**2)
    print(round(imt,2))

