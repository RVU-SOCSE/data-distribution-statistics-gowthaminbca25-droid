Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> df2 = pd.read_csv(r"4laptops.csv")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df2 = pd.read_csv(r"4laptops.csv")
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
FileNotFoundError: [Errno 2] No such file or directory: '4laptops.csv'
>>> df2 = pd.read_csv(r"C:\Users\RVUW268\OneDrive\Desktop\10prog_4laptops.csv")
>>> sns.heatmap(df2.corr(numeric_only=True),annot=True)
<Axes: >
