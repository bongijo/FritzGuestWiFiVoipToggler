<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="./images/logo.png" alt="Logo" width="60%">
  </a>

<br />

<h1 align="center">Fritz Guest WiFi Voip Toggler</h1>

<p>
    Switch on and off your guest wifi just with a call!
  </p>

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" />
  <a href='https://github.com/bongijo/FritzGuestWiFiVoipToggler/releases'>  
  <img src='https://img.shields.io/github/v/release/bongijo/FritzGuestWiFiVoipToggler?color=%23FDD835&label=version&style=for-the-badge'>
  </a>
  <a href='https://github.com/bongijo/FritzGuestWiFiVoipToggler/blob/main/LICENSE'>
  <img src='https://img.shields.io/github/license/bongijo/FritzGuestWiFiVoipToggler?style=for-the-badge'>
  </a>

</div>

## 🧰 Getting Started

### ‼ Prerequisites

- A valid **VoIP account** on your Fritz!Box: you can follow [this](https://en.avm.de/service/knowledge-base/dok/FRITZ-Box-7590/42_Registering-an-IP-telephone-with-the-FRITZ-Box-and-setting-it-up/) guide to create a LAN/Wi-Fi telephone
- **TR-064** interface **enabled**: you can do it by activating the settings *Allow access for applications* and *Transmit status information over UPnP* in the *Home Network -> Network -> Network Settings* menu
- A valid **Fritz!Box user** with *settings permissions* enabled (I recommend to create a new user just for this app)

### 🐳 Installing - Docker

You can easily install it by running the provided docker container.
But first, create a `.env` file filled up with the access parameters:

| Parameter        | Description                                                                                                                            |
|:----------------:| -------------------------------------------------------------------------------------------------------------------------------------- |
| `VOIP_HOST`      | The Fritz!Box ip address                                                                                                               |
| `VOIP_USER`      | The VoIP account username                                                                                                              |
| `VOIP_PASSWD`    | The VoIP account password                                                                                                              |
| `VOIP_CLIENT_IP` | The ip address of the machine where this app is executing. **N.B.** the ip address must be a valid ip address in the Fritz!Box network |
| `FRITZ_ADDRESS`  | The Fritz!Box ip address                                                                                                               |
| `FRITZ_USER`     | The Fritz!Box account username                                                                                                         |
| `FRITZ_PASSWD`   | The Fritz!Box account password                                                                                                         |

Run the docker container:

```shell
docker run -d ghcr.io/bongijo/FritzGuestWiFiVoipToggler --network host --name FritzGuestWiFiVoipToggler --env-file .env
```

## 👀 Usage

Just call with a telephone the correspondent internal number (e.g. `**620`)

## 🏗 Built With

- [pyVoIP](https://github.com/tayler6000/pyVoIP) - Python VoIP/SIP/RTP library
- [fritzconnection](https://github.com/kbr/fritzconnection) - Python tool to communicate with the AVM Fritz!Box

## 📜 License

This project is released under the MIT License. See [LICENSE](https://github.com/bongijo/FritzGuestWiFiVoipToggler/blob/master/LICENSE) for more information.
