def moving_average(sightings_data, num_months):
    n = len(sightings_data)
    moving_averages = []

    # Calculate the moving average
    for i in range(n):
        # Use modulo to wrap around to the beginning of the list
        window = [sightings_data[(i + j) % n] for j in range(num_months)]
        window_average = sum(window) / num_months
        moving_averages.append(window_average)    
    return moving_averages

# Example usage:
monthly_sightings_data = [3.2, 4.1, 5.0, 3.8, 2.9, 4.6, 5.2, 3.1, 2.7, 4.0, 3.9, 4.3]
num_months_average = 3
print(moving_average(monthly_sightings_data, num_months_average))
