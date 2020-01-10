from collections import deque


def single(iterable):
    i = iter(iterable)
    try:
        item = next(i)
    except StopIteration:
        raise ValueError("Too few items")

    try:
        next(i)
    except StopIteration:
        return item
    raise ValueError("Too many items")


def one(item):
    yield item


def alternate_with(items, alternate_item):
    """Generate a series from items, alternating with an alternate item.
    
    items[0], alternate_item, items[1], alternate_item, ... ,items[n - 1], alternate_item
    """
    for item in items:
        yield item
        yield alternate_item


def ensure_contains(items, ensured_item):
    """Yield items, followed by ensured_item, if ensured_item is not already present.
    """
    present = False
    for item in items:
        present = present and (item == ensured_item)
        yield item
        
    if not present:
        yield ensured_item
        
        
def tail(items, n):
    return Tail(items, n)
   
    

    
    
    
class Tail:
    
    def __init__(self, items, n):
        self._i = iter(items)
        self._n = n
        self._d = deque()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while len(self._d) < self._n:
            self._d.append(next(self._i))
        
        assert len(self._d) == self._n
        incoming_item = next(self._i)
        outgoing_item = self._d.popleft()
        self._d.append(incoming_item)
        assert len(self._d) == self._n
        return outgoing_item
            
    @property
    def items(self):
        deque(self, maxlen=0)  # Consume all items
        return self._d
