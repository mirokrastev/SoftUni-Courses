import math

money = float(input())
money *= 100
money = math.floor(money)
counter = 0

while money > 0:
    if money / 200 >= 1:
        counter += 1
        money -= 200
    else:
        if money / 100 >= 1:
            counter += 1
            money -= 100
        else:
            if money / 50 >= 1:
                counter += 1
                money -= 50
            else:
                if money / 20 >= 1:
                    counter += 1
                    money -= 20
                else:
                    if money / 10 >= 1:
                        counter += 1
                        money -= 10
                    else:
                        if money / 5 >= 1:
                            counter += 1
                            money -= 5
                        else:
                            if money / 2 >= 1:
                                counter += 1
                                money -= 2
                            else:
                                if money / 1 >= 0:
                                    counter += 1
                                    money -= 1
print(counter)