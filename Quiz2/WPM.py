"""WPM"""
def kids(rank):
    """kids"""
    if rank < 11:
        return "Very Slow"
    elif 11 <= rank <= 20:
        return "Slow"
    elif 21 <= rank <= 30:
        return "Average"
    elif 31 <= rank <= 40:
        return "Fast"
    else:
        return "Very Fast"
def adults(rank):
    """adults"""
    if rank < 26:
        return "Very Slow"
    elif 26 <= rank <= 35:
        return "Slow/Beginner"
    elif 36 <= rank <= 45:
        return "Intermediate/Average"
    elif 46 <= rank <= 65:
        return "Fast/Advanced"
    elif 66 <= rank <= 80:
        return "Very Fast"
    else:
        return "Insane"
def main(gen, rank):
    """main"""
    if gen == "Kids":
        print(kids(rank))
    else:
        print(adults(rank))
main(input(), int(input()))
