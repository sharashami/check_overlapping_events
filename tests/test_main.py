import unittest
from src import events
from datetime import datetime

class TestEventsOverlapping(unittest.TestCase):

    def test_overlap_event1_occurs_exactly_same_time_event2(self):
        e1 = {
            'start_time' : '',
            'end_time' : '',
            'name' : '',
        }
        e2 = {
            'start_time' : '',
            'end_time' : '',
            'name' : '',
        }

        self.assertTrue(events.is_overlapping([],[]))

    
    def test_overlap_event1_starts_after_event2_starts_AND_event1_ends_same_time_event2_ends(self):
        
        self.assertTrue(events.is_overlapping([],[]))     



    def test_overlap_event1_is_in_event2(self):
        
        
        self.assertTrue(events.is_overlapping([],[]))


    def test_overlap_event1_starts_after_event2_starts_AND_event1_ends_after_event2_ends(self):
        
        
        self.assertTrue(events.is_overlapping([],[]))    



    def test_overlap_event1_starts_same_time_event2_ends(self):
        
        
        self.assertTrue(events.is_overlapping([],[]))

    def test_not_overlap_event1_occurs_before_event2(self):
        
        
        self.assertFalse(events.is_overlapping([],[]))


    def test_not_overlap_event1_occurs_after_event2(self):
        
        self.assertFalse(events.is_overlapping([],[]))



    def test_overlap_event1_covers_event2(self):
        
        self.assertTrue(events.is_overlapping([],[]))



    def test_overlap_event1_starts_before_event2_starts_AND_event1_ends_before_event2_ends(self):
        
        self.assertTrue(events.is_overlapping([],[]))



    def test_overlap_event1_starts_same_time_event2_starts_AND_event1_ends_before_event2_ends(self):
        
        self.assertTrue(events.is_overlapping([],[]))


    def test_overlap_event1_starts_same_time_event2_starts_AND_event1_ends_after_event2_ends(self):
        
        self.assertTrue(events.is_overlapping([],[]))

    #SAME TESTS WITH CHANGED PARAMETERS    
    


if __name__ == '__main__':
    unittest.main()