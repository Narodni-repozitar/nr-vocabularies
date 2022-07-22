"""Facet definitions."""

from elasticsearch_dsl import Facet
from elasticsearch_dsl.query import Nested
from invenio_records_resources.services.records.facets import TermsFacet


class NestedLabeledFacet(Facet):
    agg_type = "nested"

    def __init__(self, path, nested_facet, label=""):
        self._path = path
        self._inner = nested_facet
        self._label = label
        super(NestedLabeledFacet, self).__init__(
            path=path,
            aggs={
                "inner": nested_facet.get_aggregation(),
            },
        )

    def get_values(self, data, filter_values):
        return self._inner.get_values(data.inner, filter_values)

    def add_filter(self, filter_values):
        inner_q = self._inner.add_filter(filter_values)
        if inner_q:
            return Nested(path=self._path, query=inner_q)

    def get_labelled_values(self, data, filter_values):
        """Get a labelled version of a bucket."""
        try:
            out = data["buckets"]
        except:
            out = []
        return {"buckets": out, "label": str(self._label)}


relatedURI_COAR = TermsFacet(field="relatedURI.COAR")


relatedURI_CrossrefFunderID = TermsFacet(field="relatedURI.CrossrefFunderID")


relatedURI_ROR = TermsFacet(field="relatedURI.ROR")


relatedURI_URL = TermsFacet(field="relatedURI.URL")


marcCode = TermsFacet(field="marcCode")


dataCiteCode = TermsFacet(field="dataCiteCode")


alpha3Code = TermsFacet(field="alpha3Code")


alpha3CodeENG = TermsFacet(field="alpha3CodeENG")


alpha3CodeNative = TermsFacet(field="alpha3CodeNative")


acronym = TermsFacet(field="acronym")


RID = TermsFacet(field="RID")


ICO = TermsFacet(field="ICO")


coarType = TermsFacet(field="coarType")


dataCiteType = TermsFacet(field="dataCiteType")


nameType = TermsFacet(field="nameType")


nonpreferredLabels_cs = TermsFacet(field="nonpreferredLabels.cs")


nonpreferredLabels_en = TermsFacet(field="nonpreferredLabels.en")


pair = TermsFacet(field="pair")


uuid = TermsFacet(field="uuid")


indexed_at = TermsFacet(field="indexed_at")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


type_pid_type = TermsFacet(field="type.pid_type")


type_id = TermsFacet(field="type.id")


pid_pk = TermsFacet(field="pid.pk")


pid_pid_type = TermsFacet(field="pid.pid_type")


pid_obj_type = TermsFacet(field="pid.obj_type")


pid_status = TermsFacet(field="pid.status")


title_sort = TermsFacet(field="title_sort")


icon = TermsFacet(field="icon")


hierarchy_level = TermsFacet(field="hierarchy.level")


_id = TermsFacet(field="id")


_schema = TermsFacet(field="$schema")


contexts = TermsFacet(field="contexts")


tags = TermsFacet(field="tags")
