from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship("Freebie", back_populates="company")

    def __repr__(self):
        return f'<Company {self.name}>'

    @property
    def devs(self):
        """Returns a collection of all devs who collected freebies from this company"""
        return list(set([freebie.dev for freebie in self.freebies]))

    def give_freebie(self, session, dev, item_name, value):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f'<Dev {self.name}>'

    @property
    def companies(self):
        """Returns a collection of all companies this dev has collected freebies from"""
        return list(set([freebie.company for freebie in self.freebies]))

    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    def give_away(self, session, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def __repr__(self):
        return f'<Freebie {self.item_name}, Value: {self.value}>'
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"