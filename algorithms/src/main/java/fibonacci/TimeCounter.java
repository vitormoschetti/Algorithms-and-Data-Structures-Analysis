package fibonacci;

import java.util.concurrent.TimeUnit;

public class TimeCounter {

    private final Long startTime;
    private Long endTime;

    public TimeCounter() {
        this.startTime = System.nanoTime();
    }

    public void stop() {
        this.endTime = System.nanoTime();
    }

    public long getResult() {
        return TimeUnit.NANOSECONDS.toMicros(endTime - startTime);
    }
}
