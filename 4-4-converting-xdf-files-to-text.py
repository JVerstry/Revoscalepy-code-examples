# 4.4 Converting .xdf Files to Text
import os
import settings as st
from revoscalepy import rx_data_step, RxTextData, RxXdfData

# Import / Export
infile = os.path.join(st.SAMPLE_DATA_DIR,'claims.txt')
outfile = os.path.join(st.RESULTS_LOCATION,'claims.xdf')

claimsCsv = RxTextData(infile)
claimsXdf = RxXdfData(outfile)

rx_data_step(input_data = claimsCsv,
    output_file = claimsXdf, 
    overwrite = True)

outfile2 = os.path.join(st.RESULTS_LOCATION,'claimsMyDelimiter.txt')
claimsTxt = RxTextData(outfile2, delimiter = "\t")

rx_data_step(input_data = claimsXdf,
    output_file = claimsTxt,
    overwrite = True)

## REM: It seems like the 'delimiter' parameter is not taken into account.
## A release 0.9.2 bug?
