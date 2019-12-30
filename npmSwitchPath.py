import os
print('''
  Select form the option (1 or 2)  =>>>>>>
    1-http://172.29.227.98:9081/artifactory/api/npm/npm-registry
    2-https://registry.npmjs.com/
''')
try:
  options = int(input("Option: "));
  cmd = ""
  if options is 2:
    cmd = "npm config set registry https://registry.npmjs.com/"
  elif options is 1:
    cmd = "npm config set registry http://172.29.227.98:9081/artifactory/api/npm/npm-registry"
  print(cmd)
  os.system(cmd)
except Exception as e:
  print(e)