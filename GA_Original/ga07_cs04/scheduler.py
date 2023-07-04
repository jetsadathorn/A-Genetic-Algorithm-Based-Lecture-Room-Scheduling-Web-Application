import sqlite3 as sqlite
from itertools import chain
from abc import abstractmethod, ABC
import prettytable as prettytable
import random as rnd
from enum import Enum
POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
VERBOSE_FLAG = False
PT_STUDENT_MAX_CLASS_LOAD = 3
FT_STUDENT_MAX_CLASS_LOAD = 5
class DBMgr:
    def __init__(self):
        self._connection = sqlite.connect('class_schedule.db')
        self._cursor = self._connection.cursor()
        self._rooms = self._select_rooms()
        self._meetingTimes = self._select_meeting_times()
        self._instructors = self._select_instructors()
        self._students = self._select_students()
        self._courses = self._select_courses()
        self._depts = self._select_depts()
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())
    def _select_rooms(self):
        self._cursor.execute("SELECT * FROM room")
        roomsRS = self._cursor.fetchall()
        returnRooms = []
        for i in range(0, len(roomsRS)):
            returnRooms.append(Room(roomsRS[i][0], roomsRS[i][1]))
        return returnRooms
    def _select_meeting_times(self):
        self._cursor.execute("SELECT * FROM meeting_time")
        meetingTimesRS = self._cursor.fetchall()
        returnMeetingTimes = []
        for i in range(0, len(meetingTimesRS)):
            returnMeetingTimes.append(MeetingTime(meetingTimesRS[i][0], meetingTimesRS[i][1]))
        return returnMeetingTimes
    def _select_instructors(self):
        self._cursor.execute("SELECT * FROM instructor")
        instructorsRS = self._cursor.fetchall()
        returnInstructors = []
        for i in range(0, len(instructorsRS)):
            returnInstructors.append(Instructor(instructorsRS[i][0], instructorsRS[i][1],
                                                self._select_instructor_availability(instructorsRS[i][0])))
        return returnInstructors
    def _select_students(self):
        self._cursor.execute("SELECT * FROM student")
        studentsRS = self._cursor.fetchall()
        returnStudents = []
        for i in range(0, len(studentsRS)):
            self._cursor.execute("SELECT course_number FROM courses_passed where student_id == '" + studentsRS[i][0] + "'")
            passedCourses = list(chain.from_iterable(self._cursor.fetchall()))
            returnStudents.append(Student(studentsRS[i][0], studentsRS[i][1], passedCourses,
                                          self._select_student_availability(studentsRS[i][0]), studentsRS[i][2]))
        return returnStudents
    def _select_instructor_availability(self, instructor):
        self._cursor.execute("SELECT meeting_time_id from instructor_availability where instructor_id = '" + instructor + "'")
        instructorMTs = list(chain.from_iterable(self._cursor.fetchall()))
        instructorAvailability = []
        for i in range(0, len(self._meetingTimes)):
            if self._meetingTimes[i].get_id() in instructorMTs:
                instructorAvailability.append(self._meetingTimes[i])
        return instructorAvailability
    def _select_student_availability(self, student):
        self._cursor.execute("SELECT meeting_time_id from student_availability where student_id = '" + student + "'")
        studentMTs = list(chain.from_iterable(self._cursor.fetchall()))
        studentAvailability = []
        for i in range(0, len(self._meetingTimes)):
            if self._meetingTimes[i].get_id() in studentMTs:
                studentAvailability.append(self._meetingTimes[i].get_id())
        return studentAvailability
    def _select_courses(self):
        self._cursor.execute("SELECT * FROM course")
        coursesRS = self._cursor.fetchall()
        returnCourses = []
        for i in range(0, len(coursesRS)):
            self._cursor.execute("SELECT prereq_course_number FROM course_prereqs where course_number == '" + coursesRS[i][0] + "'")
            prereqs = list(chain.from_iterable(self._cursor.fetchall()))
            returnCourses.append(Course(coursesRS[i][0], coursesRS[i][1], self._select_course_instructors(coursesRS[i][0]),
                                        coursesRS[i][2], prereqs, coursesRS[i][3]))
        return returnCourses
    def _select_depts(self):
        self._cursor.execute("SELECT * FROM dept")
        deptsRS = self._cursor.fetchall()
        returnDepts = []
        for i in range(0, len(deptsRS)):
            returnDepts.append(Department(deptsRS[i][0], self._select_dept_courses(deptsRS[i][0]),
                                          self._select_dept_instructors(deptsRS[i][0])))
        return returnDepts
    def _select_course_instructors(self, courseNumber):
        self._cursor.execute("SELECT instructor_number FROM course_instructor where course_number == '" + courseNumber + "'")
        instructorNumbers = list(chain.from_iterable(self._cursor.fetchall()))
        returnValue = []
        for i in range(0, len(self._instructors)):
           if  self._instructors[i].get_id() in instructorNumbers:
               returnValue.append(self._instructors[i])
        return returnValue
    def _select_dept_courses(self, deptName):
        self._cursor.execute("SELECT course_numb FROM dept_course where name == '" + deptName + "'")
        courseNumbers = list(chain.from_iterable(self._cursor.fetchall()))
        returnValue = []
        for i in range(0, len(self._courses)):
           if self._courses[i].get_number() in courseNumbers:
               returnValue.append(self._courses[i])
        return returnValue
    def _select_dept_instructors(self, deptName):
        self._cursor.execute("SELECT instructor_id FROM dept_instructor where dept_name == '" + deptName + "'")
        instructorIds = list(chain.from_iterable(self._cursor.fetchall()))
        returnValue = []
        for i in range(0, len(self._instructors)):
           if self._instructors[i].get_id() in instructorIds:
               returnValue.append(self._instructors[i])
        return returnValue
    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_students(self): return self._students
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses
class Schedule:
    def __init__(self):
        self._data = dbMgr
        self._classes = []
        self._conflicts = []
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self._conflicts = []
        self._sessionsMap = {}
        self._studentMaxClassLoadMap = {}
        self._courseMaxStudentLoadMap = {}
    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                for k in range(0, courses[j].get_numbOfSessions()):
                    newClass = Class(self._classNumb, depts[i], courses[j])
                    self._classNumb += 1
                    newClass.set_meetingTime(dbMgr.get_meetingTimes()[rnd.randrange(0, len(dbMgr.get_meetingTimes()))])
                    newClass.set_room(dbMgr.get_rooms()[rnd.randrange(0, len(dbMgr.get_rooms()))])
                    newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])
                    students = self.find_students_to_register_in_class(courses[j])
                    newClass.set_students(students)
                    self._classes.append(newClass)
        return self
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    def calculate_fitness(self):
        self._conflicts = []
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents()):
                self._conflicts.append(NumbOfStudentsConflict(Conflict.ConflictType.NUMB_OF_STUDENTS,
                                                              classes[i], classes[i].get_room()))
            if (classes[i].get_meetingTime() not in classes[i].get_instructor().get_availability()):
                self._conflicts.append(InstructorAvailabilityConflict(Conflict.ConflictType.INSTRUCTOR_AVAILABILITY,
                                                                      classes[i], classes[i].get_instructor()))
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime().get_id() == classes[j].get_meetingTime().get_id() and
                    classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room().get_number() == classes[j].get_room().get_number()):
                            roomBookingConflict = list()
                            roomBookingConflict.append(classes[i])
                            roomBookingConflict.append(classes[j])
                            self._conflicts.append(RoomBookingConflict(Conflict.ConflictType.ROOM_BOOKING,
                                                                       roomBookingConflict, classes[j].get_room()))
                        if (classes[i].get_instructor().get_id() == classes[j].get_instructor().get_id()):
                            instructorBookingConflict = list()
                            instructorBookingConflict.append(classes[i])
                            instructorBookingConflict.append(classes[j])
                            self._conflicts.append(InstructorBookingConflict(Conflict.ConflictType.INSTRUCTOR_BOOKING,
                                                                             instructorBookingConflict,
                                                                             classes[j].get_instructor()))
        students = self._data.get_students()
        for i in range(0, len(students)):
            for j in range(0, len(classes)):
                if (classes[j].get_meetingTime().get_id() not in students[i].get_availability()):
                    self._conflicts.append(
                        StudentAvailabilityConflict(Conflict.ConflictType.STUDENT_AVAILABILITY, classes[j], students[i]))
            self.find_student_time_conflicts(self._conflicts, students[i])
        return 1 / ((1.0 * len(self._conflicts) + 1))
    def find_student_time_conflicts(self, conflicts, student):
        classes = self._classes
        for i in range(0, len(classes)):
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and
                            classes[i].get_id() != classes[j].get_id()):
                        if (student in classes[i].get_students() and student in classes[j].get_students()):
                            studentBookingConflict = list()
                            studentBookingConflict.append(classes[i])
                            studentBookingConflict.append(classes[j])
                            self._conflicts.append(StudentBookingConflict(Conflict.ConflictType.STUDENT_BOOKING,
                                                                          studentBookingConflict, student))
    def find_students_to_register_in_class(self, course):
        courseMaxNumbOfStudents = course.get_maxNumbOfStudents()
        student = self._data.get_students()
        returnStudents = []
        for i in range(0, len(student)):
            maxClassLoad = PT_STUDENT_MAX_CLASS_LOAD
            if (student[i].get_status()=='FT'): maxClassLoad = FT_STUDENT_MAX_CLASS_LOAD
            if student[i].did_pass_prereqs(course) and \
                    student[i].have_not_already_passed_course_to_register_in(course):
                if (student[i].get_id() not in self._studentMaxClassLoadMap):
                    self._studentMaxClassLoadMap[student[i].get_id()] = 1
                if (self._classNumb not in self._courseMaxStudentLoadMap):
                   self._courseMaxStudentLoadMap[self._classNumb] = 1
                if (self._studentMaxClassLoadMap.get(student[i].get_id()) <= maxClassLoad):
                    if (self._courseMaxStudentLoadMap[self._classNumb] <= courseMaxNumbOfStudents):
                        if (student[i].get_id() not in self._sessionsMap):
                            courseNames = []
                            self._sessionsMap[student[i].get_id()] = courseNames
                        if (course.get_number() not in self._sessionsMap.get(student[i].get_id())):
                            self._sessionsMap[student[i].get_id()].append(course.get_number())
                            self._studentMaxClassLoadMap[student[i].get_id()] = self._studentMaxClassLoadMap.get(student[i].get_id())+1
                            self._courseMaxStudentLoadMap[self._classNumb] = self._courseMaxStudentLoadMap.get(self._classNumb)+1
                            returnStudents.append(student[i])
        return returnStudents
    def get_conflicts(self): return self._conflicts
    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes)-1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes)-1])
        return returnValue
