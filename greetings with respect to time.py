import datetime

# get the current time
current_time = datetime.datetime.now()

# extract the hour from the current time
current_hour = current_time.hour

# check if it's morning or afternoon
if current_hour <12:
    greeting = "Good morning"
elif current_hour >18:
    greeting = "Good Evening"

else:
    greeting = "Good afternoon"

# print the current time and greeting
print("The current time is:", current_time.strftime("%H:%M:%S"))
print(greeting + ", sir!")


#for local time
# import time

# current_time = time.localtime()
# hour = current_time.tm_hour
# minute = current_time.tm_min

# if hour < 12:
#     greeting = "Good morning"
# else:
#     greeting = "Good afternoon"

# print("The current time is: {:02d}:{:02d} {}".format(
#     12 if hour == 0 else hour if hour <= 12 else hour - 12, minute,
#     "AM" if hour < 12 else "PM"))
# print("{} sir!".format(greeting))
