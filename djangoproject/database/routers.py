class DefaultRouter:
    def db_for_read(self, model, **hints):
        return 'common' if model._meta.app_label == 'accounts' else 'default'

    def db_for_write(self, model, **hints):
        return 'common' if model._meta.app_label == 'accounts' else 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return app_label != 'accounts'