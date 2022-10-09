"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary.
schools: dict[str, int]

# Initialize to an empty dictionary.
schools = dict()

# Set a key-value pairing in the dictionary. 
schools["UNC"] = 19_400
schools["DUKE"] = 6_717
schools["NCSU"] = 26510

# Print a dictionary literal representation.
print(schools)

# Access a value but its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key -value pair from a dictionary. 
# by its key. 
schools.pop("DUKE")

# Test for the existence of a key. 
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

# Update/ reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200 
print(schools)

# Demonstration of dictionary literals 
# Empty dicitonary literal 
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 2615}
print(schools)

# What happens when a key does not exist?
print(schools["UNCC"])