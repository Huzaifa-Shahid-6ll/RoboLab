# Building a simple study session calculator that claculates how much you have studied . My first project to get good with the Basics

name = str(input("What is your name?: "))
study_sessions_counter = int(input("How many study session have you had?: "))
minutes_per_session = float(input("How many minutes did you study on average in your study sessions?: "))
time_in_hours = round((minutes_per_session/60),2)

print(f"""OK so you had {study_sessions_counter} sessions and on average you studied {minutes_per_session} mins , in hours that would equate to {time_in_hours} hrs .""")