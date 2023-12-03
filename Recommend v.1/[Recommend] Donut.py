"""[Recommend] Donut"""
def donut(price, buy, free, want):
    """donut!!!"""
    piece = buy + free
    total_piece = want // piece
    total_price = buy * price
    left = want - (total_piece * piece)
    if left >= buy:
        total_piece += 1
        left = 0
    print(total_piece * total_price + left * price, piece * total_piece + left)
donut(int(input()), int(input()), int(input()), int(input()))
