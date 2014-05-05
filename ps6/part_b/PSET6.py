from Request import *
from bisect import bisect_left
# BEGIN STUDENT CODE
####################

# create_schedule
# input: requests := unordered list of Request objects
# output: schedule := unordered list of Request objects, a sub-set of requests
#     such that the requests inn the schedule are non-overlapping
#     and the total time slots are maximized
'''Klink Reasoning: 
At the end of any given time request, the maximum profit for that endpoint
either includes of doesn't include that endpoint.  In other words, if you were
maximizing profit as you go along, the maximum profit at each endpoint would be
the max of the previous endpoint and the sum of the best at the start of the 
time stamp (the endpoint closest going left from the start) and the value. '''
def create_schedule(requests):
  schedule = []
  sort_by_end = sort_requests(requests,end)
  end_points = [x.end for x in sort_by_end]
  i = 1
  length = len(end_points) + 1
  max_so_far = [0]*(length)
  max_so_far[0] = 0
  while ( i < length ):
    # Value at i if current time stamp is included
    stamp = sort_by_end[i-1]
    start = stamp.start
    index_nearest_start = bisect_left(end_points, start, 0, i)
    valBefore = max_so_far[index_nearest_start]
    valInclude = valBefore + len(stamp)
    valMax = max(valInclude, max_so_far[i-1])
    max_so_far[i] = valMax
    i += 1
  # Was not able to come up with a way to avoid doing this.  After doing part A, will look for way
  #  to do this with one pass.
  # Use list of max so far, in reverse order, to get list of things in optimal schedule
  i = len(max_so_far) - 1
  j = len(max_so_far) - 2
  while ( j >= 0 ):
    val_i = max_so_far[i]
    val_j = max_so_far[j]
    if ( val_i > val_j ): #include the stamp in ith position
      stamp_i = sort_by_end[i-1]
      if ( len(stamp_i) + val_j == val_i ): #Previous step was j
        schedule.append(stamp_i)
        i = j
        j -= 1
      else:
        j -= 1
    else: # don't include stamp
      i = j
      j -= 1
      
  return schedule
####################
# END STUDENT CODE
