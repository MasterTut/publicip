import requests
import pygame
def getip():
    response = requests.get('https://api.ipify.org?format=json')
    print(response.json())

getip()
