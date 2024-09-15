from Controller import get_destination_info

def save_trips_to_csv(yes_trips, no_trips):
    """
    Saves the 'Yes' and 'No' trips to a CSV file. 
    
    Args:
        yes_trips (list): List of trip IDs that were marked 'Yes'.
        no_trips (list): List of trip IDs that were marked 'No'.
    
    Writes the trips to 'trip_selections.csv' in the following format:
    - Yes Trips section followed by the trip details.
    - No Trips section followed by the trip details.
    """
    yes_data = [get_destination_info(trip_id) for trip_id in yes_trips]
    no_data = [get_destination_info(trip_id) for trip_id in no_trips]

    yes_section = ["Yes Trips:"] + yes_data
    no_section = ["No Trips:"] + no_data

    with open('trip_selections.csv', 'w') as file:
        file.write("\n".join(yes_section))
        file.write("\n\n")
        file.write("\n".join(no_section))
