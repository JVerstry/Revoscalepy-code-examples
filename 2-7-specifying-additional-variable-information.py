# 2.7 Specifying Additional Variable Information
import os
import settings as st
from revoscalepy import rx_import, rx_get_info

# Importing Delimited Text Data
inFileAddVars = os.path.join(st.SAMPLE_DATA_DIR,'claims.txt')

## REM: Our RxOptions.set_option("OutDataPath", [RESULTS_LOCATION])
## is not taken into account (bug?). Hence, we specify the full location
outfileTypeRelabeled = os.path.join(st.RESULTS_LOCATION,'claimsTypeRelabeled.xdf')

# Defining transformation
colInfoList = {
    'type': {
        'type': 'factor',
        'levels': [ 'A', 'B', 'C', 'D' ],
        'newLevels': [ 'Subcompact', 'Compact', 'Mid-size', 'Full-size' ],
        'description' : 'Body Type'
    }
}

# Applying transformation
rx_import(input_data = inFileAddVars, output_file = outfileTypeRelabeled,
    column_info = colInfoList,
    overwrite = True)

## REM: Contrary to what is mentioned in the documentation, rx_import
## does not return a RxXdfData object when an output file is specified
## but a <class 'bool'>.
## See: https://docs.microsoft.com/en-us/machine-learning-server/python-reference/revoscalepy/rx-import#returns

# Displaying info
claims_data_frame = rx_import(outfileTypeRelabeled)

info = rx_get_info(claims_data_frame, get_var_info = True)
print(info)

print(claims_data_frame.head())
