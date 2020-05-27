from django.apps import AppConfig


# class AppConfig(AppConfig):
#     name = 'app'

# users/apps.py

class UsersConfig(AppConfig):
    name = 'app'
    #app名字后台显示中文
    verbose_name = "用户管理"

    def ready(self):
        import app.signals