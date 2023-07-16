import os

class node:
	def __init__(self, id, ele, root) -> None:
		self.id = id
		self.root = root
		self.ele = ele
		self.left = None
		self.right = None

def filter(dict, callback):
	newDict = {}
	for(key, value) in dict.items():
		if(callback(key, value)):
			newDict[key] = value
	return newDict

def safe_get(list: list, i: int):
	try:
		return list[i]
	except IndexError:
		return None
		
def relationship_observer(dict, idx, line):
	id, *rest = line.split(' ')
	left_id = safe_get(rest, 0)
	right_id = safe_get(rest, 1)
	if(left_id):
		dict[id].left = dict[left_id]
	if(right_id):
		dict[id].right = dict[right_id]

def build_trees():
	dict = {}
	for path, subdirs, files in os.walk('/tmp'):
		for name in files:
			filePath = os.path.join(path, name)
			file = open(filePath)
			lines = file.read().splitlines()
			observer = None
			for idx, line in enumerate(lines):
				if(line == 'nodes'):
					observer = node_observer
				elif(line == 'relationships'):
					observer = relationship_observer
				else:
					observer(dict, idx, line)
	return [filter(dict, lambda elem: elem[1].root), dict]

[roots, nodes] = build_trees()

print(f'Root Count: {len(roots)}')
print(f'Node Count: {len(nodes)}')

def findNode(node, path, search):
	if(node.data == search):
		return node, path
	else:
		left = findNode(node.left, path.copy().append(node.left.id))
		if(left.data == search):
			return left, path

		right = findNode(node.right, path.copy().append(node.right.id))
		if(right.data == search):
			return right, path
	return None, []


search = 'FindMe!'

for root in roots:
	rootNode = roots[root]
	target_node, path = findNode(rootNode, [], search)
	if(target_node != None):
		print(f'Root node {rootNode.id} {rootNode.data} contains {search} under node {target_node.id} ({" => ".join(path)})')
		break
	else:
		print("Not Found")
