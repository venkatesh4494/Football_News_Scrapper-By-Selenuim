from pathlib import Path
Path.cwd()
import os
os.chdir("/Users/venky/Desktop/udemy")
from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd
from faker import Faker

doc = DocxTemplate("/Users/venky/Desktop/udemy/template-my-info (1).docx")
my_name = "venky"
my_phone = "8892329494"
my_email = "venkyarya004@gmail.com"
my_address = "via cefalu"
today_date = datetime.today().strftime("%d %b, %Y")
context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
           'today_date': today_date}
doc.render(context)
doc.save("New_doc.docx")


fake=Faker()
profile=[fake.profile() for i in range(10)]
df=pd.DataFrame(profile)
df = df[['name', 'mail', 'address', 'job', 'company']]
numbers=[fake.phone_number() for i in range(10)]
df['phone_number']=numbers
df.rename(columns={'mail': 'email'}, inplace=True)
df.to_csv('fake_data.csv', index=False)


doc = DocxTemplate("/Users/venky/Desktop/udemy/template-manager-info.docx")
my_name = "venky"
my_phone = "8892329494"
my_email = "venkyarya004@gmail.com"
my_address = "via cefalu"
today_date = datetime.today().strftime("%d %b, %Y")
mycontext = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
           'today_date': today_date}
for idx,row in df.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone_number': row['phone_number'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']}

    context.update(mycontext)
    doc.render(context)
    doc.save(f"generated_doc_{idx}.docx")

a=0