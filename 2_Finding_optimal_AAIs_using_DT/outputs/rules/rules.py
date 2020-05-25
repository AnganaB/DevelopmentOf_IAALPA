#This rule was reconstructed from outputs/rules/rules.json
def findDecision(obj):
	if obj[1]<=0.6567280329999999:
		if obj[4]>0.001963384:
			if obj[0]<=6.0975609760000005:
				if obj[2]<=1.8268292680000002:
					if obj[3]<=219631423.1:
						return 'RA'
					else: return 'RA'
				elif obj[2]>1.8268292680000002:
					return 'RA'
				else: return 'RA'
			elif obj[0]>6.0975609760000005:
				if obj[2]<=1.8268292680000002:
					if obj[3]<=219631423.1:
						return 'WA2'
					else: return 'WA2'
				else: return 'WA2'
			else: return 'WA2'
		elif obj[4]<=0.001963384:
			return 'RWA'
		else: return 'RWA'
	elif obj[1]>0.6567280329999999:
		if obj[2]<=1.8268292680000002:
			if obj[3]>219631423.1:
				return 'WA3'
			elif obj[3]<=219631423.1:
				return 'WA2'
			else: return 'WA2'
		elif obj[2]>1.8268292680000002:
			return 'WA3'
		else: return 'WA3'
	else: return 'WA3'
