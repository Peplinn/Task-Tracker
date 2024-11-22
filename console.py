"""
Documentation
"""
from datetime import datetime
import json
import re

task_operations = ['add', 'update', 'list', 'delete',
                   'mark-in-progress', 'mark-done', 'exit']

list_options = ['done', 'todo', 'in-progress']


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


class TaskManager():
    """
    """
    def __init__(self):
        self.stored_tasks = self.load_storage()
        pass

    def load_storage(self):
        with open("storage.json", "r+") as storage:
            try:
                self.stored_tasks = json.load(storage)
            except:
                self.stored_tasks = []

    def save_storage(self, mode, task=None, new_status=None):
        with open("storage.json", "w") as storage:
            json.dump(self.stored_tasks, storage, indent=2)
            if mode == "add":
                print(f"{bcolors.OKGREEN}\
                      Task added successfully (ID: {task['id']})\
                        {bcolors.ENDC}")
            elif mode == "update":
                print(f"{bcolors.OKGREEN}\
                      Task updated successfully (ID: {task['id']})\
                        {bcolors.ENDC}")
            elif mode == "delete":
                print(f"{bcolors.OKGREEN}Task deleted successfully \
                      (ID: {task['id']}) -\
                        \"{task['description']}\"\
                            {bcolors.ENDC}")
            elif mode == "status":
                print(f"{bcolors.OKGREEN}\"\
                      {task['description']}\" set to \"{new_status}\"\
                        {bcolors.ENDC}")

    def init_console(self):
        await_raw_input = "(task_man)$ "
        raw_input = input(await_raw_input)
        self.parse_input(raw_input)

    def parse_input(self, raw_input):
        task_operations = {
            'add': self.add_task,
            'update': self.update_task,
            'list': self.list_task,
            'delete': self.delete_task,
            'mark-in-progress': self.change_status,
            'mark-done': self.change_status,
            'exit': self.exit
        }

        if len(raw_input) > 0:
            pattern = r'(?:"([^"]*)"|(\S+)|(\d+))'
            matches = re.findall(pattern, raw_input)

            user_input = [match[0] if match[0]
                          else match[1] for match in matches]
            if user_input[0] not in task_operations:
                print(f"{bcolors.FAIL}\
                      Unknown command \'{user_input[0]}\'\
                        {bcolors.ENDC}")
            else:
                task = TaskManager()
                return task_operations[user_input[0]](user_input)
        else:
            pass

    def console_loop(self):
        first_display = True
        self.load_storage()
        print(f"{bcolors.OKCYAN}{bcolors.BOLD}Welcome to Task Man CLI\
                {bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Type \'help\' to view all commands.\
            \nType \'help <command_name>\' to see usage.{bcolors.ENDC}")

        while True:
            try:
                self.init_console()
            except KeyboardInterrupt:
                print(f"{bcolors.BOLD}Quitting console...{bcolors.ENDC}")
                break

    def add_task(self, input):
        if len(input) < 2:  # This is not airtight
            print(f"{bcolors.FAIL}\
                  Syntax: add \"task_description\"\
                  {bcolors.ENDC}")
            return

        task = {
            "id": "",
            "description": "",
            "status": "",
            "createdAt": "",
            "updatedAt": "",
        }

        task["id"] = int(self.stored_tasks[-1]['id']) + 1
        task["description"] = input[1]
        task["status"] = "todo"
        task["createdAt"] = str(datetime.now().strftime("%x, %H:%M"))
        task["updatedAt"] = None

        self.stored_tasks.append(task)

        self.save_storage("add", task)

    def update_task(self, input):
        # print(input)
        if len(input) < 3:  # This is not airtight
            print(f"{bcolors.FAIL}\
                  Syntax: update \"task_id\" \"new_task_description\"\
                  {bcolors.ENDC}")
            return

        """
        WE ARE REPLACING THE PREVIOUS IMPLEMENTATION
        IN CASE THE STORAGE GETS TAMPERED WITH MANUALLY
        I.E. ALTERATIONS DO NOT HAPPEN VIA CONSOLE.
        """
        # GRAB THE TASK_ID TO BE UPDATED
        try:
            task_id = int(input[1])
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            return

        task_id_present = False

        # FIND THE INDEX OF THE TASK TO BE UPDATED
        for task in self.stored_tasks:
            if task_id == int(task['id']):
                print(f"task number: {task['id']}")
                task_id_present = True
                position = self.stored_tasks.index(task)
                print(f"The position is {position}")
        if not task_id_present:
            print(f"Task ID: {task_id} not found")
            return

        # UPDATE THE TASK BY ITS INDEX
        self.stored_tasks[position]["description"] = input[2]

        self.stored_tasks[position]["updatedAt"] \
            = str(datetime.now().strftime("%x, %H:%M"))
        self.save_storage("update", self.stored_tasks[position])

    def delete_task(self, input):
        if len(input) < 2:  # This is not airtight
            print(f"{bcolors.FAIL}Syntax: delete \"task_id\"{bcolors.ENDC}")
            return

        # GRAB THE TASK_ID TO BE DELETED
        try:
            task_id = int(input[1])
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            return

        task_id_present = False

        # FIND THE INDEX OF THE TASK TO BE DELETED
        for task in self.stored_tasks:
            if task_id == int(task['id']):
                print(f"task number: {task['id']}")
                task_id_present = True
                position = self.stored_tasks.index(task)
                print(f"The position is {position}")
        if not task_id_present:
            print(f"Task ID: {task_id} not found")
            return

        # DELETE THE TASK BY ITS INDEX
        try:
            deleted_task = self.stored_tasks.pop(position)
        except:
            print("Delete Unsuccessful")
            return

        # UDPATED THE INDEXES OF ALL TASKS
        i = 0
        while i < len(self.stored_tasks):
            self.stored_tasks[i]['id'] = i + 1
            i += 1

        self.save_storage("delete", deleted_task)

    def change_status(self, input):
        if len(input) < 2:  # This is not airtight
            print(f"{bcolors.FAIL}Syntax: mark-in-progress or\
                   mark-done \"task_id\"{bcolors.ENDC}")
            return

        # GRAB THE TASK_ID OF TASK TO STATUS CHANGE
        try:
            task_id = int(input[1])
        except:
            print(f"{bcolors.FAIL}Invalid Task ID{bcolors.ENDC}")
            return

        task_id_present = False

        # FIND THE INDEX OF THE TASK TO STATUS CHANGE
        for task in self.stored_tasks:
            if task_id == int(task['id']):
                print(f"task number: {task['id']}")
                task_id_present = True
                position = self.stored_tasks.index(task)
                print(f"The position is {position}")
        if not task_id_present:
            print(f"Task ID: {task_id} not found")
            return

        # UPDATE THE STATUS BY TASK INDEX
        if input[0] == "mark-in-progress":
            self.stored_tasks[position]["status"] = "in-progress"
            new_status = "in-progress"
        elif input[0] == "mark-done":
            self.stored_tasks[position]["status"] = "done"
            new_status = "done"
        elif input[0] == "mark-todo":
            self.stored_tasks[position]["status"] = "todo"
            new_status = "todo"
        self.stored_tasks[position]["updatedAt"] \
            = str(datetime.now().strftime("%x, %H:%M"))

        self.save_storage("status", self.stored_tasks[position], new_status)

    def list_task(self, input):
        tasks_to_list = []

        if len(input) == 1:
            print(json.dumps(self.stored_tasks, indent=2))
            print(f"{bcolors.BOLD}\
                  {len(self.stored_tasks)} tasks listed\
                    {bcolors.ENDC}")
            return
        else:
            if input[1] not in list_options:
                # GRAB THE TASK_ID TO BE LISTED
                try:
                    task_id = int(input[1])
                except:
                    print(f"{bcolors.FAIL}\
                          Invalid Task ID\
                          {bcolors.ENDC}")
                    return

                task_id_present = False

                # FIND THE INDEX OF THE TASK TO BE DELETED
                for task in self.stored_tasks:
                    if task_id == int(task['id']):
                        print(f"task number: {task['id']}")
                        task_id_present = True
                        position = self.stored_tasks.index(task)
                        print(f"The position is {position}")
                if not task_id_present:
                    print(f"Task ID: {task_id} not found")
                    return

                # LIST THE TASK BY ITS INDEX
                tasks_to_list.append(self.stored_tasks[position])
                print(json.dumps(tasks_to_list, indent=2))
                print(f"{bcolors.BOLD}\
                        Task No.: {task_id} listed\
                        {bcolors.ENDC}")
            else:
                for task in self.stored_tasks:
                    if task["status"] == input[1]:
                        tasks_to_list.append(task)
                print(json.dumps(tasks_to_list, indent=2))
                print(f"{bcolors.BOLD}\
                      {len(tasks_to_list)} \"{input[1]}\" tasks listed\
                        {bcolors.ENDC}")
                return

    def exit(self, input=None):
        print(f"{bcolors.BOLD}Quitting console...{bcolors.ENDC}")
        raise SystemExit


if __name__ == "__main__":
    TaskManager().console_loop()
