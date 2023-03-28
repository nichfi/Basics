# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 21:26:34 2023

@author: nicko

"""
import datetime
def main():

    
    # Lambda function to check if it is currently December
    is_december = lambda: datetime.datetime.now().month == 12
    
    # Lambda function to check how many months are left until December
    months_until_december = lambda: 12 - datetime.datetime.now().month
    
    # Lambda function to check if it is currently past 21:00 (bedtime)
    is_past_bedtime = lambda: datetime.datetime.now().time() >= datetime.time(21, 0, 0)
    
    # Lambda function to check how many hours, minutes, and seconds are left until 21:00
    time_until_bedtime = lambda: (datetime.datetime.combine(datetime.date.today(), datetime.time(21, 0, 0)) - datetime.datetime.now()).seconds
    
    print("Welcome to Christmas countdown!")
    print("Is Christmas this month?")
    
    if is_december():
        print("Yes! Let's make Santa happy and go to sleep early!")
    else:
        months = months_until_december()
        print("Nope, but the number of months until December is: {:d}".format(months))
        print("Let's make Santa happy and go to sleep early!")
    if is_past_bedtime():
        print("It's already past your bedtime! Time to go to bed!")
    else:
        time = time_until_bedtime()
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        print("You have {:d} hours, {:d} minutes, and {:d} seconds until bedtime.".format(hours, minutes, seconds))
main()