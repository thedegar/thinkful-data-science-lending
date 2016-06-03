#####################################################
# Tyler Hedegard
# 6/3/2016
# Thinkful Data Science
# Lending Data (Chi Squared Test)
#####################################################

from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('lending_data.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# plt.figure()
# plt.bar(freq.keys(), freq.values(), width=1)
# plt.show()

chi, p = stats.chisquare(freq.values())

print("chi = {}".format(chi))
print("p value = {}".format(p))
