import requests
import json
import math
import numpy as np
import pandas as pd

class RateMyProfScraper:
        def __init__(self,schoolid):
            self.UniversityId = schoolid
            self.numProfs = 0
            self.professorlist = self.createprofessorlist()
            self.indexnumber = False
            self.prof_names = self.GetProfessorNames()
                    
        def createprofessorlist(self):#creates List object that include basic information on all Professors from the IDed University
            tempprofessorlist = []
            num_of_prof = self.GetNumOfProfessors(self.UniversityId)
            self.numProfs = num_of_prof
            num_of_pages = math.ceil(num_of_prof / 20)
            i = 1
            while (i <= num_of_pages):# the loop insert all professor into list
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    self.UniversityId))
                temp_jsonpage = json.loads(page.content)
                temp_list = temp_jsonpage['professors']
                tempprofessorlist.extend(temp_list)
                i += 1
            return tempprofessorlist

        def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page
            temp_jsonpage = json.loads(page.content)
            num_of_prof = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            return num_of_prof

        def SearchProfessor(self, ProfessorName):
            self.indexnumber = self.GetProfessorIndex(ProfessorName)
            self.PrintProfessorInfo()
            return self.indexnumber

        def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def PrintProfessorInfo(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
            else:
                print(self.professorlist[self.indexnumber])

        def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
                return "error"
            else:
                #print(self.professorlist[self.indexnumber][key])
                return self.professorlist[self.indexnumber][key]
        def GetProfessorNames(self):
            names = []
            for dict in self.professorlist:
                if dict['tMiddlename'] == '':
                    name = dict['tFname'] + ' ' + dict['tLname']
                else:
                    name = dict['tFname'] + ' ' + dict['tMiddlename'] + ' '+ dict['tLname']
                
                names.append(name)
                
            return names
                    
            

def ratings_to_csv(lis, scraper):
    num_of_profs = len(lis)
    blank = np.zeros(num_of_profs)
    df = pd.DataFrame(data = blank, columns= ['Rating'], index= lis)
    
    print(df)
    
    for name in lis:
        scraper.SearchProfessor(name)
        rating = scraper.PrintProfessorDetail('overall_rating')
        df.loc[name]['Rating'] = rating

    df.to_csv('prof_ratings.csv')

uiucProfRatings = RateMyProfScraper(1112)
profs = uiucProfRatings.prof_names
ratings_to_csv(profs, uiucProfRatings)