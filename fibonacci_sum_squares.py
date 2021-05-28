# Uses python3
from sys import stdin


def get_pisano_period(m):
    a, b = 0, 1
    c = a + b

    for _ in range(m*m):
        c = (a+b) % m
        a = b
        b = c

        if (a == 0 and b == 1):
            return _ + 1

        
def get_fibonacci_huge_efficient(n, m):
    remainder = n % get_pisano_period(m)
    first, second = 0, 1
    res = remainder

    for _ in range(1,remainder):
        res = (first + second) % m
        first = second
        second = res
    
    return res % m
    
    
def fibonacci_sum_squares_efficient(n):
    return (get_fibonacci_huge_efficient(n, 10) * get_fibonacci_huge_efficient(n+1, 10)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_efficient(n))
