# 4.3 Using the Data Step to Create an .xdf File from a Data Frame
import os
import settings as st
import pandas as pd
import numpy as np
from revoscalepy import rx_data_step, rx_get_info

np.random.seed(39)

x1 = np.random.normal(size = 10000)
x2 = np.random.uniform(size = 10000)
x3 = x1 + x2

s = np.stack((x1,x2,x3))
s = np.transpose(s)

myData = pd.DataFrame(s, columns = ['x1','x2','x3']).query("x2 > .1")

# Export files directory
outFile = os.path.join(st.RESULTS_LOCATION, 'testFile.xdf')

rx_data_step(input_data = myData,
    output_file = outFile,
    rows_per_read = 5000, 
    overwrite = True)

print(rx_get_info(outFile))