class Population:
    def __init__(self, size):
        self._size = size
        self._data = dbMgr
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())
    def get_schedules(self): return self._schedules
class GeneticAlgorithm:
    def evolve(self, population): return self._mutate_population(self._crossover_population(population))
    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop
    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population
    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule
    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule
    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop
class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents, prereqs, numbOfSessions):
        self._number = number
        self._name = name
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors
        self._prereqs = prereqs
        self._numbOfSessions = numbOfSessions
    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def get_instructors(self): return self._instructors
    def get_prereqs(self): return self._prereqs
    def get_numbOfSessions(self): return self._numbOfSessions
    def __eq__(self, o: object):
        returnFlag = False
        if isinstance(o, Course):
            if o.get_number() == self._number:
                returnFlag = True
        return returnFlag
    def __hash__(self): return hash(self._number)
    def __repr__(self): return self._number
    def __str__(self): return self._number
class Instructor:
    def __init__(self, id, name, availability):
        self._id = id
        self._name = name
        self._availability = availability
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_availability(self): return self._availability
    def __eq__(self, o: object):
        returnFlag = False
        if isinstance(o, Instructor):
            if o.get_id() == self._id:
                returnFlag = True
        return returnFlag
    def __hash__(self): return hash(self._id)
    def __repr__(self): return self._id
    def __str__(self): return self._id
