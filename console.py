"""
Doumentation
"""
import json, datetime

while (True):
    storage = open("storage.json", "a+")
    first_display = True
    await_user_input = "(task_man)$ "

    user_input = input(await_user_input)
    first_display = False

    if user_input == "exit":
        print("Quitting console...")
        break



