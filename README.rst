.. contents:: :local:

Introduction
============

``collective.portletalias`` allows "alias" portlets from
other locations to show on the current content in `Plone CMS <http://plone.org>`_.
This is useful if you need to have the same portlet to be visible in different unrelated locations
and have only one copy where the portlet content is edited and maintaned.

Installation
============

Install package as ``collective.portletalias`` and then install in Add on setup.

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to/

@@portlet-data helper view
===========================

Add ``/@@portlet-data`` to URL of any content item to
show debug information about the portlets assigned there.
Admin priviledges needed.

.. image :: http://cloud.github.com/downloads/collective/collective.portletalias/Screen%20Shot%202012-11-21%20at%209.28.53%20PM.png

.. note ::

    If you have a default item set (like front-page) for the content append
    /front-page/@@portlet-data to URL to see all the portlets.

Setting up alias
==================

* Go to Manage portlets view in the target folder

* Choose *Add new portlet...* *Alias Portlet*

* Enter the path to the source folder

* Enter the portlet id of the source portlet. Use @@portlet-data view (above) to
  find out portlet assignment name

  .. image :: https://github.com/downloads/collective/collective.portletalias/Screen%20Shot%202012-11-21%20at%2010.44.02%20PM.png

Source code
=============

* https://github.com/collective/collective.portletalias

Author
========

`Mikko Ohtamaa <http://opensourcehacker.com>`_
