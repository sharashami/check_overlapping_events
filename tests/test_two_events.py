import unittest
from src import util as events
from datetime import datetime

class TestTwoEventsOverlapping(unittest.TestCase):

    def test_overlap_event1_occurs_exactly_same_time_event2(self):
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertFalse(events.is_overlapping(
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
        self.assertFalse(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(            
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertFalse(events.is_overlapping(
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
        self.assertFalse(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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
        self.assertTrue(events.is_overlapping(
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


if __name__ == '__main__':
    unittest.main()