from django.apps import AppConfig


class AlunosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alunos'

class ProfessorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'professor'

