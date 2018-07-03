# 2.2 Importing Delimited Text Data
import os
import settings as st
from revoscalepy import rx_import, rx_get_info, RxOptions

# Importing Delimited Text Data
infile = os.path.join(st.SAMPLE_DATA_DIR,'claims.txt')

claims_data_frame = rx_import(infile)

# Displaying info
info = rx_get_info(claims_data_frame, get_var_info = True)
print(info)

# Saving text data into XDF file

## REM: Our RxOptions.set_option("OutDataPath", [RESULTS_LOCATION])
## is not taken into account (bug?). Hence, we specify the full location
outfile = os.path.join(st.RESULTS_LOCATION,'claims.xdf')

rx_import(input_data = infile, output_file = outfile,
    overwrite = True)
