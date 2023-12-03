"""Colors"""
def main():
    """main"""
    mycolor = []
    for _ in range(2):
        color = input().lower()
        mycolor.append(color)
    if 'red' in mycolor and 'yellow' in mycolor:
        print('Orange')
    elif 'red'in mycolor and 'blue' in mycolor:
        print('Violet')
    elif 'blue' in mycolor and 'yellow' in mycolor:
        print('Green')
    elif mycolor[0] == mycolor[1] and (mycolor[0] and mycolor[1] in ('red', 'blue', 'yellow')):
        print(mycolor[0].title())
    else:
        print('Error')
main()
