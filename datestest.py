from datetime import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta
def oneyear(start,end):
    strt_dt = datetime.strptime(start, '%Y-%m-%d')
    end_dt = datetime.strptime(end, '%Y-%m-%d')
    dates = [dt.strftime('%Y-%m-%d') for dt in rrule(
                MONTHLY, dtstart=strt_dt, until=end_dt
            )]
    new_start = str(
                strt_dt.year-1) + "-" + str(
                strt_dt.month) + "-" + str(
                strt_dt.day)
    new_end = str(
                end_dt.year-1) + "-" + str(
                end_dt.month) + "-" + str(
                end_dt.day)
    new_start1 = datetime.strptime(new_start, '%Y-%m-%d')
    new_end1 = datetime.strptime(new_end, '%Y-%m-%d')
    dates = [dt.strftime('%Y-%m-%d') for dt in rrule(
                MONTHLY, dtstart=new_start1, until=new_end1
            )] + dates
    return dates

def fiveyear(start,end):
    strt_dt = datetime.strptime(start, '%Y-%m-%d')
    end_dt = datetime.strptime(end, '%Y-%m-%d')
    new_start = str(
                strt_dt.year-4) + "-" + str(
                strt_dt.month) + "-" + str(
                strt_dt.day)
    new_start1 = datetime.strptime(new_start, '%Y-%m-%d')
    dates = [dt.strftime('%Y-%m-%d') for dt in rrule(
                MONTHLY, dtstart=new_start1, until=end_dt
            )]
    return dates

def splitdates(start,end):
    strt_dt = datetime.strptime(start, '%Y-%m-%d')
    end_dt = datetime.strptime(end, '%Y-%m-%d')
    dates = [dt.strftime('%Y-%m-%d') for dt in rrule(
                MONTHLY, dtstart=strt_dt, until=end_dt
            )]
    return dates

def twelvemonths(end):
    end_dt = datetime.strptime(end, '%Y-%m-%d')
    start_dt=end_dt + relativedelta(months=-11)
    dates = [dt.strftime('%Y-%m-%d') for dt in rrule(
                MONTHLY, dtstart=start_dt, until=end_dt
            )]
    return dates

if __name__=='__main__':
    start_date="2017-01-01"
    end_date="2017-06-01"
    print "one year back"
    print oneyear(start_date,end_date)
    print "five year back"
    print fiveyear(start_date, end_date)
    print "just splitting"
    print splitdates(start_date, end_date)
    print "12 months back"
    print twelvemonths(end_date)