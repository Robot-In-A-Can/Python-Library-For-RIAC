from distutils.core import setup
setup(
  name = 'evelabs',
  packages = ['evelabs'],
  classifiers = ['Programming Language :: Python :: 2', 'Programming Language :: Python :: 3', 'Topic :: Education', 'License :: OSI Approved :: MIT License'],
  install_requires=[
    "websocket-client",
  ],
)