class Student:
    def __init__(self, id, name, passedCourses, availability, status):
        self._id = id
        self._name = name
        self._passedCourses = passedCourses
        self._availability = availability
        self._scheduledCourses = []
        self._status = status
    def get_scheduled_courses_numbers(self):
        coursesNumbers = []
        for i in range(0, len(self._scheduledCourses)):
            coursesNumbers.append(self._scheduledCourses[i].get_number())
        return coursesNumbers
    def did_pass_prereqs(self, course):
        flag = True
        for i in range(0, len(course.get_prereqs())):
            if str(course.get_prereqs()[i]) not in self.get_passedCourses(): flag = False
        return flag
    def have_not_already_passed_course_to_register_in(self, course):
        flag = True
        if course.get_number() in self._passedCourses: flag = False
        return flag
    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_passedCourses(self): return self._passedCourses
    def get_availability(self): return self._availability
    def get_status(self): return self._status
    def __eq__(self, o: object):
        returnFlag = False
        if isinstance(o, Student):
            if o.get_id() == self._id:
                returnFlag = True
        return returnFlag
    def __hash__(self): return hash(self._id)
    def __str__(self): return self._name
class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity
    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity
class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time
    def get_id(self): return self._id
    def get_time(self): return self._time
    def __repr__(self): return self._id
    def __eq__(self, o) :
        returnFlag = False
        if isinstance(o, MeetingTime):
            if o.get_id() == self._id:
                returnFlag = True
        return returnFlag
    def __hash__(self): return hash(self._id)
    def __str__(self): return self._id
