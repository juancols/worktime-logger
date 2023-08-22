import os
import csv
import datetime

LUNCH_BREAK_IN_HOURS = 0.75 # 45 min lunch break

def log_work_hours():
    """
    Logs the working hours per day in a local text file named "MM-DD-worktime.csv" where MM
    is the month and DD is the date of the Monday of that week.
    The user should run the script once in the morning when they arrive at work
    and once before leaving in the afternoon. The script calculates the time
    passed between these two runs and subtracts 1 hour for lunch time.
    """
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    file_name = "logs\{:02d}-{:02d}-worktime.csv".format(monday.month, monday.day)

    # Get current date and time
    current_time = datetime.datetime.now().strftime('%H:%M')
    day_of_week = today.strftime('%A')
    date_str = today.strftime('%Y-%m-%d')

    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            header = ["{}[{}]".format(weekday, (today + datetime.timedelta(days=i - today.weekday())).strftime('%Y-%m-%d')) for i, weekday in enumerate(weekdays)]
            writer.writerow(header)

    row_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}

    with open(file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        lines = list(reader)

    if len(lines) < 4:
        for _ in range(4 - len(lines)):
            lines.append([""] * 5)

    if lines[1][row_dict[day_of_week]] == "":
        # Start time
        lines[1][row_dict[day_of_week]] = "Start:{}".format(current_time)
    elif lines[2][row_dict[day_of_week]] == "":
        # End time
        lines[2][row_dict[day_of_week]] = "End:{}".format(current_time)

    # Calculate hours worked if both Start and End times are defined
    if lines[1][row_dict[day_of_week]] != "" and lines[2][row_dict[day_of_week]] != "" and lines[3][row_dict[day_of_week]] == "":
        start_time = datetime.datetime.strptime(lines[1][row_dict[day_of_week]][6:], '%H:%M')
        end_time = datetime.datetime.strptime(lines[2][row_dict[day_of_week]][4:], '%H:%M')

        hours_worked = (end_time - start_time).seconds / 3600.0 - LUNCH_BREAK_IN_HOURS  # Subtract 45 min for lunch
        lines[3][row_dict[day_of_week]] = "{:.2f} h".format(hours_worked)

    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lines)

if __name__ == "__main__":
    log_work_hours()
