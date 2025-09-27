# Q.8 For a given dictionary [Add few more entries]

# employees = {'Amol' : ['C', 'C++','Java'],.....}

# 1. print employees and their skill sets
# 2. Find all the employees who know Java
# 3. Update skill for an employee
# 4. Add/remove employee data



employees = {
    'Amol'    : ['C', 'C++', 'Java'],
    'Sneha'   : ['Python', 'SQL', 'HTML'],
    'Rohit'   : ['JavaScript', 'React', 'Node.js'],
    'Priya'   : ['C#', '.NET', 'SQL Server'],
    'Vikram'  : ['Go', 'Kubernetes', 'Docker'],
    'Neha'    : ['Python', 'Machine Learning', 'TensorFlow','Java'],
    'Karan'   : ['Ruby', 'Rails', 'PostgreSQL'],
    'Anjali'  : ['PHP', 'Laravel', 'MySQL']
}

'''# 1. print employees and their skill sets'''

for name, skills in employees.items():
    print(f"{name} {', '.join(skills)}")
    

'''# 2. Find all the employees who know Java'''

know_java = dict(filter(lambda item: 'Java' in item[1], employees.items()))
print(know_java)


'''# 3. Update skill for an employee'''

def update_all_skills(name, new_skills):
    if name in employees:
        employees[name] = new_skills
    else:
        print(f"{name} not found in employees.")

update_all_skills('Sneha', ['HTML', 'CSS', 'JavaScript'])
print(employees['Sneha'])


'''# 4. Add/remove employee data'''

def add_employee(name, skills):
    employees[name] = skills

def remove_employee(name):
    return employees.pop(name, None)

add_employee('Arjun', ['C', 'Python'])
print(employees['Arjun'])

removed_data = remove_employee('Sneha')
print("Removed data:", removed_data)
