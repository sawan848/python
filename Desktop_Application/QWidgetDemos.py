import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QProgressBar, QPushButton, QApplication, QMessageBox, QFileDialog, QLabel,QCheckBox,QComboBox
from PyQt5.QtCore import Qt, QDir

class QWidgetDemo(QDialog):

    def  __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('QWidgets Demo')

        self.comboBox=QComboBox()

        self.comboBox.addItems(['Item 1','Items 2','Items 3'])

        # self.comboBox.addItem('Item 1')
        # self.comboBox.addItem('Item 2')
        # self.comboBox.addItem('Item 3')


        self.checkbox=QCheckBox()
        self.checkbox.setText('remember password!!!')
        # checkbox.setChecked(True)

        line_edit=QLineEdit()        
        line_edit1=QLineEdit()
        label=QLabel()

        label.setText('<b>hi</b>')


        line_edit.setText("Enter username")

        line_edit1.setPlaceholderText('Password')
        text=line_edit.text()
        line_edit1.setEchoMode(QLineEdit.Password)
        print('you typed '+text)


        close_button=QPushButton('close')
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(line_edit1)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.comboBox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()
        self.checkbox.stateChanged.connect(self.selected)
        self.comboBox.currentIndexChanged.connect(self.comboSelect)


    
    def comboSelect(self):
        current_text=self.combobox.currentText()
        current_index=str(self.comboBox.currentIndex())
        print(current_text+"at the index"+current_index)

    def selected(self):
        if self.checkbox.isChecked():
            print('yes')
        else:
            print('No :(')

app = QApplication(sys.argv)
dl = QWidgetDemo()
dl.show()
app.exec_()
