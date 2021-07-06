import uiuc_api as ua
from util.export import OutputCSV
from util.extractor import extract_crosslist_from_description as get_crosslist

with OutputCSV('crosslist.csv', [
            'courseDept', 'courseNum', 'targetDept', 'targetNum'
        ]) as out, open('./data/deptCodes.txt', 'r') as codeFile:
    out.write_header()
    for dept in codeFile:
        dept = dept.strip()
        try:
            catalog = ua.get_subject_catalog(dept)
        except ValueError:
            print(f"Couldn't get information about department {dept}! Skipping...")
            continue
        for course in ua.get_courses(catalog):
            try:
                xlist = get_crosslist(course.description)
                if xlist:
                    out.insert(
                        targetDept=xlist[0],
                        targetNum=xlist[1],
                        courseDept=course.subject,
                        courseNum=course.number
                    )
            except TypeError as e:
                print("Got TypeError! Check course: {} {}".format(course.subject, course.number))