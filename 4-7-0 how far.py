# 4-7-0 how far will I go
# totalTime - How long the horse will be traveling (in seconds)
# runTime - How long the horse can run for before having to rest (in seconds)
# restTime - How long the horse have to rest for after running (in seconds)
# speed - The max speed of the horse (in metres/second)
# from decimal import Decimal, getcontext
# getcontext().prec = 15

def travel(total_time, run_time, rest_time, speed):
    meters_traveled = 0

    #if total_time < run_time:
    #    return speed * total_time
    if total_time == 0 or run_time == 0 or speed == 0:
         return 0
    else:
        while total_time > 0:
            if total_time < run_time:
                meters_traveled += speed * total_time
                return meters_traveled
            total_time -= run_time
            meters_traveled += speed * run_time
            total_time -= rest_time
        return meters_traveled

# print (travel(1000, 10, 127, 14)) # 1120
# print (travel(1000, 10, 0, 10)) #  10000
# print (travel(25, 50, 120, 18)) # 450

# Test.it("works for big numbers")
# print (travel(35869784, 90, 100, 5)) # 84954920
# print (travel(1234567, 4, 3, 11)) #  7760148
# print (travel(100000000, 21, 5, 14)) #  1130769276

# Test.it("handles zero values")
# print (travel(0, 100, 10, 14)) #  0
# print (travel(250, 0, 5, 14)) # 0
# print (travel(100, 10, 0, 14)) # 1400
print (travel(500, 100, 10, 0)) #  0
