from util.export import OutputCSV
from util.web import get_xml_tree, get_dept_url
import uiuc_api as ua

outObj = OutputCSV(
    'data/crn_info.csv', 
    [
        'crn',
        'courseDept', 
        'courseNum', 
        'hours',
        'startTime',
        'endTime',
        'days',
        'instructorFirstName',
        'instructorLastName'
    ]
)

with outObj as out, open('data/deptCodes.txt', 'r') as codeFile:
    out.write_header()
    for dept in codeFile:
        dept = dept.strip()
        soup = get_xml_tree(get_dept_url(dept, mode="cascade"))
        for course in soup.select("cascadingCourse"):
            for section in course.select("detailedSection"):
                dept = section.select_one("parents subject")['id']
                number = section.select_one("parents course")['id']
                crn = section['id']
                profFirstName = ''
                profLastName = ''
                startTime = ''
                endTime = ''
                days = ''
                hours = ''
                if hoursObj := section.find('creditHours'):
                    # Assuming a section can't have more than one set of credit hours.
                    hours = hoursObj.text.split()[0]
                else:
                    if courseCH := course.select_one("creditHours", recursive=False):
                        candidate = courseCH.text.strip()
                        if sum(c.isdigit() for c in candidate) == 1:
                            candidate = candidate.split()[0]
                        hours = candidate
                meeting = section.select_one("meeting")
                if meeting:
                    if prof := meeting.find('instructor'):
                        profFirstName = prof['firstName']
                        profLastName = prof['lastName']
                    if start := meeting.find('start'):
                        startTime = start.text.strip()
                    if end := meeting.find('end'):
                        endTime = end.text.strip()
                    if daysObj := meeting.find('daysOfTheWeek'):
                        days = daysObj.text.strip()
                out.insert(
                    crn=crn,
                    instructorFirstName=profFirstName,
                    instructorLastName=profLastName,
                    courseDept=dept,
                    courseNum=number,
                    hours=hours,
                    days=days,
                    startTime=startTime,
                    endTime=endTime
                )