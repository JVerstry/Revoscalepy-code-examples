# 2.11 Importing Wide Data
import os
import settings as st
from revoscalepy import rx_import, rx_get_info, RxOptions

# Import/Export file
infile = os.path.join(st.SAMPLE_DATA_DIR,'claims.txt')
outfile = os.path.join(st.RESULTS_LOCATION,'claimsWithColInfo.xdf')

# Defining transformation
colInfoList = {
    'age': {
        'type': 'factor',
        'levels': [ '17-20','21-24','25-29','30-34','35-39','40-49','50-59','60+' ]
    },
    'car.age': {
        'type': 'factor',
        'levels': [ '0-3','4-7','8_9','10+' ]
    },
    'type': {
        'type': 'factor',
        'levels': [ 'A','B','C','D' ]
    },
}

# Applying transformation
rx_import(input_data = infile, output_file = outfile,
    column_info = colInfoList,
    overwrite = True)

# Displaying info
claims_data_frame = rx_import(outfile)

print(rx_get_info(claims_data_frame, get_var_info = True))
print(claims_data_frame.head())

