# <Minutes> <Hours> <Day of Month> <Month> <Day of Week> <Command>

alias = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12',
    'Sun': '0', 'Mon': '1', 'Tue': '2', 'Wed': '3',
    'Thu': '4', 'Fri': '5', 'Sat': '6',
}

month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def cross_all(l1, l2):
    cross_res = []
    for i in l1:
        for j in l2:
            cross_res.append('%s%s' % (i, j))
    return cross_res

def cross(l1, l2):
    cross_res = []
    for i in l1:
        for j in l2:
            cross_res.append('%02d%02d' % (int(i), int(j)))
    return cross_res

def cross_4(l1, l2):
    cross_res = []
    for i in l1:
        for j in l2:
            cross_res.append('%04d%04d' % (int(i), int(j)))
    return cross_res


def get_week(y, m, d):
    return (d + 1 + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7


def check_date_legal(dates_to_check, legal_week):
    legal_dates = []
    int_legal_week = list(map(int, legal_week))
    for _date in dates_to_check:
        year = _date[:4]
        month = _date[4:6]
        day = _date[6:]

        if int(day) > month_days[int(month) - 1]:
            continue
        
        d = int(day)
        m = int(month)
        y = int(year)
        
        if get_week(y, m, d) not in int_legal_week:
            continue
            
        if not (y % 4 == 0 and y % 400 != 0) and m == 2 and d == 29:
            continue
            
        legal_dates.append(_date)
    
    return legal_dates


class Analyser:
    @classmethod
    def analyse_crontab(cls, crontab, start_year, end_year):
        data = crontab.split()
        minutes, hours, day_of_month, month, day_of_week, command = data

        minutes = cls.no_nickname(minutes, 0, 60)
        hours = cls.no_nickname(hours, 0, 24)
        day_of_month = cls.no_nickname(day_of_month, 1, 32)
        month = cls.no_nickname(month, 1, 13)
        day_of_week = cls.no_nickname(day_of_week, 0, 7)

        years = [
            '%04d' % y
            for y in range(start_year, end_year + 1)
        ]

        time_res = cross(hours, minutes)
        date_res = check_date_legal(cross_4(years, cross(month, day_of_month)), day_of_week)

        return cross_all(date_res, time_res), command

    @classmethod
    def no_nickname(cls, indata, start=0, end=0):
        tmp = indata.split(',')
        res = []
        for i in tmp:
            if '*' == i:
                res = [
                    '%02d' % x
                    for x in range(start, end)
                ]
                return res
            if '-' not in i:
                if i in alias.keys():
                    res.append(alias[i])
                else:
                    res.append(i)
                continue
            
            _t = i.split('-')
            if _t[0] in alias.keys():
                _t[0] = alias[_t[0]]
            if _t[1] in alias.keys():
                _t[1] = alias[_t[1]]

            for j in range(int(_t[0]), int(_t[1]) + 1):
                res.append('%02d' % j)
        return res


def main():
    n, start, end = input().split()
    n = int(n)

    start_year = int(start[:4])
    end_year = int(end[:4])

    res = []
    names = []
    for _ in range(n):
        cron = input()
        _res, name = Analyser.analyse_crontab(cron, start_year, end_year)
        names.append(name)

        for i in _res:
            if int(i) < int(start) or int(i) >= int(end):
                continue
            res.append((i, name))

    sorted_list = sorted(
        res, 
        key=lambda x: int(x[0]) + float(names.index(x[1]) / 21)
    )

    for i in sorted_list:
        print('%s %s' % (i[0], i[1]))

if __name__ == '__main__':
    main()

