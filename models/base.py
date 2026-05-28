"""Base model with common attributes and serialization helpers."""

from datetime import datetime
import uuid


class BaseModel:
	"""Provide shared attributes for stored models."""

	def __init__(self, *args, **kwargs):
		"""Create a new base model or rebuild one from serialized data."""

		if kwargs:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					try:
						parsed_value = datetime.strptime(
							value, "%Y-%m-%d %H:%M:%S")
					except ValueError:
						parsed_value = datetime.strptime(
							value, "%Y-%m-%d %H:%M:%S.%f")
					setattr(
						self,
						key,
						parsed_value)
				elif key != "__class__":
					setattr(self, key, value)
		else:
			now = datetime.utcnow()
			self.id = str(uuid.uuid4())
			self.created_at = now
			self.updated_at = now

	def __str__(self):
		"""Return a readable string representation of the instance."""

		return "[{}] ({}) {}".format(
			self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""Update the timestamp and persist the object."""

		self.updated_at = datetime.utcnow()
		from models.engine.file_storage import storage

		storage.new(self)
		storage.save()

	def to_dict(self):
		"""Serialize the instance into a dictionary."""

		data = dict(self.__dict__)
		data["__class__"] = self.__class__.__name__
		if "created_at" in data and isinstance(data["created_at"], datetime):
			data["created_at"] = data["created_at"].strftime(
				"%Y-%m-%d %H:%M:%S")
		if "updated_at" in data and isinstance(data["updated_at"], datetime):
			data["updated_at"] = data["updated_at"].strftime(
				"%Y-%m-%d %H:%M:%S")
		return data
