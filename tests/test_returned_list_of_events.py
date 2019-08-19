import unittest
from src import events

class TestReturnedListOfOverlappingEvents(unittest.TestCase):

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
                    'name' : 'event2',
                    }
                ])
                )
        )
        
           


if __name__ == '__main__':
    unittest.main()