import uiuc_api as ua
from util.export import OutputCSV
from util.extractor import extract_crosslist_from_description as get_crosslist

with OutputCSV('data/prereqs.csv', [
            'courseDept', 'courseNum', 'id', 'prereqDept', 'prereqNum', 'type'
        ], verbose=True) as out, open('./data/deptCodes.txt', 'r') as codeFile:
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
                if get_crosslist(str(course.description)):
                    print("Found crosslisted, skipping...")
                    continue
                for i, prereqs in enumerate(course.prereqs):
                    for prereq in prereqs: 
                        prereqDept, prereqNum = prereq.split()
                        out.insert(
                            courseDept=course.subject,
                            courseNum=course.number,
                            id=i,
                            prereqDept=prereqDept,
                            prereqNum=prereqNum,
                            type='PREREQ'
                        )
                for i, coreqs in enumerate(course.coreqs):
                    for coreq in coreqs:
                        coreqDept, coreqNum = prereq.split()
                        out.insert(
                            courseDept=course.subject,
                            courseNum=course.number,
                            id=i,
                            prereqDept=coreqDept,
                            prereqNum=coreqNum,
                            type='COREQ'
                        )                   
            except TypeError as e:
                print("Got TypeError! Check course: {} {}".format(course.subject, course.number))