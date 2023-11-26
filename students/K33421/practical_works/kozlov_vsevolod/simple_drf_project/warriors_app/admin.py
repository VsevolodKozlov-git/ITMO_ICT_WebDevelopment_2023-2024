from django.contrib import admin
from warriors_app import models
# Register your models here.
admin.register(models.Skill)
admin.register(models.Warrior)
admin.register(models.Profession)
admin.register(models.SkillOfWarrior)