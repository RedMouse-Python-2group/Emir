def stroke_count():
	stroke = str(raw_input('Input your text: '))
	stroke_list = list(stroke.split(' '))
	for x in stroke_list:
		print '%s - %s' % (x, len(x))

stroke_count()