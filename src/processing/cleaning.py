
# Looks at a pandas dataframe that was from json and gets the certain range of latitude and longitude and returns a subsest of that dataframe
# Coordinate range for Carlton, Parkville, and North Melbourne
BORDERS = {
    'Carlton': {'north_east': (-37.792851, 144.976203),
                'south_east': (-37.808227, 144.973369),
                'south': (-37.806537, 144.959499),
                'west': (-37.799950, 144.958614)
                }, 
     'Parkville': {'north_east': (-37.777953, 144.960530), 
                 'south_east': (-37.800536, 144.964275),
                 'north_west': (-37.773670, 144.936181)
                 },
    'North Melbourne': {'north_west': (-37.785526, 144.935914),
                        'south_west': (-37.804610, 144.934593),
                        'south_east': (-37.806459, 144.958817)
                        }
    }

min_lat, min_lon = (-37.804129, 144.933823)
max_lat, max_lon = (-37.772974, 144.975980)

def extrema_borders():
    # Get an iterator for all coordinate tuples.
    all_coords = []
    for city_coords in BORDERS.values():
        for coord_tuple in city_coords.values():
            all_coords.append(coord_tuple)

    # Initialize min/max values with the first coordinate.
    min_lat, min_lon = all_coords[0]
    max_lat, max_lon = all_coords[0]

    # Iterate through the rest of the coordinates to find the true min/max.
    for lat, lon in all_coords[1:]:
        # Update min/max latitude.
        if lat < min_lat:
            min_lat = lat
        if lat > max_lat:
            max_lat = lat

        # Update min/max longitude.
        if lon < min_lon:
            min_lon = lon
        if lon > max_lon:
            max_lon = lon

    # Print the results.
    print("Overall Min and Max Coordinates:")
    print(f"Min Latitude: {min_lat}")
    print(f"Max Latitude: {max_lat}")
    print(f"Min Longitude: {min_lon}")
    print(f"Max Longitude: {max_lon}")
    return {'min': (min_lat, min_lon), 'max': (max_lat, max_lon)}

def filter_by_coordinates(df, lat_min=min_lat, lat_max=max_lat, lon_min=min_lon, lon_max=max_lon):
    """
    Filters a pandas DataFrame to return a subset of data within a
    specific latitude and longitude range.
    """
    return df[
        (df['lat'] >= lat_min) & (df['lat'] <= lat_max) &
        (df['lon'] >= lon_min) & (df['lon'] <= lon_max)
    ].copy()

