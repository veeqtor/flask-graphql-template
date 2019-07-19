"""User schema"""

# third party imports
import graphene
from graphql import GraphQLError
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# local imports
from database.models import User
from src.input_object_type.user_input import CreateUserInput


class UserObjectType(SQLAlchemyObjectType):
	"""
	User schema object
	"""

	class Meta:
		"""Meta class"""

		model = User
		interfaces = (graphene.relay.Node,)


class CreateUser(graphene.Mutation):
	"""
	Mutation class for creating users.
	"""
	
	user = graphene.Field(UserObjectType)
	
	class Arguments:
		"""
		Argument class
		"""
		
		data = CreateUserInput(required=True)
	
	def mutate(self, info, data):
		"""
		Mutate method.
		"""
		
		user = User.query.filter_by(username=data['email']).first()
	
		if user:
			raise GraphQLError('User already Exist.')
		
		new_user = User(**data).save()
	
		return CreateUser(user=new_user)


class Mutation(graphene.ObjectType):
	"""
	Mutation class
	"""
	
	create_user = CreateUser.Field()


class Query(graphene.ObjectType):
	"""
	Query class
	"""

	node = graphene.relay.Node.Field()
	all_users = SQLAlchemyConnectionField(UserObjectType)
