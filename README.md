# **Task Tracker CLI**

A Python-based **Command-Line Interface (CLI)** application for managing tasks efficiently. This tool allows users to create, update, list, delete, and manage the status of their tasks with ease.


This project is inspired by [Roadmap.sh](https://roadmap.sh/projects/task-tracker).

## **Features**

- **Add Tasks**: Quickly add new tasks with a description.
- **Update Tasks**: Modify task descriptions by ID.
- **Delete Tasks**: Remove tasks permanently using their ID.
- **List Tasks**: Display tasks filtered by status or by ID.
- **Change Task Status**: Update task statuses to `todo`, `in-progress`, or `done`.
- **Persistent Storage**: All tasks are saved in a `storage.json` file.
- **User-Friendly Output**: Outputs are styled with color-coded messages for clarity.
- **Command Help**: Displays available commands and their usage.


## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher installed on your system.

### **Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/Peplinn/Task-Tracker.git
   cd task-manager-cli
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```


## **Usage**

To start the Task Manager CLI, simply run:
```bash
python console.py
```

### **Commands**
| Command                | Syntax                                       | Description                                   |
|------------------------|----------------------------------------------|-----------------------------------------------|
| **Add Task**           | `add "task_description"`                     | Adds a new task.                              |
| **Update Task**        | `update "task_id" "new_task_description"`    | Updates the description of a task.           |
| **Delete Task**        | `delete "task_id"`                           | Deletes a task by its ID.                     |
| **List Tasks**         | `list [done/todo/in-progress/task_id]`       | Lists tasks by status or by ID.               |
| **Mark In-Progress**   | `mark-in-progress "task_id"`                 | Marks a task as `in-progress`.                |
| **Mark Done**          | `mark-done "task_id"`                        | Marks a task as `done`.                       |
| **Mark Todo**          | `mark-todo "task_id"`                        | Marks a task as `todo`.                       |
| **Help**               | `help`                                       | Displays a list of available commands.        |
| **Exit**               | `exit`                                       | Exits the CLI application.                    |


## **Examples**

### **Adding a Task**
```bash
(task_man)$ add "Complete the project documentation"
Task added successfully (ID: 1)
```

### **Updating a Task**
```bash
(task_man)$ update 1 "Finalize README documentation"
Task updated successfully (ID: 1)
```

### **Listing All Tasks**
```bash
(task_man)$ list
[
  {
    "id": 1,
    "description": "Finalize README documentation",
    "status": "todo",
    "createdAt": "11/21/24, 12:15",
    "updatedAt": "11/21/24, 12:30"
  }
]
1 tasks listed
```


## **Customization**

- **Color Coding**: You can customize output colors by modifying the `bcolors` class.
- **Persistent Storage**: Task data is stored in `storage.json`. Ensure this file is not accidentally deleted.


## **Error Handling**

- Invalid commands or inputs are gracefully handled with descriptive error messages.
- Missing or corrupted `storage.json` files are auto-handled by initializing a new file.


## **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Feature description"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.


## **License**

This project is licensed under the MIT License.


## **Author**

Developed by [Chidiebube Oluoma](https://github.com/Peplinn). Feel free to reach out for feedback or suggestions!