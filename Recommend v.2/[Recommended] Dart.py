"""[Recommended] Dart"""
import math
def main(num):
    """main"""
    point = 0
    for _ in range(num):
        position = input().split(" ")
        valx = int(position[0])
        valy = int(position[1])
        distance = math.hypot(valx, valy)
        if distance <= 2:
            point += 5
        elif distance <= 4:
            point += 4
        elif distance <= 6:
            point += 3
        elif distance <= 8:
            point += 2
        elif distance <= 10:
            point += 1
    print(point)
main(int(input()))
