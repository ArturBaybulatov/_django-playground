from django.db import models
from django.core import urlresolvers
import mptt.models
import autoslug
import trans

from pprint import pprint
import pydash as _; _.map = _.map_; _.filter = _.filter_
import itertools
import inspect



def slugify(val):
  return trans.trans(val, 'slug').lower()


class Category(mptt.models.MPTTModel):
  name = models.CharField(max_length=50)
  slug = autoslug.AutoSlugField(populate_from='name', slugify=slugify, primary_key=True, unique=True, db_index=True)
  parent = mptt.models.TreeForeignKey('self', blank=True, null=True, related_name='children', db_index=True)
  hidden = models.NullBooleanField(blank=True, null=True)
  foo = models.CharField(max_length=10, blank=True, null=True)
  
  class Meta:
    verbose_name_plural = 'categories'
  
  # class MPTTMeta:
  #   order_insertion_by = ['name']
  
  def __str__(self):
    return self.name + ' (' + self.slug + ')'
  
  def get_absolute_url(self):
    return urlresolvers.reverse('category-update', kwargs={'slug': self.slug})






class Advert(models.Model):
  name = models.CharField(max_length=50)
  category = mptt.models.TreeForeignKey('Category', related_name='adverts', blank=True, null=True)
  # bar = models.CharField(max_length=10, blank=True, null=True)
  
  def get_absolute_url(self):
    return urlresolvers.reverse('advert-update', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name_plural = 'adverts'
  
  def __str__(self):
    return self.name





class AdvertPicture(models.Model):
  file = models.ImageField(upload_to='media')
  advert = models.ForeignKey('Advert', related_name='pictures', blank=True, null=True)
  
  class Meta:
    verbose_name_plural = 'advert-pictures'
  
  def __str__(self):
    return self.file.name








#------------------------------------


def setup():
  import django.contrib.auth.models
  django.contrib.auth.models.User.objects.create_superuser('admin', '', 'thisismypassword')
  
  
  
  _root = Category.objects.create(name='_root'); \
  
  obuv = Category.objects.create(name='Обувь', parent=_root); \
    Category.objects.create(name='ботинки', parent=obuv); \
    Category.objects.create(name='сандалии/босоножки', parent=obuv); \
    Category.objects.create(name='балетки / туфли', parent=obuv); \
    Category.objects.create(name='шлепанцы', parent=obuv); \
    Category.objects.create(name='кросовки/кеды', parent=obuv); \
    Category.objects.create(name='мокасины', parent=obuv); \
    Category.objects.create(name='резиновые сапоги', parent=obuv); \
    Category.objects.create(name='сноубутсы', parent=obuv); \
    Category.objects.create(name='валенки', parent=obuv); \
    Category.objects.create(name='сапоги', parent=obuv); \
    Category.objects.create(name='унты', parent=obuv); \
    Category.objects.create(name='угги', parent=obuv); \
  
  odezhda = Category.objects.create(name='Одежда', parent=_root); \
    x = Category.objects.create(name='одежда для новорожденных', parent=odezhda); \
      Category.objects.create(name='конверты', parent=x); \
      Category.objects.create(name='царапки', parent=x); \
      Category.objects.create(name='пинетки', parent=x); \
      Category.objects.create(name='пеленки', parent=x); \
      Category.objects.create(name='комбинезоны', parent=x); \
      Category.objects.create(name='на крещение', parent=x); \
    Category.objects.create(name='бодики/песочники', parent=odezhda); \
    Category.objects.create(name='для плавания', parent=odezhda); \
    Category.objects.create(name='футболки / топы', parent=odezhda); \
    Category.objects.create(name='шорты/юбки', parent=odezhda); \
    Category.objects.create(name='платья', parent=odezhda); \
    Category.objects.create(name='брюки', parent=odezhda); \
    Category.objects.create(name='рубашки/сорочки', parent=odezhda); \
    Category.objects.create(name='костюмы/пиджаки', parent=odezhda); \
    Category.objects.create(name='школьная форма', parent=odezhda); \
    Category.objects.create(name='маскарадные костюмы', parent=odezhda); \
    Category.objects.create(name='комплекты', parent=odezhda); \
    Category.objects.create(name='свитеры и кардиганы', parent=odezhda); \
    Category.objects.create(name='толстовки', parent=odezhda); \
    Category.objects.create(name='жилеты', parent=odezhda); \
    Category.objects.create(name='куртки/пуховики', parent=odezhda); \
    Category.objects.create(name='пальто/шубы', parent=odezhda); \
    Category.objects.create(name='комбинезоны', parent=odezhda); \
    Category.objects.create(name='головные уборы', parent=odezhda); \
    Category.objects.create(name='шарфы', parent=odezhda); \
    Category.objects.create(name='одежда для рук', parent=odezhda); \
  
  detsk_mebel = Category.objects.create(name='Детская мебель', parent=_root); \
    Category.objects.create(name='кроватки', parent=detsk_mebel); \
    Category.objects.create(name='колыбельки/люльки', parent=detsk_mebel); \
    Category.objects.create(name='комоды', parent=detsk_mebel); \
    Category.objects.create(name='манежи', parent=detsk_mebel); \
    Category.objects.create(name='пеленальные столики/доски', parent=detsk_mebel); \
    Category.objects.create(name='стульчики для кормления', parent=detsk_mebel); \
    Category.objects.create(name='шезлонги/качели', parent=detsk_mebel); \
    Category.objects.create(name='ходунки, прыгунки', parent=detsk_mebel); \
    Category.objects.create(name='стулья', parent=detsk_mebel); \
    Category.objects.create(name='столы', parent=detsk_mebel); \
    Category.objects.create(name='комплекты мебели', parent=detsk_mebel); \
    Category.objects.create(name='детские спортивные комплексы', parent=detsk_mebel); \
    Category.objects.create(name='детские ковры', parent=detsk_mebel); \
    Category.objects.create(name='элементы безопасности', parent=detsk_mebel); \
  
  igrushki = Category.objects.create(name='Игрушки', parent=_root); \
    x = Category.objects.create(name='Для новорожденных', parent=igrushki); \
      Category.objects.create(name='погремушки/прорезыватели', parent=x); \
      Category.objects.create(name='мобили', parent=x); \
      Category.objects.create(name='игровые столики', parent=x); \
      Category.objects.create(name='игрушки для автокресел и колясок', parent=x); \
      Category.objects.create(name='пирамидки', parent=x); \
      Category.objects.create(name='проекторы и ночники', parent=x); \
      Category.objects.create(name='развивающие коврики', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    Category.objects.create(name='детские книги', parent=igrushki); \
    Category.objects.create(name='мягкие', parent=igrushki); \
    Category.objects.create(name='интерактивные', parent=igrushki); \
    Category.objects.create(name='экологичные', parent=igrushki); \
    x = Category.objects.create(name='головоломки и конструкторы', parent=igrushki); \
      Category.objects.create(name='конструкторы', parent=x); \
      Category.objects.create(name='кубики', parent=x); \
      Category.objects.create(name='сортеры/головоломки', parent=x); \
      Category.objects.create(name='мозайки / паззлы', parent=x); \
      Category.objects.create(name='шнуровки', parent=x); \
      Category.objects.create(name='рамки-вкладыши', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    x = Category.objects.create(name='кукольный мир', parent=igrushki); \
      Category.objects.create(name='куклы', parent=x); \
      Category.objects.create(name='кукольные домики и аксессуары', parent=x); \
      Category.objects.create(name='игрушечные коляски', parent=x); \
      Category.objects.create(name='игрушечные кроватки', parent=x); \
    x = Category.objects.create(name='ролевые игры', parent=igrushki); \
      Category.objects.create(name='шпионы/полицейские', parent=x); \
      Category.objects.create(name='детские театры', parent=x); \
      Category.objects.create(name='детская посуда', parent=x); \
      Category.objects.create(name='наборы инструментов', parent=x); \
      Category.objects.create(name='наборы доктора', parent=x); \
      Category.objects.create(name='научные игры', parent=x); \
      Category.objects.create(name='все для кухни', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    x = Category.objects.create(name='крупные игрушки', parent=igrushki); \
      Category.objects.create(name='палатки / домики', parent=x); \
      Category.objects.create(name='игрушки качалки', parent=x); \
      Category.objects.create(name='ящики для игрушек', parent=x); \
      Category.objects.create(name='мячи/прыгуны', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    Category.objects.create(name='игрушечное оружие', parent=igrushki); \
    Category.objects.create(name='фигурки героев / солдатики', parent=igrushki); \
    x = Category.objects.create(name='творчество', parent=igrushki); \
      Category.objects.create(name='доски и мольберты', parent=x); \
      Category.objects.create(name='наборы для рисования', parent=x); \
      Category.objects.create(name='аппликации и наклейки', parent=x); \
      Category.objects.create(name='бисер и шитье', parent=x); \
      Category.objects.create(name='пластилин / лепка', parent=x); \
      Category.objects.create(name='кинетический песок', parent=x); \
      Category.objects.create(name='музыкальные инструменты', parent=x); \
      Category.objects.create(name='неокубики', parent=x); \
      Category.objects.create(name='муравьиные фермы', parent=x); \
      Category.objects.create(name='танцевальные коврики', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    x = Category.objects.create(name='техника/транспорт', parent=igrushki); \
      Category.objects.create(name='железные дороги', parent=x); \
      Category.objects.create(name='игрушечные треки и гаражи', parent=x); \
      Category.objects.create(name='корабли и лодки', parent=x); \
      Category.objects.create(name='машинки', parent=x); \
      Category.objects.create(name='электромобили', parent=x); \
      Category.objects.create(name='каталки', parent=x); \
      Category.objects.create(name='педальные машинки', parent=x); \
      Category.objects.create(name='радиоуправляемые', parent=x); \
      Category.objects.create(name='самолеты/вертолеты', parent=x); \
      Category.objects.create(name='военная техника', parent=x); \
      Category.objects.create(name='сборные модели', parent=x); \
    x = Category.objects.create(name='настольные игры', parent=igrushki); \
      Category.objects.create(name='бильярд', parent=x); \
      Category.objects.create(name='дартс', parent=x); \
      Category.objects.create(name='домино', parent=x); \
      Category.objects.create(name='лото', parent=x); \
      Category.objects.create(name='настольный хоккей/футбол', parent=x); \
      Category.objects.create(name='морской бой', parent=x); \
      Category.objects.create(name='монополия', parent=x); \
      Category.objects.create(name='стратегии', parent=x); \
      Category.objects.create(name='квесты', parent=x); \
      Category.objects.create(name='шахматы/шашки/нарды', parent=x); \
      Category.objects.create(name='твистер', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
  
  avtokresla = Category.objects.create(name='Автокресла', parent=_root); \
    Category.objects.create(name='автокресло', parent=avtokresla); \
    Category.objects.create(name='бустер', parent=avtokresla); \
    Category.objects.create(name='аксессуары для автокресел', parent=avtokresla); \
    Category.objects.create(name='аксессуары для путешествий', parent=avtokresla); \
  
  vse_dlya_vannoy = Category.objects.create(name='Всё для ванной', parent=_root); \
    Category.objects.create(name='Накопители подгузников', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Подгузники', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Весы для детей', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Горшки', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Подставки для умывания', parent=vse_dlya_vannoy); \
    x = Category.objects.create(name='Детская косметика', parent=vse_dlya_vannoy); \
      Category.objects.create(name='зубная паста', parent=x); \
      Category.objects.create(name='уход за кожей', parent=x); \
      Category.objects.create(name='уход за волосами', parent=x); \
      Category.objects.create(name='наборы', parent=x); \
      Category.objects.create(name='декоративная косметика', parent=x); \
      Category.objects.create(name='парфюмерия', parent=x); \
      Category.objects.create(name='прочее', parent=x); \
    Category.objects.create(name='Термометры', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Товары для здоровья', parent=vse_dlya_vannoy); \
    Category.objects.create(name='Увлажнители и очистители воздуха', parent=vse_dlya_vannoy); \
    Category.objects.create(name='ванночки', parent=vse_dlya_vannoy); \
    Category.objects.create(name='горки и сиденья для ванн', parent=vse_dlya_vannoy); \
    Category.objects.create(name='полотенца', parent=vse_dlya_vannoy); \
    Category.objects.create(name='все для купания', parent=vse_dlya_vannoy); \
  
  pomosch_mame = Category.objects.create(name='Помощь маме', parent=_root); \
    Category.objects.create(name='радио-няни / рации', parent=pomosch_mame); \
    Category.objects.create(name='видео-няни', parent=pomosch_mame); \
    Category.objects.create(name='мониторы для дыхания', parent=pomosch_mame); \
    Category.objects.create(name='сумки', parent=pomosch_mame); \
    Category.objects.create(name='молокоотсосы', parent=pomosch_mame); \
    Category.objects.create(name='стерилизаторы', parent=pomosch_mame); \
    Category.objects.create(name='сушилки для бутылочек', parent=pomosch_mame); \
    Category.objects.create(name='подогреватели', parent=pomosch_mame); \
    Category.objects.create(name='блендеры-пароварки', parent=pomosch_mame); \
    Category.objects.create(name='измельчители/комбайны', parent=pomosch_mame); \
    Category.objects.create(name='аксессуары для кормления', parent=pomosch_mame); \
    Category.objects.create(name='подушки', parent=pomosch_mame); \
    Category.objects.create(name='бутылочки детские', parent=pomosch_mame); \
    Category.objects.create(name='поильники', parent=pomosch_mame); \
    Category.objects.create(name='термосы', parent=pomosch_mame); \
    Category.objects.create(name='термосумки', parent=pomosch_mame); \
    Category.objects.create(name='детское питание', parent=pomosch_mame); \
    Category.objects.create(name='одежда для беременных', parent=pomosch_mame); \
    Category.objects.create(name='детская посуда', parent=pomosch_mame); \
  
  kolyaski = Category.objects.create(name='Коляски', parent=_root); \
    Category.objects.create(name='коляски-люльки', parent=kolyaski); \
    Category.objects.create(name='прогулочная коляска', parent=kolyaski); \
    x = Category.objects.create(name='коляска универсальная', parent=kolyaski); \
      Category.objects.create(name='трансформер', parent=x); \
      Category.objects.create(name='универсальная (2 в 1)', parent=x); \
      Category.objects.create(name='универсальная (3 в 1)', parent=x); \
    Category.objects.create(name='коляски для двойни и более', parent=kolyaski); \
    Category.objects.create(name='аксессуары для колясок', parent=kolyaski); \
  
  raznoe = Category.objects.create(name='Разное', parent=_root); \
  
  
  
  
  
  
  
  
  
  
  
  
  igry_na_ulitse = Category.objects.create(name='Игры на улице', parent=_root, hidden=True); \
    Category.objects.create(name='бассейны и аксессуары', parent=igry_na_ulitse); \
    Category.objects.create(name='батуты и аксессуары', parent=igry_na_ulitse); \
    Category.objects.create(name='качели', parent=igry_na_ulitse); \
    Category.objects.create(name='игровые комплексы', parent=igry_na_ulitse); \
    Category.objects.create(name='горки', parent=igry_na_ulitse); \
    Category.objects.create(name='песочницы', parent=igry_na_ulitse); \
    Category.objects.create(name='аксессуары для песочницы', parent=igry_na_ulitse); \
    Category.objects.create(name='игровые домики и палатки', parent=igry_na_ulitse); \
    x = Category.objects.create(name='велотехника', parent=igry_na_ulitse); \
      Category.objects.create(name='беговелы', parent=x); \
      Category.objects.create(name='вело-мобили', parent=x); \
      Category.objects.create(name='велосипеды', parent=x); \
    Category.objects.create(name='электро-мобили', parent=igry_na_ulitse); \
    Category.objects.create(name='самокаты', parent=igry_na_ulitse); \
    Category.objects.create(name='санки / снегокаты', parent=igry_na_ulitse); \
    Category.objects.create(name='лыжи и сноуборды', parent=igry_na_ulitse); \
    Category.objects.create(name='коньки ледовые', parent=igry_na_ulitse); \
    Category.objects.create(name='скейтборды', parent=igry_na_ulitse); \
    Category.objects.create(name='ролики', parent=igry_na_ulitse); \
    Category.objects.create(name='воздушные змеи', parent=igry_na_ulitse); \
    Category.objects.create(name='комплекты защиты', parent=igry_na_ulitse); \
    Category.objects.create(name='спортивные игры', parent=igry_na_ulitse); \
  
  postel = Category.objects.create(name='Постельные принадлежности', parent=_root, hidden=True); \
    Category.objects.create(name='постельное белье', parent=postel); \
    Category.objects.create(name='матрасы', parent=postel); \
    Category.objects.create(name='наматрасники', parent=postel); \
    Category.objects.create(name='подушки', parent=postel); \
    Category.objects.create(name='одеяла', parent=postel); \
    Category.objects.create(name='подвески', parent=postel); \
    Category.objects.create(name='бортики/бамперы', parent=postel); \
    Category.objects.create(name='позиционеры для сна', parent=postel); \
    Category.objects.create(name='спальные пижамы/ спальные мешки', parent=postel); \
    Category.objects.create(name='одеяла', parent=postel); \
    Category.objects.create(name='электропростыни', parent=postel); \
    Category.objects.create(name='пледы', parent=postel); \
  
  shkola = Category.objects.create(name='Школа', parent=_root, hidden=True); \
    Category.objects.create(name='школьная форма', parent=shkola); \
    Category.objects.create(name='ранцы/рюкзаки', parent=shkola); \
    Category.objects.create(name='пеналы', parent=shkola); \
    Category.objects.create(name='парты', parent=shkola); \
    Category.objects.create(name='прочее', parent=shkola)
  
  
  
  
  #---------------------------------------------------------
  
  
  
  
  
  
  
  
  
  categories = [
    Category.objects.filter(name='трансформер')[0],
    Category.objects.filter(name='шорты/юбки')[0],
    Category.objects.filter(name='видео-няни')[0],
    Category.objects.filter(name='уход за волосами')[0],
    Category.objects.filter(name='спортивные игры')[0],
    Category.objects.filter(name='позиционеры для сна')[0],
    Category.objects.filter(name='прогулочная коляска')[0],
    Category.objects.filter(name='каталки')[0],
    Category.objects.filter(name='шлепанцы')[0],
    Category.objects.filter(name='пеленальные столики/доски')[0],
    Category.objects.filter(name='все для купания')[0],
    Category.objects.filter(name='бортики/бамперы')[0],
    Category.objects.filter(name='аксессуары для кормления')[0],
    Category.objects.filter(name='ранцы/рюкзаки')[0],
    Category.objects.filter(name='комбинезоны')[0],
    Category.objects.filter(name='детские ковры')[0],
    Category.objects.filter(name='велосипеды')[0],
    Category.objects.filter(name='столы')[0],
    Category.objects.filter(name='твистер')[0],
    Category.objects.filter(name='шпионы/полицейские')[0],
  ]
  
  
  adverts = _.map(
    [
      'advert-1','advert-2','advert-3','advert-4','advert-5','advert-6','advert-7',
      'advert-8','advert-9','advert-10','advert-11','advert-12','advert-13','advert-14',
      'advert-15','advert-16','advert-17','advert-18','advert-19','advert-20','advert-21',
      'advert-22','advert-23','advert-24','advert-25','advert-26','advert-27','advert-28',
      'advert-29','advert-30','advert-31','advert-32','advert-33','advert-34','advert-35',
      'advert-36','advert-37','advert-38','advert-39','advert-40','advert-41','advert-42',
      'advert-43','advert-44','advert-45','advert-46','advert-47','advert-48','advert-49',
      'advert-50','advert-51','advert-52','advert-53','advert-54','advert-55','advert-56',
      'advert-57','advert-58','advert-59','advert-60','advert-61','advert-62','advert-63',
      'advert-64','advert-65','advert-66','advert-67','advert-68','advert-69','advert-70',
      'advert-71','advert-72','advert-73','advert-74','advert-75','advert-76','advert-77',
      'advert-78','advert-79','advert-80','advert-81','advert-82','advert-83','advert-84',
      'advert-85','advert-86','advert-87','advert-88','advert-89','advert-90','advert-91',
      'advert-92','advert-93','advert-94','advert-95','advert-96','advert-97','advert-98',
      'advert-99','advert-100','advert-101','advert-102','advert-103','advert-104','advert-105',
      'advert-106','advert-107','advert-108','advert-109','advert-110','advert-111','advert-112',
      'advert-113','advert-114','advert-115','advert-116','advert-117','advert-118','advert-119',
      'advert-120','advert-121','advert-122','advert-123','advert-124','advert-125','advert-126',
      'advert-127','advert-128','advert-129','advert-130','advert-131','advert-132','advert-133',
      'advert-134','advert-135','advert-136','advert-137','advert-138','advert-139','advert-140',
      'advert-141','advert-142','advert-143','advert-144','advert-145','advert-146','advert-147',
      'advert-148','advert-149','advert-150','advert-151','advert-152','advert-153','advert-154',
    ],
    
    lambda name: Advert.objects.create(name=name),
  )
  
  # advert_pictures = []
  
  def take(coll, n):
    chunk = coll[0:n]
    del coll[0:n]
    return chunk
  
  for cat in categories:
    cat.adverts = take(adverts, _.random(1, 10))
    cat.save()
