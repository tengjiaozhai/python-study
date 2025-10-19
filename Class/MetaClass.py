#元类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
print(h.hello())

"""
1.要创建一个class对象，type()函数依次传入3个参数：
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
2. (object,) 为什么有一个括号和逗号
在 type 的参数 bases 里，你必须给一个 元组（tuple）表示基类列表。即使只有一个基类，仍然需要一个 元组。
在 Python 中，一个元素的元组必须写成 (object,) 而不是 (object)，因为 (object) 只是把 object 括起来的表达式，而不构成元组。 
因此 (object,) 表示一个只有一个元素 object 的元组，符合 bases 参数期望“基类集合”的类型。
3. dict(hello=fn) 是什么作用
dict(...) 是 Python 内建函数，用于创建一个字典（dictionary）对象。
在这个用法中，dict(hello=fn) 等价于 {'hello': fn}：创建一个字典，该类生成的类将拥有一个属性 hello，其值是函数 fn。
把这个字典作为 type() 的第三个参数，就是把这个函数 fn 绑定为类的新方法 hello。
"""
def fn(self ,name = 'world'):
    print('Hello, %s.' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
print(h.hello())
# 简易orm框架
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
"""
---
## 💡 总体思路
这段 Python 代码是一个“简易版 ORM 框架”（类似于 Java 的 MyBatis 或 Hibernate）。
它的作用是：
> 把类（Class）和数据库表（Table）之间建立映射关系，让你通过操作类对象，就能自动生成 SQL。
比如：
```python
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
```
会自动输出：
```
SQL: insert into User (id, username, email, password) values (?, ?, ?, ?)
ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
```
就像在 Java 里：
```java
User u = new User(12345, "Michael", "test@orm.org", "my-pwd");
userDao.save(u);
```
---
## 一步步拆解
### 1️⃣ Field 类 — 对应数据库字段的“定义”
```python
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
```
相当于 Java 里定义：
```java
public class Field {
    private String name;
    private String columnType;
}
```
👉 它只是保存 “字段名” 和 “字段类型”。
---
### 2️⃣ StringField / IntegerField — 子类化不同类型的字段
```python
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')
```
类似 Java：
```java
public class StringField extends Field {
    public StringField(String name) {
        super(name, "varchar(100)");
    }
}
```
---
### 3️⃣ ModelMetaclass — 元类（相当于 Java 的**编译期处理器**）
Python 中 `metaclass` 就像 Java 的 **反射 + 注解处理器**。
当 Python 解释器执行：
```python
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
```
时，`ModelMetaclass.__new__()` 会**拦截类的创建过程**，提取类属性中的 `Field` 对象。
举个比喻：
> 在 Java 里，Spring 或 Hibernate 在启动时扫描你的 `@Entity` 类、`@Column` 注解，收集元信息。
同理：
```python
Found model: User
Found mapping: id ==> <IntegerField:id>
Found mapping: name ==> <StringField:username>
...
```
这些信息被收集到：
```python
attrs['__mappings__'] = mappings  # 保存属性到字段的映射关系
attrs['__table__'] = name         # 假设表名 = 类名
```
---
### 4️⃣ Model 类 — 相当于 ORM 基类
```python
class Model(dict, metaclass=ModelMetaclass):
```
表示：
* 它继承 `dict`（可以像字典那样操作属性）
* 使用 `ModelMetaclass` 来拦截类的定义阶段
Java 类比：
```java
public abstract class Model extends HashMap<String, Object> {
    // 拥有反射信息和公共方法
}
```
其中的 `save()` 方法相当于 MyBatis 的：
```java
public void save() {
    // 拼SQL
    String sql = "INSERT INTO table (...) VALUES (...)";
}
```
---
### 5️⃣ User 类 — 真正的业务实体
```python
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    ...
```
在 Java 里等价于：
```java
@Entity
@Table(name="User")
public class User extends Model {
    @Column(name="id")
    private Long id;

    @Column(name="username")
    private String name;
}
```
---
### 6️⃣ 最后：实例化并保存
```python
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
```
执行结果：
```
SQL: insert into User (id, username, email, password) values (?, ?, ?, ?)
ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
```
就像 Java 中：
```java
User u = new User(12345, "Michael", "test@orm.org", "my-pwd");
userDao.insert(u);
```
---
## ✅ 总结对比表

| Python 概念        | Java 类比                | 作用             |
| ---------------- | ---------------------- | -------------- |
| `Field`          | 字段定义类 / `@Column`      | 定义列名和类型        |
| `ModelMetaclass` | 注解处理器 / 反射扫描器          | 自动收集映射关系       |
| `Model`          | ORM 基类（如 `BaseEntity`） | 提供通用操作（如 save） |
| `User`           | 实体类 `User`             | 继承模型，定义映射字段    |
| `save()`         | DAO 层的 `insert` 方法     | 拼接并执行 SQL      |

---
"""