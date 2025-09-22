def calculate_percentage(amount, percentage):
    """
    Calculate the percentage value of a given amount.
    
    Args:
        amount (float or int): The base amount.
        percentage (float or int): The percentage to calculate.
    
    Returns:
        float: The calculated percentage of the amount.
    """
    return amount * percentage / 100

total_amount = 200  # The base amount
percent_value = 15  # The percentage to calculate

# Print the result of calculating 15% of 200
print(calculate_percentage(total_amount, percent_value))
