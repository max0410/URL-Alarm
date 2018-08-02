import webbrowser, time, random, sys, argparse

def alarm(hour, minute, am):
    if am and hour == 12: hour = 0
    if not am: hour += 12
    nowHour, nowMinute, nowSecond = time.strftime("%H %M %S", time.localtime()).split()
    waitTime = (hour - int(nowHour))*360 + (minute - int(nowMinute))*60 - int(nowSecond)
    try:
        time.sleep(waitTime)
    except ValueError:
        print("Please pick a time that hasn't happened yet.")
        sys.exit()
    webbrowser.open(random.choice(open("urls.txt").read().split("\n")))

parser = argparse.ArgumentParser()
parser.add_argument('--hour')
parser.add_argument('--minute')
parser.add_argument('--AM', action='store_true')
parser.add_argument('--PM', action='store_true')
args = parser.parse_args()
alarm(int(args.hour), int(args.minute), args.AM)

    
