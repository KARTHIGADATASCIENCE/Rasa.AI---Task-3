def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    :param arr1: First sorted array
    :param arr2: Second sorted array
    :return: Merged sorted array
    """
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements from arr1 or arr2
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"student(name={self.name}, age={self.age})"