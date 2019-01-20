# twittabase
Twitter database generation using Tweepy libraries

## Usage
```
python twittabase.py -q {query} -l {limit} -g {geocode} -o {output (csv file)}
```

## Example
```
python twittabase.py -q "le pen" -l 100 -g "40.432,-3.708,10km" -o aaa.csv
```

![Screenshot](images/img1.png)

## Requirements

Python 2.x:

```
sudo pip install -r requirements.txt
```

Python 3.x:

```
sudo pip3 install -r requirements.txt
```

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)