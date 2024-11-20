"""
Doumentation
"""
from datetime import datetime
import json, re

task_operations = ['add', 'update', 'list', 'delete',
                   'mark-in-progress', 'mark-done']



while True:
    with open("storage.json", "r+") as storage:
        try:
            stored_tasks = json.load(storage)
        except:
            stored_tasks = []

    print(stored_tasks[-1])

    first_display = True # Using this to display useful first-launch info
    await_raw_input = "(task_man)$ "
    raw_input = input(await_raw_input)

    if len(raw_input) > 0:
        pattern = r'(?:"([^"]*)"|(\S+)|(\d+))'
        matches = re.findall(pattern, raw_input)

        user_input = [match[0] if match[0] else match[1] for match in matches]
    else:
        continue

    first_display = False

    if user_input[0] not in task_operations:
        print(f"Unknown command \'{user_input[0]}\'")

    if user_input[0] == "exit":
        print("Quitting console...")
        break

    if user_input[0] == "add" :
        if len(user_input) < 2 : # This is not airtight
            print("Syntax: add \"task_description\"")
            continue
        # elif 

        task = {
            "id": "",
            "description": "",
            "status": "",
            "createdAt": "",
            "updatedAt": "",
        }

        task["id"] = str(len(stored_tasks) + 1)
        task["description"] = user_input[1]
        task["createdAt"] = str(datetime.now().strftime("%x, %H:%M"))

        stored_tasks.append(task)

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"Task added successfully (ID: {task['id']})")

    if user_input[0] == "update" :
        print(user_input)
        if len(user_input) < 3 : # This is not airtight
            print("Syntax: update \"task_id\" \"new_task_description\"")
            continue

        task_id = int(user_input[1]) - 1

        stored_tasks[task_id]["description"] = user_input[2]
        # task = {
        #     "id": "",
        #     "description": "",
        #     "status": "",
        #     "createdAt": "",
        #     "updatedAt": "",
        # }

        # task["id"] = str(len(stored_tasks) + 1)
        # task["description"] = user_input[1]
        stored_tasks[task_id]["updatedAt"] = str(datetime.now().strftime("%x, %H:%M"))

        # stored_tasks.append(task)

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"Task updated successfully (ID: {task_id})")

    if user_input[0] == "delete" :
        print(user_input)

        try:
            task_id = int(user_input[1]) - 1
        except:
            print("Invalid Task ID")
            continue

        if len(user_input) < 2 or not isinstance(int(user_input[1]), int): # This is not airtight
            print("Syntax: delete \"task_id\"")
            continue

        # task_id = int(user_input[1]) - 1

        try:
            deleted_task = stored_tasks.pop(task_id)["description"]
        except:
            print("Delete Unsuccessful")
            continue

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"Task deleted successfully (ID: {task_id}) \"{deleted_task}\"")

    



