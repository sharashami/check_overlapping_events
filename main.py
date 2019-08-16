from datetime import datetime
from src.events import check_overlapping_events

events = [
    {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:25",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event2',
        },
    {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 00:30",
        'name' : 'event3',
    }

]

r = check_overlapping_events(events)
for i in r:
    print(i)
print(len(r))
