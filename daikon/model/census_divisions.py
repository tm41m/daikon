from daikon.model import db, ma


class CensusDivisions(db.Model):
    __table_args__ = {"schema": "stahl"}
    __tablename__ = "dim_census_division"

    id = db.Column(db.String())
    dguid = db.Column(db.String())
    census_division_name = db.Column(db.String())
    census_division_type = db.Column(db.String())
    land_area = db.Column(db.Numeric(32, 2))
    region_code = db.Column(db.String())
    md5_key = db.Column(db.String(32), primary_key=True)

    def __repr__(self):
        return "<Post %s>" % self.title


class CensusDivisionsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "dguid",
            "census_division_name",
            "census_division_type",
            "land_area",
            "region_code",
            "md5_key",
        )
        model = CensusDivisions
