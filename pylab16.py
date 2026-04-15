Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:/Users/RVUW268/Downloads/11prog_3Salary_Data.csv")
plt.plot(df['YearsExperience'],df['Salary'])
[<matplotlib.lines.Line2D object at 0x000001B96CBB1310>]
plt.ylabel('YearsExperience')
Text(0, 0.5, 'YearsExperience')
plt.xlabel('Index')
Text(0.5, 0, 'Index')
plt.legend()

Warning (from warnings module):
  File "<pyshell#7>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x000001B96974AA50>
plt.show()
sns.lineplot(y=df['YearsExperience'],x=df['Salary'])
<Axes: xlabel='Salary', ylabel='YearsExperience'>
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"3Salary_Data.csv")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df = pd.read_csv(r"3Salary_Data.csv")
  File "C:\Users\RVUW268\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW268\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW268\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW268\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW268\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '3Salary_Data.csv'
>>> df = pd.read_csv(r"C:/Users/RVUW268/Downloads/11prog_3Salary_Data.csv")
>>> plt.scatter(df['YearsExperience'], df['Salary'])
<matplotlib.collections.PathCollection object at 0x000001B96974AE40>
>>> plt.ylabel('Salary')
Text(0, 0.5, 'Salary')
>>> plt.xlabel('YearsExperience')
Text(0.5, 0, 'YearsExperience')
>>> plt.legend()

Warning (from warnings module):
  File "<pyshell#21>", line 1
UserWarning: No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
<matplotlib.legend.Legend object at 0x000001B96CF3EAD0>
>>> plt.show()
>>> sns.scatterplot(x = df['Salary'], y = df['YearsExperience'])
<Axes: xlabel='Salary', ylabel='YearsExperience'>
>>> plt.show()
