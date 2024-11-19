"""
Doumentation
"""
from datetime import datetime
import json

while True:
    with open("storage.json", "r+") as storage:
        try:
            stored_tasks = json.load(storage)
        except:
            stored_tasks = []

    first_display = True
    await_user_input = "(task_man)$ "

    user_input = input(await_user_input).split(" ")
    first_display = False

    if user_input[0] == "exit":
        if stored_tasks:
            print(json.dumps(stored_tasks, indent=2))
        print("Quitting console...")
        break

    if user_input[0] == "add" :
        if len(user_input) < 2 :
            print("Syntax: add \"task_description\"")
            continue

        task = {
            "id": "",
            "description": "",
            "status": "",
            "createdAt": "",
            "updatedAt": "",
        }

        task["id"] = str(len(stored_tasks) + 1)
        task["description"] = user_input[1]
        task["createdAt"] = str(datetime.now())

        stored_tasks.append(task)

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)

    



