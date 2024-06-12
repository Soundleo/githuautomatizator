import pyautogui as auto
import time 

auto.PAUSE = 0.5

user_name = input('Informe seu user Name utilizado no GitHub: ')
user_email = input('Informe seu email utilizado no GitHub: ')
projeto = input('Informe o nome do seu projeto, ex: "projeto versão1": ')
url = input('Informe qual a URL de destino: ')

auto.hotkey('ctrl', 'shift', "'")
auto.write('git init')
auto.press('enter')

auto.write(f'git config user.name "{user_name}"')
auto.press('enter')

auto.write(f'git config user.email "{user_email}"')
auto.press('enter')
auto.write('git add .')
auto.press('enter')

auto.write(f'git commit -m "{projeto}"')
auto.press('enter')
auto.write('git branch -M main')
auto.press('enter')

auto.write(f'git remote add origin {url}')  # Adicione um espaço após 'origin'
auto.press('enter')
auto.write('git push -u origin main')
auto.press('enter')
