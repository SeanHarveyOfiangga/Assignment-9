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

resume.set_font('Times', '', 15)
resume.set_text_color(0,0,0)
resume.cell(0, 35,"                          Complete Name       : " + str(ResumeInfo["FullName"]), align='L', ln=True)
resume.cell(0, -20,"                          Age                          : " + str(ResumeInfo["Age"]), align='L', ln=True)
resume.cell(0, 35,"                          Gender                     : " + str(ResumeInfo["Gender"]), align='L', ln=True)
resume.line(50, 61, 210, 61)

resume.set_font('Helvetica', 'B', 18)
resume.cell(0, -5, "EDUCATIONAL ATTAINMENT",  align='L', ln=True)
resume.set_font('courier', '', 13)
resume.cell(0, 23,"Primary Education       : " + str(ResumeInfo["PrimarySchool"]), align='L', ln=True)
resume.cell(0, -10,"Secondary Education     : " + str(ResumeInfo["SecondarySchool"]), align='L', ln=True)
resume.cell(0, 23,"Tertiary Education      : " + str(ResumeInfo["TertiarySchool"]), align='L', ln=True)
resume.cell(0, -10,"College Education       : " + str(ResumeInfo["CollegeUniv"]), align='L', ln=True)
resume.line(10, 105, 210, 105)

resume.set_font('Helvetica', 'B', 18)
resume.cell(0, 40, "ACHIEVEMENTS",  align='L', ln=True)
resume.set_font('courier', '', 13)
resume.cell(0, -21,"A. " + str(ResumeInfo["Achievement1"]), align='L', ln=True)
resume.cell(0, 35,"B. " + str(ResumeInfo["Achievement2"]), align='L', ln=True)
resume.cell(0, -21,"C. " + str(ResumeInfo["Achievement3"]), align='L', ln=True)
resume.cell(0, 35,"D. " + str(ResumeInfo["Achievement4"]), align='L', ln=True)
resume.cell(0, -21,"E. " + str(ResumeInfo["Achievement5"]), align='L', ln=True)
resume.line(10, 156, 210, 156)

resume.set_font('Helvetica', 'B', 18)
resume.cell(0, 50, "SKILLS",  align='L', ln=True)
resume.set_font('courier', '', 13)
resume.cell(0, -30,"A. " + str(ResumeInfo["Skills1"]), align='L', ln=True)
resume.cell(0, 45,"B. " + str(ResumeInfo["Skills2"]), align='L', ln=True)
resume.cell(0, -30,"C. " + str(ResumeInfo["Skills3"]), align='L', ln=True)
resume.cell(0, 45,"D. " + str(ResumeInfo["Skills4"]), align='L', ln=True)
resume.cell(0, -30,"E. " + str(ResumeInfo["Skills5"]), align='L', ln=True)
resume.cell(0, 45,"F. " + str(ResumeInfo["Skills6"]), align='L', ln=True)
resume.line(10, 218, 210, 218)

resume.set_font('Helvetica', 'B', 18)
resume.cell(0, -15, "CONTACT",  align='L', ln=True)
resume.set_font('courier', '', 13)
resume.cell(0, 30,"Email : " + str(ResumeInfo["email"]), align='L', ln=True)
resume.cell(0, -19,"Cellphone Number : " + str(ResumeInfo["PhoneNum"]), align='L', ln=True)
resume.cell(0, 30,"Address : " + str(ResumeInfo["address"]), align='L', ln=True)

