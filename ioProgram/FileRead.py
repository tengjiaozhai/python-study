# 文件读写
fpath = '/Users/shenmingjie/studyNotes/React/React.md'

with open(fpath, 'r') as f:
    for line in f.readlines():
        print(line.strip())

# 运行代码观察结果
