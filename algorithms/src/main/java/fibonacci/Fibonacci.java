package fibonacci;

import java.util.Arrays;

public class Fibonacci {

    private Fibonacci() {
    }

    public static void fibonacciDefault(long n) {
        fiboHelper(n);
    }

    private static long fiboHelper(long n) {
        if (n == 0 || n == 1)
            return n;

        return fiboHelper(n - 1) + fiboHelper(n - 2);
    }

    public static void fibonacciDynamicTopDown(long n) {

        long[] memo = new long[Math.toIntExact(n + 1)];
        Arrays.fill(memo, -1);
        fiboTopDownHelper(n, memo);

    }

    private static long fiboTopDownHelper(long n, long[] memo) {
        if (n == 0 || n == 1)
            return n;

        if (memo[(int) n] == -1) {
            memo[(int) n] = fiboTopDownHelper(n - 1, memo) + fiboTopDownHelper(n - 2, memo);
        }

        return memo[(int) n];
    }

    public static void fibonacciDynamicBottomUp(long n) {

        fiboBottomUpHelper(n);

    }

    private static long fiboBottomUpHelper(long n) {

        if (n == 0 || n == 1)
            return n;

        long a = 0;
        long b = 1;
        long c = 0;

        for (long i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }

        return c;

    }

}
