import requests, os, sys
from time import sleep
from bs4 import BeautifulSoup as bs

dataAV = []
RESET ='\033[0m'
UNDERLINE = '\033[04m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
RED ='\033[31m'
CYAN = '\033[36m'
BOLD = '\033[01m'
URL_L = '\033[36m'
LI_G='\033[92m'
F_CL = '\033[0m'


if os.path.exists('.banner_840'):
    pass
else:
    os.system('clear')
    try:
        bannerTX = open('README.md', encoding='utf-8').read()
        print(bannerTX[265:855])
        print(f'{LI_G}Этот текст покажется лишь один раз!{RESET}')
        open('.banner_840','w')
        input(f'{LI_G}Напишите что нибудь чтобы очистить экран: {RESET}')
    except FileNotFoundError:
        os.system('clear')
    os.system('clear')

if os.path.exists('dataFile.txt'):
    try:
        os.system('clear')
        print(f'{CYAN}{BOLD}[1] {LI_G}Перезаписать данные в файл.{RESET}')
        print(f'{CYAN}{BOLD}[2] {LI_G}Добавить к остальным.{RESET}\n')
        dataV = input(f'{CYAN}{BOLD}[~] {LI_G}Выберите метод: {RESET}')
        if dataV == '1':
            os.remove('dataFile.txt')
            os.system('clear') 
            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Перезаписаны\n')
        elif dataV == '2':
            os.system('clear')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Добавляться\n')
        else:
            sys.exit(f'{YELLOW}{BOLD}[+] {RED}Выберите метод работы пожалуйста{RESET}')
    except KeyboardInterrupt:
        sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
else:
   pass
os.system('clear')
def getNumber():
    try:
        while type:
            print(f'{YELLOW}{BOLD}[~] {LI_G}Пример: {RESET}7ХХХХХХХХХ')
            getTempNumber=input(f'{YELLOW}{BOLD}[~] {LI_G}Введите номер: {RESET}+')
            try:                                      
                getTempNumber=int(getTempNumber)
            except ValueError:                 
                print (f'\n{YELLOW}{BOLD}[!] {RED}"{getTempNumber}" - Не является числом{RESET}')
            else:                                 
                break
        return abs(getTempNumber)
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')

