# Vacation Destination Selector

A Tkinter-based Python application that allows users to view vacation destinations and mark them as "Yes" or "No." Upon closing the application, the user's selections are saved to a CSV file.

## Features

- Randomized vacation destination selection.
- Allows users to choose "Yes" or "No" for each destination.
- Saves all selections to a CSV file upon closing the window.
- CSV output is divided into two sections: one for "Yes" selections and one for "No" selections.

## Project Structure

```
.
├── GUI.py              # Handles the graphical user interface.
├── Controller.py       # Manages data access and retrieval.
├── CSVWriter.py        # Handles saving user selections to a CSV file.
├── travel.csv          # Sample CSV with vacation destination data.
└── README.md           # Project documentation.
```

### `GUI.py`

The main script that launches the graphical user interface. It allows users to choose "Yes" or "No" for random vacation destinations and tracks the user's choices.

### `Controller.py`

This script handles reading the `travel.csv` file and retrieving trip information for the GUI.

### `CSVWriter.py`

Manages writing the user's "Yes" and "No" selections to a CSV file when the application exits.

## Requirements

Ensure the following are installed:

- **Python 3.x**
- **pandas** (for handling CSV data)
- **tkinter** (comes pre-installed with most Python installations)

## How to Run

1. Clone or download this repository to your local machine.
2. Place your vacation data in a CSV file named `travel.csv` in the same directory as the Python scripts. The CSV should have the following columns:
   - `Trip ID`
   - `Destination`
   - `Start Date`
   - `End Date`
   - `Accommodation Type`
   - `Accommodation Cost`
   - `Transportation Type`
   - `Transportation Cost`
   - `Rating`
   - `Average Trip Cost`
   - `Photos URL`
3. Run the `GUI.py` script to launch the application.

## Example CSV Structure (`travel.csv`)

```
Trip ID,Destination,Start Date,End Date,Accommodation Type,Accommodation Cost,Transportation Type,Transportation Cost,Rating,Average Trip Cost,Photos URL
1,Paris,2024-06-15,2024-06-22,Hotel,1200,Flight,800,9,2000,https://example.com/paris.jpg
2,Tokyo,2024-07-10,2024-07-18,Hostel,700,Flight,1200,8,1900,https://example.com/tokyo.jpg
```

## Future Improvements

- Add more details to the vacation options, such as images or descriptions.
- Implement a scoring or recommendation system based on user preferences.
- Improve the CSV output format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
