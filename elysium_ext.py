from TDStoreTools import StorageManager
import TDFunctions as TDF


class ElysiumExtension:
	"""
	Main patch extension for Elysium.
	Provides promoted references to all vital sub-components.

	Access from anywhere inside the component:
		ext.ElysiumExtension.FixtureLibrary
		ext.ElysiumExtension.AudioInput
		... etc.

	Or externally if promoted:
		op('elysium').FixtureLibrary
	"""

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

	# ------------------------------------------------------------------
	# Sub-component references (promoted = capitalized)
	# ------------------------------------------------------------------

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

	# ------------------------------------------------------------------
	# Lifecycle
	# ------------------------------------------------------------------

	# def onInitTD(self):
	# 	pass

	# def onDestroyTD(self):
	# 	pass
