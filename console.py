"""
Doumentation
"""
from datetime import datetime
import json, re

task_operations = ['add', 'update', 'list', 'delete',
                   'mark-in-progress', 'mark-done', 'exit']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

first_display = True # Using this to display useful first-launch info
while True:
    with open("storage.json", "r+") as storage:
        try:
            stored_tasks = json.load(storage)
        except:
            stored_tasks = []

    print(stored_tasks[-1])

    if first_display == True:
        print(f"{bcolors.OKCYAN}{bcolors.BOLD}Welcome to Task Man CLI{bcolors.ENDC}")
        first_display = False

    await_raw_input = "(task_man)$ "
    raw_input = input(await_raw_input)

    if len(raw_input) > 0:
        pattern = r'(?:"([^"]*)"|(\S+)|(\d+))'
        matches = re.findall(pattern, raw_input)

        user_input = [match[0] if match[0] else match[1] for match in matches]
    else:
        continue

    if user_input[0] not in task_operations:
        print(f"{bcolors.FAIL}Unknown command \'{user_input[0]}\'{bcolors.ENDC}")
        continue

    if user_input[0] == "exit":
        print(f"{bcolors.BOLD}Quitting console...{bcolors.ENDC}")
        break

    if user_input[0] == "list":
        print(json.dumps(stored_tasks, indent=2))
        continue

    if user_input[0] == "add" :
        if len(user_input) < 2 : # This is not airtight
            print(f"{bcolors.FAIL}Syntax: add \"task_description\"{bcolors.ENDC}")
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
        task["status"] = "todo"
        task["createdAt"] = str(datetime.now().strftime("%x, %H:%M"))

        stored_tasks.append(task)

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"{bcolors.OKGREEN}Task added successfully (ID: {task['id']}){bcolors.ENDC}")

    if user_input[0] == "update" :
        print(user_input)
        if len(user_input) < 3 : # This is not airtight
            print(f"{bcolors.FAIL}Syntax: update \"task_id\" \"new_task_description\"{bcolors.ENDC}")
            continue

        try:
            task_id = int(user_input[1]) - 1
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            continue

        if task_id not in range(len(stored_tasks)):
            print(f"{bcolors.FAIL}Task ID out of range{bcolors.ENDC}")
            continue

        stored_tasks[task_id]["description"] = user_input[2]

        stored_tasks[task_id]["updatedAt"] = str(datetime.now().strftime("%x, %H:%M"))

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"{bcolors.OKGREEN}Task updated successfully (ID: {task_id + 1}){bcolors.ENDC}")

    if user_input[0] == "delete" :
        print(user_input)

        # if len(user_input) < 2 or not isinstance(int(user_input[1]), int): # This is not airtight
        if len(user_input) < 2: # This is not airtight
            print(f"{bcolors.FAIL}Syntax: delete \"task_id\"{bcolors.ENDC}")
            continue

        try:
            task_id = int(user_input[1]) - 1
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            continue

        if task_id not in range(len(stored_tasks)):
            print(f"{bcolors.FAIL}Task ID out of range{bcolors.ENDC}")
            continue

        deleted_task = stored_tasks.pop(task_id)["description"]

        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"{bcolors.OKGREEN}Task deleted successfully (ID: {task_id + 1}) - \"{deleted_task}\"{bcolors.ENDC}")


    if user_input[0] == "mark-in-progress":
        
        print(user_input)
        if len(user_input) < 2: # This is not airtight
            print(f"{bcolors.FAIL}Syntax: mark-in-progress \"task_id\"{bcolors.ENDC}")
            continue

        try:
            task_id = int(user_input[1]) - 1
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            continue

        if task_id not in range(len(stored_tasks)):
            print(f"{bcolors.FAIL}Task ID out of range{bcolors.ENDC}")
            continue

        updated_task = stored_tasks[task_id]["description"]
        stored_tasks[task_id]["status"] = "in-progress"
        stored_tasks[task_id]["updatedAt"] = str(datetime.now().strftime("%x, %H:%M"))


        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"{bcolors.OKGREEN}\"{updated_task}\" set to \"in-progress\"{bcolors.ENDC}")

    if user_input[0] == "mark-done":
        
        print(user_input)
        if len(user_input) < 2: # This is not airtight
            print(f"{bcolors.FAIL}Syntax: mark-done \"task_id\"{bcolors.ENDC}")
            continue

        try:
            task_id = int(user_input[1]) - 1
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            continue

        if task_id not in range(len(stored_tasks)):
            print(f"{bcolors.FAIL}Task ID out of range{bcolors.ENDC}")
            continue

        updated_task = stored_tasks[task_id]["description"]
        stored_tasks[task_id]["status"] = "done"
        stored_tasks[task_id]["updatedAt"] = str(datetime.now().strftime("%x, %H:%M"))


        with open("storage.json", "w") as storage:
            json.dump(stored_tasks, storage, indent=2)
            print(f"{bcolors.OKGREEN}\"{updated_task}\" set to \"\"{bcolors.ENDC}")

    



