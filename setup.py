try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

setup(name='ble_central',
      version='2017.7.16',
      description=("Bluetooth Low Energy Central Device Server."),
      author="necromuralist",
      platforms=['linux'],
      url='https://github.com/necromuralist/ble_central_server',
      author_email="necromuralist@gmail.com",
      packages=find_packages(),
      install_requires=['connexion', 'click'],
      entry_points="""
      [console_scripts]
      blec=ble_central.command_line_interface:main
      """
      )
