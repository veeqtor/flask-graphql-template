"""Module for User input"""

# system imports
import graphene


class CreateUserInput(graphene.InputObjectType):
	"""
	Input objects
	"""
	
	email = graphene.String(required=True, description="Email")
	username = graphene.String(required=True, description="Username")
	password = graphene.String(required=True, description="User password")
