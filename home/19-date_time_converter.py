d_months = {'01':'January'
,'02':'February'
,'03':'March'
,'04':'April'
,'05':'May'
,'06':'June'
,'07':'July'
,'08':'August'
,'09':'September'
,'10':'October'
,'11':'November'
,'12':'December'}

def date_time(time: str) -> str:
    hour = 'hour' if int(time[11:13]) == 1 else 'hours'
    minute = 'minute' if int(time[14:]) == 1 else 'minutes'
    return (str(int(time[:2]))+' '+d_months[time[3:5]]+' '+time[6:10]+' '+'year'
    +' '+str(int(time[11:13]))+' '+hour+' '+str(int(time[14:]))+' '+minute)