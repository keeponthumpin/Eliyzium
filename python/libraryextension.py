from light import Light
import csv


class libraryextension:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.Show = tdu.Dependency([])

		if self.ownerComp.par.Showfilepath.val:
			self.LoadShow()

	def LoadShow(self):
		path = self.ownerComp.par.Showfilepath.eval()
		if not path:
			debug("[ShowManager] No ShowFilePath set.")
			return

		try:
			lights = []
			with open(path, newline="") as fh:
				for row in csv.DictReader(fh):
					lights.append(Light.from_csv_row(row))

			self.Show.val = lights
			debug(f"[ShowManager] Loaded {len(lights)} lights from: {path}")

		except FileNotFoundError:
			debug(f"[ShowManager] File not found: {path}")
		except Exception as e:
			debug(f"[ShowManager] Error loading show: {e}")

	def GetLight(self, light_id: int):
		for light in self.Show.val:
			if light.id == light_id:
				return light
		return None

	def GetGroup(self, group: int) -> list:
		return [l for l in self.Show.val if l.group == group]

	def GetUniverse(self, universe: int) -> list:
		return [l for l in self.Show.val if l.universe == universe]

	def LightCount(self) -> int:
		return len(self.Show.val)

	@property
	def FixturesPoints(self) -> nullPOP:
		return self.ownerComp.op('null_show_points')
