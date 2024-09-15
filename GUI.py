import tkinter as tk
import random
import atexit
from Controller import get_destination_info, get_destination_name, get_all_trip_ids
from CSVWriter import save_trips_to_csv

yes_trips = []
no_trips = []

def on_yes_click():
    """
    Handles the 'Yes' button click event. Selects a random trip, shows its destination, and adds it to the 'Yes' list.
    """
    global random_trip_id
    trip_ids = get_all_trip_ids()
    random_trip_id = random.choice(trip_ids)
    destination_name = get_destination_name(random_trip_id)
    info_label.config(text=f"Destination: {destination_name}")
    next_button.pack(pady=20)
    yes_trips.append(random_trip_id)

def on_next_click():
    """
    Handles the 'Next' button click event. Displays the full information of the randomly selected trip.
    """
    destination_info = get_destination_info(random_trip_id)
    info_label.config(text=destination_info)
    next_button.pack_forget()

def on_no_click():
    """
    Handles the 'No' button click event. Selects a random trip, hides its details, and adds it to the 'No' list.
    """
    global random_trip_id
    trip_ids = get_all_trip_ids()
    random_trip_id = random.choice(trip_ids)
    info_label.config(text="No information will be shown.")
    no_trips.append(random_trip_id)

def on_exit():
    """
    Handles the exit event. Saves all the trips marked 'Yes' or 'No' to a CSV file when the program exits.
    """
    save_trips_to_csv(yes_trips, no_trips)

atexit.register(on_exit)

window = tk.Tk()
window.title("Travel Destination Selector")

info_label = tk.Label(window, text="Click Yes or No", font=("Arial", 14))
info_label.pack(pady=20)

yes_button = tk.Button(window, text="Yes", font=("Arial", 14), command=on_yes_click)
yes_button.pack(side="left", padx=20)

no_button = tk.Button(window, text="No", font=("Arial", 14), command=on_no_click)
no_button.pack(side="right", padx=20)

next_button = tk.Button(window, text="Next", font=("Arial", 14), command=on_next_click)

window.mainloop()
