#%%
%load_ext autoreload
import numpy as np
import matplotlib.pyplot as plt
#%%
dataFile = "../data/spx_d_1950.csv"

# %%
import pandas as pd
data = pd.read_csv(dataFile, delimiter=",")
data["date"] = pd.to_datetime(data["date"])
""" Append column with day of week number """
data['dayofweek'] = data.date.dt.dayofweek

data.head(5)
data.describe()

# %%

%autoreload
from utils_plot import candlesticks

#%%
fig = plt.figure()
ax = plt.subplot(111)
sampleSize = 100
sample = np.array(data[-sampleSize:])
print(sample[-5:])
candlesticks(ax, sample);
# %%

# %%
