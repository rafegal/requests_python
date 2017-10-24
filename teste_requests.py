
import requests
TOKEN = '124348504:AAFqwQUXXGgaOmmX-Fsm0lpPy6_Y1mAglRk'

def consulta_cep(cep):
    url = 'https://viacep.com.br/ws/%s/json/'%cep
    response = requests.get(url)
    #print response.content
    response_json = response.json()
    logradouro = response_json['logradouro']
    localidade = response_json['localidade']
    return logradouro, localidade


def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{0}/sendMessage'.format(TOKEN)
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
    print response.content

def get_message(update_id):
    url = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(TOKEN, update_id)
    response = requests.get(url)
    response_json = response.json()
    last_updated_id = update_id
    for i in response_json['result']:
        first_name = i['message']['chat']['first_name']
        last_name = i['message']['chat']['last_name']
        chat_id = i['message']['chat']['id']
        last_updated_id = i['update_id']
        text = i['message']['text']
        print first_name, last_name, chat_id, update_id, text
        if last_updated_id <> update_id:
            if "Palmeiras" in text:
                send_message('Palmeiras nao tem mundial', chat_id)
            elif "Corinthians" in text:
                send_message('Perdeu para o Botafogo', chat_id)
    return last_updated_id

if __name__=='__main__':
    #send_message()
    import time
    update_id = "525000714"
    while True:
        update_id = get_message(update_id)
        time.sleep(5)
    #consulta_cep('123')
