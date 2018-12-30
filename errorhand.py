import sys
try:
  f=('s','ss','s','f')
  f[7]
  1/0
  with open('myfile.txt') as file:
    filedata = file.read()
    print(filedata)
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('you have no permission to view the file')
except Exception as err:
    print('Some other error has occured which is: ', str(err))
