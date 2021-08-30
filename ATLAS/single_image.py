# Converts steps into single image
def single_view(steps):
    # Stores all steps as a string
    all_steps = ""
    # Step number
    count = 1
    # Concatenating each step to "single_view" string
    for i in steps:
        all_steps += "\\text{"+str(count)+". }" + (i[1]) + "$$$$"
        count += 1
    return ("single", all_steps)