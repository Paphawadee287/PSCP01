"""Distinguish"""
def height_check():
    """height check"""
    tall = int(input())
    if tall > 180:
        print("You're hit the door edge.")
    else:
        print("Nothing happens.")
height_check()
