# 3.6 Working with an Xdf Data Source
import os
import settings as st
from revoscalepy import rx_data_step

## REM: The rxOpen and rxReadNext functions are not implemented in RevoscalePy
## However, a workaround can be implemented:

# Importing data by chunks
infile = os.path.join(st.SAMPLE_DATA_DIR,'claims.xdf')

readLines = 0

while True:

    myClaims = rx_data_step(input_data = infile,
        start_row = readLines,
        number_rows_read = 8,
        report_progress = 0)

    # More lines to process?  
    if myClaims is None:
        # Nope
        break

    readLines = readLines + myClaims.shape[0]

    # Process read lines...
    print("Number of read lines: " + str(readLines))
