from es_engine.bases.field import BaseField


class ModelMetaclass(type):

    def __new__(mcls, name, bases, attrs):  # noqa
        attrs['_fields'] = {}
        for key, value in attrs.iteritems():
            if isinstance(value, BaseField):
                attrs['_fields'][key] = value
        for key in attrs['_fields'].keys():
            if attrs['_fields'][key]._multi:
                attrs[key] = []
            else:
                attrs[key] = None
        cls = type.__new__(mcls, name, bases, attrs)
        if any(x.__name__ == 'EmbeddedDocument' for x in bases):
            cls.__type__ = cls
        return cls