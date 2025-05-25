#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    # Set up the engine and session
    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # OPTIONAL: Uncomment the line below if you need to create tables the first time
    # Base.metadata.create_all(engine)

    # Retrieve companies and devs
    amazon = session.query(Company).filter_by(name='Amazon').first()
    google = session.query(Company).filter_by(name='Google').first()
    gloria = session.query(Dev).filter_by(name='Gloria').first()
    oscar = session.query(Dev).filter_by(name='Oscar').first()

    # Test: give_freebie
    print("\n--- Testing give_freebie ---")
    amazon.give_freebie(session, gloria, "Mug", 15)
    google.give_freebie(session, oscar, "Water Bottle", 25)

    # Check all freebies
    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie.print_details())

    # Test: oldest_company
    print("\n--- Testing oldest_company ---")
    oldest = Company.oldest_company(session)
    print(f"The oldest company is {oldest.name}, founded in {oldest.founding_year}")

    # Test: received_one
    print("\n--- Testing received_one ---")
    has_mug = gloria.received_one("Mug")
    print(f"Gloria has a Mug? {'Yes' if has_mug else 'No'}")
    has_sticker = oscar.received_one("Sticker")
    print(f"Oscar has a Sticker? {'Yes' if has_sticker else 'No'}")

    # Test: give_away
    print("\n--- Testing give_away ---")
    mug_freebie = session.query(Freebie).filter_by(item_name='Mug').first()
    print(f"Before give_away: {mug_freebie.print_details()}")
    gloria.give_away(session, oscar, mug_freebie)
    session.refresh(mug_freebie)  # refresh from DB to see updated relationship
    print(f"After give_away: {mug_freebie.print_details()}")
