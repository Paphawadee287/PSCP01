"""[Midterm 2023] Niwarn World"""
import math
def find_x(val_n):
    """find x"""
    return 2 + (math.log(val_n ** 2, 2) / (2 * val_n * math.log(val_n, 2)))
def find_y(val_n, val_s):
    """find y"""
    return (math.sin(math.radians(30)) + (2 * val_s) ** 0.5) / (find_x(val_n) + 3)
def find_z(val_k):
    """find z"""
    return (find_y(val_k, val_k) ** 2) + (8456 * ((find_x(val_k)) ** 4) / (24 * val_k))
def main(val_n, val_s, val_k):
    """main"""
    val_x = find_x(val_n)
    val_y = find_y(val_n, val_s)
    val_z = find_z(val_k)
    print("X: %.1f, Y: %.1f, Z: %.1f" %(val_x, val_y, val_z))
main(float(input()), float(input()), float(input()))
