from flaskquick import db,User
db.create_all()
one = User(username='tom',email='tom@yahoo.com')
two = User(username='jerry',email='jerry@yahoo.com')
db.session.add(one)
db.session.add(two)
db.session.commit()

print(User.query.all())
