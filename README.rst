.. contents:: :local:

Introduction
============

Allow "alias" portlets from other locations to show in the current folder in `Plone CMS <http://plone.org>`_.
This is useful if you need to have the same portlet to pop-up in different unrelated locations
and you want to have only one copy for the site editors to maintain the portlet content.

* Go to Manage portlets

* Choose Add new portlet... Alias

* Enter the path to the source folder

* Enter the portlet id of the source portlet. This add-on provides @@portlet-data view which dumps
  out the folder portlet info and related its.

Installation
============

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to/

portlet-data helper view
=========================

Add ``/@@portlet-data`` to URL of any content item to
show debug information about the portlets assigned there.
Admin priviledges needed.

.. image :: http://cloud.github.com/downloads/collective/collective.portletalias/Screen%20Shot%202012-11-21%20at%209.28.53%20PM.png

Author
========

`Mikko Ohtamaa <http://opensourcehacker.com>`_
