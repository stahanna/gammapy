# read date (today)
# create subdirectory YEAR-MONTH-DAY
# inside the subdirectory create a README.md file using a template
import os
current_directory = os.getcwd()
from datetime import datetime, timedelta
today = str(datetime.today().strftime('%Y-%m-%d'))
time_now = str(datetime.today().strftime('%d/%m/%Y, %H:%M:%S'))
today_long = str(datetime.today().strftime('%A, %B %d, %Y'))
today_report = os.path.join(current_directory, "dev-meetings", today)
print(today_report)
isExist = os.path.exists(today_report)
print(isExist)
title =  f'# Gammapy Developer Meeting \n'
report_heading = f' * {today_long}, at 2 pm (CET) \n ' \
         '* Gammapy Developer Meeting on Zoom (direct link on Slack) \n' \
         '# Agenda\n'

report_footer = f'report created at {time_now}'


#***************** connecting to the repository of gammapy***************
from github import Github
gh = Github('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')#(token='token path')
gh.get_repo("gammapy/gammapy")
repo_gammapy = gh.get_repo("gammapy/gammapy")

#***************** getting pulls**********************
gammapy_pulls_all = repo_gammapy.get_pulls('open')
gammapy_pulls_all_closed = repo_gammapy.get_pulls('closed')
gammapy_pulls_count = gammapy_pulls_all.totalCount
print(f'gammapy pulls count: {gammapy_pulls_count}')
pulls_page1 = gammapy_pulls_all.get_page(0)
page1_length = len(pulls_page1)
print(f'page1 length {page1_length }')

#*************** one week long **********************
d = datetime.today() - timedelta(days=8)
print(f'd :  {d} type d {type(d)}')

pulls_text ='### PRs opened last week (younger than 8 days) \n'

for i in pulls_page1: #gammapy_pulls_all :#
    if i.created_at > d:
        #print(f'PR #{i.number} - {i.title} - was created at {i.created_at} by {i.user}')
        pulls_text = pulls_text + f'[#{i.number}] ({i.issue_url}) {i.title} - {i.user.name}  \n'  #{i.created_at}


for i in gammapy_pulls_all_closed.get_page(0):
    if i.created_at > d:
        print(f'merged {i}')



issues = f'### issues opened last week: \n' \
      f''

report = title + report_heading + pulls_text + issues + report_footer


if not isExist:
   os.makedirs(today_report)
   print("The new directory is created!")

#not in the if loop so MAJ is possible
today_report_md = os.path.join(today_report, "README.md")
f = open(today_report_md, "w")
f.write(report)

import markdown
markdown_string = '# Hello World'
markdown_string = markdown_string + ' cos tam cos'
markdown_string = pulls_text
# 3
html_string = markdown.markdown(report)

template = "dev/dev-meetings/TEMPLATE_README.md"


if __name__ == "__main__":
    print(html_string)