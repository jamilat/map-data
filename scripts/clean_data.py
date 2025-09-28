import os
from dotenv import load_dotenv
from src.processing.cleaning import filter_by_coordinates, extrema_borders, wpgmaps_add_required_fields, wpgmaps_format_venues, wpgmaps_format_hospitality, wpgmaps_format_bicycle_rails
from src.processing.io import load_json, save_csv, load_csv
import pandas as pd

# Load .env file
load_dotenv()

MAP_ID = os.getenv("MAP_ID")

def categorize_seat_count(seat_count):
    """Categorize seat count into ranges"""
    try:
        seats = int(seat_count)
        if seats <= 20:
            return "Small (1-20 seats)"
        elif seats <= 50:
            return "Medium (21-50 seats)"
        elif seats <= 200:
            return "Large (51-200 seats)"
        else:
            return "Extra Large (201+ seats)"
    except (ValueError, TypeError):
        return "Unknown"
    
def transform_hospitality_csv(input_file, output_file=None):
    """
    Transform hospitality CSV by combining seating_type, seat size ranges, 
    and industry description into the category column.
    
    Parameters:
        input_file (str): Path to input CSV file
        output_file (str, optional): Path to output CSV file. If None, returns DataFrame
    
    Returns:
        pandas.DataFrame: Transformed DataFrame if output_file is None
    """
    
    df = load_csv(input_file)
    # Create the new category column by combining elements
    df['category'] = df.apply(lambda row: 
        f"Hospitality, {row['seating_type']}, {categorize_seat_count(row['number_of_seats'])}, {row['industry_anzsic4_description']}",
        axis=1
    )
    
    # If output file is specified, save the transformed data
    if output_file:
        save_csv(df, output_file)
        print(f"Transformed CSV saved to: {output_file}")
    
    return df

def clean_venues(boundary):
    df_venues = load_json('venues_with_flat_coords.json')
    df = df.rename(columns={'lon': 'lng'})
    df_venues_in_our_suburbs=filter_by_coordinates(df_venues, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
    print(df_venues_in_our_suburbs)
    df_wpgmaps = wpgmaps_add_required_fields(df_venues_in_our_suburbs, 1, 21)
    df_wpgmaps_venues = wpgmaps_format_venues(df_wpgmaps, category="venues")
    save_csv(df_wpgmaps_venues, 'wpgmaps_venues.csv')

def clean_data(boundary, input_csv, category, map_id):
    df = load_csv(f'{input_csv}.csv')
    df_in_our_suburbs=filter_by_coordinates(df, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
    df_wpgmaps = wpgmaps_add_required_fields(df_in_our_suburbs, category, map_id)
    save_csv(df_wpgmaps, f'{category}-cleaned.csv')
    print('Saved', f'{category}-cleaned.csv')
    return

def main():
    boundary = extrema_borders()
    # clean_venues(boundary)
    # clean_data(boundary, "2023-cafes-and-restaurants-with-seating-capacity", "Hospitality", MAP_ID)
    # clean_data(boundary, "Sprint 2 venues + 8 selected(Feuil1)", "Venues", MAP_ID)
    # Manually change the `category` for the `Category`=`Selected` to `Featured` in `Venues-cleaned.csv`
    # clean_data(boundary, "wp_8_wpgmza-bicycle_rails_subset", "Bicycle Rails", MAP_ID)
    # clean_data(boundary, "wp_8_wpgmza-bus-stops", "Bus Stops", MAP_ID)
    # clean_data(boundary, "wp_8_wpgmza-parking_meters_subset", "Parking Meters", MAP_ID)
    # clean_data(boundary, "taxi-ranks-raw", "Taxi Ranks", MAP_ID)
    transform_hospitality_csv(input_file="Hospitality-cleaned.csv", output_file="Hospitality-cleaned-filter.csv")
    return

if __name__ == "__main__":
    main()