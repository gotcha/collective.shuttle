Overview
========

Sometimes, a Zope 2 application needs to traverse to objects that are not
persisted in the ZODB.

``collective.shuttle`` provides a traversal adapter and a dispatcher base class
that traverses to those objects. 
