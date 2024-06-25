# decorator - real example

import time

def note_time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken: " + str(end_time - start_time))
    return wrapper()


@note_time_decorator
def logs_function():
    time.sleep(5)
    print("Print the logs of time taken")


@note_time_decorator
def reporting_function():
    time.sleep(2)
    print("Print the time taken for reporting")

    # real use - we can reuse
