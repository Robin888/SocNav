

def formatMeasure(measure):
	newMeasure = ""
	for ch in measure:
		if ch == " ":
			newMeasure += "_"
		else:
			newMeasure += ch
	return newMeasure.strip().lower()
