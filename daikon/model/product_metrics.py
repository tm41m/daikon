from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class ProductMetrics(db.Model):
    __tablename__ = "product_timeseries_metrics"

    calendar_date = db.Column(db.Date())
    product_id = db.Column(db.Integer())
    avg_price = db.Column(db.Numeric(32, 2))
    md5_key = db.Column(db.String(32), primary_key=True)

    def __repr__(self):
        return "<Post %s>" % self.title


class ProductMetricsSchema(ma.Schema):
    class Meta:
        fields = ("calendar_date", "product_id", "avg_price", "md5_key")
        model = ProductMetrics
