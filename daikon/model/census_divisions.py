from daikon.model import db, ma


class CensusDivisions(db.Model):
    __table_args__ = {"schema": "stahl"}
    __tablename__ = "dim_census_division"

    id = db.Column(db.String(4), primary_key=True)
    name = db.Column(db.String())
    type = db.Column(db.String())
    land_area = db.Column(db.Numeric(32, 2))
    region_code = db.Column(db.String(2))

    def __repr__(self):
        return "<Post %s>" % self.title


class CensusDivisionsSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "type", "land_area", "region_code")
        model = CensusDivisions
