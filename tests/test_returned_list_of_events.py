import unittest
from src import events

class TestReturnedListOfOverlappingEvents(unittest.TestCase):

    
    def test_number_of_pairs_of_overlapping_events_equals_0(self):
        
        self.assertEqual(
            0, len( events.check_overlapping_events(
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
        overlapped_events = events.check_overlapping_events(
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
        
        overlapped_events =  events.check_overlapping_events(
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
            1, len( events.check_overlapping_events(
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
            2, len( events.check_overlapping_events(
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
        
           


if __name__ == '__main__':
    unittest.main()