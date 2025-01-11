import json

def isAnagram(s: str, s2: str):
    return sorted(s) == sorted(s2)

print(isAnagram("pal", "lap"))
print(isAnagram("pal", "lapfd"))
print(isAnagram("pal", "lapa"))

json.loads