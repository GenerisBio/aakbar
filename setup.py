from distutils.core import setup

setup(
    name='aakbar',
    version='0.1',
    url='http://github.com/GenerisBio/aakbar',
    download_url='http://github.com/GenerisBio/aakbar/tarball/'+version,
    keywords=['bioinformatics', 'peptide', 'science', 'signatures'],
    platforms=['Linux', 'Mac OSX', 'Windows', 'Unix'],
    license='GenerisBio',
    description='Amino-Acid k-mer phylogenetic signature tools',
    long_description='Creating, searching, and analyzing k-mer signatures in space',
    author='Joel Berendzen',
    author_email='joel@generisbio.com',
    packages=['aakbar'],
    zip_safe=True,
    install_requires=['pyfaidx','bitarray', 'numpy', 'matplotlib', 'pandas', 'click'],
    entry_points={
                 'console_scripts': [
                                     'aakbar = aakbar:aakbar'
                                    ]
                 },
    classifiers=[
                        'Development Status :: 4 - Beta Development Status',
                        'Environment :: Console',
                        'Environment :: MacOS X',
                        'Environment :: Win32 (MS Windows)',
                        'Intended Audience :: Science/Research',
                        'License :: Other/Proprietary License ',
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Topic :: Scientific/Engineering :: Bio-Informatics',
                        ]
)