# 4.1 Creating a Subset of Rows and Columns
import pandas as pd
import numpy as np
from revoscalepy import rx_data_step

np.random.seed(59)

x = np.random.normal(size = 100)
y = np.random.uniform(size = 100)
z = np.tile(np.array(range(1,21)),5);

s = np.stack((x, y, z))
s = np.transpose(s)

myData = pd.DataFrame(s, columns = ['x','y','z'])

myNewData = rx_data_step(input_data = myData,
    vars_to_keep = ['y','z']).query("y > .5")

print(myNewData)

## REM: The 'row selection' parameter is not implemented in RevoscalePy.
## Therefore, the next example cannot be implemented. However, a workaround
## could be implemented (see 3.6)

