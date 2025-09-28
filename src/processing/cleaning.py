
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

def wpgmaps_format_coords(df):
    df = df.rename(columns={'lon': 'lng'})
    df = df.rename(columns={'longitude': 'lng'})
    df = df.rename(columns={'latitude': 'lat'})
    df = df.rename(columns={'Longitude': 'lng'})
    df = df.rename(columns={'Latitude': 'lat'})
    return df

def filter_by_coordinates(df, lat_min=min_lat, lat_max=max_lat, lon_min=min_lon, lon_max=max_lon, lat='lat', lng='lng'):
    """
    Filters a pandas DataFrame to return a subset of data within a
    specific latitude and longitude range.
    """
    df = wpgmaps_format_coords(df)
    return df[
        (df[lat] >= lat_min) & (df[lat] <= lat_max) &
        (df[lng] >= lon_min) & (df[lng] <= lon_max)
    ].copy()

def wpgmaps_add_required_fields(df, category, map_id):
    """Bulk changes to a single value for attributes"""
    # TODO: WP Go Maps formatting: https://www.wpgmaps.com/help/
    # TASK 1: add necessary columns with corresponding values
    # Add a new column with the same value for all rows
    
    # Format requirements for the import file `column(is_required): value`
    # map_id: This allows you to specify the ID of the map you would like the markers to be imported into.
    df['map_id'] = map_id
    # icon: The icon column allows you to set the marker’s icon that will display on the map. This is done by entering the URL for the icon you want to use.
    # infoopen: default open and close toggle
    df['infoopen'] = 0
    # category: The category column allows you to set which categories your marker belongs to. This is done by entering the category id into the column.
    df['category'] = category
    # approved (Required): The approved column refers to sets whether the marker is allowed to be displayed on the frontend of your site or not. Setting it to 1 means that the marker will be displayed on the frontend, whereas setting it to 0 means it will not be displayed on the frontend.
    df['approved'] = 1
    # retina (Required): The retina column refers to whether or not the Retina is enabled to disabled. Setting it as 1 will enable the Retina, whereas setting it to 0 will disable the Retina.
    df['retina'] = 1
    # TASK 2: change the names of additional columns as per the docs
    return df

def wpgmaps_format_venues(df, category):
    # id (Required): This refers to the ID given to your marker.
    df = df.rename(columns={'block_id': 'id'})
    # address (Not Required if lat/lng present): This is the physical address of the marker. E.g. 123 Imaginary Drive, Los Angeles, California, USA.
    # description: The description is the paragraph in the Infowindow which gives a description of your location or what your marker represents.
    # pic: The pic column allows you to add an image to your marker by specifying the image URL. You can only add one image per marker when importing.
    # link: The link column allows you to specify the link for the “More Details” button in the Infowindow.
    # lat (Not Required if Address is present): The lat column refers to the latitude value for the marker’s position.
    # lng (Not Required if Address is present): The lng column refers to the longitude value for the marker’s position.
    # icon: The icon column allows you to set the marker’s icon that will display on the map. This is done by entering the URL for the icon you want to use.
    # title: The title column refers to the Title given to the marker/Name of the marker. E.g. Beijing Railway Station.
    df = df.rename(columns={'full_name': 'title'})
    return df

def wpgmaps_format_hospitality(df, category):
    # df = df.rename(columns={'property_id': 'id'})
    df = df.rename(columns={'trading_name': 'title'})
    df = df.rename(columns={'longitude': 'lng'})
    df = df.rename(columns={'latitude': 'lat'})
    return df

def wpgmaps_format_bicycle_rails(df, category):
    return df
