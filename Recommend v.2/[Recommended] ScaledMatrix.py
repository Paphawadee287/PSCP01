"""[Recommended] ScaledMatrix"""
def main(val_m, val_n):
    """main"""
    all_matrix = []
    for _ in range(val_m*val_n):
        matrix = float(input())
        all_matrix.append(matrix)
    max_matrix = max(all_matrix)
    min_matrix = min(all_matrix)
    all_matrix = all_matrix[::-1]
    for _ in range(val_m):
        for _ in range(val_n):
            scale = (all_matrix.pop() - min_matrix) / (max_matrix - min_matrix)
            print("%.2f" %scale, end=" ")
        print()
main(int(input()), int(input()))
