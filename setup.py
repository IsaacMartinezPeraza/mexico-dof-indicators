from setuptools import setup

setup(
    name='indicatorsDOF',
    version='0.alpha.0',
    description='Module to obtain official rates from Mexico DOF',
    url='https://https://github.com/IsaacMartinezPeraza/mexico-dof-indicators',
    author='Isaac Martinez',
    author_email='alex97925@gmail.com',
    license='MIT License',
    packages=['indicatorsDOF'],
    install_requires=['bs4',
                      'requests',                     
                      ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Programming Language :: Python :: 3.13',
    ],
)
