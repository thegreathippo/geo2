from .shape2 import Shape2


class Box2(Shape2):

    def __init__(self, *args):
        if len(args) != 4:
            raise TypeError(
                    "{0} accepts 4 args, "
                    "received: {1}".format(
                    type(self).__name__, 
                    len(args)))
        self._corners = args


