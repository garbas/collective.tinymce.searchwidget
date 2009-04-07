from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.tinymce.searchwidget',
      version=version,
      description="SearchWidget TinyMCE plugin for Plone3",
      long_description='',
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope plone tinymce plugin searchtool search',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='http://github.com/garbas/collective.tinymce.searchwidget',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'':'src'},
      namespace_packages=['collective','collective.tinymce'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.TinyMCE',
          'archetypes.searchwidget'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
