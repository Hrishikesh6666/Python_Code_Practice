def watch_delay(initial_hour, initial_minute, watch_hour, watch_minute, elapsed_hours):
    # Convert initial correct time to minutes
    initial_time = initial_hour * 60 + initial_minute
    
    # Correct time after elapsed_hours
    correct_time = initial_time + elapsed_hours * 60
    
    # Convert watch reading to minutes
    watch_time = watch_hour * 60 + watch_minute
    
    # Calculate delay in minutes
    delay_minutes = correct_time - watch_time
    
    # Optionally return delay in hours and minutes
    delay_hours = delay_minutes // 60
    delay_remaining_minutes = delay_minutes % 60
    
    return delay_minutes, (delay_hours, delay_remaining_minutes)
    

    