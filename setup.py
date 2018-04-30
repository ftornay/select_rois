from setuptools import setup

setup(name='select_rois',
      version='0.1',
      description='Program to select regions of interest in thermal images',
      url='http://github.com/ftornay/select_rois',
      author='ftornay',
      author_email='ftornay@ugr.es',
      license='MIT',
      python_requires='>=3',
      packages=['select_rois'],
      entry_points={
          'gui_scripts': [
            'select_rois = select_rois.select_rois:create_app'
          ]
      },
      install_requires=[
          'matplotlib',
          'scipy',
          'easygui'
          ],
      zip_safe=False)
