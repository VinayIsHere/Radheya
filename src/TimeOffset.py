from datetime import datetime

class TimeOffset:
    def __init__(self, reference_time):
        self.reference_time = reference_time

    def changeReferenceTime(self, reference_time):
        self.reference_time= reference_time
    
    #return the time difference in milli second
    def calculate_time_offset(self, current_time):
        if not isinstance(current_time, datetime):
            raise ValueError("Input must be a datetime object.")

        time_difference = current_time - self.reference_time
        time_offset_milliseconds = int(time_difference.total_seconds() * 1000)

        return time_offset_milliseconds