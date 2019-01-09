from app import models
from django import http
from django.contrib import auth
import copy
import datetime
import random

from pprint import pprint
import pydash as _; _.map = _.map_; _.filter = _.filter_
import itertools
import inspect



def setup(req):
  def take(coll, n):
    chunk = coll[0:n]
    del coll[0:n]
    return chunk
  
  
  def take_random(coll, n):
    if n == 0:
      return []
    
    chunk = _.sample(coll, n)
    
    for item in chunk:
      coll.remove(item)
    
    return chunk
  
  
  def take_one_random(coll):
    if len(coll) == 0:
      return None
    
    return coll.pop(_.random(0, len(coll)-1))
  
  
  def random_phone():
    return '+7(' + str(_.sample((917, 964, 965, 987, 912, 935))) + ')' + str(_.random(1000000, 9999999))
  
  
  def random_date():
    return datetime.datetime(_.random(2010, 2016), _.random(1, 12), _.random(1, 28))
  
  
  def random_amount():
    return random.random() * random.choice((100, 1000, 10000))
  
  
  
  models.User.objects.create_superuser('admin', '', 'thisismypassword')
  
  
  
  _root = models.Category.objects.create(name='_root'); \
  
  obuv = models.Category.objects.create(name='Обувь', parent=_root); \
    models.Category.objects.create(name='ботинки', parent=obuv); \
    models.Category.objects.create(name='сандалии/босоножки', parent=obuv); \
    models.Category.objects.create(name='балетки / туфли', parent=obuv); \
    models.Category.objects.create(name='шлепанцы', parent=obuv); \
    models.Category.objects.create(name='кросовки/кеды', parent=obuv); \
    models.Category.objects.create(name='мокасины', parent=obuv); \
    models.Category.objects.create(name='резиновые сапоги', parent=obuv); \
    models.Category.objects.create(name='сноубутсы', parent=obuv); \
    models.Category.objects.create(name='валенки', parent=obuv); \
    models.Category.objects.create(name='сапоги', parent=obuv); \
    models.Category.objects.create(name='унты', parent=obuv); \
    models.Category.objects.create(name='угги', parent=obuv); \
  
  odezhda = models.Category.objects.create(name='Одежда', parent=_root); \
    x = models.Category.objects.create(name='одежда для новорожденных', parent=odezhda); \
      models.Category.objects.create(name='конверты', parent=x); \
      models.Category.objects.create(name='царапки', parent=x); \
      models.Category.objects.create(name='пинетки', parent=x); \
      models.Category.objects.create(name='пеленки', parent=x); \
      models.Category.objects.create(name='комбинезоны', parent=x); \
      models.Category.objects.create(name='на крещение', parent=x); \
    models.Category.objects.create(name='бодики/песочники', parent=odezhda); \
    models.Category.objects.create(name='для плавания', parent=odezhda); \
    models.Category.objects.create(name='футболки / топы', parent=odezhda); \
    models.Category.objects.create(name='шорты/юбки', parent=odezhda); \
    models.Category.objects.create(name='платья', parent=odezhda); \
    models.Category.objects.create(name='брюки', parent=odezhda); \
    models.Category.objects.create(name='рубашки/сорочки', parent=odezhda); \
    models.Category.objects.create(name='костюмы/пиджаки', parent=odezhda); \
    models.Category.objects.create(name='школьная форма', parent=odezhda); \
    models.Category.objects.create(name='маскарадные костюмы', parent=odezhda); \
    models.Category.objects.create(name='комплекты', parent=odezhda); \
    models.Category.objects.create(name='свитеры и кардиганы', parent=odezhda); \
    models.Category.objects.create(name='толстовки', parent=odezhda); \
    models.Category.objects.create(name='жилеты', parent=odezhda); \
    models.Category.objects.create(name='куртки/пуховики', parent=odezhda); \
    models.Category.objects.create(name='пальто/шубы', parent=odezhda); \
    models.Category.objects.create(name='комбинезоны', parent=odezhda); \
    models.Category.objects.create(name='головные уборы', parent=odezhda); \
    models.Category.objects.create(name='шарфы', parent=odezhda); \
    models.Category.objects.create(name='одежда для рук', parent=odezhda); \
  
  detsk_mebel = models.Category.objects.create(name='Детская мебель', parent=_root); \
    models.Category.objects.create(name='кроватки', parent=detsk_mebel); \
    models.Category.objects.create(name='колыбельки/люльки', parent=detsk_mebel); \
    models.Category.objects.create(name='комоды', parent=detsk_mebel); \
    models.Category.objects.create(name='манежи', parent=detsk_mebel); \
    models.Category.objects.create(name='пеленальные столики/доски', parent=detsk_mebel); \
    models.Category.objects.create(name='стульчики для кормления', parent=detsk_mebel); \
    models.Category.objects.create(name='шезлонги/качели', parent=detsk_mebel); \
    models.Category.objects.create(name='ходунки, прыгунки', parent=detsk_mebel); \
    models.Category.objects.create(name='стулья', parent=detsk_mebel); \
    models.Category.objects.create(name='столы', parent=detsk_mebel); \
    models.Category.objects.create(name='комплекты мебели', parent=detsk_mebel); \
    models.Category.objects.create(name='детские спортивные комплексы', parent=detsk_mebel); \
    models.Category.objects.create(name='детские ковры', parent=detsk_mebel); \
    models.Category.objects.create(name='элементы безопасности', parent=detsk_mebel); \
  
  igrushki = models.Category.objects.create(name='Игрушки', parent=_root); \
    x = models.Category.objects.create(name='Для новорожденных', parent=igrushki); \
      models.Category.objects.create(name='погремушки/прорезыватели', parent=x); \
      models.Category.objects.create(name='мобили', parent=x); \
      models.Category.objects.create(name='игровые столики', parent=x); \
      models.Category.objects.create(name='игрушки для автокресел и колясок', parent=x); \
      models.Category.objects.create(name='пирамидки', parent=x); \
      models.Category.objects.create(name='проекторы и ночники', parent=x); \
      models.Category.objects.create(name='развивающие коврики', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    models.Category.objects.create(name='детские книги', parent=igrushki); \
    models.Category.objects.create(name='мягкие', parent=igrushki); \
    models.Category.objects.create(name='интерактивные', parent=igrushki); \
    models.Category.objects.create(name='экологичные', parent=igrushki); \
    x = models.Category.objects.create(name='головоломки и конструкторы', parent=igrushki); \
      models.Category.objects.create(name='конструкторы', parent=x); \
      models.Category.objects.create(name='кубики', parent=x); \
      models.Category.objects.create(name='сортеры/головоломки', parent=x); \
      models.Category.objects.create(name='мозайки / паззлы', parent=x); \
      models.Category.objects.create(name='шнуровки', parent=x); \
      models.Category.objects.create(name='рамки-вкладыши', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    x = models.Category.objects.create(name='кукольный мир', parent=igrushki); \
      models.Category.objects.create(name='куклы', parent=x); \
      models.Category.objects.create(name='кукольные домики и аксессуары', parent=x); \
      models.Category.objects.create(name='игрушечные коляски', parent=x); \
      models.Category.objects.create(name='игрушечные кроватки', parent=x); \
    x = models.Category.objects.create(name='ролевые игры', parent=igrushki); \
      models.Category.objects.create(name='шпионы/полицейские', parent=x); \
      models.Category.objects.create(name='детские театры', parent=x); \
      models.Category.objects.create(name='детская посуда', parent=x); \
      models.Category.objects.create(name='наборы инструментов', parent=x); \
      models.Category.objects.create(name='наборы доктора', parent=x); \
      models.Category.objects.create(name='научные игры', parent=x); \
      models.Category.objects.create(name='все для кухни', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    x = models.Category.objects.create(name='крупные игрушки', parent=igrushki); \
      models.Category.objects.create(name='палатки / домики', parent=x); \
      models.Category.objects.create(name='игрушки качалки', parent=x); \
      models.Category.objects.create(name='ящики для игрушек', parent=x); \
      models.Category.objects.create(name='мячи/прыгуны', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    models.Category.objects.create(name='игрушечное оружие', parent=igrushki); \
    models.Category.objects.create(name='фигурки героев / солдатики', parent=igrushki); \
    x = models.Category.objects.create(name='творчество', parent=igrushki); \
      models.Category.objects.create(name='доски и мольберты', parent=x); \
      models.Category.objects.create(name='наборы для рисования', parent=x); \
      models.Category.objects.create(name='аппликации и наклейки', parent=x); \
      models.Category.objects.create(name='бисер и шитье', parent=x); \
      models.Category.objects.create(name='пластилин / лепка', parent=x); \
      models.Category.objects.create(name='кинетический песок', parent=x); \
      models.Category.objects.create(name='музыкальные инструменты', parent=x); \
      models.Category.objects.create(name='неокубики', parent=x); \
      models.Category.objects.create(name='муравьиные фермы', parent=x); \
      models.Category.objects.create(name='танцевальные коврики', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    x = models.Category.objects.create(name='техника/транспорт', parent=igrushki); \
      models.Category.objects.create(name='железные дороги', parent=x); \
      models.Category.objects.create(name='игрушечные треки и гаражи', parent=x); \
      models.Category.objects.create(name='корабли и лодки', parent=x); \
      models.Category.objects.create(name='машинки', parent=x); \
      models.Category.objects.create(name='электромобили', parent=x); \
      models.Category.objects.create(name='каталки', parent=x); \
      models.Category.objects.create(name='педальные машинки', parent=x); \
      models.Category.objects.create(name='радиоуправляемые', parent=x); \
      models.Category.objects.create(name='самолеты/вертолеты', parent=x); \
      models.Category.objects.create(name='военная техника', parent=x); \
      models.Category.objects.create(name='сборные модели', parent=x); \
    x = models.Category.objects.create(name='настольные игры', parent=igrushki); \
      models.Category.objects.create(name='бильярд', parent=x); \
      models.Category.objects.create(name='дартс', parent=x); \
      models.Category.objects.create(name='домино', parent=x); \
      models.Category.objects.create(name='лото', parent=x); \
      models.Category.objects.create(name='настольный хоккей/футбол', parent=x); \
      models.Category.objects.create(name='морской бой', parent=x); \
      models.Category.objects.create(name='монополия', parent=x); \
      models.Category.objects.create(name='стратегии', parent=x); \
      models.Category.objects.create(name='квесты', parent=x); \
      models.Category.objects.create(name='шахматы/шашки/нарды', parent=x); \
      models.Category.objects.create(name='твистер', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
  
  avtokresla = models.Category.objects.create(name='Автокресла', parent=_root); \
    models.Category.objects.create(name='автокресло', parent=avtokresla); \
    models.Category.objects.create(name='бустер', parent=avtokresla); \
    models.Category.objects.create(name='аксессуары для автокресел', parent=avtokresla); \
    models.Category.objects.create(name='аксессуары для путешествий', parent=avtokresla); \
  
  vse_dlya_vannoy = models.Category.objects.create(name='Всё для ванной', parent=_root); \
    models.Category.objects.create(name='Накопители подгузников', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Подгузники', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Весы для детей', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Горшки', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Подставки для умывания', parent=vse_dlya_vannoy); \
    x = models.Category.objects.create(name='Детская косметика', parent=vse_dlya_vannoy); \
      models.Category.objects.create(name='зубная паста', parent=x); \
      models.Category.objects.create(name='уход за кожей', parent=x); \
      models.Category.objects.create(name='уход за волосами', parent=x); \
      models.Category.objects.create(name='наборы', parent=x); \
      models.Category.objects.create(name='декоративная косметика', parent=x); \
      models.Category.objects.create(name='парфюмерия', parent=x); \
      models.Category.objects.create(name='прочее', parent=x); \
    models.Category.objects.create(name='Термометры', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Товары для здоровья', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='Увлажнители и очистители воздуха', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='ванночки', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='горки и сиденья для ванн', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='полотенца', parent=vse_dlya_vannoy); \
    models.Category.objects.create(name='все для купания', parent=vse_dlya_vannoy); \
  
  pomosch_mame = models.Category.objects.create(name='Помощь маме', parent=_root); \
    models.Category.objects.create(name='радио-няни / рации', parent=pomosch_mame); \
    models.Category.objects.create(name='видео-няни', parent=pomosch_mame); \
    models.Category.objects.create(name='мониторы для дыхания', parent=pomosch_mame); \
    models.Category.objects.create(name='сумки', parent=pomosch_mame); \
    models.Category.objects.create(name='молокоотсосы', parent=pomosch_mame); \
    models.Category.objects.create(name='стерилизаторы', parent=pomosch_mame); \
    models.Category.objects.create(name='сушилки для бутылочек', parent=pomosch_mame); \
    models.Category.objects.create(name='подогреватели', parent=pomosch_mame); \
    models.Category.objects.create(name='блендеры-пароварки', parent=pomosch_mame); \
    models.Category.objects.create(name='измельчители/комбайны', parent=pomosch_mame); \
    models.Category.objects.create(name='аксессуары для кормления', parent=pomosch_mame); \
    models.Category.objects.create(name='подушки', parent=pomosch_mame); \
    models.Category.objects.create(name='бутылочки детские', parent=pomosch_mame); \
    models.Category.objects.create(name='поильники', parent=pomosch_mame); \
    models.Category.objects.create(name='термосы', parent=pomosch_mame); \
    models.Category.objects.create(name='термосумки', parent=pomosch_mame); \
    models.Category.objects.create(name='детское питание', parent=pomosch_mame); \
    models.Category.objects.create(name='одежда для беременных', parent=pomosch_mame); \
    models.Category.objects.create(name='детская посуда', parent=pomosch_mame); \
  
  kolyaski = models.Category.objects.create(name='Коляски', parent=_root); \
    models.Category.objects.create(name='коляски-люльки', parent=kolyaski); \
    models.Category.objects.create(name='прогулочная коляска', parent=kolyaski); \
    x = models.Category.objects.create(name='коляска универсальная', parent=kolyaski); \
      models.Category.objects.create(name='трансформер', parent=x); \
      models.Category.objects.create(name='универсальная (2 в 1)', parent=x); \
      models.Category.objects.create(name='универсальная (3 в 1)', parent=x); \
    models.Category.objects.create(name='коляски для двойни и более', parent=kolyaski); \
    models.Category.objects.create(name='аксессуары для колясок', parent=kolyaski); \

  
  
  
  
  
  
  
  
  
  
  
  
  igry_na_ulitse = models.Category.objects.create(name='Игры на улице', parent=_root); \
    models.Category.objects.create(name='бассейны и аксессуары', parent=igry_na_ulitse); \
    models.Category.objects.create(name='батуты и аксессуары', parent=igry_na_ulitse); \
    models.Category.objects.create(name='качели', parent=igry_na_ulitse); \
    models.Category.objects.create(name='игровые комплексы', parent=igry_na_ulitse); \
    models.Category.objects.create(name='горки', parent=igry_na_ulitse); \
    models.Category.objects.create(name='песочницы', parent=igry_na_ulitse); \
    models.Category.objects.create(name='аксессуары для песочницы', parent=igry_na_ulitse); \
    models.Category.objects.create(name='игровые домики и палатки', parent=igry_na_ulitse); \
    x = models.Category.objects.create(name='велотехника', parent=igry_na_ulitse); \
      models.Category.objects.create(name='беговелы', parent=x); \
      models.Category.objects.create(name='вело-мобили', parent=x); \
      models.Category.objects.create(name='велосипеды', parent=x); \
    models.Category.objects.create(name='электро-мобили', parent=igry_na_ulitse); \
    models.Category.objects.create(name='самокаты', parent=igry_na_ulitse); \
    models.Category.objects.create(name='санки / снегокаты', parent=igry_na_ulitse); \
    models.Category.objects.create(name='лыжи и сноуборды', parent=igry_na_ulitse); \
    models.Category.objects.create(name='коньки ледовые', parent=igry_na_ulitse); \
    models.Category.objects.create(name='скейтборды', parent=igry_na_ulitse); \
    models.Category.objects.create(name='ролики', parent=igry_na_ulitse); \
    models.Category.objects.create(name='воздушные змеи', parent=igry_na_ulitse); \
    models.Category.objects.create(name='комплекты защиты', parent=igry_na_ulitse); \
    models.Category.objects.create(name='спортивные игры', parent=igry_na_ulitse); \
  
  postel = models.Category.objects.create(name='Постельные принадлежности', parent=_root); \
    models.Category.objects.create(name='постельное белье', parent=postel); \
    models.Category.objects.create(name='матрасы', parent=postel); \
    models.Category.objects.create(name='наматрасники', parent=postel); \
    models.Category.objects.create(name='подушки', parent=postel); \
    models.Category.objects.create(name='одеяла', parent=postel); \
    models.Category.objects.create(name='подвески', parent=postel); \
    models.Category.objects.create(name='бортики/бамперы', parent=postel); \
    models.Category.objects.create(name='позиционеры для сна', parent=postel); \
    models.Category.objects.create(name='спальные пижамы/ спальные мешки', parent=postel); \
    models.Category.objects.create(name='одеяла', parent=postel); \
    models.Category.objects.create(name='электропростыни', parent=postel); \
    models.Category.objects.create(name='пледы', parent=postel); \
  
  shkola = models.Category.objects.create(name='Школа', parent=_root); \
    models.Category.objects.create(name='школьная форма', parent=shkola); \
    models.Category.objects.create(name='ранцы/рюкзаки', parent=shkola); \
    models.Category.objects.create(name='пеналы', parent=shkola); \
    models.Category.objects.create(name='парты', parent=shkola); \
    models.Category.objects.create(name='прочее', parent=shkola); \
  
  
  
  
  _root = models.Location.objects.create(name='_root'); \
  
  x = models.Location.objects.create(name='Амурская область', type='region', parent=_root); \
    y = models.Location.objects.create(name='Томск', type='town', parent=x); \
      z = models.Location.objects.create(name='Первый район', type='district', parent=y); \
        models.Location.objects.create(name='Технопарк', type='subway', parent=z); \
        models.Location.objects.create(name='Бульвар Рокоссовского', type='subway', parent=z); \
        models.Location.objects.create(name='Театральная', type='subway', parent=z); \
      z = models.Location.objects.create(name='Второй район', type='district', parent=y); \
        models.Location.objects.create(name='Ботанический сад', type='subway', parent=z); \
        models.Location.objects.create(name='Академическая', type='subway', parent=z); \
        models.Location.objects.create(name='Чистые пруды', type='subway', parent=z); \
        models.Location.objects.create(name='Царицыно', type='subway', parent=z); \
        models.Location.objects.create(name='Планерная', type='subway', parent=z); \
        models.Location.objects.create(name='Маяковская', type='subway', parent=z); \
  
  
  x = models.Location.objects.create(name='Архангельская область', type='region', parent=_root); \
    y = models.Location.objects.create(name='Кемерово', type='town', parent=x); \
      z = models.Location.objects.create(name='Третий район', type='district', parent=y); \
        models.Location.objects.create(name='Пятницкое шоссе', type='subway', parent=z); \
        models.Location.objects.create(name='Славянский бульвар', type='subway', parent=z); \
        models.Location.objects.create(name='Полежаевская', type='subway', parent=z); \
      z = models.Location.objects.create(name='Четвёртый район', type='district', parent=y); \
        models.Location.objects.create(name='Волгоградский проспект', type='subway', parent=z); \
        models.Location.objects.create(name='Комсомольская', type='subway', parent=z); \
        models.Location.objects.create(name='Ясенево', type='subway', parent=z); \
        models.Location.objects.create(name='Фрунзенская', type='subway', parent=z); \
        models.Location.objects.create(name='Бибирево', type='subway', parent=z); \
      z = models.Location.objects.create(name='Пятый район', type='district', parent=y); \
        models.Location.objects.create(name='Войковская', type='subway', parent=z); \
        models.Location.objects.create(name='Белорусская', type='subway', parent=z); \
        models.Location.objects.create(name='Волоколамская', type='subway', parent=z); \
        models.Location.objects.create(name='Новокосино', type='subway', parent=z); \
        models.Location.objects.create(name='Деловой центр', type='subway', parent=z); \
  
  
  x = models.Location.objects.create(name='Белгородская область', type='region', parent=_root); \
    y = models.Location.objects.create(name='Великий Новгород', type='town', parent=x); \
      models.Location.objects.create(name='Шестой район', type='district', parent=y); \
      models.Location.objects.create(name='Седьмой район', type='district', parent=y); \
      models.Location.objects.create(name='Восьмой район', type='district', parent=y); \
      models.Location.objects.create(name='Девятый район', type='district', parent=y); \
      models.Location.objects.create(name='Десятый район', type='district', parent=y); \
  
  
  
  
  adverts = _.times(lambda i: models.Advert.objects.create(name='advert-%s' % i), 500)
  categories = models.Category.objects.order_by('?')[:100] # 100 random records
  locations = models.Location.objects.get(name='_root').get_descendants()
  user_types = ('person', 'company', None)
  
  
  
  adverts_ = copy.copy(adverts)
  
  for cat in categories:
    cat.adverts = take(adverts_, _.random(1, 10))
    cat.save()
  
  
  
  def create_user(i):
    username = 'user-%s' % i
    
    return models.User.objects.create(
      email = '%s@example.com' % username,
      first_name = username.capitalize(),
      last_name = 'Mc' + username.capitalize() + _.sample(('son', 'lds', 'ker', 'ters')),
      location = locations.order_by('?').first(),
      type = _.sample(user_types),
      username = username,
    )
  
  users = _.times(create_user, 100)
  
  
  
  adverts_ = copy.copy(adverts)
  
  
  for user in users:
    user.adverts = take(adverts_, _.random(0, 15))
    user.set_password('123')
    
    user.save()
  
  
  
  return http.HttpResponse('OK')





#----------------------------------------------------------------






# airplanes__MATERIALS = eav.models.EnumGroup.objects.create(name='airplanes__MATERIALS') # no `slug` attribute
# 
# airplanes__MATERIALS.enums = tuple(map(
#   lambda v: eav.models.EnumValue.objects.create(value=v),
#   ('airplanes__MATERIALS__plastic', 'airplanes__MATERIALS__rubber', 'airplanes__MATERIALS__wood'),
# ))
# 
# Attribute.objects.create(
#   name='age', slug='airplanes__age', datatype=Attribute.TYPE_INT, django_model=airplanes,
# )
# 
# Attribute.objects.create(
#   name='has sound fx', slug='airplanes__has_sound_fx', datatype=Attribute.TYPE_BOOLEAN, django_model=airplanes,
# )
# 
# Attribute.objects.create(
#   name='has light fx', slug='airplanes__has_light_fx', datatype=Attribute.TYPE_BOOLEAN, django_model=airplanes,
# )
# 
# Attribute.objects.create(
#   name='power', slug='airplanes__power', datatype=Attribute.TYPE_INT, django_model=airplanes,
# )
# 
# Attribute.objects.create(
#   name='material', slug='airplanes__material', datatype=Attribute.TYPE_ENUM, enum_group=airplanes__MATERIALS,
# )
# 
# 
# 
# Attribute.objects.create(
#   name='brand', slug='vaporizers__brand', datatype=Attribute.TYPE_TEXT, django_model=vaporizers,
# )
# 
# Attribute.objects.create(
#   name='is ionic', slug='vaporizers__is_ionic', datatype=Attribute.TYPE_BOOLEAN, django_model=vaporizers,
# )
# 
# 
# 
# jackets__MATERIALS = eav.models.EnumGroup.objects.create(name='jackets__MATERIALS')
# 
# jackets__MATERIALS.enums = tuple(map(
#   lambda v: eav.models.EnumValue.objects.create(value=v),
#   
#   (
#     'jackets__MATERIALS__cotton',
#     'jackets__MATERIALS__denim',
#     'jackets__MATERIALS__leather',
#     'jackets__MATERIALS__fur',
#     'jackets__MATERIALS__nylon',
#   ),
# ))
# 
# Attribute.objects.create(
#   name='brand', slug='jackets__brand', datatype=Attribute.TYPE_TEXT, django_model=jackets,
# )
# 
# Attribute.objects.create(
#   name='size', slug='jackets__size', datatype=Attribute.TYPE_INT, django_model=jackets,
# )
# 
# Attribute.objects.create(
#   name='material', slug='jackets__material', datatype=Attribute.TYPE_ENUM, enum_group=jackets__MATERIALS,
# )
# 
# 
# 
# x = Advert.objects.filter(category__name='airplanes')[0]
# x.eav.airplanes__age=10; x.eav.airplanes__has_light_fx=True; x.eav.airplanes__has_sound_fx=False; x.eav.airplanes__power=85; x.save()
# 
# x = Advert.objects.filter(category__name='airplanes')[1]
# x.eav.airplanes__age=16; x.eav.airplanes__has_light_fx=True; x.eav.airplanes__has_sound_fx=True; x.eav.airplanes__power=100; x.save()
# 
# 
# x = Advert.objects.filter(category__name='vaporizers')[0]
# x.eav.vaporizers__brand='brand-1'; x.eav.vaporizers__is_ionic=True; x.save()
# 
# x = Advert.objects.filter(category__name='vaporizers')[1]
# x.eav.vaporizers__brand='brand-2'; x.eav.vaporizers__is_ionic=False; x.save()
# 
# 
# x = Advert.objects.filter(category__name='jackets')[0]
# material = eav.models.EnumGroup.objects.get(name='jackets__MATERIALS').enums.get(value='jackets__MATERIALS__denim')
# x.eav.jackets__size=38; x.eav.jackets__material=material; x.save()
# 
# x = Advert.objects.filter(category__name='jackets')[1]
# material = eav.models.EnumGroup.objects.get(name='jackets__MATERIALS').enums.get(value='jackets__MATERIALS__cotton')
# x.eav.jackets__size=45; x.eav.jackets__material=material; x.save()
