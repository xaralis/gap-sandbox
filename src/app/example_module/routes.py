from models import ExampleModel

routes = (
    ('.*', 'app.example_module.views.module_welcome_screen'),
)

from resources import register
register.register(ExampleModel)
