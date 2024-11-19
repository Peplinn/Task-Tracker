"""
Doumentation
"""
from datetime import datetime
import json, re



while True:
    with open("storage.json", "r+") as storage:
        try:
            stored_tasks = json.load(storage)
        except:
            stored_tasks = []

    first_display = True
    await_raw_input = "(task_man)$ "
    raw_input = input(await_raw_input)

    pattern = r'(?:"([^"]*)"|(\S+))'
    matches = re.findall(pattern, raw_input)

    user_input = [match[0] if match[0] else match[1] for match in matches]

    # user_input = re.split("\s",input(await_user_input))
    # print(f"user input: {user_input}")
    first_display = False

    if user_input[0] == "exit":
        # if stored_tasks:
        #     print(json.dumps(stored_tasks, indent=2))
        print("Quitting console...")
        break

    if user_input[0] == "add" :
        if len(user_input) < 2 : # This is not airtight
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
            print(f"Task added successfully (ID: {task['id']})")

    



