import csv

class Firewall:
	def __init__(self, path):
		self.path = path
	def accept_packet(direction, protocol, port, ip_address):
		direc = False
		prot = False
		pt = False
		ip = False
		with open(self.path) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				if direction == row[0]:
					direc = True
				if protocol == row[1]:
					prot = True
				if port == row[2]:
					pt = True
				else:
					split = row[2].split('-')
					if port in range(int(split[0]), int(split[1]) + 1):
						pt = True
				if ip_address == row[3]:
					ip = True
				else:
					split = row[3].split('-')
					left = split[0].split('.')
					right = split[1].split('.')
					inp = ip_address.split('.')
					true = 0
					for i in inp:
						if i in range(int(left), int(right) + 1):
							true += 1
					if true == 4:
						ip = True
		return (direc and prot and pt and ip)
