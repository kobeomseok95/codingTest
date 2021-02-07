def str_to_int(string):
    return int(string[0:2]) * 3600 + int(string[3:5]) * 60 + int(string[6:8])


def int_to_str(second):
    hour = second // 3600
    second -= hour * 3600
    minute = second // 60
    second -= minute * 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)


def solution(play_time, adv_time, logs):
    n = len(logs)
    play_time_sec = str_to_int(play_time)
    adv_time_sec = str_to_int(adv_time)

    total_time = [0] * (play_time_sec + 1)
    for i in range(n):
        start, end = logs[i].split("-")
        total_time[str_to_int(start)] += 1
        total_time[str_to_int(end)] -= 1

    for i in range(1, play_time_sec + 1):
        total_time[i] += total_time[i - 1]

    max_time, max_count, sums = 0, 0, 0
    for i in range(0, play_time_sec + 1):
        if i < adv_time_sec:
            sums += total_time[i]
            max_count = sums
        else:
            sums += total_time[i]
            sums -= total_time[i - adv_time_sec]
            if sums > max_count:
                max_count = sums
                max_time = i - adv_time_sec + 1

    return int_to_str(max_time)