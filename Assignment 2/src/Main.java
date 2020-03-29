import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.util.logging.*;

public class Main extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    // private Logger LOG = Logger.getLogger(Main.class.getName());

    @Override
    public void start(Stage primaryStage) throws Exception {
        // Creates a new scene by loading session.fxml
        Scene scene = new Scene(FXMLLoader.load(Main.class.getResource("session.fxml")));
        // FXMLLoader loader = new FXMLLoader(Main.class.getResource("MainWindowView.fxml"));
        primaryStage.setScene(scene);
        // Sets the Dimensions of the Scene
        primaryStage.setHeight(675);
        primaryStage.setWidth(753);
        // Does not allow to resize the User Interface
        primaryStage.setResizable(false);
        primaryStage.show();


    }

}