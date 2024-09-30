def set_age(age):
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным!")
    return age


print(set_age(3))