from telethon import TelegramClient
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import InputPeerUser

api_id = 'seu_api_id'
api_hash = 'seu_api_hash'

client = TelegramClient('nome_do_seu_app', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()
    print(me.stringify())

    # Criando um novo grupo
    users = ['@nome_de_usuario']  # substitua com os nomes de usuário reais
    response = await client(CreateChatRequest(users, 'Nome do Grupo'))

    # Adicionando um usuário a um grupo
    user_to_add = client.get_input_entity('nome_de_usuario')  # substitua com o nome de usuário real
    group_to_add = client.get_input_entity('Nome do Grupo')  # substitua com o nome do grupo real
    client(InviteToChannelRequest(group_to_add, [user_to_add]))

    # print(response.stringify())

with client:
    client.loop.run_until_complete(main())
