def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    # Sorting logic
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# test cases
'''
print(sort(100, 100, 100, 10))  # STANDARD
print(sort(200, 50, 50, 10))    # SPECIAL (bulky)
print(sort(100, 100, 100, 25))  # SPECIAL (heavy)
print(sort(200, 150, 150, 25))  # REJECTED (both bulky and heavy)
'''
'''
Test Coverage:
This implementation includes edge cases like:

Small packages with no special conditions.
Large packages based on volume and size.
Heavy packages with a mass over 20 kg.
Packages that are both bulky and heavy.
'''