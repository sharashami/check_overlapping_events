from datetime import datetime, date
import random

def check_overlapping_events(events):
    if events == None or len(events) == 0:
        raise ValueError("Empty or None list. Provide a valid list of events")
    if len(events) == 1:
        return None
        
    n_events = len(events)
    overlapping_events = []
    eventsToDatetime(events)

    for i in range(0,n_events):        
        for j in range(i+1,n_events):
            if events[i]['end_time'] < events[j]['start_time']:#no need to keep checking
                break
            if is_overlapping(events[i],events[j]):
                overlapping_events.append([events[i],events[j]]) 
    
    return overlapping_events


def eventsToDatetime(events):    
    return list(map(lambda e : strToDatetime, events))

def strToDatetime(e):
        f = lambda a : datetime.strptime(a,"%m/%d/%Y %H:%M")
        e['start_time'] = f(e['start_time'])
        e['end_time'] = f(e['end_time'])
        return e

def is_overlapping(event1, event2):    
    if event1 == None or len(event1) == 0 or event2 == None or len(event2) == 0:
        raise ValueError("Empty or None events. Provide a valid event")


    return not ( 
                event1['end_time'] < event2['start_time']  
                or event1['start_time'] > event2['end_time']                
                )


def generateEvents(num):
    if num == 0:
        raise ValueError("Provide number of events greater than zero")
        
    start = datetime(2019, 8, 1,hour=0, minute=0).timestamp()
    end =  datetime(2020, 11, 1,hour=0, minute=0).timestamp()
    size = 345600 #4 days
    events = [datetimeEventToDict(start,start+size,0)]
    
    for i in range(num-1):
        e_size = random.randrange(0, 345600) if random.random() > 0.5 else 345600
        if (random.random() > 0.5):
            e_start = datetime.strptime(events[-1]['start_time'],"%m/%d/%Y %H:%M").timestamp() if ( random.random() > 0.6 ) else random.randrange(start, end)
        else:
            e_start = datetime.strptime(events[-1]['end_time'],"%m/%d/%Y %H:%M").timestamp() if (random.random() > 0.6 ) else random.randrange(start, end)
            
        events.append(datetimeEventToDict( e_start,  e_start + e_size,  i+1))
    
    return sorted(events, key= lambda e: datetime.strptime(e['start_time'],"%m/%d/%Y %H:%M").timestamp())

def datetimeEventToDict(start, end, n):
    return {'name' : str(n),
            'start_time' : datetime.fromtimestamp(start).strftime("%m/%d/%Y %H:%M"),
            'end_time' : datetime.fromtimestamp(end).strftime("%m/%d/%Y %H:%M"),
           
        }

def printOverlappingEvents(events):
    print(f'{len(events)} pair(s) of overlapping events')
    print()
    eventDetail = lambda i : f'event {i["name"]} starting at {i["start_time"]}, ending at {i["end_time"]}'
    for i in events:
        print(eventDetail(i[0]))
        print(eventDetail(i[1]))
        print()



                


