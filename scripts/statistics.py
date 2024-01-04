import json
from tabulate import tabulate
from  scripts.tasks import load_closed_tasks, load_open_tasks

class Task:
    def __init__(self, name, time_spent=0, status="open"):
        self.name = name
        self.time_spent = time_spent
        self.status = status

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    total_open_tasks = sum(1 for task in tasks if task.status == 'open')
    total_closed_tasks = sum(1 for task in tasks if task.status == 'closed')

    total_time_spent = sum(task.time_spent for task in tasks)
    total_time_spent_closed = sum(task.time_spent for task in tasks if task.status == 'closed')
    total_time_spent_open = sum(task.time_spent for task in tasks if task.status == 'open')

    mean_time_spent_per_task = total_time_spent / total_tasks if total_tasks > 0 else 0
    percentage_closed_tasks = (total_closed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    statistics = {
        'Total Tasks': total_tasks,
        'Total Open Tasks': total_open_tasks,
        'Total Closed Tasks': total_closed_tasks,
        'Percentage Closed Tasks': percentage_closed_tasks,
        'Mean Time Spent Per Task': mean_time_spent_per_task,
        'Total Time Spent': total_time_spent,
        'Total Time Spent on Closed Tasks': total_time_spent_closed,
        'Total Time Spent on Open Tasks': total_time_spent_open
    }

    return statistics

def display_statistics(statistics):
    headers = ["Statistic", "Value"]
    rows = []

    for key, value in statistics.items():
        rows.append([key, value])

    table = tabulate(rows, headers, tablefmt="fancy_grid", numalign="right")
    print(table)

def main():
    # Example usage
    closedtasks=load_closed_tasks()
    opentasks= load_open_tasks()
    tasks = closedtasks + opentasks
    print(tasks)

    statistics_data = calculate_statistics(tasks)
    display_statistics(statistics_data)

if __name__ == "__main__":
    main()
