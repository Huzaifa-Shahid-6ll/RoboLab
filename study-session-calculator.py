# Building a simple study session calculator that claculates how much you have studied . My first project to get good with the Basics

name = str(input("What is your name?: "))
study_sessions_counter = int(input("How many study session have you had?: "))
time_per_session = []

for i in range(study_sessions_counter):
    per_session_time = int(input(f"For study session {i+1} , how much did you study in minutes?: "))
    time_per_session.append(per_session_time)
    

print("Ok got it!")

print(time_per_session)
print(f"""OK so you had {study_sessions_counter} sessions .""")