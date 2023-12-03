"""[Pre] Kayak"""
def main():
    """
    เรือ2 n-1
    เรือ1 2
    weigh1 - weigh2
    """
    val_n = int(input())
    weight = input()
    weight_list = weight.split()
    
    mylist = []

    for i in range(len(weight_list)):
        for j in range(i + 1, len(weight_list)):
            weight1 = int(weight_list[i])
            weight2 = int(weight_list[j])
            result = abs(weight1 - weight2)
            mylist.append(result)
    sorted_mylist = sorted(mylist)
    all_num = sorted_mylist[:val_n - 1]
    print(all_num)
    # mylist = []
    # check = weigh.split(" ")
    # mylist.append(check)
    # print(mylist)
main()