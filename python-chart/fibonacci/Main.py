import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(20000)

INIT = 0
END = 10000

FIBO_DEFAULT = []
FIBO_TOP_DOWN = []
FIBO_BOTTOM_UP = []

class TimeCounter:
    def __init__(self):
        self.start = time.time()
        self.end = None

    def stop(self):
        self.end = time.time()

    def duration_ms(self):
        return (self.end - self.start) * 1000  # Em milissegundos

class Fibonacci:

    @staticmethod
    def fibonacci_default(n):
        return Fibonacci._fibo_helper(n)

    @staticmethod
    def _fibo_helper(n):
        if n == 0 or n == 1:
            return n
        return Fibonacci._fibo_helper(n - 1) + Fibonacci._fibo_helper(n - 2)

    @staticmethod
    def fibonacci_dynamic_top_down(n):
        memo = [-1] * (n + 1)
        return Fibonacci._fibo_top_down_helper(n, memo)

    @staticmethod
    def _fibo_top_down_helper(n, memo):
        if n == 0 or n == 1:
            return n
        if memo[n] == -1:
            memo[n] = Fibonacci._fibo_top_down_helper(n - 1, memo) + Fibonacci._fibo_top_down_helper(n - 2, memo)
        return memo[n]

    @staticmethod
    def fibonacci_dynamic_bottom_up(n):
        return Fibonacci._fibo_bottom_up_helper(n)

    @staticmethod
    def _fibo_bottom_up_helper(n):
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def main():
    # fibo_default()
    fibo_top_down()
    fibo_bottom_up()
    plot_results()

def fibo_default():
    for i in range(INIT, END + 1):
        timer = TimeCounter()
        Fibonacci.fibonacci_default(i)
        timer.stop()
        FIBO_DEFAULT.append(timer)

def fibo_top_down():
    for i in range(INIT, END + 1):
        timer = TimeCounter()
        Fibonacci.fibonacci_dynamic_top_down(i)
        timer.stop()
        FIBO_TOP_DOWN.append(timer)

def fibo_bottom_up():
    for i in range(INIT, END + 1):
        timer = TimeCounter()
        Fibonacci.fibonacci_dynamic_bottom_up(i)
        timer.stop()
        FIBO_BOTTOM_UP.append(timer)

def plot_results():
    x = list(range(INIT, END + 1))
    # y_default = [tc.duration_ms() for tc in FIBO_DEFAULT]
    y_top_down = [tc.duration_ms() for tc in FIBO_TOP_DOWN]
    y_bottom_up = [tc.duration_ms() for tc in FIBO_BOTTOM_UP]

    plt.figure(figsize=(12, 6))
    # plt.plot(x, y_default, label="Recursivo Simples", color='red')
    plt.plot(x, y_top_down, label="Top-Down", color='blue')
    plt.plot(x, y_bottom_up, label="Bottom-Up", color='green')

    plt.title("Comparação de Performance - Algoritmos de Fibonacci")
    plt.xlabel("n")
    plt.ylabel("Tempo de execução (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
