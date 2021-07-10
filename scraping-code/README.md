## scrape_crosslists.py 

Run scraper with `python3 ./scrape_crosslists.py`.

### Error Log

Basically we need to check these courses/departments ourselves for crosslisted courses (where it says "See CC ###.", specifically)

```
Couldn't get information about department ARTJ! Skipping...
Got TypeError! Check course: BSE 585
Got TypeError! Check course: CIC 390
Got TypeError! Check course: CWL 593
Couldn't get information about department DTX! Skipping...
Got TypeError! Check course: FIN 432
Couldn't get information about department RSOC! Skipping...
Got TypeError! Check course: STAT 587
Couldn't get information about department ZULU! Skipping...
```

## scrape_restrictions.py tips

You need `nltk` for this.

In the Python interactive console, run 

```py
import nltk
nltk.download()
```

And download the "popular" package. This is so that you can split the restrictions up into individual sentences.

Run the scraper with `python3 ./scrape_restrictions.py`. 

Because there are duplicates, run this: 

```sh
sort ./restrictions.csv | uniq > restrictions2.csv
```

## Extracting GPAs from util/uiuc_classes_bot_data/2021-sp.csv

Download [q](https://harelba.github.io/q/).

Then, run

```sh
q -H -d , "SELECT Subject,Number, GPA from ./util/uiuc_classes_bot_data/2021-sp.csv GROUP BY Subject,Number, GPA" > out.csv
```


## Combining GPA and Course Info for importing into MySQL

```sh
q -H -d ',' "SELECT courseDept, courseNum, GPA, title FROM ./classDeptNumGPA.csv NATURAL JOIN ./courseInfo.csv infofile" > test
```

## Getting existing professors listed in crns

```sh
q -H -d ',' "SELECT instructorFirstName, instructorLastName from ./crn_info.csv WHERE instructorFirstName IS NOT NULL GROUP BY instructorFirstName, instructorLastName" | sort > crnProfs.csv
```

## Creating requirement groups from prereqs.csv

```sh
q -H -d ',' "SELECT DISTINCT courseDept, courseNum, id, type FROM ./prereqs.csv" > requirementGroups.csv
```

## Scraping interests from the ECE subdisciplines site using tampermonkey

1. Install tampermonkey
1. Install the tampermonkey extension here (ends with .zip)
1. Enable it and visit each subdiscipline in https://ece.illinois.edu/academics/ugrad/subdisciplines
