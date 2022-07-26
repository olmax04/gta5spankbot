import subprocess
from colorama import Fore
from colorama import Style
import requests
from main import script_start
version = "1.2"


def get_id():
    current_machine_id = str(subprocess.check_output(
        'wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

    return current_machine_id


def login(key, hwid, version):
    request = requests.post(
        'https://bot.olmaxdeveloper.online/api/login', json={'key': key, "vers": version, "hwid": hwid})
    return request.json()


if(__name__ == "__main__"):
    try:
        hwid = get_id()
        while True:
            key = input("Enter access code: ")
            response = login(key, hwid, version)
            match response["status"]:
                case 'error':
                    print(f"{Fore.RED}" +
                          response["message"] + f"{Style.RESET_ALL}")
                case 'expired':
                    print(f"{Fore.RED}" +
                          response["message"] + f"{Style.RESET_ALL}")
                case 'active':
                    estimatedTime = response["estimatedTime"]
                    days = response["estimatedTime"]['days']
                    hours = response["estimatedTime"]['hours']
                    minutes = response["estimatedTime"]['minutes']
                    print(
                        f"{Fore.RED}GTA5SPANKBOT v{version}{Style.RESET_ALL} by Olmax04")
                    print(response["message"])
                    print(
                        f"{Fore.GREEN}Expiry in {days} days {hours} hours {minutes} minutes{Style.RESET_ALL}")
                    print(f"Push 'E' to start and 'F9' to exit script")
                    break
                case 'blocked':
                    print(f"{Fore.RED}" +
                          response["message"] + f"{Style.RESET_ALL}")
        script_start()
    except Exception as e:
        print("Connection lost... Please try again later.")
    # if(status == 'admin'):
    #     g = Github("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")

    #     # Then play with your Github objects:
    #     version = g.get_user().get_repo(
    #         'gta5spankbot').get_latest_release().title
    #     print(version)

    # using an access token
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    # headers = {'user-agent': user_agent}
    # login_url = 'https://github.com/session'
    # session = requests.Session()
    # response = session.get(login_url, headers=headers)
    # authenticity_token = bs(response.text, 'lxml').find('input', attrs={'name': 'authenticity_token'})['value']
    # session.post(
    #     login_url,
    #     headers=headers,
    #     data=dict(
    #         commit='Sign in',
    #         utf8='%E2%9C%93',
    #         login=auth[0],
    #         password=auth[1],
    #         authenticity_token=authenticity_token
    #     )
    # )
    # # Now I'm logged in properly, I can download the private repository assets
    # response = session.get(asset.browser_download_url, headers=headers)
    # save_to = Path.home() / 'Downloads' / asset.name
    # save_to.write_bytes(response.content)
