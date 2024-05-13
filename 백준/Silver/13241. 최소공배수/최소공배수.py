import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def main():
    import sys
    input = sys.stdin.read
    a, b = map(int, input().split())
    
    result = lcm(a, b)
    print(result)

if __name__ == "__main__":
    main()