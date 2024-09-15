import pandas as pd

df = pd.read_csv('travel.csv')

def get_destination_name(trip_id):
    """
    Retrieves the destination name for a given trip ID.
    
    Args:
        trip_id (int): The ID of the trip.
    
    Returns:
        str: The destination name of the trip.
    """
    row = df[df['Trip ID'] == trip_id]
    if not row.empty:
        return row['Destination'].values[0]
    return "No destination found"

def get_destination_info(trip_id):
    """
    Retrieves the full information for a given trip ID.
    
    Args:
        trip_id (int): The ID of the trip.
    
    Returns:
        str: A formatted string containing the full trip details.
    """
    row = df[df['Trip ID'] == trip_id]
    if not row.empty:
        destination = row['Destination'].values[0]
        start_date = row['Start date'].values[0]
        end_date = row['End date'].values[0]
        accommodation_type = row['Accommodation type'].values[0]
        accommodation_cost = row['Accommodation cost'].values[0]
        transportation_type = row['Transportation type'].values[0]
        transportation_cost = row['Transportation cost'].values[0]
        rating = row['Rating'].values[0]
        info = (
            f"Destination: {destination}\n"
            f"Start Date: {start_date}\n"
            f"End Date: {end_date}\n"
            f"Accommodation: {accommodation_type} (${accommodation_cost})\n"
            f"Transportation: {transportation_type} (${transportation_cost})\n"
            f"Rating: {rating}/5"
        )
        return info
    return "No information found for this Trip ID."

def get_all_trip_ids():
    """
    Retrieves the list of all trip IDs from the dataset.
    
    Returns:
        list: A list of all trip IDs.
    """
    return df['Trip ID'].tolist()
