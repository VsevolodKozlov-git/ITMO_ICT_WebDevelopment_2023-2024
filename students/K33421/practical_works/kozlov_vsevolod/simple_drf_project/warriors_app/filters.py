from django_filters import rest_framework as filters
from warriors_app import models
import django.db.models as dj_models




'select * from Warrior where (select title from )'


'''
SELECT * FROM "warriors_app_warrior" 
INNER JOIN 
"warriors_app_skillofwarrior" ON 
("warriors_app_warrior"."id" = "warriors_app_skillofwarrior"."warrior_id") 
INNER JOIN 
"warriors_app_skill" 
ON ("warriors_app_skillofwarrior"."skill_id" = "warriors_app_skill"."id") WHERE "warriors_app_skill"."title" IN (Skill1, Skill2, Skill3)

'''


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class WarriorNameFilter(filters.FilterSet):
    # имя_параметра = (field_name='поле', lookup_expr)
    # Если имя параметра совпадает с именем поля,
    # то необязательно прописывать field_name

    # level = filters.CharFilter(field_name='level', lookup_expr='gt')
    skill__in = CharFilterInFilter(field_name='skill__title', lookup_expr='in').distinct
    # skill__level__gt = filters.NumberFilter(field_name='warrior_skill__level', lookup_expr='gt')

    all_skill_levels_gt = filters.NumberFilter(field_name='warrior_skill',method='filter_all_skill_levels_gt')


    class Meta:
        model = models.Warrior
        # Задает по каким значениям можем фильровать, не прописывая
        fields = {'level': ['gt', 'lt']}

    def filter_all_skill_levels_gt(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(
                num_skills=dj_models.Count(name)
            ).annotate(
                num_skills_gt_value=dj_models.Count('warrior_skill', filter=Q(warrior_skill__level__gt=value))
            ).filter(
                num_skills=dj_models.F('num_skills_gt_value')
            )
        return queryset

    @property
    def qs(self):
        # Более низкоуровневый чем queryset в view
        # return None
        return super(WarriorNameFilter, self).qs



