from Acquisition import Implicit
from OFS.Traversable import Traversable
from OFS.interfaces import ITraversable
from ZPublisher.BaseRequest import DefaultPublishTraverse

from zope.component import queryAdapter
from five import grok


class TraversableItem(Traversable, Implicit):

    def __init__(self, id):
        self.id = str(id)

    def getId(self):
        return self.id


class Traverser(DefaultPublishTraverse, grok.MultiAdapter):
    grok.baseclass()

    def publishTraverse(self, request, name):
        name = name.lower()
        container = queryAdapter(self.context, ITraversable, name=name)
        if container is not None:
            return container.__of__(self.context)
        else:
            return super(Traverser, self).publishTraverse(
                request, name)
