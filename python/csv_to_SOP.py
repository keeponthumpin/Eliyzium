def setupParameters(scriptOp):
	return


def onPulse(par):
	return


def cook(scriptOp):
	scriptOp.clear()

	lights = parent.library.Show.val
	if not lights:
		return

	for light in lights:
		p = scriptOp.appendPoint()
		p.x = light.pos_x
		p.y = light.pos_y
		p.z = light.pos_z

	scriptOp.pointAttribs.create('rotation',    0.0)
	scriptOp.pointAttribs.create('kx',          0.0)
	scriptOp.pointAttribs.create('ky',          0.0)
	scriptOp.pointAttribs.create('kz',          0.0)
	scriptOp.pointAttribs.create('pan',         0.0)
	scriptOp.pointAttribs.create('cam_pan',     0.0)
	scriptOp.pointAttribs.create('cam_h',       0.0)
	scriptOp.pointAttribs.create('zoom',        0.0)
	scriptOp.pointAttribs.create('id',          0.0)
	scriptOp.pointAttribs.create('group',       0.0)
	scriptOp.pointAttribs.create('dmx_address', 0.0)
	scriptOp.pointAttribs.create('universe',    0.0)
	scriptOp.pointAttribs.create('stand_type',  0.0)
	scriptOp.pointAttribs.create('mode',        0.0)

	for i, light in enumerate(lights):
		p = scriptOp.points[i]

		p.rotation    = light.rotation
		p.kx          = light.kx
		p.ky          = light.ky
		p.kz          = light.kz
		p.pan         = light.pan
		p.cam_pan     = light.cam_pan
		p.cam_h       = light.cam_h
		p.zoom        = light.zoom

		p.id          = float(light.id)
		p.group       = float(light.group)
		p.dmx_address = float(light.dmx_address)
		p.universe    = float(light.universe)
		p.stand_type  = float(light.stand_type)
		p.mode        = float(light.mode)
