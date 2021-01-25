import datetime


def solution(n, t, m, timetable):
    time = datetime.datetime.strptime("09:00", '%H:%M')
    bus_time = []
    bus_passenger = {}
    for i in range(n):
        bus_time.append(time)
        bus_passenger[time] = []
        time += datetime.timedelta(minutes=t)

    # 24:00이 주어지므로 치환하기
    for i in range(len(timetable)):
        if timetable[i] == "24:00":
            timetable[i] = "23:59"

    timetable.sort()
    for time in timetable:
        passenger = datetime.datetime.strptime(time, '%H:%M')
        for i in range(len(bus_time)):
            if passenger <= bus_time[i] and len(bus_passenger[bus_time[i]]) < m:
                bus_passenger[bus_time[i]].append(passenger)
                break

    if len(bus_passenger[bus_time[n - 1]]) < m:
        return str(bus_time[n - 1]).split()[1][:5]
    elif len(bus_passenger[bus_time[n - 1]]) == m:
        times = bus_passenger[bus_time[n - 1]]
        return str(times[-1] - datetime.timedelta(minutes=1)).split()[1][:5]