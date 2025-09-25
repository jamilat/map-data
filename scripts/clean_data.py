from src.processing.cleaning import filter_by_coordinates, extrema_borders, wpgmaps_add_required_fields, wpgmaps_format_venues
from src.processing.io import load_json, save_csv, load_csv

def clean_venues(boundary):
    df_venues = load_json('venues_with_flat_coords.json')
    df_venues_in_our_suburbs=filter_by_coordinates(df_venues, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
    print(df_venues_in_our_suburbs)
    df_wpgmaps = wpgmaps_add_required_fields(df_venues_in_our_suburbs, 1, 21)
    df_wpgmaps_venues = wpgmaps_format_venues(df_wpgmaps, 1)
    save_csv(df_wpgmaps_venues, 'wpgmaps_venues.csv')

def clean_data(boundary):
    df = load_csv('data.csv')
    df = df.rename(columns={'longitude': 'lon'})
    df = df.rename(columns={'latitude': 'lat'})
    df_in_our_suburbs=filter_by_coordinates(df, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
    print(df_in_our_suburbs)
    save_csv(df_in_our_suburbs, 'data_out.csv')
    return

def main():
    boundary = extrema_borders()
    # clean_venues(boundary)
    clean_data(boundary)
    return

if __name__ == "__main__":
    main()