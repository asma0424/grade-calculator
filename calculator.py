def calculate_average(grades):
    if not grades:
        raise ValueError("The grades list cannot be empty")
    return sum(grades) / len(grades)


def is_passing(average):
    return average >= 10


def get_grade(average):
    if average < 0 or average > 20:
        raise ValueError("Average must be between 0 and 20")

    if average >= 16:
        return "A"
    elif average >= 14:
        return "B"
    elif average >= 12:
        return "C"
    elif average >= 10:
        return "D"
    else:
        return "F"
