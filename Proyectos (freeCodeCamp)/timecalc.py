def add_time(start, duration, starting_day=False):

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    am_or_pm = start[start.find('M') - 1:]
    starter_time = start.split()[0].split(':')
    duration_time = duration.split(':')
    total_minutes = int(starter_time[1]) + int(duration_time[1])
    final_minutes = total_minutes
    total_hours = int(starter_time[0]) + int(duration_time[0])

    if total_minutes >= 60:
        final_minutes = total_minutes%60
        total_hours += total_minutes//60

    final_minutes = str(final_minutes)
    if len(final_minutes) < 2:
        final_minutes = final_minutes.zfill(2)

    incremented_days = 0
    if total_hours > 12 and am_or_pm == 'PM':
        incremented_days = (total_hours + 12)//24
        final_hour = ((total_hours + 12)%24)
        if final_hour > 12:
            final_hour -= 12
            am_or_pm = 'PM'
        elif final_hour == 0:
            final_hour = 12
            am_or_pm = 'AM'
        else:
            am_or_pm = 'AM'

    elif total_hours > 24 and am_or_pm == 'AM':
        incremented_days = total_hours//24
        final_hour = total_hours%24
        if final_hour > 12:
            final_hour -= 12
            am_or_pm = 'PM'
        elif final_hour == 12:
            am_or_pm = 'PM'
        else:
            am_or_pm = 'AM'

    elif total_hours > 12 and am_or_pm == 'AM':
        final_hour = total_hours - 12
        am_or_pm = 'PM'
    ## Si las horas totales son menores a 12, eso significa que la adicion no fue suficiente ni para cambiarlo de dia ni de horario (PM/AM).
    else:
        final_hour = total_hours
        if final_hour > 12:
            am_or_pm = 'AM'
        elif final_hour == 12:
            am_or_pm = 'PM'


    if incremented_days == 1:
        time_passed = '(next day)'
    elif incremented_days > 1:
        time_passed = '(' + str(incremented_days) + ' ' + 'days later)'


    new_time = str(final_hour) + ':' + str(final_minutes) + ' ' + str(am_or_pm)
    if starting_day != False:
        for day in week_days:
            if starting_day.upper() == day.upper():
                starting_day = day
        day_position = week_days.index(starting_day)
        final_day = incremented_days + (day_position + 1)

        if incremented_days >= 1:
            if final_day > 7:
                new_day = final_day%7
                final_day = week_days[new_day - 1]
            else:
                final_day = week_days[(day_position) + incremented_days]
            new_time += ', ' + final_day + ' ' + time_passed
        else:
            new_time += ', ' + starting_day
    elif incremented_days >= 1:
        new_time += ' ' + time_passed

    print(new_time)
    return new_time

add_time("11:59 PM", "24:05")
