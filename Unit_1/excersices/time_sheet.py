# Make a dictionary where the key is a worker’s name, and the value is a
# list where the first element is the clock in time, second element is the clock out time,
# and the third element is the total hours worked that day. Each worker’s list starts at [0, 0, 0].
# Create functions for clock_in and clock_out.
#   clock_in takes the dictionary of workers, the name of the worker,
#   and the clock in time as parameters. When the worker clocks in, enter and
#   save their clock in time as the first element in the associated list value.
#   clock_out takes the same parameters, but with a clock out time instead of clock in time.
#   When the worker clocks out, enter and save their clock out time and calculate the hours
#   worked for that day and store it as the third element in the list.


def clock_out(workers, worker, time):

    if worker in workers:
        workers[worker][1] = int(time)
        time_total = workers[worker][1] - workers[worker][0]
        workers[worker][2] = int(time_total)


def clock_in(workers, worker, time):

    for worker in workers:
        workers[worker][0] = int(time)


def main():
    workers = {"George Spelvin": [0, 0, 0], "Jane Doe": [0, 0, 0], "John Smith": [0, 0, 0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", 8)
    clock_out(workers, "George Spelvin", 17)
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]


if __name__ == "__main__":
    main()
