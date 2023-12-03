"""Easy Histogram"""
def main(txt):
    """main"""
    mydict = {}
    new = "".join(sorted(txt, key=lambda x: (x.lower(), x.isupper(), x)))
    for i in new:
        if i in mydict:
            mydict[i] += 1
        else:
            mydict[i] = 1
    for key, value in mydict.items():
        print("%s = %d" %(key, value))
    #res = "\n".join([f'{key} = {value}' for key, value in mydict.items()])
main(input().replace(" ", ""))