number = getNumber()
try:
    num_P_S = requests.post('https://htmlweb.ru/geo/api.php?json&telcod='+str(number))
    num_P = num_P_S.json()
    
    print(f'{YELLOW}{BOLD}[+] {LI_G}Поиск данных... {RESET}\n')
    try:
        country = num_P['country']
        for a in country:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Страна:{F_CL} {country["name"]}, {country["fullname"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Код страны:{F_CL} {country["country_code3"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Код номера:{F_CL} {str(country["telcod"])}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Длина номера:{F_CL} {str(country["telcod_len"])}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Локация:{F_CL} {country["location"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Язык:{F_CL} {country["lang"]}{RESET}')
            break
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:
        print(f'{YELLOW}{BOLD}[!] {RED}Данные Страна/Язык не найдены{RESET}')
        pass

    try:
        region = num_P['region']
        for b in region:
            endIndex = region['name'].split()
            if endIndex[1] == 'край':
                print(f'{YELLOW}{BOLD}[+] {LI_G}Край:{F_CL} {region["name"]}{RESET}')
            elif endIndex[1] == 'область':
                print(f'{YELLOW}{BOLD}[+] {LI_G}Область:{F_CL} {region["name"]}{RESET}')
            else:
                print(f'{YELLOW}{BOLD}[+] {LI_G}Название:{F_CL} {region["name"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Округ:{F_CL} {region["okrug"]}{RESET}')
            break
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:
        print(f'{YELLOW}{BOLD}[!] {RED}Данные Область/Край не найдены{RESET}')

    try:
        capital = num_P['capital']
        for c in capital:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Столица:{F_CL} {capital["name"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Код домашнего номера столицы:{F_CL} +{str(capital["telcod"])}{RESET}')
            break
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:
        print(f'{YELLOW}{BOLD}[!] {RED}Данные Код/Столица не найдены{RESET}')

    try:
        data = num_P['0']
        for c in data:
            print(f'{YELLOW}{BOLD}[+] {LI_G}Город:{F_CL} {data["name"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Район:{F_CL} {str(data["rajon"])}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Оператор:{F_CL} {data["oper_brand"]}{RESET}')
            print(f'{YELLOW}{BOLD}[+] {LI_G}Номера:{F_CL} {str(data["def"])}{RESET}')
            break
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:
        print(f'{YELLOW}{BOLD}[!] {RED}Данные Город/Оператор не найдены{RESET}')
    if num_P['limit'] == 0:
        pass
    else: 
        name = []
        dataAV = []
        dataOB = []
        try:
            def get_url_name_avito(number):
                resAV = requests.get('https://mirror.bullshit.agency/search_by_phone/'+str(number))
                contentAV = bs(resAV.text, 'html.parser')
                h1 = contentAV.find('h1')
                if h1.text == '503 Service Temporarily Unavailable':
                    print(f'{YELLOW}{BOLD}[!] {RED}Ваш запрос временно заблокирован. Пожалуйста, подождите 6-15 минут.{RESET}')
                else:
                    count = 0
                    h1T = h1.text.replace("  ","")
                    print(f'\n{YELLOW}{BOLD}[+] {LI_G}Поиск данных по Авито: {RESET}')
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Найден: {F_CL}{h1T}\n{RESET}')
                    for oBV in contentAV.find_all(['h4', 'span']):
                        print(f'{YELLOW}{BOLD}[+] {LI_G}{oBV.text}{RESET}')  
                        dataOB.append(oBV.text)
                    
                    with open('dataFile.txt', 'a', encoding='utf-8') as f:
                        for data in dataOB:
                            f.write('[-] '+ data +'\n')

                    for url in contentAV.find_all(['a']):
                        count += 1
                        user_link = url['href']
                        user_url = requests.get('https://mirror.bullshit.agency'+user_link)
                        
                        avito_url = requests.get('https://mirror.bullshit.agency'+user_link)
                        content = bs(avito_url.text, 'html.parser')
                        url = content.find(['a'])
                        
                        linkAV = url['href']
                        print(f'{YELLOW}{BOLD}[{count}] {URL_L}{UNDERLINE}{linkAV}{RESET}')

                        u_name = bs(user_url.text, 'html.parser')
                        nameU = u_name.find('strong')

                        name.append(nameU.text)
                        dataAV.append(f'[{count}] {linkAV}')

                    with open('dataFile.txt', 'a', encoding='utf-8') as fileD:
                        fileD.write('[∩] Номер: +'+str(number)+'\n')
                        for data in dataAV:
                            fileD.write(data +'\n')
                        fileD.write(f'[-] https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20NO-Blackmail')
                        fileD.write(f'\n[-] Все имена с ссылок: {str(name)}\n\n')
                    if not name:
                        pass
                    else:
                        print(f'\n{YELLOW}{BOLD}[+] {LI_G}Все имена с ссылок: {RESET}{str(name)}')
                    print(f'{YELLOW}{BOLD}[+] {LI_G}Данные о номере: +{str(number)} добавлены в файл {RESET}dataFile.txt')
            
            get_url_name_avito(number)
            
        except KeyboardInterrupt:
            sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')

        except:
            with open('dataFile.txt', 'a', encoding='utf-8') as fileD:
                fileD.write('[∩] Номер: +'+str(number)+'\n')
                for data in dataAV:
                    fileD.write(data +'\n')
                fileD.write(f'[-] https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20NO-Blackmail')
                fileD.write(f'\n[-] Все имена с ссылок: {str(name)}\n\n')
            print(f'{YELLOW}{BOLD}[!] {RED}Ваш запрос временно заблокирован или Ссылки/Имена не найдены. Пожалуйста, подождите 4-10 минуты.{RESET}')
                
        print(f'{YELLOW}{BOLD}[+] {LI_G}Создан прямая ссылка в WhatsApp: {RESET}')
        print(f'{YELLOW}{BOLD}[+] {URL_L}{UNDERLINE}https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20No-BlackMail{RESET}')
    print(f'\n{YELLOW}{BOLD}[!] {RED}Всего лимитов: {str(num_P["limit"])}{RESET}')

except KeyboardInterrupt:
    print(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
except:
    print(f'{YELLOW}{BOLD}[!] {RED}Возможно, плохое интернет-соединение, попробуйте перезагрузить или напишите мне:{RESET}\n{YELLOW}{BOLD}[+] {RED}Telegram:{YELLOW} @FELIX4{RESET}')
