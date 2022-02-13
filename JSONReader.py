#Assignment 9

#PDF Resume Creator
#	- Create a python program that will create your personal resume in PDF format
#	- All personal details are stored in a JSON file
#	- Your program should read the JSON file and write the details in the PDF
#	- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
#	- Search for available PDF library that you can use
#	- Search how data is structured using JSON format
#	- Search how to read JSON file
#	- You will create the JSON file manually
#	- Your code should be in github before Feb12

import json
from turtle import width
from fpdf import FPDF

resumeVar = "ResumeInfo.json"
with open(resumeVar, "r") as JSONFile:
    ResumeInfo = json.loads(JSONFile.read())

name = ResumeInfo["FullName"]
age = ResumeInfo["Age"]
gender = ResumeInfo["Gender"]
school1 = ResumeInfo["PrimarySchool"]
school2 = ResumeInfo["SecondarySchool"]
school3 = ResumeInfo["TertiarySchool"]
school4 = ResumeInfo["CollegeUniv"]
achievement1 = ResumeInfo["Achievement1"]
achievement2 = ResumeInfo["Achievement2"]
achievement3 = ResumeInfo["Achievement3"]
achievement4 = ResumeInfo["Achievement4"]
achievement5 = ResumeInfo["Achievement5"]

















