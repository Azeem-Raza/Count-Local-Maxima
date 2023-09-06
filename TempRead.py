# Define a function to count local maxima in a list of temperatures
def count_local_maxima(temperatures):
    local_maxima = 0  #initialize a counter for local maxima
    n = len(temperatures)  #check the number of temperature samples in the list

    if n < 3:
        return local_maxima  # If they're fewer than 3 samples return 0 local maxima

    # Loop through the temperature samples. excluding the first and last elements
    for i in range(1, n - 1):
        #Check if the current sample is greater than its neighbors
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            local_maxima += 1  #increment the local maxima counter if a local maxima is found

    return local_maxima  #Return the total count of local maxima

#read temperature data from the text file
with open('hw1a.txt', 'r') as file:
    #rread each line from the file, convert it to a float, and store it in a list
    temp_samples = [float(line.strip()) for line in file]

#count local maxima in the temperature data using function
total_maxima = count_local_maxima(temp_samples)

#print the number of local maxima found in the temperature data
print(f'The number of local maxima is: {total_maxima}')
