"""Run Length Encoding"""
def main(txt):
    """main"""
    current_txt = txt[0]
    count = 1
    result = ""
    for i in range(1, len(txt)):
        if txt[i] == current_txt:
            count += 1
        else:
            result += str(count) + current_txt
            current_txt = txt[i]
            count = 1
    result += str(count) + current_txt
    print(result)
main(input())
