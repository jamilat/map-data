from src.processing.io import save_csv, load_csv
from src.clean_data.py import transform_hospitality_data, transform_hospitality_csv



        



if __name__ == "__main__":
    # Example 1: Transform from file to file
    transform_hospitality_csv('Hospitality-cleaned.csv', 'output_hospitality.csv')
    
    # Example 2: Transform and return DataFrame
    df = transform_hospitality_csv('input_hospitality.csv')
    print(df['category'].head())
    
    # Example 3: Transform existing DataFrame
    df_original = pd.read_csv('hospitality_data.csv')
    df_transformed = transform_hospitality_data(df_original)
    
