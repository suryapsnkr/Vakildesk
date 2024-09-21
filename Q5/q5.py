from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    # Initialize an empty dictionary to hold the grouped data
    grouped_data = {}
    
    # Iterate through each dictionary in the data
    for entry in data:
        # Get the value of the specified key
        group_key = entry.get(key)
        # print(group_key)
        
        # If the group key doesn't exist in the grouped data, initialize it
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        
        # Append the value (or entire entry) to the appropriate group
        grouped_data[group_key].append(entry)
    # print(grouped_data)

    # Initialize a result dictionary to hold aggregated results
    aggregated_result = {}
    
    # Iterate through the grouped data and apply the aggregator
    for group_key, entries in grouped_data.items():
        # Apply the aggregator function to the list of entries
        aggregated_result[group_key] = aggregator(entries)

    return aggregated_result


data = [
    {'category': 'A', 'value': 30},
    {'category': 'A', 'value': 40},
    {'category': 'B', 'value': 30},
    {'category': 'B', 'value': 20},
    {'category': 'C', 'value': 40},
    {'category': 'C', 'value': 20},
    {'category': 'C', 'value': 30},
    {'category': 'B', 'value': 10},
    {'category': 'A', 'value': 10},
]

# Define an aggregator function to sum the values
def sum_values(entries):
    return sum(entry['value'] for entry in entries)

# Call the aggregate_data function
result = aggregate_data(data, 'category', sum_values)
print(result)
