import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns

def regression_plot(filename, xlabel, ylabel):
    df = pd.read_csv(filename)
    sns.set(rc={'figure.figsize':(12,6)})
    sns.regplot(x=xlabel, y=ylabel, data=df)
    plt.show()
    return

if __name__ == '__main__':
    regression_plot('tempRainYearly.csv', 'Temp', 'Rain')