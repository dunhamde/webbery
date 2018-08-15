def oneaway(a, b):
    lena = len(a)
    lenb = len(b)
    if a == b:
        return False
    if abs(lena - lenb) > 1:
        return False
    if lenb < lena:
        temp = a
        a = b
        b = temp

    for i,c in enumerate(a):
        if a[i] != b[i]:
            if a[i+1:] == b[i+1:]:
                return True
            elif a[i:] == b[i+1:]:
                return True
            elif a[i+1:] == b[i:]:
                return True
            else:
                return False
    return True

def test_oneaway():
    if oneaway('bake','pale'):
        print('true') 
    else:
        print('false')

def check_palindrome(string):
    strmap = dict()
    for c in string:
        if c not in strmap.keys():
            strmap[c] = 1
        else:
            strmap[c] = strmap[c] + 1
    if len(string)%2 == 0:
        print('even')
        for key in strmap.keys():
            if strmap[key] != 2:
                return False
        return True
    else:
        print('odd')
        oneoff = False
        for key in strmap.keys():
            if strmap[key] != 2:
                if strmap[key] != 1:
                    return False
                else:
                    if oneoff == True:
                        return False
                    oneoff = True
        return True

def test_palindrome():
    if not check_palindrome('derekrk'):
        print('not pal')
    else:
        print('palindrome')

def urlify(strarr, len):
    print("array len: " + str(len))
    print(strarr)
    end = len - 1
    foundword = False
    for index in range(end, 0, -1):
        if strarr[index] != ' ':
            print('end: ' + str(end))
            print('index: ' + str(index))

            foundword = True
            strarr[end] = strarr[index]
            end = end - 1
            print(strarr)
        else:
            if foundword:
                print('end: ' + str(end))
                print('index: ' + str(index))

                strarr[end-2:end+1] = '%20'
                end = end - 3
                print(strarr)
            
def test_urlify():
    url = ['M','r',' ','J','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' ']
    url2 = ['M','r',' ',' ','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' ',' ',' ']
    
    urlify(url2, len(url2))
    
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

def test_isperm():
    if IsPerm("catkdogg","ggotdac"):
        print("perm found")
    else:
        print("not a perm!")

test_oneaway()


