"""MoreEntryway"""
def display():
    """display 20 lines"""
    print("Output_", end="")
    print(*range(1, 21), sep="\nOutput_")
display()

"""
def main(i):
    if i <= 20:
        #i += 1
        print("Output_%d" % i)
        main(i+1)
        return
main(1)
"""