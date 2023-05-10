# age: int
# name: str
# height: float
# is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        check_result = True
    else:
        check_result = "False"
    return check_result

print(police_check(12))