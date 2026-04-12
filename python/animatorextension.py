import TDFunctions as TDF


class animatorextension:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

	@property
	def MappedOutput(self) -> nullPOP:
		return self.ownerComp.op('null_mapped_output')
