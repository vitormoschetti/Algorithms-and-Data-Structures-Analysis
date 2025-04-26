package programacaoDinamica;

import java.util.ArrayList;
import java.util.List;

import static programacaoDinamica.Fibonacci.*;

public class Main {

    private static final int INIT = 0;
    private static final int END = 50;

    private static final List<TimeCounter> FIBO_DEFAULT = new ArrayList<>(END + 1);
    private static final List<TimeCounter> FIBO_TOP_DOWN = new ArrayList<>(END + 1);
    private static final List<TimeCounter> FIBO_BOTTOM_UP = new ArrayList<>(END + 1);

    public static void main(String[] args) {

        FiboDefault();
        fiboTopDown();
        fiboBottomUp();

    }

    private static void fiboBottomUp() {

        for (int i = INIT; i <= END; i++) {
            final var timeCounter = new TimeCounter();
            fibonacciDynamicBottomUp(i);
            timeCounter.stop();
            FIBO_BOTTOM_UP.add(timeCounter);
        }

    }

    private static void fiboTopDown() {

        for (int i = INIT; i <= END; i++) {
            final var timeCounter = new TimeCounter();
            fibonacciDynamicTopDown(i);
            timeCounter.stop();
            FIBO_TOP_DOWN.add(timeCounter);
        }

    }

    private static void FiboDefault() {

        for (int i = INIT; i <= END; i++) {
            final var timeCounter = new TimeCounter();
            fibonacciDefault(i);
            timeCounter.stop();
            FIBO_DEFAULT.add(timeCounter);

        }

    }

}
