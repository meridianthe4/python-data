# Q.6 
# 1.Find employees that know 'python'
# 2. Add a new skill - 'test' in skillset of all employees
# 3. Sort employees by skills 
# for the given dictionary of employees

# emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
#             'Aditi': ['Python', 'PHP', 'Database']}


emp_data = {
    'Amol': ['C', 'C++', 'Java'],
    'Aditya': ['Angular', 'Java'],
    'Aditi': ['Python', 'PHP', 'Database']
}


# 1. Find employees that know Python
print("Employees who know Python:")
for name, skills in emp_data.items():
    if "Python" in skills:
        print(name)


# 2. Add a new skill 'test'
for skills in emp_data.values():
    if "test" not in skills:
        skills.append("test")


# 3. Sort employees by skills
for skills in emp_data.values():
    skills.sort()

print("\nFinal employee data:")
print(emp_data)
