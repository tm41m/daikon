from daikon.model import db, ma


class StatcanFoodPrices(db.Model):
    __table_args__ = {"schema": "stahl"}
    __tablename__ = "statcan_food_prices"

    calendar_date = db.Column(db.Date())
    time_grain = db.Column(db.String())
    region_code = db.Column(db.String(2))
    product_name = db.Column(db.String())
    amount = db.Column(db.Numeric(32, 2))
    unit = db.Column(db.String())
    currency = db.Column(db.String(3))
    price = db.Column(db.Numeric(32, 2))
    previous_price = db.Column(db.Numeric(32, 2))
    price_chng = db.Column(db.Numeric(32, 4))

    md5_key = db.Column(db.String(32), primary_key=True)

    def __repr__(self):
        return "<Post %s>" % self.title


class StatcanFoodPricesSchema(ma.Schema):
    class Meta:
        fields = (
            "calendar_date",
            "time_grain",
            "region_code",
            "product_name",
            "amount",
            "unit",
            "currency",
            "price",
            "previous_price",
            "price_chng",
            "md5_key",
        )
        model = StatcanFoodPrices
