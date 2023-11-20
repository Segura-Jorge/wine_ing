import pandas as pd



# URLs for the datasets
red_wine_url = 'https://query.data.world/s/qgc7p446ulzlgtja2626fwkzcm6ttf?dws=00000'
white_wine_url = 'https://query.data.world/s/f5oqq5ltnxcdnoh7uykzubtxnnspne?dws=00000'


def load_and_prepare_wine_data(red_wine_url, white_wine_url):
    # Load the data from URLs
    df_red = pd.read_csv(red_wine_url)
    df_white = pd.read_csv(white_wine_url)
    df_red['color'] = 'red'
    df_white['color'] = 'white'
    # Create and set new index column for red wine
    df_red['wine_id'] = ['r-' + str(i) for i in range(1, len(df_red) + 1)]
    df_red = df_red.set_index('wine_id')

    # Create and set new index column for white wine
    df_white['wine_id'] = ['w-' + str(i) for i in range(1, len(df_white) + 1)]
    df_white = df_white.set_index('wine_id')

    # Concatenate the DataFrames
    df_combined = pd.concat([df_white, df_red], axis=0)

    return df_combined

 
def categorize_quality(quality):
    if quality in [3, 4]:
        return 'Low'
    elif quality in [5, 6, 7]:
        return 'Average'
    else:  # for quality 8 and 9
        return 'High'

    
def prepare_wine(df):
    '''
    This function takes in a dataframe 
    Creates a column that bins quality of the wines into 3 groups
    Then returns a cleaned dataframe
    '''
#     filename = 'wines.csv'
    
#     if os.path.isfile(filename): 
#         df = pd.read_csv(filename, index_col=0)
#         return df
#     else:
#         df = load_and_prepare_wine_data(red_wine_url, white_wine_url)

#         df.to_csv(filename)
#     return df

import pandas as pd
import os

def prepare_wine(red_wine_url, white_wine_url, filename='wines.csv'):
    def categorize_quality(quality):
        if quality in [3, 4]:
            return 'Low'
        elif quality in [5, 6, 7]:
            return 'Average'
        else:  # for quality 8 and 9
            return 'High'

    if os.path.isfile(filename): 
        # Load the DataFrame from CSV if it already exists
        df = pd.read_csv(filename, index_col=0)
    else:
        # Load the data from URLs
        df_red = pd.read_csv(red_wine_url)
        df_white = pd.read_csv(white_wine_url)
        
        # Create and set new index column for red wine
        df_red['wine_id'] = ['r-' + str(i) for i in range(1, len(df_red) + 1)]
        df_red = df_red.set_index('wine_id')
        df_red['color'] = 'red'
        
        # Create and set new index column for white wine
        df_white['wine_id'] = ['w-' + str(i) for i in range(1, len(df_white) + 1)]
        df_white = df_white.set_index('wine_id')
        df_white['color'] = 'white'
        # Concatenate the DataFrames
        df = pd.concat([df_white, df_red], axis=0)
        
# Rename columns
        rename_dict = {
                'fixed acidity': 'fixed_acidity',
                'volatile acidity': 'volatile_acidity',
                'citric acid':'citric_acid',
                'residual sugar':'residual_sugar',
                'free sulfur dioxide':'free_sulfur_dioxide',
                'total sulfur dioxide':'total_sulfur_dioxide'
                }

        df = df.rename(columns=rename_dict)
 
        # Categorize the quality column
        df['quality_category'] = df['quality'].apply(categorize_quality)

        # Save the processed DataFrame to CSV
        df.to_csv(filename)

    return df
