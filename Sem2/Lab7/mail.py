import requests
import xml.etree.ElementTree as ET


MAIL_URL = 'https://tracking.russianpost.ru/rtm34'
MESSAGETYPE = 0


def choice():
    while True:
        try:
            user_input = int(input('''Вы хотите:
                    1. Получить информацию о отправлении
                    2. Получить информацию об операциях с наложенным платежом
                    Введите число: '''))

            if user_input == 1:
                return getOperationHistory(login, password)
            elif user_input == 2:
                return PostalOrderEventsForMail(login, password)
            else:
                print('\nОшибка: Пожалуйста, выберите 1 или 2')

        except ValueError:
            print('\nОшибка: Введите целое число')


def getOperationHistory(login, password):
    barcode = 'RA644000001RU'
    xml_request = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:oper="http://russianpost.org/operationhistory" xmlns:data="http://russianpost.org/operationhistory/data" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header/>
    <soap:Body>
        <oper:getOperationHistory>
            <data:OperationHistoryRequest>
                <data:barcode>{barcode}</data:barcode>
                <data:MessageType>{MESSAGETYPE}</data:MessageType>
                <data:Language>RUS</data:Language>
            </data:OperationHistoryRequest>
            <data:AuthorizationHeader soapenv:mustUnderstand="1">
                <data:login>{login}</data:login>
                <data:password>{password}</data:password>
            </data:AuthorizationHeader>
        </oper:getOperationHistory>
    </soap:Body>
    </soap:Envelope>
    """

    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    response = requests.post(MAIL_URL, data=xml_request.encode("utf-8"),
                             headers=headers)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        for record in root.findall(".//{http://russianpost.org/operationhistory/data}historyRecord"):

            oper_type = record.find(".//{http://russianpost.org/operationhistory/data}OperType/{http://russianpost.org/operationhistory/data}Name")
            oper_date = record.find(".//{http://russianpost.org/operationhistory/data}OperDate")
            oper_place = record.find(".//{http://russianpost.org/operationhistory/data}OperationAddress/{http://russianpost.org/operationhistory/data}Description")

            print("Операция:", oper_type.text
                  if oper_type is not None else "—")
            print("Дата:", oper_date.text if oper_date is not None else "—")
            print("Место:", oper_place.text if oper_place is not None else "—")
            print("-" * 40)

    else:
        print("Ошибка:", response.status_code)


def PostalOrderEventsForMail(login, password):
    barcode = '14102192069353'
    xml_request = f"""
    <soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:oper="http://russianpost.org/operationhistory"
        xmlns:data="http://russianpost.org/operationhistory/data"
        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:data1="http://www.russianpost.org/RTM/DataExchangeESPP/Data">

        <soap:Header/>

        <soap:Body>
            <oper:PostalOrderEventsForMail>

                <data:AuthorizationHeader soapenv:mustUnderstand="1">
                    <data:login>{login}</data:login>
                    <data:password>{password}</data:password>
                </data:AuthorizationHeader>

                <data1:PostalOrderEventsForMailInput
                    Barcode="{barcode}"
                    Language="RUS"/>

            </oper:PostalOrderEventsForMail>
        </soap:Body>

    </soap:Envelope>
    """

    headers = {
        "Content-Type": "application/soap+xml; charset=utf-8"
    }

    response = requests.post(MAIL_URL, data=xml_request.encode("utf-8"),
                             headers=headers)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        events = root.findall(".//PostalOrderEvent")

        print("Найдено событий:", len(events))

        for event in events:
            number = event.get("Number")
            date = event.get("EventDateTime")
            name = event.get("EventName")
            event_type = event.get("EventType")
            sum_payment = event.get("SumPaymentForward")
            index = event.get("IndexTo")

            print("Номер перевода:", number)
            print("Дата:", date)
            print("Операция:", name)
            print("Тип:", event_type)
            print("Сумма (копейки):", sum_payment)
            print("Индекс получателя:", index)
            print("-" * 40)

    else:
        print("Ошибка:", response.status_code)
        print(response.text)


if __name__ == '__main__':
    login = 'ofJOLczcuGEQQB'
    password = 'yFUSVTOg8kAV'
    # barcode
    choice()
