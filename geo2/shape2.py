class Shape2(object):

    def collides(self, obj):
        raise NotImplementedError(
            "{0}.collides({1})".format(
            type(self).__name__, obj))
    
    def touches(self, obj):
        raise NotImplementedError(
            "{0}.touches({1})".format(
            type(self).__name__, obj))


