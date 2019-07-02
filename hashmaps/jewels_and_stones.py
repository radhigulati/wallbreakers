# My solution
def numJewelsInStones(J, S):
    count = 0
    for jewel in J:
        for stone in S:
            if jewel == stone:
                count += 1
            else:
                continue
    return count

# faster solution


def numJewelsInStones(J, S):
    jewelToStone = {}
    count = 0

    for jewel in J:
        if jewel not in jewelToStone:
            jewelToStone[jewel] = 1
        else:
            jewelToStone[jewel] += 1

    for stone in S:
        if stone in jewelToStone:
            count += 1
        else:
            continue
    return count


print(numJewelsInStones('aA', 'aAAbbbb'))
print(numJewelsInStones('z', 'ZZ'))
