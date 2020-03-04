from py2neo import Graph, Node, Relationship
from py2neo.ogm import GraphObject, RelatedFrom, Property, RelatedTo, Related

db = Graph("bolt://localhost:7687", user="neo4j", password="test")


class Event(GraphObject):
    __primarykey__ = 'name'

    name = Property()

    participants = RelatedFrom("Person", "PARTICIPATED")


class Person(GraphObject):
    __primarykey__ = 'name'

    name = Property()

    participated = Related(Event)
"""
db.delete_all()
tx = db.begin()

meetup = Event()
meetup.name = "Meetup"
conf = Event()
conf.name = "Conference"
db.create(meetup)
db.create(conf)

p = Person()
p.name = "qwe Иванов"
try:
    db.pull(p)
except:
    db.push(p)
p.participated.add(conf)
db.push(p)
print(p, list(p.participated))

print()


q = Person()
q.name = "qwe Иванов"
db.pull(q)
print(q, list(q.participated))
q.participated.add(meetup)

print(q, list(q.participated))
db.push(q)
print(q == p)

tx.commit()
"""

import pandas as pd
df = pd.DataFrame(columns=["a", "b"])
new = pd.DataFrame([[1,2]]                   , columns = ["a", "b"])
print(new)
df = df.append(new)
print()

print(df)
