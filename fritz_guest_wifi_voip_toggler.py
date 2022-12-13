from pyVoIP.VoIP import VoIPPhone, InvalidStateError
from fritzconnection.lib.fritzwlan import FritzGuestWLAN
from os import environ as env
from dotenv import load_dotenv
import sys

load_dotenv()

if 'VOIP_HOST' not in env:
    print('[error]: VOIP_HOST required')
    sys.exit(1)

if 'VOIP_USER' not in env:
    print('[error]: VOIP_USER required')
    sys.exit(1)

if 'VOIP_PASSWD' not in env:
    print('[error]: VOIP_PASSWD required')
    sys.exit(1)

if 'VOIP_CLIENT_IP' not in env:
    print('[error]: VOIP_CLIENT_IP required')
    sys.exit(1)

if 'FRITZ_ADDRESS' not in env:
    print('[error]: VOIP_HOST required')
    sys.exit(1)

if 'FRITZ_USER' not in env:
    print('[error]: VOIP_HOST required')
    sys.exit(1)

if 'FRITZ_PASSWD' not in env:
    print('[error]: VOIP_HOST required')
    sys.exit(1)


def answer(call):
    try:
        intern = call.request.headers['From']['number'].startswith("**")
        
        if intern:
            call.answer()

            guest_wlan = FritzGuestWLAN(
                address=env['FRITZ_ADDRESS'], user=env['FRITZ_USER'], password=env['FRITZ_PASSWD'])
            if guest_wlan.is_enabled:
                guest_wlan.disable()
                print('Guest WLAN disabled')
            else:
                guest_wlan.enable()
                print('Guest WLAN enabled')

            call.hangup()
    except InvalidStateError:
        pass


if __name__ == "__main__":
    phone = VoIPPhone(env['VOIP_HOST'], 5060, env['VOIP_USER'],
                      env['VOIP_PASSWD'], callCallback=answer, myIP=env['VOIP_CLIENT_IP'])
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()
