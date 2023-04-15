# %%
import os
import pandas as pd

# set directory path where CSV files are located
dir_path = r'D:\___Projects\son-of-the-water\rawdata\world'

# set desired name for concatenated file
concat_file_name = 'data.csv'

# delete all CSV files in directory

# initialize an empty list to store all DataFrames
df_list = []

# loop through each file in directory with .csv extension
for file in os.listdir(dir_path):
    if file.endswith('.csv'):
        file_path = os.path.join(dir_path, file)
        # read csv file and append to df_list
        df_list.append(pd.read_csv(file_path))


for file in os.listdir(dir_path):
    if file.endswith('.csv'):
        file_path = os.path.join(dir_path, file)
        os.remove(file_path)
# concatenate all DataFrames in df_list into a single DataFrame
concat_df = pd.concat(df_list, ignore_index=True)

# write concatenated DataFrame to new csv file
concat_df.to_csv(os.path.join(dir_path, concat_file_name), index=False)

print(f'Successfully concatenated {len(df_list)} csv files into {concat_file_name}.')



