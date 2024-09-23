from audiofeatureextractor import DatasetConstructor

# Extract features and save dataset in dictionary format
dataset_dict = DatasetConstructor.extract_from_folder("/Users/benjaminheyderman/Documents/QM Final Project Research/Track-Preview-Scrape/audio")

# Convert to dataframe
dataset_df = DatasetConstructor.dict2df(dataset_dict)

print(dataset_df.head())
