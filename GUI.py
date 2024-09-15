import tkinter as tk
import random
import atexit
from Controller import get_destination_info, get_destination_name, get_all_trip_ids
from CSVWriter import save_trips_to_csv

yes_trips = []
no_trips = []

def on_yes_click():
    """
    Handles the 'Yes' button click event. 
    Selects a random trip, displays its destination name, and adds it to the 'Yes' list.
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
    Handles the 'Next' button click event. 
    Displays the full details of the randomly selected trip.
    """
    destination_info = get_destination_info(random_trip_id)
    info_label.config(text=destination_info)
    next_button.pack_forget()

def on_no_click():
    """
    Handles the 'No' button click event. 
    Selects a random trip and adds it to the 'No' list without showing detailed information.
    """
    global random_trip_id
    trip_ids = get_all_trip_ids()
    random_trip_id = random.choice(trip_ids)
    info_label.config(text="No information will be shown.")
    no_trips.append(random_trip_id)

def on_exit():
    """
    Handles the exit event. 
    Saves all the trips marked as 'Yes' or 'No' to a CSV file when the program exits.
    """
    save_trips_to_csv(yes_trips, no_trips)

def style_button(button):
    """
    Applies a uniform style to buttons, including font, background color, padding, and border.
    
    Args:
        button (tk.Button): The button to apply styles to.
    """
    button.config(
        font=("Arial", 14, "bold"), 
        bg="#4CAF50", 
        fg="white", 
        activebackground="#45a049",
        padx=10, pady=10, 
        relief="raised",
        borderwidth=2
    )

atexit.register(on_exit)

window = tk.Tk()
window.title("Travel Destination Selector")
window.geometry("600x400")
window.configure(bg="#f0f0f0")

info_label = tk.Label(
    window, text="Click Yes or No", 
    font=("Arial", 18), 
    bg="#f0f0f0", 
    fg="#333", 
    padx=20, pady=20
)
info_label.pack(pady=40)

yes_button = tk.Button(window, text="Yes", command=on_yes_click)
style_button(yes_button)
yes_button.pack(side="left", padx=50, pady=20)

no_button = tk.Button(window, text="No", command=on_no_click)
style_button(no_button)
no_button.pack(side="right", padx=50, pady=20)

next_button = tk.Button(window, text="Next", command=on_next_click)
style_button(next_button)

window.mainloop()
