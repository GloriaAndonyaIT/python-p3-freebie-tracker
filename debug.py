#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    # Set up the engine and session
    engine = create_engine('sqlite:///app.db')

    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Get a sample freebie
    sample_freebies = session.query(Freebie).all()

if sample_freebies:
    for freebie in sample_freebies:
        print(freebie.print_details())
else:
    print("No freebies found in the database.")

