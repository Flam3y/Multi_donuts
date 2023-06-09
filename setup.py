from distutils.core import setup
setup(
  name = 'Multi_donuts',         # How you named your package folder (MyLib)
  packages = ['Multi_donuts'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Yow want add colorfull easter egg in your project, but all the code for donut consuming file space? Use Multi-donuts lib!',   # Give a short description about your library
  author = 'Flam3y',                   # Type in your name
  author_email = 'glebnextik@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Flam3y/Multi_donuts',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Flam3y/Multi_donuts/archive/refs/tags/Python.tar.gz',    # I explain this later on
  keywords = ['DONUT', 'CONSOLE-GRAPHIC', 'RGB'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'ansicolors',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)