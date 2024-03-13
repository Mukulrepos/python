from time import process_time
start_time = process_time()

def average(a=9, b=1):
        print("the average of two numbers is -->", int((a + b) / 2)) # Corrected spelling of 'average' and 'numbers'
average()
end_time = process_time() # Corrected spacing around the '=' operator

print("Start time:", start_time) # Added a print statement to display start time
print("End time:", end_time) # Added a print statement to display end time
print("Elapsed time:", end_time - start_time) # Added a print statement to display elapse