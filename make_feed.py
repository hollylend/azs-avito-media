import html
U='https://raw.githubusercontent.com/hollylend/azs-avito-media/main/img/banner_{}.jpg'
ADDR='Краснодарский край, Краснодар, ул. Будённого, 147'
FOOT=('<p>Работаем по Краснодару и краю. Опыт в сфере 10+ лет, гарантия на работы.</p>'
      '<p>На фото — наши объекты: как было и как стало.</p><p>Напишите в сообщения — обсудим задачу и рассчитаем смету.</p>')
ADS=[
 dict(id='azs-001',sub='Коммерческое строительство',title='Строительство и реконструкция АЗС под ключ',imgs=['01','02','03','04','05','06','07','09','10','14'],
  extra='<Objects><Option>Объекты сферы услуг</Option><Option>Торговые объекты</Option></Objects><ContractorType><Option>Подрядчик под ключ</Option></ContractorType>',
  desc='<p>Строительство и реконструкция автозаправочных станций и нефтебаз под ключ.</p><ul><li>Проектирование с учётом норм безопасности</li><li>Реконструкция и ребрендинг действующих АЗС</li><li>Навесы, освещение, здания касс и магазинов</li><li>Установка ТРК, технологические трубопроводы</li><li>Резервуарные парки: монтаж, зачистка, калибровка</li><li>Мощение и благоустройство территории</li></ul>'),
 dict(id='azs-002',sub='Фасадные работы',title='Облицовка фасадов АЗС композитными панелями',imgs=['13','16','17','11','12','20'],
  extra='<FacadeWork><Option>Монтаж</Option><Option>Отделочные работы</Option></FacadeWork><FacadeType><Option>Вентилируемые</Option></FacadeType><FacadeMaterials><Option>Фасадные панели</Option></FacadeMaterials>',
  desc='<p>Облицовка зданий АЗС, касс, кафе и автомоек композитными панелями, в том числе с фактурой дерева.</p><ul><li>Монтаж подсистемы из оцинкованного профиля</li><li>Навесной вентилируемый фасад</li><li>Входные группы, витрины, примыкания</li></ul>'),
 dict(id='azs-003',sub='Коммерческое строительство',title='Резервуарные парки АЗС: монтаж и обвязка',imgs=['14','15','18','10'],
  extra='<Objects><Option>Объекты сферы услуг</Option></Objects>',
  desc='<p>Монтаж резервуарных парков для АЗС и нефтебаз.</p><ul><li>Земляные работы и установка резервуаров</li><li>Технологические колодцы и обвязка трубопроводов</li><li>Дыхательная арматура, площадки обслуживания</li><li>Зачистка и калибровка резервуаров</li></ul>'),
 dict(id='azs-004',sub='Коммерческое строительство',title='Островки ТРК, мощение и благоустройство АЗС',imgs=['08','19','09','05','06'],
  extra='<Objects><Option>Объекты сферы услуг</Option></Objects>',
  desc='<p>Обустройство площадки АЗС: островки ТРК, установка колонок, мощение под навесом, бордюры и отбойники.</p><ul><li>Каркас и облицовка островков</li><li>Подключение ТРК</li><li>Укладка тротуарной плитки</li></ul>'),
]
out=['<?xml version="1.0" encoding="UTF-8"?>','<Ads formatVersion="3" target="Avito.ru">']
for a in ADS:
    out+=['<Ad>',f'<Id>{a["id"]}</Id>','<Category>Предложение услуг</Category>','<ServiceType>Строительство</ServiceType>',f'<ServiceSubtype>{a["sub"]}</ServiceSubtype>',
      f'<Title>{a["title"]}</Title>',f'<Description><![CDATA[{a["desc"]}{FOOT}]]></Description>','<Price>5000</Price>',f'<Address>{ADDR}</Address>',
      '<ContactMethod>По телефону и в сообщениях</ContactMethod>','<WorkExperience>7 лет</WorkExperience>','<Guarantee>Есть</Guarantee>','<TeamSize>5-20 человек</TeamSize>',a['extra'],
      '<Images>'+''.join(f'<Image url="{U.format(i)}"/>' for i in a['imgs'])+'</Images>','</Ad>']
out.append('</Ads>')
open('feed.xml','w').write('\n'.join(out)); print('ok', len(ADS))
