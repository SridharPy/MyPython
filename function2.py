def minutes_to_hour(min):
    hour = min /60
    return hour
def seconds_to_hour(sec):
    hour = sec / 3600
    return hour

print("Enter Minutes to be convereted to Hour")
print(minutes_to_hour(int(input())))
print("Enter Seconds to be converetd to Hour")
print(seconds_to_hour(int(input())))
