import sys

try:
    import py2exe
except:
    raw_input('Please install py2exe first...')
    sys.exit(-1)

from distutils.core import setup
import shutil

sys.argv.append('py2exe')

from glob import glob
extra_data_files = [("Microsoft.VC90.CRT", glob(r'C:\Python27\py2exe\*.dll'))]

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows=[{'script': "main.py"}],
	data_files=extra_data_files,
    zipfile=None,
)

shutil.move('dist\\main.exe', '.\\main.exe')
shutil.rmtree('build')
shutil.rmtree('dist')

print "Py2Exe Done"