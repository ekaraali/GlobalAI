nameSurname = 'Ediz Karaali'

right = 3
while (right>0):
    checkName = str(input('Please type your name and surname: '))
    if (checkName == nameSurname):
      print("Welcome")
      break
    else:
      right -= 1
      if (right == 0):
            print("Please try again later.")

if (0 < right <= 3):
 courseList = list()
 for course in range(5):
    print("If you want to quit, please enter 'q'.")
    course = str(input("Please enter your course name: "))
    if (course == 'q'):
         break
    else:
     courseList.append(course)

 def courseLength():
     if (len(courseList) < 3):
      return "You failed in class."

 courseLength()

 while True:
  examCourse = str(input('Please select a course from list to take the exam: '))
  if (examCourse not in courseList):
    print("Please enter a course from list...")
  else:
     break

 Midterm = int(input('Please enter your midterm grade: '))
 Final = int(input('Please enter your final grade: '))
 Project = int(input('Please enter your project grade: '))

 examCourseDict = {'Midterm': Midterm, "final": Final, "project": Project}
 courseGrade = 0.3*examCourseDict["Midterm"] + 0.5*examCourseDict["final"] + 0.20*examCourseDict["project"]

 if (courseGrade > 90):
    grade = 'AA'
 elif (70 < courseGrade < 90):
    grade = 'BB'
 elif (50 < courseGrade < 70):
    grade = 'CC'
 elif (30 < courseGrade < 50):
    grade = 'DD'
 elif (courseGrade < 30):
    grade = 'FF'
    print("Failed this course...:(")