from marshmallow import Schema, fields


class ProductListing(object):
    def __init__(self,
                 id,
                 name,
                 product_id,
                 store_id,
                 price,
                 unit,
                 currency,
                 method_id,
                 is_exact_association,
                 is_exact_price,
                 version,
                 created_at,
                 updated_at):

        self.id = id
        self.name = name
        self.product_id = product_id
        self.store_id = store_id
        self.price = price
        self.unit = unit
        self.currency = currency
        self.method_id = method_id
        self.is_exact_association = is_exact_association
        self.is_exact_price = is_exact_price
        self.version = version
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<ProductListing(name={self.name!r})>'.format(self=self)


class ProductListingSchema(Schema):

    id = fields.Int()
    name = fields.Str()
    product_id = fields.Int()
    store_id = fields.Int()
    price = fields.Number()
    unit = fields.Str()
    currency = fields.Str()
    method_id = fields.Int()
    is_exact_association = fields.Bool()
    is_exact_price = fields.Bool()
    version = fields.Int()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

# class PricesTimeSeries(object):
#     def __init__(self,
#                  dte,
#                  item_name,
#                  item_id,
#                  price):

#         self.dte = dte
#         self.item_name = item_name
#         self.item_id = item_id
#         self.price = price

#     def __repr__(self):
#         return '<PricesTimeSeries(name={self.item_name!r})>'.format(self.self)


# class PricesTimeSeries(Schema):

#     dte = fields.Date()
#     item_name = fields.Str()
#     item_id = fields.Str()
#     price = fields.Number()
