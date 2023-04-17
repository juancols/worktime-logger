# Work Time Logger

A simple Python script that logs your working hours per day in a local CSV file.

## Usage

1. Run the script `worktime_logger.py` once in the morning when you arrive at work.
2. Run the script again before leaving work in the afternoon.

The script will create a "work-time.csv" file in the same directory, logging the start and end times, as well as the total hours worked per day, excluding 1 hour for lunch.

## Example Output

The "work-time.csv" file will have the following format:

```
Monday[2023-04-17],Tuesday[2023-04-18],Wednesday[2023-04-19],Thursday[2023-04-20],Friday[2023-04-21]
Start:7:23,,,,
End:18:56,,,,
10.55 h,,,,
```