Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
... import seaborn as sns
SyntaxError: multiple statements found while compiling a single statement
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df4 = pd.read_csv(r"C:\Users\RVUW268\OneDrive\Desktop\14prog_5ds_salaries.csv")
>>> plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5) #
... edgecolor='white',linewidth=0.4)
SyntaxError: multiple statements found while compiling a single statement
>>> plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5) #
<BarContainer object of 3755 artists>
>>> edgecolor='white',linewidth=0.4)
SyntaxError: unmatched ')'
>>> plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5) #
... edgecolor='white',linewidth=0.4)
SyntaxError: multiple statements found while compiling a single statement
>>> plt.bar(df4['experience_level'], df4['salary_in_usd'], width = 0.5)#edgecolor='white',linewidth=0.4)
<BarContainer object of 3755 artists>
>>> plt.show()
>>> sns.barplot(x=df4['experience_level'], y=df4['salary_in_usd'])
<Axes: xlabel='experience_level', ylabel='salary_in_usd'>
