def test_create_app(app):
    """Test create_app."""

    assert app.name == "app"
    assert app.url_map.strict_slashes is False
    assert len(app.blueprints) == 2
    assert app.blueprints["ping"].name == "ping"
    assert app.blueprints["slack_events"].name == "slack_events"
