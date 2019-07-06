def countOfAtoms(formula):
    stack = [1]
    i = len(formula) - 1
    nums_str = ""
    num = 1
    element = ''
    atom_count = {}
    while i >= 0:

        while '0' <= formula[i] <= '9':
            nums_str = formula[i] + nums_str
            i -= 1

        if nums_str != "":
            num = int(nums_str)

        if formula[i] == ")":
            stack.append(stack[-1]*num)
        elif 'a' <= formula[i] <= 'z' or 'A' <= formula[i] <= 'Z':
            while 'a' <= formula[i] <= 'z':
                element = formula[i] + element
                i -= 1
            element = formula[i] + element
            if element in atom_count:
                atom_count[element] += num*stack[-1]
            else:
                atom_count[element] = num*stack[-1]
        else:  # if (
            stack.pop()
        nums_str = ""
        num = 1
        element = ''
        i -= 1

    outputs = ["{}{}".format(k, v) if v > 1 else k for k,
               v in atom_count.items()]
    outputs.sort()
    str_output = "".join(outputs)
    return str_output


print(countOfAtoms("H2O"))
print(countOfAtoms("Mg(OH)2"))
