#####################################################
# Tyler Hedegard
# 6/3/2016
# Thinkful Data Science
# Lending Data
#####################################################

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('lending_data.csv')
# loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# Can't access github from work so had to download the file locally via other means...

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("images/boxplot.png")

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("images/histogram.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("images/qqplot.png")
