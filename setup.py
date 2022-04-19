from setuptools import setup, find_packages


setup(
    name='TMS_homework',
    version='0.6',
    license='GNU GENERAL PUBLIC LICENSE',
    author="Nikita Suhomlin",
    author_email='nekit_suhomlinkas@tut.by',
    packages=find_packages('tank_game'),
    package_dir={'': 'tank_game'},
    url='https://github.com/nikitasuhomlin/TMS_homework/tree/suhomlinn',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)