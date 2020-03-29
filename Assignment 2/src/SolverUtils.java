import javafx.application.Application;
import javafx.collections.transformation.SortedList;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class SolverUtils {

    // private static int count = 0;

    /**
     * Generate state that all queens have row # 0
     * @param n - number of queens
     * Creates an initial arrangement of queens by placing them in row 0 - row (number of queens) i.e. first column
     */
    public static int[] generateAllOneState(int n) {
        return new int[n];
    }

    /**
     *
     * Randomly places the queens in the entire n x n board
     * Randomizes state
     */
    public static int[] randomizeState(int[] r) {

        for (int i = 0; i < r.length; i++)
            r[i] = (int) (Math.random() * r.length);

        return r;
    }


    /**
     *
     * Generates a random state as a whole and returns the entire state
     * Generates random initial state
     */
    public static int[] generateRandomState(int n) {
        // System.out.println(Arrays.toString(randomizeState(generateAllOneState(n))));
        return randomizeState(generateAllOneState(n));
    }


    /**
     * Calculates the Heuristic Cost - Number of pairs of queen attacking each other
     * Returns heuristic cost
     * When heuristic cost is zero, it means no queen is attacking each other
     */
    public static int getHeuristicCost(int[] r) {
        int h = 0;
        // increment cost if two queens are in same row or in same diagonal.
        for (int i = 0; i < r.length; i++)
            for (int j = i + 1; j < r.length; j++)
                if (r[i] == r[j] || Math.abs(r[i] - r[j]) == j - i)
                    h += 1;
        // count += 1;
        // System.out.println("Count: " + count);
        // System.out.println("Heuristic Cost: " + h);
        return h;
    }
}
