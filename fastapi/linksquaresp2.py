# Objective: Return a hash containing the difference in each hash when there are missing keys.

a = {
    "name": "Jill",
    "role": "Sales",
    "company": "LinkSquares",
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
        "city": "Somerville",
        "zip_code": "02145"
    }
}

# Expected Output: { name: ['Jill', 'Jack'], company: ['LinkSquares'], location: { city: ['Boston', 'Somerville'], zip_code: ['02145'] } }

def key_length_checker(obj1, obj2):
    return obj1 if len(obj1.keys()) > len(obj2.keys()) else obj2

def diff(a, b):
    result = {}

    for a_key, a_value in a.items():
        b_value = b.get(a_key)
        if a_key == 'location':
            result["location"] = {}
            location_dict = result.get("location")
            # see line 24 for better solution than just using the other
            # hard coded dict
            for inner_b_key, inner_b_value in b_value.items():
                inner_a_value = a_value.get(inner_b_key)
                if inner_b_value != inner_a_value:
                    location_dict[inner_b_key] = null_checker(inner_a_value, inner_b_value)
        elif b_value != a_value:
            result[a_key] = null_checker(a_value, b_value)
    # all keys are known to be same so I can do
    return result

def null_checker(a, b):
    if not a:
        return [b]
    elif not b:
        return [a]
    else:
        return [a, b]

print(diff(a, b))
