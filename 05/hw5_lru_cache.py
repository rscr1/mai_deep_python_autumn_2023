class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        '''get method for descriptor'''
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return None

    def set(self, key, value):
        '''set method for descriptor'''
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.limit:
                self._remove_tail()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    def _move_to_head(self, node):
        if node == self.head:
            return
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev

    def _add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _remove_tail(self):
        if not self.tail:
            return
        del self.cache[self.tail.key]
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
