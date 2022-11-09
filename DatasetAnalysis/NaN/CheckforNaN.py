import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/46bdcecb-8503-44fc-bd22-3ece9d6e026e/first_df', index_col=0)

# Calculate the total quantity of NaN values
total = df.isnull().count()

# Print the variable total
print(total)
