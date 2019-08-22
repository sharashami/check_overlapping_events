from src.util import printOverlappingEvents, generateEvents, check_overlapping_events
import sys

if len(sys.argv) != 3:
    print("Please, provide two arguments")
    print("1: the number of events to be generated")
    print("2: 0 or 1 if you want to print out the pairs of overlapped events")
    raise Exception("Provide the correct arguments")

n_events = int(sys.argv[1])
print_list = int(sys.argv[2])

if print_list:
    printOverlappingEvents( check_overlapping_events( generateEvents(n_events) ) )
else:
    n = len(check_overlapping_events( generateEvents(n_events) ))
    print(f'{n} pairs of overlapped events were found')
    
    
