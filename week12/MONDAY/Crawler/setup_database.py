import sqlalchemy
from database import Database
from models import Url
from datetime import datetime


def setup_database():
	db = Database()
	db.create()
	# url_def = Url()
	# url_def.content = 'https://facebook.com'
	# try:
	# 	db.session.add(url_def)
	# 	url_def.content = 'https://abv.bg/'
	# 	url_def.visited = datetime.now()
	# 	db.session.add(url_def)
	# except Exception as e:
	# 	print(str(e))
	db.session.commit()
	db.session.close()


if __name__ == '__main__':
	setup_database()
