def sort_dict_list(data, sort_key):
    if not data or sort_key not in data[0]:
        return data
    return sorted(data, key=lambda x: x[sort_key])
    
# Example usage
records = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 29}
]

sorted_records = sort_dict_list(records, "age")
print(sorted_records)
