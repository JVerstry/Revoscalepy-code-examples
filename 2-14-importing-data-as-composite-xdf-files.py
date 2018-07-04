# 2.14 Importing Data as Composite Xdf Files
import os
import settings as st
from revoscalepy import RxTextData, RxXdfData, rx_import

# Import files directory
mortDefaultCsvDir = os.path.join(st.DATA_LOCATION, 'mortDefaultCsv')
mortDefaultCsv = RxTextData(mortDefaultCsvDir)

# Export files directory
mortDefaultCompXdfDir = os.path.join(st.RESULTS_LOCATION, 'mortDefaultXdf')
os.makedirs(mortDefaultCompXdfDir, exist_ok = True)
mortDefaultCompXdf = RxXdfData(mortDefaultCompXdfDir, create_composite_set = True)

# Creating composite files
rx_import(input_data = mortDefaultCsv, output_file = mortDefaultCompXdf,
    overwrite = True)

# Displaying created file
metadataDir = os.path.join(mortDefaultCompXdfDir, 'metadata')
print(os.listdir(metadataDir))

dataDir = os.path.join(mortDefaultCompXdfDir, 'data')
print(os.listdir(dataDir))

