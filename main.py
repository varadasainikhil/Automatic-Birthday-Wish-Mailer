import datetime as dt
import smtplib
import pandas as pd
import random


sender_mail = "insertyourmail"
sender_password = "insert your emails app password"
# To know how to generate app password for you mail use this link - https://www.hikvision.com/content/dam/hikvision/en/support/download/how-to/nvr/How%20to%20enable%20the%20App%20password%20in%20Gmail.pdf

current_time_date = dt.datetime.now()
current_month = current_time_date.month
current_day = current_time_date.day
# Creating a dataframe
df = pd.read_csv("birthdays.csv")
data_dict = df.to_dict()  # Converting Dataframe into Dictionary

for i in range(len(data_dict["month"])):
    if current_day == data_dict["day"][i] and current_month == data_dict["month"][i]:
        receiver_name = data_dict['name'][i]
        receiver_mail = data_dict['email'][i]
        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as file:
            final_letter = file.read()
            final_letter = final_letter.replace("[NAME]", receiver_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=sender_mail, password=sender_password)
            connect.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=f"Subject:HAPPY BIRTHDAY\n\n{final_letter}")


