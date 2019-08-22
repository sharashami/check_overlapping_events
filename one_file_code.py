from datetime import datetime, date
import random
import unittest
import time

#FUNCTIONS

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



                




# TESTS 
#TestTwoEventsOverlapping
#TestReturnedListOfOverlappingEvents
#TestGenerateEvents

class TestReturnedListOfOverlappingEvents(unittest.TestCase):

    def test_input_list_sized_1(self):
        self.assertIsNone(check_overlapping_events(
                [
                   {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    }
                ])
                )
          

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            check_overlapping_events([])
        
    def test_none(self):
        with self.assertRaises(ValueError):
            check_overlapping_events(None)
        

    def test_number_of_pairs_of_overlapping_events_equals_0(self):
        
        self.assertEqual(
            0, len( check_overlapping_events(
                [
                   {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    },
                    {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event2',
                    }
                ])
                )
        )    

    def test_pairs_of_overlapped_events_sized_1(self):
        overlapped_events = check_overlapping_events(
                [
                   {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    },
                    {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event2',
                    }
                ])
        self.assertListEqual( ['event1','event2'] ,[i['name'] for i in overlapped_events[0]])
    
    def test_pairs_of_overlapped_events_sized_2(self):
        
        overlapped_events =  check_overlapping_events(
                [
                   {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    },
                    {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event2',
                    },
                    {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "10/16/2019 01:30",
                    'name' : 'event3',
                    },
                    {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "10/16/2019 01:30",
                    'name' : 'event4',
                    }
                ])
                
        self.assertListEqual( ['event1','event2'] ,[i['name'] for i in overlapped_events[0]])
        self.assertListEqual( ['event3', 'event4'] ,[i['name'] for i in overlapped_events[1]])
        

    def test_number_of_pairs_of_overlapping_events_equals_1(self):
        
        self.assertEqual(
            1, len( check_overlapping_events(
                [
                   {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    },
                    {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event2',
                    }
                ])
                )
        )
    
    def test_number_of_pairs_of_overlapping_events_equals_2(self):
        
        self.assertEqual(
            2, len( check_overlapping_events(
                [
                   {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event1',
                    },
                    {
                    'start_time' : "08/16/2019 00:30",
                    'end_time' : "08/16/2019 01:30",
                    'name' : 'event2',
                    },
                    {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "10/16/2019 01:30",
                    'name' : 'event3',
                    },
                    {
                    'start_time' : "10/16/2019 00:30",
                    'end_time' : "10/16/2019 01:30",
                    'name' : 'event4',
                    }
                ])
                )
        )
        

class TestGenerateEvents(unittest.TestCase):

    def test_corrected_return_size_when_n_equals_5(self):
        self.assertEqual(5, len(generateEvents(5)))

    def test_n_equals_1(self):
        self.assertEqual(1, len(generateEvents(1)))

    def test_n_equals_0(self):
        with self.assertRaises(ValueError):
            generateEvents(0)


