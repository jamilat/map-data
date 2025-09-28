# map-data
Data processing for Software Management and Processes subject (SWEN90016 University of Melbourne 2025 Semester 2 from July-November)

$WORKDIR is the project's working directory containing all files associated with it.


## Create a virtual environment
`python3 -m venv venv`

## Run virtual environment
`source venv/bin/activate`

## If pip and python3 are not pointing to the same Python installation, then force them to match (`python3 -m pip install...` as below)
## Install dependencies
`python3 -m pip install requests`
`python3 -m pip install python-dotenv`
`python3 -m pip install --user -e .` on MacOS
`pip install -e $WORKDIR`

## Ensure that pip and python3 are pointing to the same Python installation
`which pip`
`which python3`

## Ensure requests installation
`python3 -c "import requests; print(requests.__version__)"`

# WPGMaps in WordPress
Required columns for importing a file are outlined in
https://www.wpgmaps.com/help/docs/importing-files/

