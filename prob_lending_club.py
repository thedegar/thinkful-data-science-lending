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
# Can't access github from work so had to download the file locally fia other means...

loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Funded.By.Investors')
plt.savefig("images/amount_funded_boxplot.png")

loansData.hist(column='Amount.Funded.By.Investors')
plt.savefig("images/amount_funded_histogram.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig("images/amount_funded_qqplot.png")

plt.figure()

loansData.boxplot(column='Amount.Requested')
plt.savefig("images/amount_requested_boxplot.png")

loansData.hist(column='Amount.Requested')
plt.savefig("images/amount_requested_histogram.png")

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("images/amount_requested_qqplot.png")
