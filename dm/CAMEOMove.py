
class Move_Object:
	def __init__(self, code, move_name, move_type, IO_list,
				ph, low_resources, med_resources,
				high_resources, infrastructure):
		self.code = code
		self.move_name = move_name
		self.move_type = move_type
		self.IO = IO_list
		self.ph = ph
		self.resources = {"low": low_resources, 
						  "med": med_resources,
				          "high": high_resources}
		self.infrastructure = infrastructure
		self.probability = -1 #unassigned
		self.risk = -1 #unassigned
		self.one_hot = [] #a one hot vector representation of teh resources

	"""
	Getter functions
	"""
	def get_IO(self):
		return self.IO

	def get_code(self):
		return self.code

	def get_move_name(self):
		return self.move_name

	def get_move_type(self):
		return self.move_type

	def get_resources(self):
		return self.resources

	def get_infrastructure(self):
		return self.infrastructure

	def to_dic(self):
		move_dic = {"code": self.code,
					"IO": self.IO, 
					"move_name": self.move_name,
					"move_type": self.move_type, 
					"ph": self.ph, 
					"resources": self.resources,  
					"infrastructure": self.infrastructure}
		return move_dic