try:
    import requests, os, sys
    from time import sleep
    from bs4 import BeautifulSoup as bs
except:
    import install_requirements  # install packages

    import requests, os, sys
    from time import sleep
    from bs4 import BeautifulSoup as bs


# Мой Telegram: @FELIX4 - Для вопросов и поддержки (советы и т.д)
# Наша группа в Telegram: https://t.me/No_Black_Mail_chat - Там вы можете предлогать свои идеи и т.д

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
def banner():
    print(RED+'''█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █'''+GREEN+'''
█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄
                           '''+RESET+RED+'V: 1.0.3\n')
def clear():
    if os.sys.platform == "win32":os.system("cls")
    else:os.system("clear")

if os.path.exists('.banner_840'):
    pass
else:
    clear()
    try:
        bannerTX = open('README.md', encoding='utf-8').read()
        print(bannerTX[214:815].replace('#','').replace('*','').replace('-','•'))
        print(f'\n{LI_G}Этот текст покажется лишь один раз!{RESET}')
        open('.banner_840','w')
        input(f'{LI_G}Нажмите на ENTER чтобы очистить экран: {RESET}')
        clear()
    except FileNotFoundError:
        pass
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')

if os.path.exists('dataFile.txt'):
    try:
        clear()
        print(f'{CYAN}{BOLD}[1] {LI_G}Перезаписать данные в файл.{RESET}')
        print(f'{CYAN}{BOLD}[ENTER] {LI_G}Добавить к остальным.{RESET}\n')
        dataV = input(f'{CYAN}{BOLD}[~] {LI_G}Выберите метод: {RESET}')
        if dataV == '1':
            os.remove('dataFile.txt')
            clear() 
            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Перезаписаны')
            sleep(1)
        elif dataV == '2':
            clear()
            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Добавлены к остальным')
            sleep(1)
        else:
            clear()
            print(f'{YELLOW}{BOLD}[+] {LI_G}Данные будут:{RESET} Добавлены к остальным')
            sleep(1)
    except KeyboardInterrupt:
        sys.exit(f'\n{CYAN}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
else: 
    clear()
print(f'{YELLOW}{BOLD}[?] {LI_G}Поиск данных о номерах всех стран. {RESET}')
sleep(2)
clear()
print(f'{YELLOW}{BOLD}[#] {LI_G}Подготовка... {RESET}')
def getNumber():
    try:
        try:
            versioUR = requests.get('https://github.com/DataSC3/No-BlackM')
            versioURL = bs(versioUR.text, 'html.parser')
            get_version = versioURL.find(['span'], class_='d-none d-sm-inline').findNext(['strong']).text
            clear()
            with open('.banner_840', 'r') as fileF:
                try:
                    versionUP = fileF.read().split(':')[1]
                    if str(get_version) != str(versionUP):
                        with open('.banner_840', 'w') as fileW:
                            fileW.write('Version:'+str(get_version))
                            fileW.close()
                            print(f'{YELLOW}{BOLD}[!] {RED}Доступно новое обновление!{YELLOW}{BOLD} [!]\n\n')
                    else:
                        pass
                except IndexError:
                    with open('.banner_840', 'w') as fileW:
                        fileW.write('Version:'+str(get_version))
                        fileW.close()
        except:
            pass
        
        banner()
        getNumber=input(f'{YELLOW}{BOLD}[~] {LI_G}Введите номер: {RESET}')
        getNumber=getNumber.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        if getNumber.isdigit():return getNumber
        else:exit(f'{YELLOW}{BOLD}[!] {RED}"{RESET}{getNumber}{RED}" - Не является номером\n{RESET}')
    except KeyboardInterrupt:
        sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')

number = getNumber()
try:
    num_P_S = requests.post('https://htmlweb.ru/geo/api.php?json&telcod='+str(number))
    num_P = num_P_S.json()
    
    print(f'{YELLOW}{BOLD}[~] {LI_G}Поиск данных... {RESET}\n')
    try:
        country = num_P['country']
        for a in country:
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Страна:{F_CL} {country["name"]}, {country["fullname"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Стране не найдены{RESET}'); pass
            
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Код страны:{F_CL} {country["country_code3"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Коде страны не найдены{RESET}'); pass

            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Код номера:{F_CL} {str(country["telcod"])}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Коде номера не найдены{RESET}'); pass
            
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Длина номера:{F_CL} {str(country["telcod_len"])}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Длине номера не найдены{RESET}'); pass

            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Локация:{F_CL} {country["location"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Локации не найдены{RESET}'); pass
            
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Язык:{F_CL} {country["lang"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Языке не найдены{RESET}'); pass
            break
    except KeyboardInterrupt:sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:print(f'{YELLOW}{BOLD}[!] {RED}Данные Страна/Язык не найдены{RESET}'); pass

    try:
        region = num_P['region']
        for reg in region:
            endIndex = region['name'].split()
            
            try:
                if endIndex[1] == 'край':print(f'{YELLOW}{BOLD}[+] {LI_G}Край:{F_CL} {region["name"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Крае не найдены{RESET}')  
            
            try:
                if endIndex[1] == 'область':print(f'{YELLOW}{BOLD}[+] {LI_G}Область:{F_CL} {region["name"]}{RESET}')
                else:print(f'{YELLOW}{BOLD}[+] {LI_G}Название:{F_CL} {region["name"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные об Области не найдены{RESET}')  
            
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Округ:{F_CL} {region["okrug"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные об Округе не найдены{RESET}')  
        
            break

    except KeyboardInterrupt:sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:print(f'{YELLOW}{BOLD}[!] {RED}Данные Область/Край не найдены{RESET}'); pass

    try:
        capital = num_P['capital']
        for c in capital:
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Столица:{F_CL} {capital["name"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные об Сталице не найдены{RESET}')  

            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Код домашнего номера столицы:{F_CL} +{str(capital["telcod"])}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Домашнем номере не найдены{RESET}')  
            break

    except KeyboardInterrupt:sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:print(f'{YELLOW}{BOLD}[!] {RED}Данные Код/Столица не найдены{RESET}'); pass

    try:
        data = num_P['0']
        for c in data:
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Город:{F_CL} {data["name"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Городе не найдены{RESET}')  

            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Район:{F_CL} {str(data["rajon"])}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Районе не найдены{RESET}')  
            
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Оператор:{F_CL} {data["oper_brand"]}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные об Операторе не найдены{RESET}')  
        
            try:print(f'{YELLOW}{BOLD}[+] {LI_G}Номера:{F_CL} {str(data["def"])}{RESET}')
            except:print(f'{YELLOW}{BOLD}[!] {RED}Данные о Номерах оператора не найдены{RESET}')  

            break
    except KeyboardInterrupt:sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
    except:print(f'{YELLOW}{BOLD}[!] {RED}Данные Город/Оператор не найдены{RESET}'); pass

    if number[0] == '7' and len(number)>9:
        if num_P['limit'] == 0:pass
        else: 
            
            name = []
            dataAV = []
            dataOB = []
            
            review_ph = requests.get(f'http://phoneradar.ru/phone/{number}')
            try:reviews_rev = bs(review_ph.text, 'html.parser').find('div', class_='alert alert-danger').text.strip()
            except KeyboardInterrupt:sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода..{RESET}')
            except:
                try:reviews_rev = bs(review_ph.text, 'html.parser').find('div', class_='alert alert-info').text.strip()
                except:reviews_rev = 'Рейтинг номера не определен, отзывов о номере еще нет'
            print(f'{YELLOW}{BOLD}[+] {LI_G}Рейтин: {F_CL}{reviews_rev}{RESET}')
            
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
                        print(f'\n{YELLOW}{BOLD}[~] {LI_G}Поиск данных по Авито: {RESET}')
                        print(f'{YELLOW}{BOLD}[~] {LI_G}Авито: {F_CL}{h1T}{RESET}')
                        print(f'{YELLOW}{BOLD}[+] {LI_G}----------------------------------------- {RESET}\n')
                        for oBV in contentAV.find_all(['h4', 'span']):
                            print(f'{YELLOW}{BOLD}[+] {LI_G}{oBV.text}{RESET}')  
                            dataOB.append(oBV.text)
                        
                        with open('dataFile.txt', 'a', encoding='utf-8') as f:
                            for data in dataOB:
                                f.write('[-] '+ data +'\n')
                        
                        for url in contentAV.find_all(['a']):
                            count += 1
                            user_link = url['href']
                            try:            
                                avito_url = requests.get('https://mirror.bullshit.agency'+user_link)
                                content = bs(avito_url.text, 'html.parser')
                                url = content.find(['a'])
                                
                                linkAV = url['href']
                                print(f'{YELLOW}{BOLD}[{count}] {URL_L}{UNDERLINE}{linkAV}{RESET}')
                                
                                u_name = bs(avito_url.text, 'html.parser')
                                nameU = u_name.find('strong')

                                name.append(nameU.text)
                                dataAV.append(f'[{count}] {linkAV}')

                            except:
                                print(f'{YELLOW}{BOLD}[{count}] {RED}{UNDERLINE}{user_link}{RESET}')
                                continue
                            
                        with open('dataFile.txt', 'a', encoding='utf-8') as fileD:
                            fileD.write('[-] Номер: +'+str(number)+'\n')
                            for data in dataAV:
                                fileD.write(data +'\n')
                            if not name:pass
                            else:fileD.write('\n[-] Все имена с ссылок: ' + ', '.join(name))

                            fileD.write(f'\n[-] https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20NO-Blackmail - Поиск номера в  WhatsApp\n')
                            fileD.write(f'[-] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск аккаунтов FaceBook\n')
                            fileD.write(f'[-] https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск аккаунтов Linkedin\n')
                            fileD.write(f'[-] https://twitter.com/account/begin_password_reset - Поиск аккаунтов Twitter\n')
                            fileD.write(f'[-] viber://add?number={str(number)} - Поиск номера в Viber\n')
                            fileD.write(f'[-] skype:{str(number)}?call - Звонок на номер с Skype\n')
                            fileD.write(f'[-] tel:{str(number)} - Звонок на номер с телефона\n')
                            fileD.write(f'[-] https://nuga.app - Поиск аккаунтов Instagram' +'\n\n')
                                                        
                        if not name:pass
                        else:print('\n'+YELLOW+BOLD+'[+]'+LI_G+' Все имена с ссылок: '+RESET+', '.join(name))
                        
                
                get_url_name_avito(number)
                
            except KeyboardInterrupt:
                sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')

            except:
                with open('dataFile.txt', 'a', encoding='utf-8') as fileD:
                    fileD.write('[-] Номер: +'+str(number)+'\n')
                    for data in dataAV:
                        fileD.write(data +'\n')
                    if not name:pass
                    else:fileD.write('\n[-] Все имена с ссылок: ' + ', '.join(name))
                    
                    fileD.write(f'\n[-] https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20NO-Blackmail - Поиск номера в  WhatsApp\n')
                    fileD.write(f'[-] https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar - Поиск аккаунтов FaceBook\n')
                    fileD.write(f'[-] https://linkedin.com/checkpoint/rp/request-password-reset-submit - Поиск аккаунтов Linkedin\n')
                    fileD.write(f'[-] https://twitter.com/account/begin_password_reset - Поиск аккаунтов Twitter\n')
                    fileD.write(f'[-] viber://add?number={str(number)} - Поиск номера в Viber\n')
                    fileD.write(f'[-] skype:{str(number)}?call - Звонок на номер с Skype\n')
                    fileD.write(f'[-] tel:{str(number)} - Звонок на номер с телефона\n')
                    fileD.write(f'[-] https://nuga.app - Поиск аккаунтов Instagram'+'\n\n')
                    
                    
                print(f'{YELLOW}{BOLD}[!] {RED}Ваш запрос временно заблокирован. Пожалуйста, подождите 2-6 минуты.{RESET}')
                    
    print(f'\n{YELLOW}{BOLD}[+] {LI_G}Проверьте эти ссылки ( Месенджеры и Социальные сети ): {RESET}')
    print(f'{YELLOW}{BOLD}[1] {URL_L}{UNDERLINE}https://api.whatsapp.com/send?phone={str(number)}&text=Hello,%20this%20is%20No-BlackMail {RESET}- Поиск номера в  WhatsApp')
    print(f'{YELLOW}{BOLD}[2] {URL_L}{UNDERLINE}https://facebook.com/login/identify/?ctx=recover&ars=royal_blue_bar {RESET}- Поиск аккаунтов FaceBook')
    print(f'{YELLOW}{BOLD}[3] {URL_L}{UNDERLINE}https://linkedin.com/checkpoint/rp/request-password-reset-submit {RESET}- Поиск аккаунтов Linkedin')
    print(f'{YELLOW}{BOLD}[4] {URL_L}{UNDERLINE}https://twitter.com/account/begin_password_reset {RESET}- Поиск аккаунтов Twitter')
    print(f'{YELLOW}{BOLD}[5] {URL_L}{UNDERLINE}viber://add?number={str(number)} {RESET}- Поиск номера в Viber')
    print(f'{YELLOW}{BOLD}[6] {URL_L}{UNDERLINE}skype:{str(number)}?call {RESET}- Звонок на номер с Skype')
    print(f'{YELLOW}{BOLD}[7] {URL_L}{UNDERLINE}tel:{str(number)} {RESET}- Звонок на номер с телефона')
    print(f'{YELLOW}{BOLD}[8] {URL_L}{UNDERLINE}https://nuga.app {RESET}- Поиск аккаунтов Instagram')

    print(f'\n{YELLOW}{BOLD}[+] {LI_G}Данные о номере: +{str(number)} добавлены в файл {RESET}dataFile.txt')
    print(f'{YELLOW}{BOLD}[!] {RED}Всего лимитов: {str(num_P["limit"])}{RESET}')

except KeyboardInterrupt:
    sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Принудительная остановка кода{RESET}')
except:
    sys.exit(f'\n{YELLOW}{BOLD}[!] {RED}Возможно, плохое интернет-соединение, попробуйте перезагрузить или напишите мне:{RESET}\n{YELLOW}{BOLD}[+] {LI_G}Telegram:{YELLOW} @FELIX4{RESET}')