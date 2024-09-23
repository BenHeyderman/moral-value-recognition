import pandas as pd

# Load the datasets
mft_data = pd.read_csv('Billboard_songs_with_lyrucs_MFT_values.csv')
data = pd.read_csv('dataset.csv')
print(f"dataset length = {len(data)}")

# -1 from id to match file id and rename it to 'file_id'
mft_data['file_id'] = mft_data['id'] - 1

# Select columns to merge from  MFT dataframe
mft_columns = ['file_id', 'care', 'harm', 'fairness', 'cheating', 'loyalty', 'betrayal', 'authority', 'subversion', 'purity', 'degradation']
mft_selected = mft_data[mft_columns]

# Merge the dataframes based on  'file_id'
merged_data = data.merge(mft_selected, how='left', on='file_id')

# Drop rows from the merged dataframe where 'care' is NaN (no MFT data)
merged_data = merged_data.dropna(subset=['care'])

print(f"merged dataset length = {len(merged_data)}")

# Save the merged dataframe to a  CSV file
merged_data.to_csv('dataset_billboard_MFT.csv', index=False)
