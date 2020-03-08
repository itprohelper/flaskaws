from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('mysql+pymysql://<user>:<password>@<yourDB_hostservername>:3306/<yourDB>')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

#dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#Items for soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

Item1 = Item(user_id=1, name="Soccer cleats", description="Unleash The Speed In The Exclusive Initiator Pack. Think Fast. Play Explosive.",
                 category=category1)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1, name="Shinguards", description="Always Be Prepared For The Season With our Sporting Goods.",
                 category=category1)

session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Soccer Jersey", description="Just do it and win.",
                 category=category1)

session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Goalkeeper gloves", description="Don't let them score a single goal!",
                 category=category1)

session.add(Item4)
session.commit()
