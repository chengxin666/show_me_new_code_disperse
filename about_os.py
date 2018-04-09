import os

abs_path = os.path.abspath(__file__)
print('abs_path     :', abs_path)
print('getcwd       :', os.getcwd())

normal_path = os.path.normpath(abs_path)
print('normal_path  :', normal_path)

(x, y) = os.path.split(abs_path)
print('split        :', x, '____', y)

(x, y) = os.path.splitext(abs_path)
print('splittext    :', x, '____',y)

print('join         :', os.path.join(x, y))
print('basename     :', os.path.basename(abs_path))
print('dirname      :', os.path.dirname(abs_path))

