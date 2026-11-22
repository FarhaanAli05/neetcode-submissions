class ListNode():
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = ListNode(0,0), ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        # tc: o(1)
        # sc: o(1)
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert_node(self, node):
        # tc: o(1)
        # sc: o(1)
        prev, nxt = self.tail.prev, self.tail
        node.prev = prev
        node.next = nxt
        prev.next = nxt.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int

        tc: o(1)
        sc: o(1)
        """
        if self.cache.get(key):
            self.remove_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None

        tc: o(1)
        sc: o(n) overall
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)
        else:
            self.cache[key] = ListNode(key=key,val=value)
            self.insert_node(self.cache[key])
            if len(self.cache) > self.cap:
                del self.cache[self.head.next.key]
                self.remove_node(self.head.next)