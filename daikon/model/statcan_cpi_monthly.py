from daikon.model import db, ma


class StatcanCPIMonthly(db.Model):
    __table_args__ = {"schema": "stahl"}
    __tablename__ = "statcan_cpi_monthly"

    calendar_date = db.Column(db.Date())
    time_grain = db.Column(db.String())
    region_code = db.Column(db.String(2))
    component_name = db.Column(db.String())
    cpi = db.Column(db.Numeric(32, 2))
    previous_cpi = db.Column(db.Numeric(32, 2))
    cpi_chng = db.Column(db.Numeric(32, 4))
    r_uom = db.Column(db.String())
    r_dguid = db.Column(db.String())

    md5_key = db.Column(db.String(32), primary_key=True)

    def __repr__(self):
        return "<Post %s>" % self.title


class StatcanCPIMonthlySchema(ma.Schema):
    class Meta:
        fields = (
            "calendar_date",
            "time_grain",
            "region_code",
            "component_name",
            "cpi",
            "previous_cpi",
            "cpi_chng",
            "r_uom",
            "r_dguid",
            "md5_key",
        )
        model = StatcanCPIMonthly
