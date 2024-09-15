Vacation Destination Selector

This project is a Tkinter-based Python application that allows users to view vacation destinations and mark them as "Yes" or "No." Upon closing the application, the user's selections are saved to a CSV file. The project includes three scripts:

GUI.py: Handles the graphical user interface.
Controller.py: Manages data access and retrieval.
CSVWriter.py: Handles saving user selections to a CSV file.
Features

Randomized vacation destination selection.
Allows users to choose "Yes" or "No" for each destination.
Saves all selections to a CSV file when the window is closed.
CSV output is divided into two sections: one for "Yes" selections and one for "No" selections.
Requirements

Make sure you have the following installed:

Python 3.x
pandas (for handling CSV data)
tkinter (comes pre-installed with most Python installations)

How to Run

Clone or download this repository to your local machine.
Place your vacation data in a CSV file named travel.csv in the same directory as the Python scripts. The CSV should have the following columns:
Trip ID
Destination
Start Date
End Date
Accommodation Type
Accommodation Cost
Transportation Type
Transportation Cost
Rating
Average Trip Cost
Photos URL

Project Structure

GUI.py: The main script that launches the GUI. It allows the user to choose "Yes" or "No" for random vacation destinations and tracks the user's choices.
Controller.py: This script handles reading the CSV file and retrieving trip information.
CSVWriter.py: This script manages writing the user's "Yes" and "No" selections to a CSV file when the application exits.

Future Improvements

Add more details to the vacation options, such as images or descriptions.
Implement a scoring or recommendation system based on user preferences.
Improve the CSV output format.
License

This project is licensed under the MIT License.
