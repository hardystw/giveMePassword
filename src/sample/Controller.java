package sample;

import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

public class Controller {

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private TextField textAreaInput;

    @FXML
    private TextField textAreaOutput;

    @FXML
    private Button buttonGeneratePassword;

    @FXML
    void initialize() {
        assert textAreaInput != null : "fx:id=\"textAreaInput\" was not injected: check your FXML file 'sample.fxml'.";
        assert textAreaOutput != null : "fx:id=\"textAreaOutput\" was not injected: check your FXML file 'sample.fxml'.";
        assert buttonGeneratePassword != null : "fx:id=\"buttonGeneratePassword\" was not injected: check your FXML file 'sample.fxml'.";
        buttonGeneratePassword.setOnAction(actionEvent -> {
            textAreaOutput.setText(textAreaInput.getText() + " TEST");
        });
    }
}
