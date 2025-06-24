def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda d: d.get(key, 0))

# Example usage
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 29}
]

print(sort_dicts_by_key(data, "age"))
