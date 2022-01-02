from Course import Course

class Student :
    """
    represent a student class with name , id , and list of courses
    """
    def __init__(self, name, id):
        """
        update the name and the id
        :param name: the name of the student
        :param id: the id of the student
        """
        self._studentName = name
        self.__studentID = id
        self._courseList = []

    def getid(self):
        """
        get a students and return his id
        :return: student id
        """
        return self.__studentID

    def getname(self):
        """
        get a student and return gis name
        :return: student name
        """
        return self._studentName

    def getcourselist(self):
        """
        get a student and return a list of his courses
        :return: list of course
        """
        return self._courseList

    def addCourse(self, course):
        """
        add a course to the student courses list
        :param course: the desired course to adding
        :return: an error if the parameter is not course or if the course grade not between 0-100,
        if the parameters is valid , there is no returning , just adding
        """
        if not isinstance(course, Course):
            raise BaseException("the input must be from Course type")
        if int(course.getgrade()) < 0 or int(course.getgrade()) > 100:
            raise BaseException("valid grade must be between 0-100")
        flag = 1
        if not len(self._courseList):
            self._courseList.append(course)
        else:
            for i in self._courseList:
                if i.getname() == course.getname():
                    i = course
                    flag = 0
                    break
                elif flag == 1:
                    self._courseList.append(course)
                    break

    def __str__(self):
        """
        get a student and return a string represent the student information
        :return:
        """
        print(f' NAME : {self._studentName}\n ID :{self.__studentID }\n COURSE LIST: ')
        [i.__str__() for i in self._courseList]
        print()




















            #student1= Student('shirel',206645103)
#print(student1.getid())
