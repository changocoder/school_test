from app.school.blueprints.user.controller import UserController


def map_urls(blueprint):
    view = UserController.as_view("user")
    blueprint.add_url_rule("/<user_id>", view_func=view, methods=["GET", "PUT", "DELETE"])
    blueprint.add_url_rule("", view_func=view, methods=["POST", "GET"])
    return blueprint
