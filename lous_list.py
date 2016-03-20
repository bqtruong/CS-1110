import urllib.request

def instructors(department):
    pagename = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + department
    courses = urllib.request.urlopen(pagename)
    professors = []
    for course in courses:
        if not course.decode("UTF-8").split(";")[4] in professors:
            professors.append(course.decode("UTF-8").split(";")[4])  
    return sorted(professors)
def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    pagename = "http://stardock.cs.virginia.edu/louslist/Courses/view/" + dept_name
    allcourses = urllib.request.urlopen(pagename)
    courses = []
    for course in allcourses:
        course_info = course.decode("UTF-8").strip().split(";")
        if has_seats_available is True:
            if course_info[15] > course_info[16]:
                continue
        if level != None:
            if course_info[1][0] != str(level)[0]:
                continue
        if not_before != None:
            if int(course_info[12]) < not_before:
                continue
        if not_after != None:
            if int(course_info[13]) > not_after:
                continue
        courses.append(course_info)
    return courses
