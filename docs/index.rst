==================
sphinxnotes.extweb
==================

.. image:: https://img.shields.io/github/stars/sphinx-notes/extweb.svg?style=social&label=Star&maxAge=2592000
   :target: https://github.com/sphinx-notes/extweb

:version: |version|
:copyright: Copyright ©2022 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

Sphinx extension for embedding external web resources (like video, music, etc.).

.. bilibili:: BV1xx411c79H

.. contents::
   :local:
   :backlinks: none

Installation
============

Download it from official Python Package Index:

.. code-block:: console

   $ pip install sphinxnotes-extweb

Add extension to :file:`conf.py` in your sphinx project:

.. code-block:: python

    extensions = [
              # …
              'sphinxnotes.extweb',
              # …
              ]

.. _Configuration:

Configuration
=============

The extension provides the following configuration:

.. .. any:confval:: any_domain_name
   :type: str
   :default: 'any'

   Name of the domain.

Functionalities
===============

Change Log
==========

2022-06-XX 1.0
--------------
