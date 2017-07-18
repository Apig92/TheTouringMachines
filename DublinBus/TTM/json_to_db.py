from TTM.models import Json_reading

def json_reading():
    import json
    with open('TTM/routes.json') as f:
        json_data = json.load(f)

    for item in json_data['routes']:
        print(item['number'] + ' --- ' + item['code'])
        a = Json_reading.objects.create()
        a.JourneyPatternID = item['code']
        a.RouteID_Direction = item['number']
        a.save()

