# 集合模块
from collections import namedtuple,deque,defaultdict
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('a')
print(q)
dd = defaultdict(lambda: 'N/A')
print(dd['key2'])
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
od = LastUpdatedOrderedDict((5))
od[1] = 'value'
od[2] = 'value2'
print(od.setdefault(3, 'value3'))
print(od.popitem())
print(od.items())
