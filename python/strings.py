def IsPerm(s1, perm):
    dicto = {}
    if len(s1) != len(perm):
        return False
    for c in s1:
        if c in dicto.keys():
            dicto[c] = dicto[c] + 1
        else:
            dicto[c] = 1
    for p in perm:
        if p in dicto.keys():
            if (dicto[p] == 0):
                print("not perm")
                return False
            else:
                dicto[p] = dicto[p] - 1
    for key in dicto.keys():
        print(key)
        if dicto[key] != 0:
            print("not perm")
            return False
    print("is perm")
    return True

if IsPerm("catkdogg","ggotdac"):
    print("this worked")
else:
    print("this worked too!")