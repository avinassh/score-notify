# Cric Score Notify

Simple python script which displays Cricket Score as notification on OS X. It fetches data from [Cric Info RSS Feed](http://static.cricinfo.com/rss/livescores.xml)

**NOTE:** Works for OS X only. For Linux, check [this](https://github.com/neo1691/scorer.py), which inspired OS X version.

## Screenshots:

![notification](screenshots/screenshot0.png)
![notification center sidebar](screenshots/screenshot1.png)


## Requirements:
- OS X, Python 3
- Requires [terminal-notifier](https://github.com/alloy/terminal-notifier):
        
        brew install terminal-notifier 
- Install libraries mentioned `requirements.txt`:
        
        pip install -r requirements.txt

## Usage:

With default settings:

    python cric-score-notify.py 

If you want to change the fetch frequency, like, may be to 30 seconds:

    python cric-score-notify.py -f 30

If Cric Info is blocked on your network, then you can use proxy server to fetch the scores:

    python cric-score-notify.py -f 45 -p True

When in doubt, run for help:
    
    python cric-score-notify.py -h

## To do:
- ~~fetch frequency~~
- ~~proxy support~~
- better UI for notification?
- tests, CI integration
- Python 2 support

## License:

The MIT License (MIT). Check `LICENSE.MD`