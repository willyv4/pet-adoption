from models import db, Pet

db.drop_all()
db.create_all()


p1 = Pet(name="Nilo", species='Cat',
         photo_url='https://th.bing.com/th/id/OIP.xGABHwSybkBzkbyvLTJeVgHaE8?w=272&h=181&c=7&r=0&o=5&dpr=2&pid=1.7', age="2", notes="Nilo is the best cat ever his love runs deep and so do his nipples", available=False)
p2 = Pet(name="Drake", species='Dog',
         photo_url='https://th.bing.com/th?id=OIP.vpENuVG6_Ke79c0shGAHMQHaFn&w=287&h=217&c=8&rs=1&qlt=90&o=6&dpr=2&pid=3.1&rm=2', age="5", notes="Drake", available=True)
p3 = Pet(name="falco", species='bird', age="1", available=True)

db.session.add_all([p1, p2, p3])
db.session.commit()
