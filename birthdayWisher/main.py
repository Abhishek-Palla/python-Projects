##################### Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

from monday import connection

data = pandas.read_csv('birthdays.csv')
birthdays_dict = data.to_dict(orient='records')
# {'name': 'Test', 'email': 'test@email.com', 'year': 1961, 'month': 12, 'day': 21}


now = dt.datetime.now()
day = now.day
month = now.month
letter_content =""
txt_files = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
for i in range(len(birthdays_dict)):
    if (day,month) == (birthdays_dict[i]['day'],birthdays_dict[i]['month']):
        with open(random.choice(txt_files), 'r') as txt:
            letter_content = txt.read()
        letter_content = letter_content.replace("[NAME]", birthdays_dict[i]['name'] )
        print(letter_content)




my_email = "pallaa15@gmail.com"
password = "GET YOUR OWN PASSWORD"


connection =smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="pallaabhi45@gmail.com",msg=f"Subject: Birthday wish\n\n"
                                                                            f"{letter_content}")



