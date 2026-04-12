from TDStoreTools import StorageManager
import TDFunctions as TDF


class elysiumextension:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

	@property
	def FixtureLibrary(self):
		return self.ownerComp.op('fixture_library')

	@property
	def AudioInput(self):
		return self.ownerComp.op('audio_input')

	@property
	def AudioAnalyzer(self):
		return self.ownerComp.op('audio_analyzer')

	@property
	def PatternLibrary(self):
		return self.ownerComp.op('pattern_library')

	@property
	def Preview(self):
		return self.ownerComp.op('preview')

	@property
	def Gui(self):
		return self.ownerComp.op('gui')

	@property
	def Animator(self):
		return self.ownerComp.op('animator')
