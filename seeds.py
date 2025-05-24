#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Freebie, Company

# database engine and session
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

#COMPANY
company1 = Company(name='Amazon', founding_year=1994)
company2 = Company(name='Google', founding_year=1998)

#DEV
dev1 = Dev(name='Gloria')
dev2 = Dev(name='Oscar')

#FREEBIES
freebie1 = Freebie(item_name='Sticker', value=5, dev=dev1, company=company1)
freebie2 = Freebie(item_name='T-shirt', value=20, dev=dev2, company=company2)

# Add to session and commit
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

print("Database created  successfully!")