class Department:
    def __init__(self, name, courses, instructors):
        self._name = name
        self._courses = courses
        self._instructors = instructors
    def get_name(self): return self._name
    def get_courses(self): return self._courses
    def get_instructors(self): return self._instructors
class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
        self._students = []
    def get_student_ids(self):
        studentIds = []
        for s in self._students:
            studentIds.append(s.get_id())
        return studentIds
    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def get_students(self): return self._students
    def set_students(self, students): self._students = students
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + \
               str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + \
               str(self._meetingTime.get_id())
class Conflict(ABC):
    class ConflictType(Enum):
        INSTRUCTOR_BOOKING = 1
        ROOM_BOOKING = 2
        NUMB_OF_STUDENTS = 3
        INSTRUCTOR_AVAILABILITY = 4
        STUDENT_BOOKING = 5
        STUDENT_AVAILABILITY = 6
    @abstractmethod
    def __init__(self, conflictType): self._conflictType = conflictType
    @abstractmethod
    def get_conflict(self): pass
    def get_conflictType(self): return self._conflictType
class InstructorAvailabilityConflict(Conflict):
    def __init__(self, conflictType, conflictClass, instructor):
        super().__init__(conflictType)
        self._instructor = instructor
        self._conflictClass = conflictClass
    def get_conflict(self):
        return "["+str(self._conflictClass)+"] where instructor "+ \
               self._instructor.get_id()+ " MT not in ["+ \
               ','.join(str(x) for x in self._instructor.get_availability())+\
               "] instructor availability MTs"
class StudentAvailabilityConflict(Conflict):
    def __init__(self, conflictType, conflictClass, student):
        super().__init__(conflictType)
        self._conflictClass = conflictClass
        self._student = student
    def get_conflict(self):
        return "["+str(self._conflictClass)+ "] where student "+ \
               self._student.get_id()+ " MT not in ["+ \
               ','.join(str(x) for x in self._student.get_availability())+\
               "] student availability MTs"
class InstructorBookingConflict(Conflict):
    def __init__(self, conflictType, conflictBetweenClasses, instructor):
        super().__init__(conflictType)
        self._instructor = instructor
        self._conflictBetweenClasses = conflictBetweenClasses
    def get_conflict(self):
        return "["+str("  and  ".join(map(str, self._conflictBetweenClasses)))+\
               "] where instructor "+ self._instructor.get_id()+" scheduled to teach both classes @ same time"
class StudentBookingConflict(Conflict):
    def __init__(self, conflictType, conflictBetweenClasses, student):
        super().__init__(conflictType)
        self._student = student
        self._conflictBetweenClasses = conflictBetweenClasses
    def get_conflict(self):
        return "["+str("  and  ".join(map(str, self._conflictBetweenClasses)))+ \
               "] where student "+ self._student.get_id()+ " booked in both classes @ same meeting time"
class RoomBookingConflict(Conflict):
    def __init__(self, conflictType, conflictBetweenClasses, room):
        super().__init__(conflictType)
        self._conflictBetweenClasses = conflictBetweenClasses
        self._room = room
    def get_conflict(self):
        return "["+str("  and  ".join(map(str, self._conflictBetweenClasses)))+ \
               "] where room "+ self._room.get_number()+ " reserved for both classes @ same meeting time"
class NumbOfStudentsConflict(Conflict):
    def __init__(self, conflictType, conflictClass, room):
        super().__init__(conflictType)
        self._conflictClass = conflictClass
        self._room = room
    def get_conflict(self):
        return "["+str(self._conflictClass) + "] where (room " + self._room.get_number() + " seating capacity = "+\
               str(self._room.get_seatingCapacity())+ ") < (course "+ self._conflictClass.get_course().get_number()+\
               " max # of students = "+ str(self._conflictClass.get_course().get_maxNumbOfStudents())+")"
