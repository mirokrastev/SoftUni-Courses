from project.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'

        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name):
        tasks_var = [task.name for task in self.tasks]

        if task_name not in tasks_var:
            return f'Could not find task with the name {task_name}'

        inx = tasks_var.index(task_name)
        self.tasks[inx].completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        cleared_sections = len([task for task in self.tasks if task.completed])
        self.tasks = [task for task in self.tasks if not task.completed]

        return f'Cleared {cleared_sections} tasks.'

    def view_section(self):
        result = f'Section {self.name}:\n'

        for task in self.tasks:
            result += f'{task.details()}\n'

        return result