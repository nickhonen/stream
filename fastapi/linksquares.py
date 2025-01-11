# Objective: Return a hash containing the difference in each hash

a = {
    "name": "Jill",
    "role": "Sales",
    "location": {
        "state": "Massachusetts",
        "city": "Boston"
    }
}
b = {
    "name": "Jack",
    "role": "Sales",
    "location": {
        "state": "Massachusetts",
        "city": "Somerville"
    }
}

# Expected Output: { "name": ["Jill", "Jack"], "location": { "city": ["Boston", "Somerville"] } }


def diff(a, b):
    result = {}

    for a_key, a_value in a.items():
        b_value = b.get(a_key)
        if a_key == 'location':
            result["location"] = {}
            location_dict = result.get("location")
            for inner_a_key, inner_a_value in a_value.items():
                inner_b_value = b_value.get(inner_a_key)
                if inner_b_value != inner_a_value:
                    location_dict[inner_a_key] = [inner_a_value, inner_b_value]
                
        elif b_value != a_value:
            result[a_key] = [a_value, b_value]
    # all keys are known to be same so I can do
    return result

    

print(diff(a, b))
