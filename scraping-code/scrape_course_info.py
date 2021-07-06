from util.export import OutputCSV
from util.web import get_xml_tree, get_dept_url
import uiuc_api as ua

with OutputCSV('data/courseInfo.csv', 
            ['courseDept', 'courseNum', 'title', 'description']) as out, \
        open('data/deptCodes.txt', 'r') as codeFile:
    out.write_header()
    for dept in codeFile:
        dept = dept.strip()
        print(f"Processing {dept}...")
        try:
            catalog = ua.get_subject_catalog(dept)
        except ValueError:
            print(f"Couldn't get information about department {dept}! Skipping...")
            continue
        print(f"Got {dept}! Scraping courses...")
        for course in ua.get_courses(catalog):
            try:
                out.insert(
                    courseDept=course.subject,
                    courseNum=course.number,
                    title=course.label,
                    description=course.description
                )
            except TypeError as e:
                print("Got TypeError! Check course: {} {}".format(course.subject, course.number))