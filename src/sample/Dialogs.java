package sample;

import javafx.scene.control.Alert;

public class Dialogs {
    public void showAlertWithDefaultHeaderText() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Test Connection");

        // alert.setHeaderText("Results:");
        alert.setContentText("Connect to the database successfully!");

        alert.showAndWait();
    }
}
