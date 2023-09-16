from marshmallow import Schema, fields
from datetime import datetime

class ExampleModelsSchema(Schema):
    _id                 = fields.Str()
    name_list           = fields.Str()
    type                = fields.Str()
    status              = fields.Int()
    last_update         = fields.DateTime(default=datetime.utcnow)
   
