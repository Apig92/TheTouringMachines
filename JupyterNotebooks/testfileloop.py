import os
directory = 'C:/Users/Daniel/PycharmProjects/TheTouringMachines/JupyterNotebooks'
for filename in os.listdir(directory):
   if filename.endswith(".ipynb"):
      print("'"+filename+"'")
newpath = 'C:/Users/Daniel/PycharmProjects/TheTouringMachines/JupyterNotebooks/testfolder'
if not os.path.exists(newpath):
    os.makedirs(newpath)