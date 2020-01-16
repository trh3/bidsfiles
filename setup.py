from setuptools import setup, find_packages

setup(name='bidsfiles',
      version='1.3',
      description='In-memory BIDS dataset query engine',
      url='https://github.com/trh3/bidsfiles',
      author='Teague Henry',
      author_email='trhenry@email.unc.edu',
      license='MIT',
      python_requires='>=3.6',
      install_requires = ['pandas',
                          'parse'],
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False
      )