class TestTwoEventsOverlapping(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            is_overlapping([], [])
        
    def test_none(self):
        with self.assertRaises(ValueError):
            is_overlapping(None, None)
        

    def test_overlap_event1_occurs_exactly_same_time_event2(self):
        self.assertTrue(is_overlapping(
            {
            'start_time' : "08/16/2019 00:30",
            'end_time' : "08/16/2019 01:30",
            'name' : 'event1',
            },
            {
            'start_time' : "08/16/2019 00:30",
            'end_time' : "08/16/2019 01:30",
            'name' : 'event2',
            }))

    
    def test_overlap_event1_starts_after_event2_starts_AND_event1_ends_same_time_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))   


    def test_overlap_event1_is_in_event2(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:25",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))  


    def test_overlap_event1_starts_after_event2_starts_AND_event1_ends_after_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:35",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))  



    def test_overlap_event1_starts_same_time_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 01:30",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))  

    def test_not_overlap_event1_occurs_before_event2(self):
        self.assertFalse(is_overlapping(
        {
        'start_time' : "07/16/2019 00:30",
        'end_time' : "07/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))  


    def test_not_overlap_event1_occurs_after_event2(self):
        self.assertFalse(is_overlapping(
        {
        'start_time' : "09/16/2019 00:30",
        'end_time' : "09/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        })) 



    def test_overlap_event1_covers_event2(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:25",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        })) 


    def test_overlap_event1_starts_before_event2_starts_AND_event1_ends_before_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:25",
        'end_time' : "08/16/2019 01:20",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))



    def test_overlap_event1_starts_same_time_event2_starts_AND_event1_ends_before_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:20",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))


    def test_overlap_event1_starts_same_time_event2_starts_AND_event1_ends_after_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))

    def test_overlap_event1_starts_before_event2_starts_AND_event1_ends_same_time_event2_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:20",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))
    #SAME TESTS WITH CHANGED PARAMETERS    
    
    def test_overlap_event2_occurs_exactly_same_time_event1(self):
        self.assertTrue(is_overlapping(            
            {
            'start_time' : "08/16/2019 00:30",
            'end_time' : "08/16/2019 01:30",
            'name' : 'event2',
            },{
            'start_time' : "08/16/2019 00:30",
            'end_time' : "08/16/2019 01:30",
            'name' : 'event1',
            }))

    def test_overlap_event2_starts_after_event1_starts_AND_event2_ends_same_time_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },{
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event1',
        }
        ))    

    def test_overlap_event2_is_in_event1(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:25",
        'name' : 'event1',
        })) 


    def test_overlap_event2_starts_after_event1_starts_AND_event2_ends_after_event1_ends(self):
        
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:35",
        'end_time' : "08/16/2019 01:35",
        'name' : 'event1',
        }))  


    def test_overlap_event2_starts_same_time_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 01:30",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        })) 

    def test_not_overlap_event2_occurs_before_event1(self):
        self.assertFalse(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "07/16/2019 00:30",
        'end_time' : "07/16/2019 01:30",
        'name' : 'event1',
        }))  
    
    

    def test_not_overlap_event2_occurs_after_event1(self):
        self.assertFalse(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "09/16/2019 00:30",
        'end_time' : "09/16/2019 01:30",
        'name' : 'event1',
        })) 


    def test_overlap_event2_covers_event1(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:25",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        })) 

    def test_overlap_event2_starts_before_event1_starts_AND_event2_ends_before_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:25",
        'end_time' : "08/16/2019 01:20",
        'name' : 'event1',
        }))

    def test_overlap_event2_starts_same_time_event1_starts_AND_event2_ends_before_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:20",
        'name' : 'event1',
        }))
    
    def test_overlap_event2_starts_same_time_event1_starts_AND_event2_ends_after_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:40",
        'name' : 'event1',
        }))
    def test_overlap_event2_starts_before_event1_starts_AND_event2_ends_same_time_event1_ends(self):
        self.assertTrue(is_overlapping(
        {
        'start_time' : "08/16/2019 00:20",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event1',
        },
        {
        'start_time' : "08/16/2019 00:30",
        'end_time' : "08/16/2019 01:30",
        'name' : 'event2',
        }))

        
#MAIN

print("Hello!!")
print()
print("THE CHALLENGE: when maintaining a calendar of events, it is important to know if an event overlaps with another event. Given a sequence of events, each having a start and end time, write a program that will return the sequence of all pairs of overlapping events.")
      
print()
print("Let's start it!")

print()
print("Type 1 to run the code or 2 to test")
      
test_or_run = input()
      
if int(test_or_run) == 1:
    
    print()
    print("Ok, let's run the code. You need to say how many events you want me to generate. ")
    print("Type the number of events to be generated. The events are generated between August/2019 and November/2020 and sized up to 4 days.")
    n_events = int(input())
      
    print()
    print("Now, type 1 if you want to print out the pairs of overlapped events or 0 otherwise")
    
    print("If you want to print out the results, maybe the program will be halted for excessive output if there is a bunch of overlapped events, right? Now, type 1 if you want to print out the pairs of overlapped events or 0 otherwise")
    
    print_list = int(input())
    
    print()
    print("Running!!")
    print()
    
    if print_list:
        start_time = time.time()
        events = check_overlapping_events( generateEvents(n_events) )
        end_time = time.time()
        time_it_took = end_time-start_time
        printOverlappingEvents(events )
        print(f'runtime: {time_it_took}')
    else:
        start_time = time.time()
        events = check_overlapping_events( generateEvents(n_events) )
        end_time = time.time()
        time_it_took = end_time-start_time
        n = len(events)
        print(f'runtime: {time_it_took}')
        print(f'{n} pairs of overlapped events were found')
    
    print("Done!!")

      
elif int(test_or_run) == 2:
    unittest.main(exit=False)
