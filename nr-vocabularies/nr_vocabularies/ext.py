from nr_vocabularies import config as config


class NRVocabulariesExt(object):
    """extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.resource = None
        self.service = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_resource(app)
        app.extensions["nr-vocabularies"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.service = app.config["NR_VOCABULARIES_SERVICE_CLASS"](
            config=app.config["NR_VOCABULARIES_SERVICE_CONFIG"](),
        )
        self.resource = app.config["NR_VOCABULARIES_RESOURCE_CLASS"](
            service=self.service,
            config=app.config["NR_VOCABULARIES_RESOURCE_CONFIG"](),
        )

    def init_config(self, app):
        """Initialize configuration."""
        app.config.setdefault(
            "NR_VOCABULARIES_RESOURCE_CONFIG", config.NR_VOCABULARIES_RESOURCE_CONFIG
        )
        app.config.setdefault(
            "NR_VOCABULARIES_RESOURCE_CLASS", config.NR_VOCABULARIES_RESOURCE_CLASS
        )
        app.config.setdefault(
            "NR_VOCABULARIES_SERVICE_CONFIG", config.NR_VOCABULARIES_SERVICE_CONFIG
        )
        app.config.setdefault(
            "NR_VOCABULARIES_SERVICE_CLASS", config.NR_VOCABULARIES_SERVICE_CLASS
        )
