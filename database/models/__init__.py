"""Models"""
# third party imports
from sqlalchemy import event

# local imports
from utils.firebase_push_id import PushID
from database.models.user import User


def firebase_id(mapper, connection, target):
	"""
	Generates a firebase fancy unique Id.

		Args:
			mapper (obj): The current model class
			connection (obj): The current database connection
			target (obj): The current model instance
	Returns:
		None
	"""
	push_id = PushID()
	target.id = push_id.next_id()


tables = [
	User,
]

for table in tables:
	event.listen(table, 'before_insert', firebase_id)
