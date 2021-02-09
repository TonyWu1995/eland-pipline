from sqlalchemy import create_engine, Integer, String, Column, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin:admin@localhost:3306/id_mapping_db")
connect = engine.connect()

base = declarative_base()


class Member(base):
    __tablename__ = 'aggregate_table'

    column_not_exist_in_db = Column(Integer, primary_key=True)

    uuid = Column(String(255), index=True)
    ctid = Column(String(255), index=True)


base.metadata.create_all(engine)
member = Member(uuid='1', ctid="ac")
Session = sessionmaker(bind=engine)
session = Session()
session.add(member)
session.commit()
input = ("2", "1")
s = text(
    "select uuid, GROUP_CONCAT(DISTINCT ctid SEPARATOR ',') from aggregate_table where uuid in {} group by uuid".format(
        input))
print(s)
r = [row for row in session.execute(s)]
print(r)
