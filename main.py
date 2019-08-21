from src.util import printOverlappingEvents, generateEvents, check_overlapping_events

if __name__ == "__main__":
    printOverlappingEvents( check_overlapping_events( generateEvents(5, sort=True) ) )

