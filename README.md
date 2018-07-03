# Revoscalepy Code Examples
This repository contains the Python version of RevoscaleR code examples provided in the RevoscaleR user guide.

# Prerequisites

Check out this repository locally.

## RevoscalePy

### Installation
The examples use the `revoscalepy` package, which is available from with a 'Machine Learning Server' or 'SQL Server Machine Learning' installation (see https://docs.microsoft.com/en-us/machine-learning-server/python-reference/revoscalepy/revoscalepy-package). 

If you don't have any of these, you can install the standalone version of SQL Server 2017 Machine Learning Server (see https://docs.microsoft.com/en-us/sql/advanced-analytics/install/sql-machine-learning-standalone-windows-install?view=sql-server-2017)

### Code execution
From Visual Studio, open the solution file (`Revoscalepy-code-examples.sln`). Then:

1. Open the Python environments windows (in View > Other Windows)
2. 

The easiest way to run the example is from Visual Studio 2017 (or later). Make sure it is intalled, then lauch the Visual Studio Installer:

- Click on Install
- Make sure the Python environment is selected
- Make sure Anaconda3 is installed (select it)
- Click on Modify

### Visual Studio configuration






## Environment setting
After checking out this repository, copy the `.env_tmpl` file into `.env` in your local environment.

## Data
The data files used in the examples are available from https://packages.revolutionanalytics.com/datasets/

Downloaded them locally to `C:\Temp\Data` (or any other location specified in your `.env` file)

## Packages
Some packages may not be installed on your environment, perform:

`pip install -U python-dotenv`

# FAQ

## `ModuleNotFoundError: No module named 'revoscalepy'`


## `No matching distribution found for revoscalepy`
You are likely trying to perform `pip install revoscalepy`. This package is not available from a public repository, see the prerequisite section above.

