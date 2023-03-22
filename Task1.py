import json
import sys
import datetime

Json_Str = ""

today = datetime.date.today()

def main():
    try:
        json_dict = json.loads(Json_Str)
    except Exception as e:
        print(e)
        exit()

    for data in json_dict:
        date_end = data['end']
        date_end = datetime.datetime.strptime(data['end'],'%Y-%m-%d %H:%M:%S')
        if CheckDate(date_end):
            print(data['record_id'])
            print(data['name'])


def CheckDate( Date ):
    current_month = today.month
    current_year = today.year
    end_date = datetime.datetime.strptime( str(current_year) + '-' + str( current_month+1 ) + '-1', '%Y-%m-%d')
    return (Date < end_date)

if __name__ == "__main__":
    try:
        Json_Str = ""
        for args in sys.argv[1:]:
            Json_Str += args
        print(f"Print: " +Json_Str)
    except:
        print(f"Укажите Json Строку.")
        exit()
    main()