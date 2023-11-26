# Практика 3.1 сырая

### Упражнение 1

'''python 
from project_first_app.models import  Car, UserOwner, CarOwn, OwnerLicence 


from django.contrib.auth import get_user_model
user_model = get_user_model()


c1 = Car(id=1, serial_number='AA001A', model='toyota', color='black')
c1.save()
c2 = Car(id=2, serial_number='AA002A', model='toyota', color='white')
c2.save()
c3 = Car(id=3, serial_number='AA003A', model='toyota', color='orange')
c3.save()
c4 = Car(id=4, serial_number='AA004A', model='ford', color='black')
c4.save()
c5 = Car(id=5, serial_number='AA005A', model='ford', color='white')
c5.save()
c6 = Car(id=6, serial_number='AA006A', model='ford', color='orange')

1 = user_model(username='vasy001', first_name='Vasy', last_name='Pupkin', passport_number='00001000001')
u1.save()
u2 = user_model(username='vasy002', first_name='Ivan', last_name='Kotov', passport_number='00001000002')
u2.save()
u3 = user_model(username='vasy003', first_name='Vasy', last_name='Kozlov', passport_number='00001000003')
u3.save()
u4 = user_model(username='vasy004', first_name='Vasy', last_name='User', passport_number='00001000004')
u4.save()
u5 = user_model(username='vasy005', first_name='Jojo', last_name='Reference', passport_number='00001000005')
u5.save()
u6 = user_model(username='vasy006', first_name='Ivan', last_name='User', passport_number='00001000006')
u6.save()


car_own_list = [[u1, c1, '2022-11-01 00:00:00+03:00', '2022-11-04 00:00:00+03:00'],
                [u1, c2, '2022-11-01 00:00:00+03:00', '2022-11-04 00:00:00+03:00'],
                [u2, c1, '2022-11-04 00:00:00+03:00', '2022-11-10 00:00:00+03:00'],
                [u2, c2, '2022-11-04 00:00:00+03:00', '2022-11-10 00:00:00+03:00'],
                [u3, c3, '2022-11-01 00:00:00+03:00', '2022-11-04 00:00:00+03:00'],
                [u4, c3, '2022-11-04 00:00:00+03:00', '2022-11-10 00:00:00+03:00'],
                [u4, c4, '2022-11-01 00:00:00+03:00', '2022-11-04 00:00:00+03:00'],
                [u5, c4, '2022-11-04 00:00:00+03:00', '2022-11-10 00:00:00+03:00'],
                [u5, c5, '2022-11-01 00:00:00+03:00', '2022-11-04 00:00:00+03:00'],
                [u5, c6, '2022-11-04 00:00:00+03:00', '2022-11-10 00:00:00+03:00']]


for owner, car, start_date, end_date in car_own_list:
    print(car, owner)
    CarOwn(owner=owner, car=car, start_date=start_date, end_date=end_date).save()

for i, user in enumerate([u1, u2, u3, u4, u5, u6]):
    OwnerLicence(owner=user, Licence_number=f'000{i}', licence_type='default', issue_date='2022-11-01').save()
'''


'''
Car.objects.all()
<QuerySet [<Car: AA001A>, <Car: AA002A>, <Car: AA003A>, <Car: AA004A>, <Car: AA005A>]>

UserOwner.objects.all()
<QuerySet [<UserOwner: vasy001>, <UserOwner: vasy002>, 
            <UserOwner: vasy003>, <UserOwner: vasy004>, 
            <UserOwner: vasy005>, <UserOwner: vasy006>]>


CarOwn.objects.all()
<QuerySet [<CarOwn: vasy001 AA001A 2022-10-31 2022-11-03>, 
<CarOwn: vasy001 AA002A 2022-10-31 2022-11-03>, 
<CarOwn: vasy002 AA001A 2022-11-03 2022-11-09>, 
<CarOwn: vasy002 AA002A 2022-11-03 2022-11-09>,
<CarOwn: vasy003 AA003A 2022-10-31 2022-11-03>,
<CarOwn: vasy004 AA003A 2022-11-03 2022-11-09>, 
<CarOwn: vasy004 AA004A 2022-10-31 2022-11-03>, 
<CarOwn: vasy005 AA004A 2022-11-03 2022-11-09>,
<CarOwn: vasy005 AA005A 2022-10-31 2022-11-03>]>
'''


### Задание 2

Выведете все машины марки “Toyota” (или любой другой марки, которая у вас есть)
Car.objects.filter(model='ford')
<QuerySet [<Car: AA004A>, <Car: AA005A>]>


Найти всех водителей с именем “Олег” (или любым другим именем на ваше усмотрение)
UserOwner.objects.filter(first_name='Vasy')
<QuerySet [<UserOwner: vasy001>, <UserOwner: vasy003>, <UserOwner: vasy004>]>


Взяв любого случайного владельца получить его id, и по этому id получить экземпляр удостоверения в виде объекта модели (можно в 2 запроса)
from random import choice
rand_user = choice(user_model.objects.all())
_id = rand_user.id
licence = rand_user.owner_licence.get()
licence

<OwnerLicence: vasy003 0002>


Вывести всех владельцев красных машин (или любого другого цвета, который у вас присутствует)

UserOwner.objects.filter(owner_car__car__color='black')
UserOwner.objects.filter(cars__color='black')
<QuerySet [<UserOwner: vasy001>, <UserOwner: vasy002>, <UserOwner: vasy004>, <UserOwner: vasy005>]>


Найти всех владельцев, чей год владения машиной начинается с 2010 (или любой другой год, который присутствует у вас в базе)
UserOwner.objects.filter(owner_car__start_date__year='2022').distinct()
<QuerySet [<UserOwner: vasy001>, <UserOwner: vasy002>, <UserOwner: vasy003>, <UserOwner: vasy004>, <UserOwner: vasy005>]>


### Задание 3

OwnerLicence.objects.aggregate(max_issue_date = models.Max('issue_date'))
{'max_issue_date': datetime.date(2022, 11, 1)}

CarOwn.objects.aggregate(latest_start_date=models.Max('start_date'))
{'latest_start_date': datetime.datetime(2022, 11, 3, 21, 0, tzinfo=datetime.timezone.utc)}



count_by_user = UserOwner.objects.annotate(count=models.Count('owner_car'))
for user_count in count_by_user:
    print(user_count.username, user_count.count)
vsevolod026 0
vasy001 2
vasy002 2
vasy003 1
vasy004 2
vasy005 2
vasy006 0


count_by_model = Car.objects.values('model').annotate(count=models.Count('id'))
for model_counter in count_by_model:
    print(model_counter['model'], model_counter['count'])
    
ford 2
toyota 3

OwnerLicence.objects.order_by('issue_date')
<QuerySet [<OwnerLicence: vasy001 0000>, <OwnerLicence: vasy002 0001>, <OwnerLicence: vasy003 0002>, <OwnerLicence: vasy004 0003>, <OwnerLicence: vasy005 0004>, <OwnerLicence: vasy006 0005>]>