mountains = {'mount everest': '29029',
			'K2': '28251',
			'Kangchenjunga': '28169',
			'Lhotse': '27940',
			'Makalu': '27838'
			}

print('Names of five tallest mountains:')
for name in mountains:
	print(name)

print('Elevations of five tallest mountains:')
for elevation in mountains.values():
	print(elevation)

print('Explanatory sentences:')
for name, elevation in mountains.items():
	print(name, ' is ', elevation, ' feet tall')