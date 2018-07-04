# 2.2.1 Specifying a missed value for strings
import os
import settings as st
from revoscalepy import rx_import, rx_get_info, RxXdfData

# Importing Delimited Text Data
infile = os.path.join(st.SAMPLE_DATA_DIR,'AirlineDemoSmall.csv')

## REM: Our RxOptions.set_option("OutDataPath", [RESULTS_LOCATION])
## is not taken into account (bug?). Hence, we specify the full location
outfile = os.path.join(st.RESULTS_LOCATION,'airExample.xdf')

# The 'missingValueString' option is not available in RevoscalePy
# See: https://docs.microsoft.com/en-us/machine-learning-server/python-reference/revoscalepy/rxmissingvalues

# A question has been asked on StackOverflow for missing string values:
# https://stackoverflow.com/questions/51155965/default-value-for-strings-when-missing-in-revoscalepy-import

airData = rx_import(input_data = infile, output_file = outfile,
    strings_as_factors = True,
    # missingValueString = "M"
    rows_per_read = 200000,
    overwrite = True)
