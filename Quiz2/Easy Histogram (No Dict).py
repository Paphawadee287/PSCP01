"""Easy Histogram (No Dict)"""
def main(txt):
    """main"""
    count = 0
    current = ""
    new = "".join(sorted(txt, key=lambda x: (x.lower(), x.isupper(), x)))

    for i in new:
        if i == current:
            count += 1
        else:
            if current:
                print("%s = %d" %(current, count))
            current = i
            count = 1
    if current:
        print("%s = %d" %(current, count))

main(input().replace(" ", ""))