from Student import Student
from Course import Course
import re
from functools import reduce


def file(fileName):
    """
    get a name of file , checking if it exists , and prepares a students list by the file information
    :param fileName: the name of file to read from him
    :return: students list
    """
    try:
        with open(fileName, 'r') as f:
            arr = [line.split('   ') for line in f]
            students_arr = [Student(i[0], i[1]) for i in arr] # list of 2 student
            course_arr = [re.split('#|;', i[2].rstrip().strip()) for i in arr] #list of 2 lists
            for i, j in zip(students_arr, course_arr):
                for k in j:
                    if j.index(k) % 2 == 0:
                        course = Course(k)
                    else:
                        course.setGrade(k)
                        i.addCourse(course)
                i.__str__()
            return students_arr

    except FileNotFoundError:
        print("file not find")

def menu(filename):
    """
    representing the menu ,  and calling the methods and the help methods
    who use to return the output by the choice
    :param filename: the name of file
    :return: output by request
    """
    students_arr = file(filename)
    choice = 0
    while int(choice) != 4:
        choice = int(input('pls choose :\n 1 - for student avg\n 2 - for course avg\n 3 - for all students avg\n 4 - for exit\n'))
        if int(choice) < 1 or int(choice) > 4:
            raise BaseException('valid choice must be value between 1-4')

        if choice == 1:
            studentName = input("pls enter the student name\n")
            print(studentAVG(studentName, students_arr))
        elif choice == 2:
            print(courseAVG(students_arr))
        elif choice == 3:
            allStusentsAVG(students_arr)
        elif choice == 4:
            print("bye bye")

def studentAVG(studentName,students_arr):
    """
    calculate a student grade average
    :param studentName: name of the student
    :param students_arr: the list of all students
    :return: the id and the avg of the student
    """

    the_student = list(filter(lambda student: student.getname() == studentName, students_arr))

    if not len(the_student):
        return " there is no students by this name"
    else:
        course_list = Student.getcourselist(the_student[0])
        grade_list = list(map(lambda course: course.getgrade(), course_list))
        sumofgrade = reduce(lambda x, y: int(x) + int(y), grade_list)
        countofgrade = len(Student.getcourselist(the_student[0]))

        return f' ID : {Student.getid(the_student[0])} AVG : {sumofgrade / countofgrade}\n'

def courseAVG(students_arr):
    """
    calculate the avg of all the students in chosen course
    :param students_arr: list of all students
    :return: the name of the course and the avg of all students in this course
    """

    courseName = input("pls enter the course name\n")

    list_of_all_courses = list(reduce(lambda x, y: Student.getcourselist(x) + Student.getcourselist(y),
                                      students_arr))
    list_of_choosen_course = list(filter(lambda course: course.getname() == courseName, list_of_all_courses))
    if not len(list_of_choosen_course):
        return " there is no courses by this name"
    else:
        courseGradesList = list(map(lambda course: course.getgrade(), list_of_choosen_course))
        sumOfCourseGrades = int(reduce(lambda x, y: int(x)+int(y), courseGradesList))
        countOfCourseGrade = len(courseGradesList)
        return f' COURSE NAME: {courseName}\n AVG of all students in this ourse : {sumOfCourseGrades / countOfCourseGrade}'

def allStusentsAVG(students_arr):
    """
    calculate avg for each students and write his id and his avg to file
    :param students_arr: list of all students
    :return: success message
    """
    filename = input("pls enter file name\n")
    with open(filename, 'w', encoding='utf8') as f:
        strings_list = list(map(lambda x: studentAVG(x.getname(), students_arr), students_arr))
          #  f.write(strings_list[0])
           # f.write(strings_list[1])
        f.write('\n'.join(map(''.join, strings_list)))
        print("writing to file success , go to check! ")

filename = "studentsinfo"
menu(filename)




