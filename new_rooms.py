from booking_app.models import Room 

rooms_data = [
    {
        "title": "Standard Room",
        "price": 1000,
        "description": "Комфортний стандартний номер з усіма зручностями.",
        "capacity": 2,
        "type_room": "standart"
    },
    {
        "title": "Lux Room",
        "price": 2500,
        "description": "Просторий люкс з видом на море та великим балконом.",
        "capacity": 3,
        "type_room": "lux"
    },
    {
        "title": "Suite Room",
        "price": 3000,
        "description": "Номер класу Suite з окремою вітальнею та спальнею.",
        "capacity": 4,
        "type_room": "suite"
    },
    {
        "title": "Family Room",
        "price": 1800,
        "description": "Зручний номер для всієї родини, дві спальні та кухня.",
        "capacity": 5,
        "type_room": "family"
    },
    {
        "title": "Single Room",
        "price": 800,
        "description": "Невеликий номер для одного гостя.",
        "capacity": 1,
        "type_room": "single"
    },
    {
        "title": "Double Room",
        "price": 1200,
        "description": "Класичний двомісний номер з великим ліжком.",
        "capacity": 2,
        "type_room": "double"
    },
    {
        "title": "Twin Room",
        "price": 1300,
        "description": "Номер із двома окремими ліжками.",
        "capacity": 2,
        "type_room": "twin"
    },
    {
        "title": "Deluxe Room",
        "price": 2200,
        "description": "Делюкс із панорамними вікнами та міні-баром.",
        "capacity": 3,
        "type_room": "deluxe"
    },
    {
        "title": "Penthouse",
        "price": 6000,
        "description": "Пентхаус на останньому поверсі з власною терасою.",
        "capacity": 4,
        "type_room": "penthouse"
    },
    {
        "title": "Cottage",
        "price": 3500,
        "description": "Окремий котедж у саду, ідеально підходить для родини.",
        "capacity": 5,
        "type_room": "cottage"
    },
]

for data in rooms_data:
    Room.objects.create(**data)

print("✅ 10 номерів успішно додано!")