import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class Graphs extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        init(primaryStage);
    }

    private void init(Stage primaryStage) {
        HBox root = new HBox();
        Scene scene = new Scene(root, 450, 300);
        NumberAxis xAxis = new NumberAxis();
        xAxis.setLabel("Number of iterations");

        NumberAxis yAxis = new NumberAxis();
        yAxis.setLabel("Heuristic Cost");

        LineChart<Number, Number> lineChart = new LineChart<Number, Number>(xAxis, yAxis);
        lineChart.setTitle("Graph");

        XYChart.Series<Number, Number> data = new XYChart.Series<Number, Number>();
        data.setName("Heuristic");
        data.getData().add(new XYChart.Data<Number, Number>(120, 120));

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
