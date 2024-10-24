# Package Sorting System

This repo contains the implementation of a package sorting system that classifies packages based on their dimensions and weight. The packages are sorted into three categories:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.

## Problem Def

### Rules

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater than or equal to 150 cm.
- A package is **heavy** when its mass is greater than or equal to 20 kg.

Packages are sorted into the following categories:

- **STANDARD**: Standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: Packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: Packages that are both heavy and bulky are rejected.

### Test Cases

```python
# STANDARD package
print(sort(100, 100, 100, 10))  # Output: "STANDARD"

# SPECIAL package (bulky)
print(sort(200, 50, 50, 10))    # Output: "SPECIAL"

# SPECIAL package (heavy)
print(sort(100, 100, 100, 25))  # Output: "SPECIAL"

# REJECTED package (both bulky and heavy)
print(sort(200, 150, 150, 25))  # Output: "REJECTED"
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/amahmood561/package-sorting-system.git
```

2. Navigate to the directory:

```bash
cd package-sorting-system
```

3. Run the Python file to test the sorting function:

```bash
python sort_packages.py
```


### Files in the Repository

- `README.md`: The README file you see here.
- `sort_packages.py`: Contains the implementation of the sorting logic.

