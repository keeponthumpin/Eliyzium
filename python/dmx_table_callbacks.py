fixture_library = parent.elysium.FixtureLibrary


def onSetupParameters(scriptOp: scriptDAT):
	return


def onPulse(par: Par):
	return


def onCook(scriptOp: scriptDAT):
	scriptOp.clear()
	scriptOp.appendRow(['primindex', 'net', 'subnet', 'universe', 'channel', 'netaddress'])

	for light in fixture_library.Show.val:
		u      = max(0, light.universe - 1)
		net    = u // 256
		subnet = (u % 256) // 16

		scriptOp.appendRow([
			light.id,
			net,
			subnet,
			light.universe,
			light.dmx_address,
			light.ip_address,
		])


def onGetCookLevel(scriptOp: scriptDAT) -> CookLevel:
	return CookLevel.AUTOMATIC
