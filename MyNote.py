"""List"""
courses = ['MFIT', 'ITF', 'PSCP', 'ICS']
for index, course in enumerate(courses, start=1):
    print(index, course)

courses_str = ', '.join(courses)
print(courses_str)
new_list = courses_str.split(' - ')
print(new_list)