name = "Lisa"
semester = 2

# ❌ Old way (don't use):
text = "Hello " + name + ", semester " + str(semester)

# ✅ New way (use this!):
text = f"Hello {name}, semester {semester}"
print(text)  # "Hello Lisa, semester 2"
# With expressions:
message = f"You have {5 * 2} ECTS points"  # "You have 10 ECTS points"

test = f"sie heißt {name.upper()} und ist im {semester}. Semester"
print(test)  # "sie heißt LISA und ist im 2. Semester"
print(message)  # "You have 10 ECTS points" 

###
def greet(name: str) -> str:
    """Greets a person by name"""
    return f"Hello {name}!"

# Call the function
message = greet("Anna")
print(message)  # "Hello Anna!"

#########

def calculate_grade(points: int, max_points: int) -> float:
    """Calculates percentage grade"""
    percentage = (points / max_points) * 100
    
    if percentage >= 87.5:
        return 1.0
    elif percentage >= 75:
        return 2.0
    elif percentage >= 62.5:
        return 3.0
    elif percentage >= 50:
        return 4.0
    else:
        return 5.0

grade = calculate_grade(10, 11
        )  # 1.0
print(grade)  # 1.0 

##############


def add_numbers(a: int, b: int) -> int:
   return a + b

answer = add_numbers(5, 3)
print(answer)  # None