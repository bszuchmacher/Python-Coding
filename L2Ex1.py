import datetime
try:
    try:
        f = open("\\log_file.txt", "a")
    except OSError as e:
        print("something went wrong: " + e.strerror)
    x = datetime.datetime.now()
    f.write(x.strftime("%d/%m/%Y, %H:%M:%S") + " Here comes the Hotstepper....MURDER...lol.")
except Exception as e:
    print(e)