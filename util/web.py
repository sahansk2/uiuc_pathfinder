import re
from urllib.parse import urlunsplit, urlencode
import requests
from bs4 import BeautifulSoup

dept_re = re.compile(r'([A-Z]{4}|[A-Z]{3}|[A-Z]{2})')
course_re = re.compile(r'(\d{3})')

def get_dept_url(dept, mode):
    if not dept_re.match(dept):
        raise TypeError("Invalid format for department")
    
    path = f'/cisapp/explorer/schedule/2021/fall/{dept}.xml'
    return urlunsplit((
        'https',
        'courses.illinois.edu',
        path,
        urlencode(dict(mode=mode)),
        ''
    ))

def get_xml_tree(url) -> BeautifulSoup:
    print(f"Fetching XML from {url}")
    r = requests.get(url)
    print("Got XML!")
    return BeautifulSoup(r.text, 'xml')
