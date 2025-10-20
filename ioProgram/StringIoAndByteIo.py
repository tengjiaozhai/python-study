# StringIO 和 ByteIO
from io import StringIO
from io import BytesIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = BytesIO()
f.write('张三'.encode('utf-8'))
print(f.getvalue())
