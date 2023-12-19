import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget

import python_example.database as database
from python_example.palindrome import Palindrome


def main(argv) -> None:
    """Python Palindrome UI."""
    app = QApplication(argv)
    ex = PalindromeUI()
    ex.show()
    sys.exit(app.exec())


class PalindromeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Entry field for number
        """
        Develop a simple GUI which has a control on it to accept an integer.
        """
        self.numberInput = QLineEdit()
        self.numberInput.setPlaceholderText("Enter a number (1-10000)")
        layout.addWidget(self.numberInput)

        # Calculate button
        """
        After pressing a button, the palindrome of this integer should be calculated...
        """
        self.calculateBtn = QPushButton("Calculate")
        self.calculateBtn.clicked.connect(self.calculate)
        layout.addWidget(self.calculateBtn)

        # Readonly field for result
        self.resultDisplay = QLineEdit()
        self.resultDisplay.setReadOnly(True)
        layout.addWidget(self.resultDisplay)

        # Readonly field for iterations
        self.iterationDisplay = QLineEdit()
        self.iterationDisplay.setReadOnly(True)
        layout.addWidget(self.iterationDisplay)

        # Save button
        self.saveBtn = QPushButton("Save")
        self.saveBtn.clicked.connect(self.saveData)
        layout.addWidget(self.saveBtn)

        # Display button and table
        self.displayBtn = QPushButton("Display")
        self.displayBtn.clicked.connect(self.displayData)
        layout.addWidget(self.displayBtn)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def calculate(self):
        """After pressing a button, the palindrome of this
        integer should be calculated and the result should be displayed in the GUI."""
        try:
            number = int(self.numberInput.text())
            if 1 <= number <= 10000:
                iterations, calculated_palindrome = Palindrome.run_until_is_palindrome(
                    number
                )
                self.resultDisplay.setText(str(calculated_palindrome))
                self.iterationDisplay.setText(str(iterations))
            else:
                self.iterationDisplay.setText("Invalid input")
        except ValueError:
            self.iterationDisplay.setText("Invalid input")

    def displayData(self):
        data = database.load_from_database()
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(["Number", "Result", "Iteration"])
        for row, (number, result, iteration) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(number)))
            self.table.setItem(row, 1, QTableWidgetItem(str(result)))
            self.table.setItem(row, 2, QTableWidgetItem(str(iteration)))

    def saveData(self):
        # Read from the input field, the result and the iteration field. Take those 3 numbers and append them to a "database.csv" file that resides in the same directory. if it does not exist yet, create it.
        result = self.resultDisplay.text()
        iteration = self.iterationDisplay.text()
        number = self.numberInput.text()

        # Implement the logic to save data to file
        # Save the three values (result, iteration, number) into a csv file, called 'database.csv' and append it to the file.
        database.append_to_database(number, result, iteration)
