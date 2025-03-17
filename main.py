student_count =1000
rating  = 4.5
is_published = True
course_name = "Python Programming"
length = len(course_name)
print(course_name[2])
print(course_name[-1])
print(course_name[0:3])
print(course_name[:3])
print(course_name[0:])
print(course_name[:])
course = "Python \"Programming"
print(course)
# additonal escape characters
course = "Python \ 'Programming"
print(course)
course = "Python \\ Programming"
print(course)
course = "Python \nProgramming"
print(course)
first = "Kiran"
Last = "Verma"
full = f"{len(first)} {Last}"
print(full)
course = "   Python programming"
print(course.upper())
print(course)
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.replace("p","j"))
print("pro" in course)
print("swift" not in course)
