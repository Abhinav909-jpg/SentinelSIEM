import random
from datetime import datetime, timezone, timedelta


def iso8601_formatting(timestamp):
    iso_string = timestamp.isoformat(timespec='seconds').replace('+00:00', 'Z')
    return iso_string


# This function generates a single timestamp
def generate_random_timestamp(start_time, end_time):
    time_difference = end_time - start_time
    total_seconds = int(time_difference.total_seconds())
    random_seconds = random.randint(0, total_seconds)
    new_time = start_time + timedelta(seconds=random_seconds)
    return new_time


# This function will create a loop and make a list of desired number of timestamps
def random_timestamps(num_of_timestamps):
    start = datetime(2026, 7, 1, 10, 0, 0, tzinfo=timezone.utc)
    end = datetime(2026, 7, 1, 12, 0, 0, tzinfo=timezone.utc)

    for timestamp in range(0, num_of_timestamps):
        print(iso8601_formatting(generate_random_timestamp(start, end)))


if __name__ == "__main__":
    print(random_timestamps(10))