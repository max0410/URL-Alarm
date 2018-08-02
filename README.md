# URL-Alarm
A python alarm that opens a randomly selected website when the time is up.

## Usage

First, setup the alarm by editing the contents of ```url.txt```. For each url you want randomly selected, create a new line. Then, in the command line run ```alarm.py``` with the options:
```
[--hour HOUR]
[--minute MINUTE]
[--AM] [--PM]
```

## Examples

This command sets an alarm for 5:38 PM:
```
python alarm.py --hour 5 --minute 38 --PM
```

To run the alarm in the background, use ```pythonw``` instead.
