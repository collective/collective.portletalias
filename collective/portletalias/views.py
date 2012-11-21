from zope.interface import implements, Interface
from zope.component import getUtility, getMultiAdapter

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletAssignmentMapping


class PortletData(BrowserView):
    """
    Show info about the portlet assigned in the location.
    """

    def getPortletData(self):
        """
        """

        content = self.context.aq_inner

        managers = []

        for manager_name in ["plone.leftcolumn", "plone.rightcolumn"]:

            print "Checking portlet column:" + manager_name

            manager = getUtility(IPortletManager, name=manager_name, context=content)

            mapping = getMultiAdapter((content, manager), IPortletAssignmentMapping)

            items = []
            # id is portlet assignment id
            # and automatically generated
            for id, assignment in mapping.items():
                print "Found portlet assignment:" + id + " " + str(assignment)
                items.append({
                    "name": id,
                    "data": assignment
                })

            managers.append({
                "name": manager_name,
                "items": items
            })

        print str(managers)
        return managers

