from datetime import datetime

def check_overlapping_events(events):
    n_events = len(events)
    overlapping_events = []
    
    pre_processing_input(events)

    for i in range(0,n_events):
        for j in range(i,n_events):
            if is_overlapping(events[i],events[j]):
                overlapping_events.append([events[i],events[j]]) 
    
    return overlapping_events

def is_overlapping(event1, event2):    

    return not ( 
                event1['end_time'] < event2['start_time']  
                or event1['start_time'] > event2['end_time']                
                )
                
def strToDatetime(e):
        f = lambda a : datetime.strptime(a,"%m/%d/%Y %H:%M")
        e['start_time'] = f(e['start_time'])
        e['end_time'] = f(e['end_time'])
        return e


def pre_processing_input(events):    
    return list(map(lambda e : strToDatetime, events))
