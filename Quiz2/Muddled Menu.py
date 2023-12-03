"""Muddled Menu"""
def main():
    """Muddled Menu"""
    res = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "SOMETHING'S WRONG":
            res.clear()
            continue
        elif menu == "CLOSED":
            res.clear()
            break
        elif menu[:10] == "Can't do: ":
            res.remove(menu[10:])
        else:
            menu = menu.split(" #")
            if menu[1].isnumeric():
                res.insert(int(menu[1])-1, menu[0])
            else:
                res.append(menu[0])
    print("Full Course: " +str(res) + " Reversed: " +str(res[::-1]))
main()
