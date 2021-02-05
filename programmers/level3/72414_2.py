def str_to_sec(string):
    hour = int(string[0:2]) * 3600
    minute = int(string[3:5]) * 60
    sec = int(string[6:8])
    return hour + minute + sec


def sec_to_str(second):
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)


def solution(play_time, adv_time, logs):
    play_time = str_to_sec(play_time)
    adv_time = str_to_sec(adv_time)

    # 누적시간 계산할 배열
    accumulate_time = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = log.split("-")
        start = str_to_sec(start)
        end = str_to_sec(end)
        accumulate_time[start] += 1
        accumulate_time[end] -= 1

    # i초에 시청하고 있는 시청자 수
    for i in range(1, play_time + 1):
        accumulate_time[i] += accumulate_time[i - 1]

    # i초의 시청자들의 누적 재생시간
    for i in range(1, play_time + 1):
        accumulate_time[i] += accumulate_time[i - 1]

    max_time = 0
    max_play = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if max_play < accumulate_time[i] - accumulate_time[i - adv_time]:
                max_play = accumulate_time[i] - accumulate_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if max_play < accumulate_time[i]:
                max_play = accumulate_time[i]
                max_time = i - adv_time + 1

    return sec_to_str(max_time)