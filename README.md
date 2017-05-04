# twittabase
Twitter database generation using Tweepy libraries


## Requirements
### 1 - Pip modules
sudo pip install regex tweepy textblob argparse
### 2 - Create a twitter account and a twitter app, and fill the config.py file


## Usage
python twittabase.py -q {query} -l {limit} -g {geocode} -o {output (csv file)}

## Example
python twittabase.py -q "le pen" -l 100 -g "40.432,-3.708,10km" -o aaa.csv