class DisplayMgr:
    @staticmethod
    def display_input_data():
        print("> All Available Data")
        DisplayMgr.display_dept()
        DisplayMgr.display_course()
        DisplayMgr.display_room()
        DisplayMgr.display_instructor()
        DisplayMgr.display_meeting_times()
        DisplayMgr.display_student()
    @staticmethod
    def display_dept():
        depts = dbMgr.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses', 'instructors'])
        for i in range(0, len(depts)):
            availableDeptsTable.add_row([depts[i].get_name(), depts[i].get_courses(), depts[i].get_instructors()])
        print(availableDeptsTable)
    @staticmethod
    def display_course():
        availableCoursesTable = prettytable.PrettyTable(['course id', 'name', '# of sessions', 'max # of students', 'qualified instructors', 'prereqs'])
        courses = dbMgr.get_courses()
        for i in range(0, len(courses)):
            availableCoursesTable.add_row(
                [courses[i].get_number(), courses[i].get_name(),
                 courses[i].get_numbOfSessions(), str(courses[i].get_maxNumbOfStudents()),
                 courses[i].get_instructors(), courses[i].get_prereqs()])
        print(availableCoursesTable)
    @staticmethod
    def display_instructor():
        availableInstructorsTable = prettytable.PrettyTable(['instructor id', 'name', 'availability', 'qualification'])
        instructors = dbMgr.get_instructors()
        courses = dbMgr.get_courses()
        for i in range(0, len(instructors)):
            qualifications = []
            for j in range(0, len(courses)):
                if (instructors[i] in courses[j].get_instructors()):
                    qualifications.append(courses[j].get_number())
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name(),
                                               instructors[i].get_availability(), qualifications])
        print(availableInstructorsTable)
    @staticmethod
    def display_student():
        studentsTable = prettytable.PrettyTable(['student id', 'name', 'status', 'courses passed', 'availability'])
        students = dbMgr.get_students()
        for i in range(0, len(students)):
            studentsTable.add_row([students[i].get_id(), students[i].get_name(), students[i].get_status(),
                                   students[i].get_passedCourses(), students[i].get_availability()])
        print(studentsTable)
    @staticmethod
    def display_room():
        availableRoomsTable = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = dbMgr.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)
    @staticmethod
    def display_meeting_times():
        availableMeetingTimeTable = prettytable.PrettyTable(['id', 'Meeting Time'])
        meetingTimes = dbMgr.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)
    @staticmethod
    def display_generation(population):
        generationTable = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes [dept,course,room,instructor,meeting-time]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            generationTable.add_row([str(i+1), round(schedules[i].get_fitness(),3), len(schedules[i].get_conflicts()), str(schedules[i])])
        print(generationTable)
    @staticmethod
    def display_schedule_as_table(schedule):
        classes = schedule.get_classes()
        scheduleTable = prettytable.PrettyTable(['Class #', 'Dept', 'Course (number, max # of students)', 'Room (Capacity)', 'Instructor (Id)',  'Meeting Time (Id)', 'students'])
        for i in range(0, len(classes)):
            scheduleTable.add_row([str(i+1), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + " (" +
                           classes[i].get_course().get_number() + ", " +
                           str(classes[i].get_course().get_maxNumbOfStudents()) +")",
                           classes[i].get_room().get_number() + " (" + str(classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() +" (" + str(classes[i].get_instructor().get_id()) +")",
                           classes[i].get_meetingTime().get_time() +" (" + str(classes[i].get_meetingTime().get_id()) +")",
                           classes[i].get_student_ids()])
        print(scheduleTable)
    @staticmethod
    def display_schedule_meetingTimes(schedule):
        print("> from 'meeting time' perspective")
        meetingTimesTable = prettytable.PrettyTable(['id', 'meeting time', 'classes [dept,course,room,instructor,meeting-time] '])
        meetingTimes = dbMgr.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            classes = []
            for j in range(0, len(schedule.get_classes())):
                if schedule.get_classes()[j].get_meetingTime() == meetingTimes[i]:
                    classes.append(str(schedule.get_classes()[j]))
            meetingTimesTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time(), str(classes)])
        print(meetingTimesTable)
    @staticmethod
    def display_schedule_rooms(schedule):
        print("> from 'room' perspective")
        scheduleRoomsTable = prettytable.PrettyTable(['room','classes [dept,course,room,instructor,meeting-time] '])
        rooms = dbMgr.get_rooms()
        for i in range(0, len(rooms)):
            roomSchedule = []
            for j in range(0, len(schedule.get_classes())):
                if schedule.get_classes()[j].get_room() == rooms[i]:
                    roomSchedule.append(str(schedule.get_classes()[j]))
            scheduleRoomsTable.add_row([str(rooms[i].get_number()), str(roomSchedule)])
        print(scheduleRoomsTable)
    @staticmethod
    def display_schedule_instructors(schedule):
        print("> from 'instructor' perspective")
        instructorsTable = prettytable.PrettyTable(['id', 'instructor', "classes [dept,course,room,instructor,meeting-time]",'availability', 'qualifications'])
        instructors = dbMgr.get_instructors()
        courses = dbMgr.get_courses()
        for i in range(0, len(instructors)):
            qualifications = []
            for j in range(0, len(courses)):
                if (instructors[i] in courses[j].get_instructors()):
                    qualifications.append(courses[j].get_number())
            classSchedule = []
            for j in range(0, len(schedule.get_classes())):
                if schedule.get_classes()[j].get_instructor() == instructors[i]:
                    classSchedule.append(str(schedule.get_classes()[j]))
            instructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name(),
                                      str(classSchedule), instructors[i].get_availability(), qualifications])
        print(instructorsTable)
    @staticmethod
    def display_schedule_students(schedule):
        print("> from 'student' perspective")
        instructorsTable = prettytable.PrettyTable(
            ['id', 'student', 'status', 'classes [dept,course,room,instructor,meeting-time]', 'courses passed', 'availability'])
        students = dbMgr.get_students()
        for i in range(0, len(students)):
            classSchedule = list()
            for j in range(0, len(schedule.get_classes())):
                if students[i] in schedule.get_classes()[j].get_students() :
                    classSchedule.append(str(schedule.get_classes()[j]))
            instructorsTable.add_row(
                [students[i].get_id(), students[i].get_name(), students[i].get_status(), str(classSchedule), students[i].get_passedCourses(), students[i].get_availability()])
        print(instructorsTable)
    @staticmethod
    def display_schedule_conflicts(schedule):
        conflictsTable = prettytable.PrettyTable(['conflict type', 'conflict explanation'])
        conflicts = schedule.get_conflicts()
        for i in range(0, len(conflicts)):
            conflictsTable.add_row([str(conflicts[i].get_conflictType()),
                                    conflicts[i].get_conflict()])
        if (len(conflicts) > 0): print(conflictsTable)
