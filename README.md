# Revoscalepy Code Examples
This repository contains the Python version of RevoscaleR code examples provided in the RevoscaleR user guide.

# Prerequisites

## Environment setting
Check out this repository locally, then copy the `.env_tmpl` file into `.env` in your local environment.

## RevoscalePy

### Installation
The examples use the `revoscalepy` package, which is available from with a 'Machine Learning Server' or 'SQL Server Machine Learning' installation (see https://docs.microsoft.com/en-us/machine-learning-server/python-reference/revoscalepy/revoscalepy-package). 

If you don't have any of these, you can install the standalone version of SQL Server 2017 Machine Learning Server (see https://docs.microsoft.com/en-us/sql/advanced-analytics/install/sql-machine-learning-standalone-windows-install?view=sql-server-2017)

### Code execution
From Visual Studio, open the solution file (`Revoscalepy-code-examples.sln`). Then:

1. Open the Python environments windows (in View > Other Windows)
2. Create a custom environment where the prefix path is pointing to `C:\Program Files\Microsoft SQL Server\140\PYTHON_SERVER`
3. Make this environment the 'default environment for new project'
4. From the solution explorer window, select and right-click the custom environment
5. Select install from `requirements.txt`

## Data
The data files used in the examples are available from https://packages.revolutionanalytics.com/datasets/

Downloaded them locally to `C:\Temp\Data` (or any other location specified in your `.env` file)

## FAQ

- `ModuleNotFoundError: No module named 'revoscalepy'`: You need to select a Python execution environment where RevoscalePy is installed. See the prerequisite section above.
- `No matching distribution found for revoscalepy`: You are likely trying to perform `pip install revoscalepy`. This package is not available from a public repository, see the prerequisite section above.

