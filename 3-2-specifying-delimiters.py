# 3.2 Specifying Delimiters
import os
import settings as st
from revoscalepy import rx_import, rx_get_info, RxTextData

# Importing delimited text data
infile = os.path.join(st.SAMPLE_DATA_DIR,'hyphens.txt')

hyphensTxt = RxTextData(infile, delimiter = '-')
hyphens_data_frame = rx_import(hyphensTxt)

# Displaying info
print(rx_get_info(hyphens_data_frame, get_var_info = True))
print(hyphens_data_frame.head())