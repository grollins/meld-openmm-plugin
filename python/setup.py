from distutils.core import setup
from distutils.extension import Extension
import os
import sys
import platform

openmm_dir = '@OPENMM_DIR@'
meldplugin_header_dir = '@MELDPLUGIN_HEADER_DIR@'
meldplugin_library_dir = '@MELDPLUGIN_LIBRARY_DIR@'

# setup extra compile and link arguments on Mac
extra_compile_args = []
extra_link_args = []

openmm_lib_path = os.getenv('OPENMM_LIB_PATH')

if platform.system() == 'Darwin':
    extra_compile_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7']
    extra_link_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7', '-Wl', '-rpath', openmm_lib_path]

extension = Extension(name='_meldplugin',
                      sources=['MeldPluginWrapper.cpp'],
                      libraries=['OpenMM', 'MeldPlugin'],
                      include_dirs=[os.path.join(openmm_dir, 'include'), meldplugin_header_dir],
                      library_dirs=[os.path.join(openmm_dir, 'lib'), meldplugin_library_dir],
                      extra_compile_args=extra_compile_args,
                      extra_link_args=extra_link_args
                     )

setup(name='meldplugin',
      version='1.0',
      py_modules=['meldplugin'],
      ext_modules=[extension],
     )
