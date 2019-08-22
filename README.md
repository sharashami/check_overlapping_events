# Check overlapping events
When maintaining a calendar of events, it is important to know if an event overlaps with another event. Given a sequence of events, each having a start and end time, write a program that will return the sequence of all pairs of overlapping events.


# How to run?

* Set a python enviroment having all packages listed in requirements.txt file 
* Then, run as follow providing two arguments: 1) the number of events to be generated, and 2) 0 or 1 if you want to print out the pairs of overlapped events
* Looking at the example below, you want to generate 1000 events and you do not want to print out the results

```shell
   python main.py 1000 0    
```
## Or you can run one_file_code.py for command line interaction

```shell
   python one_file_code.py   
```

# How to test?

```shell
   python -m unittest discover -s tests  
```

# How did I approach?

* Started understanding the problem and the goals
* As I talked to Amanda, I'm free to tackle the problem my own, so
* Identified the input data, goals and output
* Overall, there is a list of events as input, then it is sorted by start date, after this it is checked if two events do not overlap, if they overlap, they are appended to the overlapping events list
* One can check all my thoughts in designing_solution folder

# The input is a list of events

* There is a function to generate n random events 
* The events are generated between August/2019 and November/2020 and sized up to 4 days 
* I tried to add events at the same start and/or end time, and with different size up to 4 days

```shell
    start = datetime(2019, 8, 1,hour=0, minute=0).timestamp()
    end =  datetime(2020, 11, 1,hour=0, minute=0).timestamp()
    size = 345600 #4 days    
```
* The events look like 

```shell
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
    ]
```
# The output is something like 

```shell
82 pair(s) of overlapping events

event 0 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00
event 1 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00

event 0 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00
event 35 starting at 08/02/2019 21:37, ending at 08/06/2019 21:37

event 0 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00
event 36 starting at 08/02/2019 21:37, ending at 08/06/2019 04:37

event 1 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00
event 35 starting at 08/02/2019 21:37, ending at 08/06/2019 21:37

event 1 starting at 08/01/2019 00:00, ending at 08/05/2019 00:00
event 36 starting at 08/02/2019 21:37, ending at 08/06/2019 04:37

event 35 starting at 08/02/2019 21:37, ending at 08/06/2019 21:37
event 36 starting at 08/02/2019 21:37, ending at 08/06/2019 04:37

event 35 starting at 08/02/2019 21:37, ending at 08/06/2019 21:37
event 22 starting at 08/06/2019 17:44, ending at 08/10/2019 17:44

event 22 starting at 08/06/2019 17:44, ending at 08/10/2019 17:44
event 24 starting at 08/09/2019 07:43, ending at 08/10/2019 20:56

event 47 starting at 08/13/2019 16:19, ending at 08/17/2019 16:19
event 23 starting at 08/14/2019 03:29, ending at 08/17/2019 13:18

event 47 starting at 08/13/2019 16:19, ending at 08/17/2019 16:19
event 32 starting at 08/14/2019 19:08, ending at 08/18/2019 19:08

event 47 starting at 08/13/2019 16:19, ending at 08/17/2019 16:19
event 9 starting at 08/14/2019 22:45, ending at 08/16/2019 19:24

event 47 starting at 08/13/2019 16:19, ending at 08/17/2019 16:19
event 10 starting at 08/16/2019 19:24, ending at 08/20/2019 10:29

event 23 starting at 08/14/2019 03:29, ending at 08/17/2019 13:18
event 32 starting at 08/14/2019 19:08, ending at 08/18/2019 19:08

event 23 starting at 08/14/2019 03:29, ending at 08/17/2019 13:18
event 9 starting at 08/14/2019 22:45, ending at 08/16/2019 19:24

event 23 starting at 08/14/2019 03:29, ending at 08/17/2019 13:18
event 10 starting at 08/16/2019 19:24, ending at 08/20/2019 10:29

event 32 starting at 08/14/2019 19:08, ending at 08/18/2019 19:08
event 9 starting at 08/14/2019 22:45, ending at 08/16/2019 19:24

event 32 starting at 08/14/2019 19:08, ending at 08/18/2019 19:08
event 10 starting at 08/16/2019 19:24, ending at 08/20/2019 10:29

event 32 starting at 08/14/2019 19:08, ending at 08/18/2019 19:08
event 46 starting at 08/18/2019 11:25, ending at 08/22/2019 11:25

event 9 starting at 08/14/2019 22:45, ending at 08/16/2019 19:24
event 10 starting at 08/16/2019 19:24, ending at 08/20/2019 10:29

event 10 starting at 08/16/2019 19:24, ending at 08/20/2019 10:29
event 46 starting at 08/18/2019 11:25, ending at 08/22/2019 11:25

event 3 starting at 08/22/2019 11:50, ending at 08/26/2019 11:50
event 4 starting at 08/22/2019 11:50, ending at 08/26/2019 11:50

event 3 starting at 08/22/2019 11:50, ending at 08/26/2019 11:50
event 26 starting at 08/22/2019 17:51, ending at 08/23/2019 12:36

event 3 starting at 08/22/2019 11:50, ending at 08/26/2019 11:50
event 49 starting at 08/23/2019 03:52, ending at 08/26/2019 23:40

event 4 starting at 08/22/2019 11:50, ending at 08/26/2019 11:50
event 26 starting at 08/22/2019 17:51, ending at 08/23/2019 12:36

...

```

# Runtime
## The runtime depends on the generated events

* 5 events between August/2019 and November/2020 
``` shell
    runtime: 0.003529787063598633
    1 pairs of overlapped events were found
```

* 10 events between August/2019 and November/2020 
``` shell
runtime: 0.00912332534790039
1 pairs of overlapped events were found
```


* 50 events between August/2019 and November/2020 
``` shell
    runtime: 0.006481170654296875
    46 pairs of overlapped events were found
```
* 1000 events between August/2019 and November/2020 
``` shell
    runtime: 0.07254600524902344
    6858 pairs of overlapped events were found
```

* 10000 events between August/2019 and November/2020 
``` shell
    runtime: 2.570497512817383
    649426 pairs of overlapped events were found
```
* 20000 events between August/2019 and November/2020 
``` shell
    runtime: 7.3763508796691895
    2570959 pairs of overlapped events were found
```

# Improvements to the future?

* Code refactoring
* Adding the output in a file
* Think about more test cases

