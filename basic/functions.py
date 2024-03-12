import time

def info_security():
    # Implementing the info_security function
    print("Security information: Area secured by drones and emergency equipment deployed.")

def robots_deploy(based_situation):
    if based_situation == "musibat":
        
        for i in range(1,20):
            time.sleep(1.5)
            print(f"Drone DM280{i} deployed for task {based_situation} for security purposes.")
    elif based_situation == "injured":
        
        for i in range(1,10):
            time.sleep(1.5)
            print(f"Drone DM280{i} deployed for task {based_situation} for security purposes.")
        for j in range(1,5):
            time.sleep(1.5)
            
            print(f"Emergency hospital equipment {j} deployed for {based_situation} owner.")
        for k in range(1,5):
            time.sleep(1.5)
            print(f"Drone for communication deployed from tower {k} to maintain communication for the owner.")
    else:
        print("CALL ONLY WIFE")

def mukul(owner, owner_location):
    if owner in ["musibat", "injured", "tension"]:
        if 50 <= owner_location <= 100:
            info_security()

# Example usage:
mukul("injured", 90)
robots_deploy("injured")

