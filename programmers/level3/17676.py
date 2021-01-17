import datetime


def get_times(lines):
    result = []
    for line in lines:
        data = line.split()
        date = str(data[0]) + " " + str(data[1])

        if '.' in data[2]:
            delay = data[2].split(".")
            delay[1] = delay[1][:-1]
        else:
            delay = list(data[2][:-1])
            delay.append("0")

        end = datetime.datetime.fromisoformat(date)
        start = end - datetime.timedelta(seconds=int(delay[0]), milliseconds=int(delay[1]) - 1)

        result.append([start, end])
    return result


def compare(point, target):
    start = point
    end = point + datetime.timedelta(milliseconds=999)

    if start <= target[0] <= end:
        return True
    if start <= target[1] <= end:
        return True
    if start <= target[0] <= end and start <= target[1] <= end:
        return True

    return False


def solution(lines):
    answer = []
    times = get_times(lines)
    for time in times:
        for t in time:
            count = 0
            for target in times:
                if compare(t, target):
                    count += 1

            answer.append(count)

    return max(answer)