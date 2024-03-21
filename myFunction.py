"""import os
def hello():
    print('hello manny')
    print('how are you?')

def hello1(name):
    print(f"hello {name}")
    print(f'how are you {name}?')


def command(cmd):
    import os
    os.system(cmd)
command('ls')


def list_files(dir_path):

    for item in os.listdir(dir_path):
            path= os.path.join(dir_path, item)
            if os.path.isfile(path):
                    print(f"{path} is a file")
            else:
                    print(f"{path} is a directory")"""

def add(a,b):
      return(a+b)

var=add(2,4)

print(var)