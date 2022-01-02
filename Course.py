class Course:
    """
    represent a course class with name and grade
    """
    def __init__(self,courseName):
        """
        update the name and the grade
        :param courseName: the name of the course
               courseGrdade: the grade of the course - automatically update to 101
        """
        self._courseName = courseName
        self._courseGrade = 101

    def setGrade(self, grade):
        """
        set the grade to the grade obtain by the parameter
        :param grade: the desires grade for updating
        :return: nothing ,just update
        """
        self._courseGrade = grade

    def getname(self):
        """
        get a coursre and return his name
        :return: course name
        """
        return self._courseName

    def getgrade(self):
        """
        get a course and return his grade
        :return: course grade
        """
        return self._courseGrade

    def __str__(self):
        """
        get a course and return a string represent the name & the grade of this course
        :return: string
        """
        print(f' NAME : {self._courseName}  GRADE : {self._courseGrade} ')
