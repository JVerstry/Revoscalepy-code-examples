# 2.15 Using Data from the Hadoop Distributed File System
import os
import settings as st
from revoscalepy import RxHdfsFileSystem, RxTextData, RxXdfData

## REM: This example is not meant to be operational.
## It only provides general guidance.

# Connecting to Hadoop file system
hdfsFS = RxHdfsFileSystem(host_name = 'x.y.z', port = 1234)

# Connecting to data
txtSource = RxTextData("/test/HdfsData/AirlineCSV/CSVs/1987.csv", file_system = hdfsFS)
xdfSource = RxXdfData("/test/HdfsData/AirlineData1987", file_system = hdfsFS)

# ...
