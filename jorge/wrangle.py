import pandas as pd

def load_and_prepare_wine_data(red_wine_url, white_wine_url):
    # Load the data from URLs
    df_red = pd.read_csv(red_wine_url)
    df_white = pd.read_csv(white_wine_url)

    # Create and set new index column for red wine
    df_red['wine_id'] = ['red-' + str(i) for i in range(1, len(df_red) + 1)]
    df_red = df_red.set_index('wine_id')

    # Create and set new index column for white wine
    df_white['wine_id'] = ['white-' + str(i) for i in range(1, len(df_white) + 1)]
    df_white = df_white.set_index('wine_id')

    # Concatenate the DataFrames
    df_combined = pd.concat([df_white, df_red], axis=0)

    return df_combined

# URLs for the datasets
red_wine_url = 'https://query.data.world/s/qgc7p446ulzlgtja2626fwkzcm6ttf?dws=00000'
white_wine_url = 'https://query.data.world/s/f5oqq5ltnxcdnoh7uykzubtxnnspne?dws=00000'