import requests

from sense_hat import SenseHat

URL_BASE = 'http://10.73.224.41:5000'
URL_MISSION = '{}/mission/'.format(URL_BASE)
URL_CHALLENGE = '{}/challenge/'.format(URL_BASE)
URL_STATUS = '{}/'.format(URL_BASE)

def check_status():
    resp = requests.get(URL_STATUS).json()
    if resp['status'] == 'ok':
        send_message("tick.png", colour=(0,255,0))

def send_message(isg,colour):
    sense = SenseHat()
    sense.set_rotation(180)
    sense.load_image(img)

if __name__ == '__main__':
    check_status()
