'''////////////////////////
lesson 01 - functions
write an app that reminds ppl to take a break from working

1. keep track of time (counter)
2. check counter periodically
3. if counter == what_we_want, trigger alarm function
4. repeat so that it triggers every 2 hours

'''

import time
import webbrowser

total_breaks = 3
break_count = 0
break_period = 10

print "This program started on",  time.asctime()

while break_count < total_breaks:
    time.sleep(break_period)
    ''' plays rick astley'''
    webbrowser.open("http://youtube.com/watch?v=dQw4w9WgXcQ")
    break_count += 1

