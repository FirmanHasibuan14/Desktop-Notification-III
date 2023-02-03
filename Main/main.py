from plyer import notification
import time

def notif(app_name,title,message):
    notification.notify(app_name=app_name,
                        title = title,
                        message = message,
                        app_icon = "C:\\Users\\ACER\\Downloads\\profile.ico",
                        timeout = 5,
                        toast = False,)
    time.sleep(5)
app_name = input("Input name of the app launching this notification: \n")
title = input("Input title of the notification: \n")
message = input("Input message: \n")
notif(app_name,title,message)
