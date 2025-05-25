

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    amazon = session.query(Company).filter_by(name='Amazon').first()
    google = session.query(Company).filter_by(name='Google').first()
    gloria = session.query(Dev).filter_by(name='Gloria').first()
    oscar = session.query(Dev).filter_by(name='Oscar').first()

    print("=== INITIAL DATA ===")
    print(f"Companies: {amazon.name}, {google.name}")
    print(f"Developers: {gloria.name}, {oscar.name}")
    print()

    print("=== TESTING RELATIONSHIPS ===")
    print(f"Gloria's freebies: {[f.item_name for f in gloria.freebies]}")
    print(f"Oscar's freebies: {[f.item_name for f in oscar.freebies]}")
    print(f"Amazon's freebies: {[f.item_name for f in amazon.freebies]}")
    print(f"Google's freebies: {[f.item_name for f in google.freebies]}")
    print()

    print("=== TESTING NEW PROPERTIES ===")
    print(f"Amazon's devs: {[dev.name for dev in amazon.devs]}")
    print(f"Google's devs: {[dev.name for dev in google.devs]}")
    print(f"Gloria's companies: {[company.name for company in gloria.companies]}")
    print(f"Oscar's companies: {[company.name for company in oscar.companies]}")
    print()

    print("=== TESTING GIVE_FREEBIE ===")
    amazon.give_freebie(session, gloria, "Mug", 15)
    google.give_freebie(session, oscar, "Water Bottle", 25)
    amazon.give_freebie(session, oscar, "Laptop Bag", 50)
    
    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie.print_details())
    print()

    print("=== TESTING OLDEST_COMPANY ===")
    oldest = Company.oldest_company(session)
    print(f"Oldest company: {oldest.name} ({oldest.founding_year})")
    print()

    print("=== TESTING RECEIVED_ONE ===")
    print(f"Gloria has Mug: {gloria.received_one('Mug')}")
    print(f"Oscar has Sticker: {oscar.received_one('Sticker')}")
    print(f"Oscar has Laptop Bag: {oscar.received_one('Laptop Bag')}")
    print()

    print("=== TESTING GIVE_AWAY ===")
    mug_freebie = session.query(Freebie).filter_by(item_name='Mug').first()
    print(f"Before: {mug_freebie.print_details()}")
    gloria.give_away(session, oscar, mug_freebie)
    session.refresh(mug_freebie)
    print(f"After: {mug_freebie.print_details()}")
    print()

    print("=== FINAL RELATIONSHIPS ===")
    print(f"Gloria's freebies: {[f.item_name for f in gloria.freebies]}")
    print(f"Oscar's freebies: {[f.item_name for f in oscar.freebies]}")
    print(f"Amazon's devs: {[dev.name for dev in amazon.devs]}")
    print(f"Oscar's companies: {[company.name for company in oscar.companies]}")

    session.close()