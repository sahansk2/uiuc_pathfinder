import unittest
import re

course_match = re.compile(r"See (\w{2}|\w{3}|\w{4}) (\d{3})\.")

def extract_crosslist_from_description(description: str):
    """
    Input: description as string
    Output: (course_code, course_number) if crosslisted, else return None
    """
    res = course_match.search(description)
    if res:
        return res.group(1, 2)
    else:
        return None
