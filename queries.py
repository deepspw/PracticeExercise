# Queries for a sqlalchemy practice exercise
# https://github.com/pgpnda
# Import me! functions are printNames(), printOlder(), printWeights(), printShelters


from sqlalchemy import create_engine, and_, asc, desc, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from database_setup import Base, Puppy, Shelter
# Various imports for querieing an sql session with sqlalchemy

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


nameAsc = session.query(Puppy).group_by(Puppy.name).order_by(asc(Puppy.name))

sixOlder = session.query(Puppy).filter(and_(Puppy.dateOfBirth > '2015-01-16'))

weightAsc = session.query(Puppy).order_by(asc(Puppy.weight))

oldshelterGroup = session.query(Puppy).add_columns(Puppy.name, Puppy.shelter_id,\
    Puppy.id).group_by(Puppy.shelter_id)

maxName = session.query(Puppy).add_columns(Puppy.name,func.char_length\
    (Puppy.name) ).group_by(Puppy.name).order_by(desc(func.char_length(Puppy.name)))

shelterGroup = session.query(Shelter, Puppy).\
    join(Puppy).\
    filter(Shelter.id == Puppy.shelter_id).\
    group_by(Puppy.shelter_id).\
    values(Shelter.id, Puppy.name)

reverseGroup = session.query(Puppy, Shelter).\
    join(Shelter).\
    filter(Puppy.shelter_id == Shelter.id).\
    group_by(Shelter.id).\
    values(Shelter.id, Puppy.name)
    
def printNames():
    print "Name Ascending"
    print 'Name'+ ' ' * ((maxName.first()[2])-4) + '|' + "Id"
    for pup in nameAsc:
        print pup.name + ((' ' * (maxName.first()[2] - len(pup.name))) +'| ' +\
        str(pup.id))

def printOlder():
    print "Six months or older"
    for pup in sixOlder:
        print pup.name
        print pup.id
        print pup.dateOfBirth
        print '\n'

def printWeights():
    print "Puppy weight ascending"
    for pup in weightAsc:
        print pup.name + str(pup.weight)
        print '\n'

def printShelters():
    print "Puppies grouped by shelter_id"

    for pup in shelterGroup:
        print pup.name
        print pup.id

