#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f'''mysql+mysqldb://{argv[1]}:{argv[2]}@
            localhost/{argv[3]}''',
                           pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)
    results = session.query(State).all()
    for st in results:
        print(f'{st.id}: {st.name}')
