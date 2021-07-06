from util.export import OutputCSV
from bs4 import BeautifulSoup

# Definitely not putting professor information here

with OutputCSV("professors.csv", [
    'lastname', 'firstname'
]) as out, open('./raw/professors.html', 'r') as profFile:
    out.write_header()
    soup = BeautifulSoup(profFile.read(), 'html.parser')
    for prof in soup.select("li a"):
        firstName, lastName = prof.text.split(', ')
        firstName = firstName.strip()
        lastName = lastName.strip()
        out.insert(
            firstname=firstName,
            lastname=lastName
        )