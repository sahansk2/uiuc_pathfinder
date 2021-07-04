from util.web import get_dept_url, get_dept_xml_tree
from util.export import OutputCSV
from util.sentence import split_into_sentences

def add_if_found(tag, st, soup):
    query = soup.find(tag, recursive=False)
    if query:
        st.update(split_into_sentences(query.text))

with OutputCSV('restrictions.csv', 
            ['crn', 'restriction']) as out, \
        open('data/deptCodes.txt', 'r') as codeFile:
    out.write_header()
    for dept in codeFile:
        dept = dept.strip()
        soup = get_dept_xml_tree(get_dept_url(dept))
        # I think half of these tags has the same/inherited data
        # but I don't really want to figure out what the relation is
        # It's easier to pipe through sort and uniq.
        for course in soup.select('cascadingCourse'):
            course_restrictions = set()
            add_if_found("sectionRegistrationNotes", course_restrictions, course)
            add_if_found("sectionApprovalCode", course_restrictions, course)
            for section in soup.find_all("detailedSection"):
                section_restrictions = set()
                crn = section['id']
                add_if_found("sectionCappArea", section_restrictions, section)
                add_if_found("specialApproval", section_restrictions, section)
                add_if_found("sectionNotes", section_restrictions, section)
                section_restrictions.update(course_restrictions)
                for restrict in section_restrictions:
                    out.insert(
                        crn=crn,
                        restriction=restrict
                    )
