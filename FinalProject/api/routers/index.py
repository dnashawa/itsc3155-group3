from . import orders, order_details, reviews, customers, promo_codes, sandwiches, sandwich_tags, resources, recipes


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(reviews.router)
    app.include_router(customers.router)
    app.include_router(promo_codes.router)
    app.include_router(sandwiches.router)
    app.include_router(sandwich_tags.router)
    app.include_router(recipes.router)
    app.include_router(resources.router)
