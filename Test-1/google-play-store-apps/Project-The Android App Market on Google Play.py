# Read in dataset
import pandas as pd
import os

a = open (os.path.expanduser('/Users/nitesh/Desktop/OneDrive\ -\ Cal\ State\ LA/data_science_practic/Test-1/google-play-store-apps/apps.csv'))
apps_with_duplicates = pd.read_csv(a)

# Drop duplicates
apps = apps_with_duplicates.drop_duplicates()

# Print the total number of apps
print('Total number of apps in the dataset = ', apps.count())

# Have a look at a random sample of 5 rows
n = 5
apps.sample(n)
