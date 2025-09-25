from src.processing.cleaning import filter_by_coordinates, extrema_borders, wpgmaps_add_required_fields
from src.processing.io import load_json, save_csv

def clean_venues():
    boundary = extrema_borders()
    df_venues = load_json('venues_with_flat_coords.json')
    df_venues_in_our_suburbs=filter_by_coordinates(df_venues, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
    print(df_venues_in_our_suburbs)
    df_wpgmaps = wpgmaps_add_required_fields(df_venues_in_our_suburbs)
    save_csv(df_wpgmaps, 'wpgmaps_venues.csv')

def main():
    clean_venues()
    return

if __name__ == "__main__":
    main()