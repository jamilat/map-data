from src.processing.cleaning import filter_by_coordinates, extrema_borders
from src.processing.io import load_json

boundary = extrema_borders()
df_venues = load_json('venues_with_flat_coords.json')
res=filter_by_coordinates(df_venues, lat_min=boundary['min'][0], lat_max=boundary['max'][0], lon_min=boundary['min'][1], lon_max=boundary['max'][1])
print(res)