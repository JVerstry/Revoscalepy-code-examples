# 2.12 Reading Data from an .xdf File into a Data Frame (row selection)
import os
import settings as st
from revoscalepy import rx_data_step, rx_get_info

## Unfortunately, the 'row_selection' parameter of rx_data_step is not supported.
## See https://docs.microsoft.com/en-us/machine-learning-server/python-reference/revoscalepy/rx-data-step#row_selection

## However, it is possible filter rows after data is loaded

# Import file
infile = os.path.join(st.SAMPLE_DATA_DIR,'CensusWorkers.xdf')

# Loading data
myCensusDF = rx_data_step(input_data = infile,
    vars_to_keep = [ 'age', 'perwt', 'sex', 'state'])

print(myCensusDF.head())

# state == "Washington" & age > 40
mySelection1 = myCensusDF.query("state=='Washington' and age>40")
print(mySelection1.head())

# Every 10th row
mySelection2 = myCensusDF.iloc[::10, :]
print(mySelection2.head())
