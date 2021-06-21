from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'sekte2pdf',
  packages = ['sekte'],
  include_package_data=True,
  version = '0.0.3',    
  license='MIT',
  description = 'Sekte2Pdf',
  long_description_content_type = 'text/markdown',
  long_description = open('README.md', 'r').read(),
  author = 'MhankBarBar', # Krypton-Byte
  author_email = 'mhankbarbar@yes.my',
  url = 'https://github.com/MhankBarBar/SekteModule',
  download_url = 'https://github.com/MhankBarBar/SekteModule/archive/0.0.3.tar.gz',
  keywords = ['manga', 'sektekomik', 'downloader', 'pdf', 'sektekomik downlader'], 
  install_requires=[           
          'pillow',
          'requests',
          'bs4'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
