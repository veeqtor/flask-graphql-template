"""Base schema"""

# third party imports
import graphene

# local imports
from src.schemas import user


class Mutation(user.Mutation):
	"""
	Mutation class
	"""

	pass


class Query(user.Query):
	"""
	Query class
	"""

	pass


schema = graphene.Schema(query=Query, mutation=Mutation)
