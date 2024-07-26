import os; 
from zeep import Client; 

wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL';
client = Client(wsdl)

country_codes = ['AR', 'BR', 'CA', 'CN', 'FR', 'DE', 'IN', 'IT', 'JP', 'MX', 'RU', 'ZA', 'ES', 'SE', 'CH', 'TR', 'GB', 'US']

countries_dict = []
def getCountryData(code):
    try:
        country_data = client.service.FullCountryInfo(code)
        country_dict = {
            'Nombre del pais': country_data.sName,
            'Capital': country_data.sCapitalCity,
            'Moneda': country_data.sCurrencyISOCode,
            'Codigo de tel': country_data.sPhoneCode
        }
        print(country_dict)
    except Exception as ex:
        print(f'Hubo un error: {ex}')

def printMenu():
    checked = False;
    while not checked:
        os.system('cls')
        print("Hola, bienvenidos a una nueva aplicación hecha con Python: \n Ingresa alguno de los siguientes códigos...\n");
        for code in country_codes:
            print(f" - Código = {code}")
        selection = input()
        if selection in country_codes:
            print("La seleccion fue exitosa...")
            input("\nPresiona una tecla para continuar...")
            getCountryData(selection)
            checked = True
        else: 
            print("Debes ingresar una opción válida")
            input("\nPresiona una tecla para continuar...")
            checked = False

printMenu()





