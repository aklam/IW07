# Configuration file for jupyter-notebook.

# Edit this line to change password:
notebook_password = 'iw07password'

from IPython.lib import passwd

c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
c.NotebookApp.certfile = u'/home/ubuntu/.jupyter/cert/cert.pem'
c.NotebookApp.keyfile  = u'/home/ubuntu/.jupyter/cert/cert.key'
c.NotebookApp.open_browser = False

c.NotebookApp.password = passwd(notebook_password)

c.IPKernelApp.pylab = 'inline'  # in-line figures when using Matplotlib
