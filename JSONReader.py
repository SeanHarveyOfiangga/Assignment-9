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
skill1 = ResumeInfo["Skills1"]
skill2 = ResumeInfo["Skills2"]
skill3 = ResumeInfo["Skills3"]
skill4 = ResumeInfo["Skills4"]
skill5 = ResumeInfo["Skills5"]
skill6 = ResumeInfo["Skills6"]
skill7 = ResumeInfo["Skills7"]
number = ResumeInfo["PhoneNum"]
email = ResumeInfo["email"]
address = ResumeInfo["address"]

resume = FPDF('P', 'mm', 'Letter')
resume.add_page()
resume.image('ResumeBG.JPG', x = -0.5, y= -0.5, w = resume.w + 1)
resume.image('Pic.JPG', 10, 13, 40, 0)

resume.set_font('Helvetica', 'B', 30)
resume.set_text_color(0,0,0)
resume.set_margins(top=20, left=20, right=20)
resume.cell(0, 0, "PERSONAL RESUME",  align='C', ln=True)
resume.line(55, 30, 210, 30)











