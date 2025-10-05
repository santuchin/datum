import src as datum


clients_id = datum.Value('./clients_id.db', int)
clients = datum.Table('./clients.db',
	id=int,
	name=str,
	credit=float,
	address=str,
	phone=str,
	email=str,
)

for _ in range(1000):

	clients.add(
		id=clients_id.value,
		name='Giuseppe Rossi',
		credit=8046.12,
		address='Via Roma 35, 86081 Agnone (IS), Italia',
		phone='+39 0865 779024',
		email='giuseppe.rossi4@gmail.com'
	)
	clients_id.value += 1

clients_id.save()
clients.save()
