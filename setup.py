from setuptools import setup, find_packages

version = '1.0'

setup(name='collective.shuttle',
      version=version,
      description="Zope 2 : traversal to objects not stored in ZODB.",
      long_description=open("README.txt").read() + "\n" +
                       open("HISTORY.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Zope2',
      ],
      extras_require=dict(
            test=['plone.testing',
                  'five.grok',
                 ]),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
