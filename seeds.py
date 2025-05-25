

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Freebie, Company


engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

#COMPANY
company1 = Company(name='Amazon', founding_year=1994)
company2 = Company(name='Google', founding_year=1998)
company3 = Company(name='Andonya Innovations', founding_year=1998)

#DEV
dev1 = Dev(name='Gloria')
dev2 = Dev(name='Oscar')
dev3 = Dev(name='Emily')

#FREEBIES
freebie1 = Freebie(item_name='Sticker', value=5, dev=dev1, company=company1)
freebie2 = Freebie(item_name='T-shirt', value=20, dev=dev2, company=company2)

freebie3 = Freebie(item_name='Water Bottle', value=25, dev=dev3, company=company3)


session.add_all([company1, company2,company3, dev1, dev2,dev3, freebie1, freebie2,freebie3])
session.commit()

print("Database created  successfully!")
