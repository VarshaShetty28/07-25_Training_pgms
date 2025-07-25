def Arithmetic_Or_Progression(prog):
    if len(prog) < 2:
        print("Need more than two number sequence")
        return

    is_AP = True
    is_GP = True
    AP_diff = prog[1] - prog[0]

    if prog[0] != 0:
        GP_ratio = prog[1] / prog[0]
    else:
        for i in prog:
            if i != 0:
                is_GP = False 
                break
        GP_ratio = 0

    for i in range(1, len(prog) - 1):
        if prog[i + 1] - prog[i] != AP_diff:
            is_AP = False

        if prog[i] == 0:
            if GP_ratio != 0:
                is_GP = False
        elif prog[i + 1] / prog[i] != GP_ratio:
            is_GP = False

        if not is_AP and not is_GP:
            break

    if is_AP and is_GP:
        print("Both Arithmetic and Geometric Progression")
    elif is_AP:
        print("Arithmetic Progression")
    elif is_GP:
        print("Geometric Progression")
    else:
        print("Neither Arithmetic nor Geometric Progression")


progression = input("Enter list : ")
progression = list(map(int, progression.strip().split()))
Arithmetic_Or_Progression(progression)
