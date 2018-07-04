# 2.8 Append to an existing file
import os
import settings as st
from revoscalepy import rx_import, rx_get_info, RxOptions

# Input file
firstFile = os.path.join(st.SAMPLE_DATA_DIR,'claims.txt')

# Output file
outfile = os.path.join(st.RESULTS_LOCATION,'claimsclaims.xdf')

# Creating 1st file
rx_import(input_data = firstFile, output_file = outfile,
    strings_as_factors = True,
    overwrite = True)

# Displaying info
claims_data_frame = rx_import(outfile)
print(rx_get_info(claims_data_frame, get_var_info = True))

# Appending the same file to the output
rx_import(input_data = firstFile, output_file = outfile,
    strings_as_factors = True,
    append = "rows")

# Re-displaying info
claims_data_frame = rx_import(outfile)
print(rx_get_info(claims_data_frame, get_var_info = True))
