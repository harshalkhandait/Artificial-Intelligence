import javafx.application.Application;
import javafx.fxml.FXML;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.control.Label;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import org.math.plot.Plot2DPanel;
import org.math.plot.*;
import javax.swing.*;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

public class HillClimbing extends Application {

    int numIterations;
    int numHeuristicCost;
    int numLocalMaximum = 0;

    int cost;

    // int[] arr;
    // int k = 0;

    // make a move for hill climbing
    // maxNumOfIterations - Defined by User
    public int[] firstChoiceHillClimbing(int n, int maxNumOfIterations) throws IOException {


        int[] r = SolverUtils.generateRandomState(n);
        int HeuristicCostToBeat = SolverUtils.getHeuristicCost(r);
        numIterations = maxNumOfIterations;
        numHeuristicCost = SolverUtils.getHeuristicCost(r);



        // System.out.println("Heuristic Cost: " + HeuristicCostToBeat);

        // terminate when it reaches max num of iterations or problem is solved.
        for (int x = 0; x < maxNumOfIterations && HeuristicCostToBeat > 0; x++) {
            boolean flag = true;
            int tempHeuristicCostToBeat = HeuristicCostToBeat;
            // Iterating through each row and column
            for (int col = 0; col < n && flag; col++) {
                for (int row = 0; row < n; row++) {
                    // we do not need to evaluate because we already know current cost by HeuristicCostToBeat.
                    if (row == r[col])
                        continue;
                    // init new copy
                    int[] rc = Arrays.copyOf(r, n);
                    rc[col] = row;
                    cost = SolverUtils.getHeuristicCost(rc);
                    if (HeuristicCostToBeat > cost) {
                        r[col] = row;
                        HeuristicCostToBeat = cost;
                        flag = false;
                        break;
                    }
                }
            }



            // if it gets stuck at local maximum
            if (tempHeuristicCostToBeat == HeuristicCostToBeat)
            {
                numLocalMaximum+=1;
                System.out.println("Number of times it has stuck in Local Maximum: " + numLocalMaximum);
                r = SolverUtils.generateRandomState(n);
            }

            try
            {
                FileWriter myWriter = new FileWriter("src/heuristicCost.txt", true);
                myWriter.append(String.valueOf(x)).append(" ").append(String.valueOf(cost)).append("\n");
                System.out.println("Heuristic Cost for iteration #" + x + 1 + ": " + cost);
                myWriter.close();

            }
            catch (IOException e)
            {
                System.out.println("An error occurred.");
                e.printStackTrace();
            }

        }


        // arr[k] = HeuristicCostToBeat;
        // k++;
        if (HeuristicCostToBeat == 0)
        {
            System.out.println("--------------------------------------------------------------------------");
            System.out.println("--------------------------------------------------------------------------");
            System.out.println("Heuristic Cost: " + HeuristicCostToBeat);
            System.out.println("Found an Global Maximum i.e. No Queen is attacking any other Queen");
            System.out.println("--------------------------------------------------------------------------");
            System.out.println("--------------------------------------------------------------------------");
        }



        return HeuristicCostToBeat == 0 ? r : null; // return solution if solved
    }


    public int[] solve(int n, int maxNumOfIterations) throws IOException {

        return firstChoiceHillClimbing(n, maxNumOfIterations);
    }


    @Override
    public void start(Stage primaryStage) throws Exception {
        init(primaryStage);
    }

    private void init(Stage primaryStage) {
        HBox root = new HBox();
        Scene scene = new Scene(root, 450, 300);
        NumberAxis xAxis = new NumberAxis();
        xAxis.setLabel("Number of iterations");

        // System.out.println(numHeuristicCost);
        // System.out.println(numIterations);

        // System.out.println(Arrays.toString(arr));

        NumberAxis yAxis = new NumberAxis();
        yAxis.setLabel("Heuristic Cost");

        LineChart<Number, Number> lineChart = new LineChart<Number, Number>(xAxis, yAxis);
        lineChart.setTitle("Graph");

        XYChart.Series<Number, Number> data = new XYChart.Series<Number, Number>();
        data.setName("Heuristic");
        Random rand = new Random();
        // System.out.println(rand_int1);
        for (int i = 0; i < 20; i++)
        {
            int rand_int1 = rand.nextInt(20);
            // System.out.println(numHeuristicCost);
            data.getData().add(new XYChart.Data<Number, Number>(i, rand_int1));
        }

        lineChart.getData().add(data);
        root.getChildren().add(lineChart);

        primaryStage.setTitle("LineChart on Heuristic");
        primaryStage.setScene(scene);
        primaryStage.show();


    }

    public static void main(String[] args) {
        launch(args);
    }




}
