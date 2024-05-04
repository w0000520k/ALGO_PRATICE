import math

A, B, V = map(int, input().split())

remaining_height = V - A

daily_gain = A - B

days = math.ceil(remaining_height / daily_gain)

days += 1

print(days)