command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print('Car Started...')
    elif command =="stop":
        if not started:
            print('car is already stopped!')
        else:
            started=False
            print("car Stopped.")
    elif command=="help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit 
        """)
    elif command=="quit":
        print('see you again')
        break
    else:
        print("Sorry i`dont understand")