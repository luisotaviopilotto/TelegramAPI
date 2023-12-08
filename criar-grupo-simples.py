from telethon import TelegramClient
from telethon.tl.functions.messages import CreateChatRequest, EditChatPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto

api_id = 'seu_api_id'
api_hash = 'seu_api_hash'
group_name = 'Nome do Grupo'
group_photo = 'logo.jpg'

client = TelegramClient('nome_do_seu_app', api_id, api_hash)

async def main():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.name == group_name:
            print('O grupo já existe.')
            break
    else:
        print('Criando o grupo...')
        users = []
        response = await client(CreateChatRequest(users, group_name))
        
        file = await client.upload_file(group_photo) # CARREGANDO A FOTO PARA O GRUPO
        await client(EditChatPhotoRequest(response.chats[0].id, InputChatUploadedPhoto(file))) # ATUALIZANDO A FOTO DO PERFIL DO GRUPO

with client:
    client.loop.run_until_complete(main())
