 PrefixPass2Base64

While hacking THM  room called "Hijacking" I had to do script who add prefix to password and encoding entire paswords in file to Base64. After done this room I though that good idea will be update this script and do this better. 

If u have passwords list and all passwords start from the new line and u need to add prefix automatically for example: admin:password where "admin:" is directly prefix and in next step u need to encoded it in Base64 this script is 4u. Fell free to use this.


```┌──(eterdiet㉿bypassbyte)-[~/THM_CTFS/Hijacking]
└─$ sudo python3 ./prefixpass2base64.py
[sudo] password for eterdiet: 

______          __ _     ______              _____ ______                 ____    ___ 
| ___ \        / _(_)    | ___ \            / __  \| ___ \               / ___|  /   |
| |_/ / __ ___| |_ ___  _| |_/ /_ _ ___ ___ `' / /'| |_/ / __ _ ___  ___/ /___  / /| |
|  __/ '__/ _ \  _| \ \/ /  __/ _` / __/ __|  / /  | ___ \/ _` / __|/ _ \ ___ \/ /_| |
| |  | | |  __/ | | |>  <| | | (_| \__ \__ \./ /___| |_/ / (_| \__ \  __/ \_/ |\___  |
\_|  |_|  \___|_| |_/_/\_\_|  \__,_|___/___/\_____/\____/ \__,_|___/\___\_____/    |_/

Author: d4xc
Site: SOON

Set path for passwords file: passwords.txt
Set prefix for passwords: admin:
Generating... \

Encoding to Base64 is done. All is saved in file called output.txt
```
Where output looks like: 

```
┌──(eterdiet㉿bypassbyte)-[~/THM_CTFS/Hijacking]
└─$ cat output.txt       
YWRtaW46VnhiMzhtU05OOHd4cUh4djZ1TVg=
YWRtaW46NTZKNFp3NmN2ejhxRHZoQ1dDVnk=
YWRtaW46cUxucVRYeWRuWTNrdHN0bnRMR3U=
YWRtaW46TjYzblBVeERHMlp2cmhaZ1A5Nzg=
YWRtaW46anczRXpyMjZ0eWdUZGdCWlZZR3I=
YWRtaW46emI5Q0ZrZDJRR0RCamd5VnZmREg=
YWRtaW46a2ZGcExBUUZoRDNTNlR2WW40bXY=
YWRtaW46bll5bjRKeFBoalNzbTRIVWVHdEs=
YWRtaW46eUdXQ2c2R05lUFVGWnpWOGYyZ1A=
YWRtaW46TEZLNDNHQWZjOEplVnBDR0NYek0=
YWRtaW46S0ZlanZESDdNTFBYWmVGenVhd1k=
YWRtaW46UWozdzZzYnpHeHV6dld6TlJ0eWI=
YWRtaW46VFVUbmZXNlZwdHlGQXRrZ0VOUFM=
```
