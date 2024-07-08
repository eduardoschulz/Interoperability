# Charts!

This folders is dedicated to all the charts produced by the experiments. It 
contains python scripts that a library called matplotlib to analyze and draw 
the charts.

## Building the charts using our data!

If you want to rebuild the graphs using the data present in this repository
you'll need to these steps:

- A computer with python 3.10 or higher
- Clone this repository using `git clone https://github.com/eduardoschulz/Interoperabilidade` or download the [zip archive](https://github.com/eduardoschulz/Interoperabilidade/archive/refs/heads/master.zip)
- Navigate to the `graphs` folder inside the repository
- Initiate a python virtual environment (optional, but recommend) with `python3 -m venv venv` (linux, mac) or `py -m venv venv` (windows)
- Activate the virtual environment `source venv/bin/activate` (linux, mac) `.\venv\bin\activate.bat` (windows)
- Install all dependencies with `pip install -r requirements.txt`
- Build the desired chart with `python3 {filename}` (linux, mac) `py {filename}` (windows). Or build all charts at once using the `build.py` script. All the files ending in `.py` (except `build.py`) inside the `graphs` folder are charts.
