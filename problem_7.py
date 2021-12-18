# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
	def __init__(self, root_value):
		# Initialize the trie with an root node and a handler, this is the root path or home page node
		self.root = RouteTrieNode(root_value)

	def insert(self, full_path, handler):
		# Similar to our previous example you will want to recursively add nodes
		# Make sure you assign the handler to only the leaf (deepest) node of this path
		paths = self._splitter(full_path)
		home = self.root
		for path in paths:
			if path not in home.children:
				home.children[path] = RouteTrieNode()
			home = home.children[path]

		home.value = handler

	def find(self, route):
		# Starting at the root, navigate the Trie to find a match for this path
		# Return the handler for a match, or None for no match
		if route == '/':
			return self.root.value

		paths = self._splitter(route)
		home = self.root
		for path in paths:
			if path in home.children:
				home = home.children[path]
			else:
				return None
		
		return home.value

	def _splitter(self, string):
		"""" 
			This function handles the splitting the full path in its needed format 
			Return: List(result)
		"""
		result = string.split('/')
		if result[-1] == '':
			return result[:-1]
		else:
			return result

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
	def __init__(self, value=None):
		# Initialize the node with children as before, plus a handler
		self.value = value
		self.children = {}

# The Router class will wrap the Trie and handle 
class Router:
	def __init__(self, root_value, fail_msg):
		# Create a new RouteTrie for holding our routes
		# You could also add a handler for 404 page not found responses as well!
		self.routeTri = RouteTrie(root_value)
		self.fail_msg = fail_msg

	def add_handler(self, full_path, handler):
		# Add a handler for a path
		# You will need to split the path and pass the pass parts
		# as a list to the RouteTrie
		self.routeTri.insert(full_path, handler)

	def lookup(self, path):
		# lookup path (by parts) and return the associated handler
		# you can return None if it's not found or
		# return the "not found" handler if you added one
		# bonus points if a path works with and without a trailing slash
		# e.g. /about and /about/ both return the /about handler
		result = self.routeTri.find(path)
		return result if result else self.fail_msg

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one