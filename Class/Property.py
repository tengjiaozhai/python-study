"""
✅ @property 是什么
@property 是 Python 内置的装饰器，用于将一个方法转换成「属性访问」的形式。
通过它，你可以定义一个名称（比如 x）作为属性，但在背后实际上是调用 x() 方法。因此，表面上访问 obj.x，背后可能执行逻辑。
它配合 .setter 和 .deleter 可以分别定义设置值和删除属性时的行为。
🧐 为什么要用 @property
使用 @property 有几个典型的好处：
封装与验证：你可以控制读取／写入属性时的逻辑，比如验证值、延迟计算、保持内部状态一致。例子：温度不能低于某个值。
API 兼容性：如果你已经把某属性当作公开属性用了，后来想加逻辑（比如验证或懒加载），使用 @property 可以避免修改外部访问方式。也就是说，外部还是 obj.attr，而不用改成 obj.get_attr()。
更干净的代码：相比传统的 getter／setter 方法（如 get_x()／set_x()），使用 @property 能让类的接口看起来更“属性化”、更 Pythonic。
"""
class Screen(object):
    def __init__(self, width, height, resolution):
        self._width = width
        self._height = height
        self._resolution = resolution
    @property
    def resolution(self):
        return self._resolution
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height

# 测试:
s = Screen('','',786432)
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

"""
✅ 为什么加了 _ 解决了你的递归问题
你的原始代码中出现的问题是：
你定义了一个属性名 width（用 @property def width(self): … 和 @width.setter）。
在 width 的 getter / setter 方法里面你又直接用 self.width = … 或 return self.width。
当你访问或设置 self.width 时，会触发属性的 getter/setter方法；而 getter/setter内部又访问或设置 self.width，于是造成自己调用自己 → 无限递归 → RecursionError。
而当你改为使用 _width 来存储实际值，并让 width 属性（getter/setter）访问/修改 self._width，就避免了这个冲突：
width 属性代表公开接口（外部代码写 obj.width）
_width 是内部存储变量（属性的实现细节）
在 width getter 中 return self._width，不会触发重新进入 width 的 getter，又或触发 setter。
在 width setter 中 self._width = value，也不会触发 width 的 setter 方法自身。
因此就没有无限递归，问题被解决。这个做法在社区也被广泛推荐。 例如在 StackOverflow 上有类似的解释：
“Use self._x instead of self.x for private member. By naming both member and property x property shadows member, and return self.x in getter body calls itself.” 
📋 背后的原理是什么
在 Python 中，@property 创建的是一种“描述器”（descriptor）。当你访问 obj.width，其背后会调用 width 的 getter 方法，而不是直接取 obj.__dict__['width']。
如果 getter 内部用 self.width，那就相当于在 getter 里又调用一次 obj.width → 再次进入 getter → 无限循环。
使用一个不同的变量名（例如 self._width）来存储实际数据，就绕过了这个访问机制：obj._width 不被 width 属性拦截（因为 ._width 没有定义对应的 property） → 是一个普通的实例属性。
用 _ 前缀也符合 Python 的一个惯例：表示“这是内部实现细节，不应该从外部直接访问”（虽然并不是强制私有，只是一种约定）。
🧠 总结一句话
在使用 @property 定义属性（getter／setter）时，不要把属性名（例如 width）用于内部存储，否则 getter／setter 调用会进入自己，造成递归。通常的做法是把内部存储变量命名为 self._width 或其他名字，而 @property def width 对外暴露。
"""