
def sun_angle(time):
    '''
    Split the time string into hours and minutes.
    One hour equals 15°, one minute corresponds to 0.25°.
    Calculate the angles and sum them.
    '''
    angle = (int(time.split(":")[0])-6) * 15 + int(time.split(":")[1]) * 0.25
    if angle < 0 or angle > 180:        # we delete the negative angles        
        return "I don't see the sun!"            
    return angle
