'''Question 3: Train Travel Time Problem:
A train covers 800 meters (400m track + 400m bridge) at a given speed (km/hr).
Calculate the time taken in seconds using the formula: (Total distance / Speed) * (18/5).'''


speed_kmhr = int(input("Enter speed: "))
def calculate_train_time(speed_kmhr):
    track_len = 400
    bridge_len = 400
    total_distance = track_len + bridge_len
    
    if speed_kmhr < 0:
        print("Invalid speed !")
        return
    
    time_secound = (total_distance/speed_kmhr)*(18/5)
    
    return time_secound
print("speed of train : ",calculate_train_time(speed_kmhr)) 
