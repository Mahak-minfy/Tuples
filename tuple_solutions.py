from collections import namedtuple

#Tuple Basics
def swap_pairs(t):
    return tuple(
        t[i + 1] if i % 2 == 0 and i + 1 < len(t) else
        t[i - 1] if i % 2 == 1 else
        t[i]
        for i in range(len(t))
    )
# Example usage:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))     # Should return (2, 1, 3)


#Tuple Unpacking
def get_stats(numbers):
    if not numbers:
        return (None, None, 0, None)
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return (minimum, maximum, total, average)
# Example usage:
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)



# Named Tuples
Student = namedtuple('Student', ['name', 'age', 'grades'])
def top_student(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades) if s.grades else float('-inf'))
# Example usage:
students = [
    Student('Alice', 20, [90, 80, 85]),
    Student('Bob', 22, [70, 75, 80]),
    Student('Charlie', 21, [95, 100])
]
print(top_student(students))  # Should return Student('Charlie', 21, [95, 100])


# Tuple as Keys
def count_coordinate_occurrences(coords):
    occurrences = {}
    for coord in coords:
        occurrences[coord] = occurrences.get(coord, 0) + 1
    return occurrences
# Example usage:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))  # Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}