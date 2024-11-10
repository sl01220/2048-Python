import sys
def find_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None
for i in sys.stdin:
    x=i.strip()
# Example usage
my_list = [x]
duplicate = find_duplicate(my_list)
if duplicate:
    print(f"Duplicate item found: {duplicate}")
else:
    print("No duplicate items found.")