def find_fittest_schedule(verboseFlag):
    generationNumber = 0
    if (verboseFlag): print("> Generation # "+str(generationNumber))
    population = Population(POPULATION_SIZE)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    if (verboseFlag):
        DisplayMgr.display_generation(population)
        DisplayMgr.display_schedule_as_table(population.get_schedules()[0])
        DisplayMgr.display_schedule_conflicts(population.get_schedules()[0])
    geneticAlgorithm = GeneticAlgorithm()
    while (population.get_schedules()[0].get_fitness() != 1.0):
        generationNumber += 1
        if (verboseFlag): print("\n> Generation # " + str(generationNumber))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        if (verboseFlag):
            DisplayMgr.display_generation(population)
            DisplayMgr.display_schedule_as_table(population.get_schedules()[0])
            DisplayMgr.display_schedule_conflicts(population.get_schedules()[0])
    print("> solution found after " + str(generationNumber) + " generations")
    return population.get_schedules()[0]
def handle_command_line(verboseFlag):
    while (True):
        entry = input("> What do you want to do (i:nitial data display, f:ind fittest schedule, d:efault mode, v:erbose mode, e:xit)\n")
        if (entry == "i"): DisplayMgr.display_input_data()
        elif (entry == "f"):
            schedule = find_fittest_schedule(verboseFlag)
            handle_schedule_display(schedule)
        elif (entry == "d"): verboseFlag = False
        elif (entry == "v"): verboseFlag = True
        elif (entry == "e"): break
def handle_schedule_display(schedule):
    while (True):
        entry = input("> What do you want to display (c:lass schedule, t:ime schedule, r:oom schedule, i:nstructor schedule, s:tudent schedule, e:lse)\n")
        if (entry == "c"):
            print("> from 'class' perspective")
            DisplayMgr.display_schedule_as_table(schedule)
        elif (entry == "t"): DisplayMgr.display_schedule_meetingTimes(schedule)
        elif (entry == "r"): DisplayMgr.display_schedule_rooms(schedule);
        elif (entry == "i"): DisplayMgr.display_schedule_instructors(schedule);
        elif (entry == "s"): DisplayMgr.display_schedule_students(schedule);
        elif (entry == "e"): break
dbMgr = DBMgr()
handle_command_line(VERBOSE_FLAG)

