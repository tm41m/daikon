from daikon.model import db, ma


class ProductMetrics(db.Model):
    __table_args__ = {"schema": "wolfram"}
    __tablename__ = "product_timeseries_metrics"

    calendar_date = db.Column(db.Date())
    region_code = db.Column(db.String())
    product_id = db.Column(db.Integer())
    currency = db.Column(db.String())
    unit = db.Column(db.String())
    avg_price = db.Column(db.Numeric(32, 2))
    avg_price_chng = db.Column(db.Numeric(32, 2))
    product_listings = db.Column(db.Integer())
    product_listings_rtn = db.Column(db.Integer())
    md5_key = db.Column(db.String(32), primary_key=True)

    def __repr__(self):
        return "<Post %s>" % self.title


class ProductMetricsSchema(ma.Schema):
    class Meta:
        fields = (
            "calendar_date",
            "region_code",
            "product_id",
            "currency",
            "unit",
            "avg_price",
            "avg_price_chng",
            "product_listings",
            "product_listings_rtn",
            "md5_key",
        )
        model = ProductMetrics
