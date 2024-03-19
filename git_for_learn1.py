#<Q1>
# def average(n1,n2):
#     result = (n1+n2)/2
#     print(result)

# a = int(input())
# b = int(input())

# average(a, b)


#<Q2>
# def add(n1,n2):
#     result = n1+n2
#     print(result)

# a = int(input())
# b = int(input())

# add(a, b)

#<Q3>
# def name_input():
#     name = str(input())
#     return name

# year = int(input())

# print(name_input(), year)

#<Q4>
import numpy as np
manu = {'딸기 탕후루': 3000, '샤인머스켓 탕후루': 3500, '레몬 탕후루': 3500 , '자몽 탕후루': 3500}
price = []
for i in manu.keys():
    price.append(manu[i])
prices = np.array(price)

def manu_print():
    print(manu)

def culculate():
    input_money = int(input())
    use = list(map(int, input().split()))
    uses = np.array(use)
    use_money = prices * uses
    use_moneys = np.sum(use_money)
    charge = input_money - use_moneys
    print("총금액:",use_moneys, "잔돈:",charge)

manu_print()
culculate()
