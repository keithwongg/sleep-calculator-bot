# user enters sleep timing, wants to check wake up timing

def handle_overflow_minutes(minutes):
    overflow_hour = 0
    if minutes >= 60:
        overflow_hour = 1
        minutes = minutes - 60
        return overflow_hour, minutes
    return overflow_hour, minutes

def handle_overflow_hours(hours):
    if hours == 24:
        return 0
    if hours >= 24:
        return hours-24
    return hours

def convert_to_string_len_2(int_value):
    int_str = str(int_value)
    if len(int_str) < 2:
        int_str = '0' + int_str
        return int_str
    else:
        return int_str

def main_calculation(user_time, rem_sleep_timings):
    sleep_prep_time = 15
    sleep_timings_return = []

    user_hours = int(user_time[:2])
    user_minutes = int(user_time[2:])

    for time in rem_sleep_timings:
        rem_minutes = int((time - (time//1))*60)
        rem_hours = int(time//1)

        # execute add timings
        minutes = user_minutes + rem_minutes + sleep_prep_time
        overflow_hour, minutes = handle_overflow_minutes(minutes)
        hours = user_hours + rem_hours + overflow_hour
        hours = handle_overflow_hours(hours)

        str_to_append = convert_to_string_len_2(hours) + convert_to_string_len_2(minutes)
        sleep_timings_return.append(str_to_append)

    return sleep_timings_return

# main function execution
def sleep_calculator(user_time):
    user_time = user_time.strip()
    rem_sleep_timings = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5]
    sleep_timings_list = main_calculation(user_time, rem_sleep_timings)
    return sleep_timings_list

if __name__ == '__main__':
    user_time = input('Enter timing >>> ')
    print(sleep_calculator(user_time))