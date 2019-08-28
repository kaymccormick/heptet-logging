import json
import logging
class StructuredMessage:
    def __init__(self, message, **kwargs):
        if not 'message' in kwargs:
            kwargs['message'] = message
        self.kwargs = kwargs
    def __str__(self):
        return self.asJSON()
    def asJSON(self):
        return json.dumps(self.kwargs)
    
class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        if not isinstance(msg, StructuredMessage):
            raise TypeError()
        msg.kwargs['collector_level'] = self.extra.collector_level
        msg.kwargs['depth_level'] = self.extra.level
        return msg.asJSON(), {}
