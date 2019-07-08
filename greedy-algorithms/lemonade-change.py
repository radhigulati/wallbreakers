def lemonadeChange(bills):
    five = ten = 0
    for cash in bills:
        if cash == 5:
            five += 1
        elif cash == 10 and five:
            five -= 1
            ten += 1
        elif cash == 20 and five and ten:
            five -= 1
            ten -= 1
        elif cash == 20 and five >= 3:
            five -= 3
        else:
            return False
    return True


print(lemonadeChange([5, 5, 5, 10, 20]))  # True
print(lemonadeChange([5, 5, 10]))  # True
print(lemonadeChange([10, 10]))  # False
print(lemonadeChange([5, 5, 10, 10, 20]))  # False
