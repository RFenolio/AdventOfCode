from pprint import pprint

with open('day07.txt') as file:
	instructions = file.read()

class gate():
	def __init__(self, str):
		self.in1, self.in2, self.operator, self.out = self.parse_input(str)

	def __repr__(self):
		return "<Gate in1: %s, in2: %s, out: %s, operator: %s>" % (self.in1, self.in2, self.out, self.operator)
		
	def parse_input(self, str):
		part = str.split()
		operator = None
		out = None
		in1 = None
		in2 = None
		if len(part) == 3:
			in1 = part[0]
			out = part[2]
			operator = 'NUM'
		elif len(part) == 4:
			operator = part[0]
			in1 = part[1]
			out = part[3]
		elif len(part) == 5:
			in1 = part[0]
			in2 = part[2]
			operator = part[1]
			out = part[4]

		return in1, in2, operator, out


class Circuit(object):

	def __init__(self, gates):
		self.gates = gates
		self.vals = {}

	def can_process_gate(self, gate):
		if gate.operator == "NUM":
			return gate.in1.isdigit() or gate.in1 in self.vals
		elif gate.operator in ("AND", "OR"):
			return (gate.in1.isdigit() or gate.in1 in self.vals) and gate.in2 in self.vals
		elif gate.operator in ("NOT", "LSHIFT", "RSHIFT"):
			return gate.in1 in self.vals

	def run_gate(self, gate):
		"""process a single gate, assumes inputs have been processed already"""
		if gate.operator == "NUM":
			self.vals[gate.out] = int(gate.in1) if gate.in1.isdigit() else self.vals[gate.in1]
		elif gate.operator == "AND":
			left = int(gate.in1) if gate.in1.isdigit() else self.vals[gate.in1]
			self.vals[gate.out] = left & self.vals[gate.in2]
		elif gate.operator == "OR":
			self.vals[gate.out] = self.vals[gate.in1] | self.vals[gate.in2]
		elif gate.operator == "LSHIFT":
			self.vals[gate.out] = self.vals[gate.in1] << int(gate.in2)
		elif gate.operator == "RSHIFT":
			self.vals[gate.out] = self.vals[gate.in1] >> int(gate.in2)
		elif gate.operator == "NOT":
			self.vals[gate.out] = ~self.vals[gate.in1]

	def process_instructions(self):
		"""takes in a list of gates, and processess them"""
		count = 0
		print "processing..."
		while self.gates and count < 100000:
			gate = self.gates.pop(0)
			if self.can_process_gate(gate):
				self.run_gate(gate)
			else:
				self.gates.append(gate)
			count += 1


instructions1 = [gate(instruction) for instruction in instructions.split('\n')]
instructions2 = [gate(instruction) for instruction in instructions.split('\n')]
instructions2 = [gate for gate in instructions2 if gate.out != 'b']
# pprint(instructions)


circuit = Circuit(instructions1)
circuit.process_instructions()
# pprint(circuit.vals)
print circuit.vals['a']
circuit2 = Circuit(instructions2)
circuit2.vals['b'] = circuit.vals['a']
circuit2.process_instructions()
pprint(circuit2.vals)

