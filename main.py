import sys
import json

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QTimer, QUrl

from ui_main import Ui_MainWindow



class LevelEditor(QMainWindow):
    def __init__(self):
        super(LevelEditor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menuExit.triggered.connect(self.close_app)
        self.ui.menuSave.triggered.connect(self.save)
        self.ui.menuSelect.triggered.connect(self.select)

        self.ui.playButton.clicked.connect(self.play_sound)
        self.ui.pauseButton.clicked.connect(self.pause_sound)
        self.ui.resetButton.clicked.connect(self.reset_sound)
        
        self.ui.playMain.sliderMoved.connect(self.seek)
        self.ui.playSound.sliderMoved.connect(self.update_volume)
        
        self.ui.r1Button.clicked.connect(self.click_act_1)
        self.ui.r2Button.clicked.connect(self.click_act_2)
        self.ui.r3Button.clicked.connect(self.click_act_3)
        
        self.ui.playButton.setEnabled(False)
        self.ui.pauseButton.setEnabled(False)
        self.ui.menuSave.setEnabled(False)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.ui.currentTime.setText("00:00.000")
        self.ui.maxTime.setText("00:00.000")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)
        self.directions = ["", "⯅", "⯆", "⯇", "⯈"]
        self.chart_data = {
            "authorName": str(),
            "songName": str(),
            "track1": list(),
            "track2": list(),
            "trackAcc": list()
        }

    def click_act_1(self):
        self.pause_sound()
        current_position = self.player.position()
        for i in range(len(self.chart_data["track1"])):
            if self.get_seconds(current_position) == self.chart_data["track1"][i]["time"]:
                self.chart_data["track1"][i]["dir"] = (self.chart_data["track1"][i]["dir"] + 1) % 5
                self.ui.r1Action.setText(self.directions[self.chart_data["track1"][i]["dir"]])
                return 
        self.chart_data["track1"].append({"time": self.get_seconds(current_position), "dir": 1})
        self.ui.r1Action.setText(self.directions[self.chart_data["track1"][len(self.chart_data["track1"]) - 1]["dir"]])

    def click_act_2(self):
        self.pause_sound()
        current_position = self.player.position()
        for i in range(len(self.chart_data["track2"])):
            if self.get_seconds(current_position) == self.chart_data["track2"][i]["time"]:
                self.chart_data["track2"][i]["dir"] = (self.chart_data["track2"][i]["dir"] + 1) % 5
                self.ui.r2Action.setText(self.directions[self.chart_data["track2"][i]["dir"]])
                return 
        self.chart_data["track2"].append({"time": self.get_seconds(current_position), "dir": 1})
        self.ui.r2Action.setText(self.directions[self.chart_data["track2"][len(self.chart_data["track2"]) - 1]["dir"]])
    
    def click_act_3(self):
        self.pause_sound()
        current_position = self.player.position()
        for i in range(len(self.chart_data["trackAcc"])):
            if self.get_seconds(current_position) == self.chart_data["trackAcc"][i]["time"]:
                self.chart_data["trackAcc"][i]["dir"] = (self.chart_data["trackAcc"][i]["dir"] + 1) % 5
                self.ui.r3Action.setText(self.directions[self.chart_data["trackAcc"][i]["dir"]])
                return 
        self.chart_data["trackAcc"].append({"time": self.get_seconds(current_position), "dir": 1})
        self.ui.r3Action.setText(self.directions[self.chart_data["trackAcc"][len(self.chart_data["trackAcc"]) - 1]["dir"]])
        
    def select(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select wav file", "", "WAV files (*.wav)")
        if file_path:
            self.ui.labelMain.setText("Now you are making level!")
            self.ui.playButton.setEnabled(True)
            self.ui.menuSave.setEnabled(True)
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.player.stop()

    def play_sound(self):
        self.ui.r1Action.setText("")
        self.ui.r2Action.setText("")
        self.ui.r3Action.setText("")
        self.player.play()
        self.ui.maxTime.setText(self.format_time(self.player.duration()))
        self.ui.playMain.setMaximum(self.player.duration())
        self.timer.start(1)  # update position every 1 milliseconds
        self.ui.playButton.setEnabled(False)
        self.ui.pauseButton.setEnabled(True)
        

    def pause_sound(self):
        self.player.pause()
        self.timer.stop()
        self.ui.playButton.setEnabled(True)
        self.ui.pauseButton.setEnabled(False)

    def reset_sound(self):
        self.ui.r1Action.setText("")
        self.ui.r2Action.setText("")
        self.ui.r3Action.setText("")
        self.player.pause()
        self.player.setPosition(0)
        current_position = self.player.position()
        self.ui.currentTime.setText(self.format_time(current_position))
        self.ui.playMain.setValue(current_position)
        self.ui.playButton.setEnabled(True)
        self.ui.pauseButton.setEnabled(False)

    def seek(self, position):
        self.player.setPosition(position)

    def update_position(self):
        current_position = self.player.position()
        self.ui.currentTime.setText(self.format_time(current_position))
        self.ui.playMain.setValue(current_position)

    def update_volume(self, value):
        self.audio_output.setVolume(value / 100.0)  # scale value to 0.0-1.0 range

    def format_time(self, millis) -> str:
        seconds = millis // 1000
        minutes = seconds // 60
        millis -= seconds * 1000
        return f"{minutes % 60:02}:{seconds % 60:02}.{millis:03}"
    
    def get_seconds(self, millis) -> float:
        seconds = millis // 1000
        millis -= seconds * 1000
        return float(f"{seconds % 60:02}.{millis:03}")

    def save(self):
        author, ok_author = QInputDialog.getText(self, "Input Author Name", "Enter the author's name:")
        if not ok_author or not author.strip():
            return

        track, ok_track = QInputDialog.getText(self, "Input Track Name", "Enter the track name:")
        if not ok_track or not track.strip():
            return

        self.chart_data["authorName"] = author.strip()
        self.chart_data["songName"] = track.strip()

        file_path, _ = QFileDialog.getSaveFileName(self, "Save chart", "", "JSON files (*.json)")

        if file_path:
            with open(file_path, "w") as file:
                json.dump(obj=self.chart_data, fp=file)

    def close_app(self):
        self.save()
        QApplication.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LevelEditor()
    window.show()
    sys.exit(app.exec_())