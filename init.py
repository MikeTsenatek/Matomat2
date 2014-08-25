#!/usr/bin/env python3
import database as db
import authentication as a
from config import dbengine

s=db.create_sessionmaker(dbengine)()
a.create_user(s,'admin','admin',None)
s.add(db.Item(name='Mate',price='100'))
s.add(db.Item(name='Bier',price='150'))
s.commit()
