import src as datum

table = datum.Table('./tests.tb', id=int, name=str, score=float, coord_x=float, coord_y=float)

"""
table.add(
	id=0,
	name='Johnny',
	score=4,
	coord_x=10,
	coord_y=23,
)
"""

for row in table:
	print(row)

table.save()
