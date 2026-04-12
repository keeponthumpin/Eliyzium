from __future__ import annotations
from dataclasses import asdict, dataclass, fields


@dataclass
class Light:
	type:         str   = "generic_light"
	id:           int   = 0
	pos_x:        float = 0.0
	pos_y:        float = 0.0
	pos_z:        float = 0.0
	group:        int   = 1
	rotation:     float = 0.0
	ip_address:   str   = "255.255.255.255"
	dmx_address:  int   = 1
	universe:     int   = 1
	kx:           float = 0.0
	ky:           float = 0.0
	kz:           float = 0.0
	pan:          float = 0.0
	stand_type:   int   = 1
	cam_pan:      float = 0.0
	cam_h:        float = 0.0
	mode:         int   = 0
	zoom:         float = 0.25

	INT_FIELDS = {"id", "group", "dmx_address", "universe", "stand_type", "mode"}
	STR_FIELDS = {"type", "ip_address"}

	@classmethod
	def csv_fieldnames(cls) -> list:
		return [f.name for f in fields(cls)]

	@classmethod
	def from_csv_row(cls, row: dict):
		coerced = {}
		for f in cls.csv_fieldnames():
			raw = row.get(f, "").strip()
			if f in cls.STR_FIELDS:
				coerced[f] = raw if raw else cls.__dataclass_fields__[f].default
			elif f in cls.INT_FIELDS:
				coerced[f] = int(float(raw)) if raw else 0
			else:
				coerced[f] = float(raw) if raw else 0.0
		return cls(**coerced)

	def to_dict(self) -> dict:
		return asdict(self)
