from example import config as config


class ExampleExt(object):
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
        app.extensions["example"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.service = app.config["EXAMPLE_SERVICE_CLASS"](
            config=app.config["EXAMPLE_SERVICE_CONFIG"](),
        )
        self.resource = app.config["EXAMPLE_RESOURCE_CLASS"](
            service=self.service,
            config=app.config["EXAMPLE_RESOURCE_CONFIG"](),
        )

    def init_config(self, app):
        """Initialize configuration."""
        app.config.setdefault("EXAMPLE_RESOURCE_CONFIG", config.EXAMPLE_RESOURCE_CONFIG)
        app.config.setdefault("EXAMPLE_RESOURCE_CLASS", config.EXAMPLE_RESOURCE_CLASS)
        app.config.setdefault("EXAMPLE_SERVICE_CONFIG", config.EXAMPLE_SERVICE_CONFIG)
        app.config.setdefault("EXAMPLE_SERVICE_CLASS", config.EXAMPLE_SERVICE_CLASS)
