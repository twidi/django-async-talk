# https://carbon.now.sh/?bg=rgba%28222%2C171%2C99%2C0%29&t=synthwave-84&wt=none&l=application%2Fjson&width=680&ds=false&dsyoff=9px&dsblur=15px&wc=false&wa=true&pv=0px&ph=0px&ln=false&fl=1&fm=Hack&fs=11px&lh=201%25&si=false&es=2x&wm=false&code=links%2520%253D%2520%257B%250A%2520%2520%2520%2520%2522Twitter%2522%253A%2520%2522%2540twidi%2522%252C%250A%2520%2520%2520%2520%2522Github%2522%253A%2520%2522%2540twidi%2522%252C%250A%2520%2520%2520%2520%2522Mastodon%2522%253A%2520%2522twidi%2540mastodon.social%2522%252C%250A%2520%2520%2520%2520%2522Twitch%2522%253A%2520%2522%2540twidi_angel%2522%252C%250A%2520%2520%2520%2520%2522Game%2522%253A%2520%2522https%253A%252F%252Fhexpo.io%2522%252C%250A%257D

links = {
    "Twitter": "@twidi",
    "Github": "@twidi",
    "Mastodon": "twidi@mastodon.social",
    "Twidi": "@twidi_angel",
    "Game": "https://hexpo.io",
}

handler = await get_or_create_handler(
    game=(game := get_game_by_token(token)),
    loop=game_loops.get_or_create(game=game),
)

create_task(game_loops.run_forever())

app = aiohttp.web.Application()
web.run_app(
    app,
    host="127.0.0.1",
    port=int(sys.argv[1])
)

#########


def __init__(self, game, loop):
    self.game = game
    self.task = create_task(self.run_forever(loop.queue)
    self.websockets = {}


async def http_get_index(self, request):
    # do stuff
    return response(render_template(...))


async def run_forever(self, queue):
    while True:
        message = queue.get()
        if message.player_id:
            await self.websockets[message.player_id].send(message)
        else:
            for ws in self.websockets.values():
                await ws.send(message)



async def ws_handler(self, request):
    await player = get_player(request))
    ws = web.WebSocketResponse()
    self.websockets[player.id] = ws
    async for message in ws:
        # handle message from player



def __init__(self, game):
    self.game = game
    self.queue = asyncio.Queue()
    self.task = create_task(self.run_forever(self.queue)


async def run_forever(self, queue):
    while not await self.game.aisover():
        step = await.get_current_step()
        messages = self.handle_step(step)
        for message in messages:
            await queue.put(message)

    await queue.put(MessageKind.END_GAME)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    async def arefresh_from_db(self):
        await sync_to_async(self.refresh_from_db)()

    async def asave(self, *args, **kwargs):
        await sync_to_async(self.save)(*args, **kwargs)

    async def adelete(self, *args, **kwargs):
        return await sync_to_async(self.delete)(*args, **kwargs)



class Game(Model):
    #...
    @sync_to_async
    def get_solo_game_creator(self):
        return self.creator

async def my_async_func(game):
    creator = await game.get_solo_game_creator()


# nope
def my_sync_func(game):
    creator = await game.get_solo_game_creator()

# nope, bis
def my_sync_func(game):
    creator = game.get_solo_game_creator()


# solution 1
class Game(Model):
    @sync_to_async
    def get_solo_game_creator(self):
        return self.creator

async def my_async_func(game):
    creator = await game.get_solo_game_creator()

def my_sync_func(game):
    creator = async_to_sync(game.get_solo_game_creator)


# solution 2
class Game(Model):
    def get_solo_game_creator(self):
        return self.creator

async def my_async_func(game):
    creator = await sync_to_async(game.aget_solo_game_creator)()

def my_sync_func(game):
    creator = game.get_solo_game_creator()


# solution 3
class Game(Model):
    def get_solo_game_creator(self):
        return self.creator

   async def aget_solo_game_creator(self):
        return await sync_to_async(self.get_solo_game_creator)()

async def my_async_func(game):
    creator = await game.aaget_solo_game_creator()

def my_sync_func(game):
    creator = game.get_solo_game_creator()



# main process                                                    # thread
async def some_async_func():
    # do stuff
    await sync_to_async(func1)()                                  def func1():
                                                                    # do stuff
    # do stuff
    await sync_to_async(func2)()                                  def func2():
                                                                    # do stuff
    return some_stuff

# thread


def get_solo_game_creator(self):
    return self.creator

def func_doing_many_sql_queries():
    # do stuff




class Game(Model):
    def __str__(self):
        return f"Game created by {self.creator.username}"

# ok
def my_sync_func(token):
    game = Game.objects.get(token=token)
    print(game))

# pas ok
async def my_async_func(game):
    game = await sync_to_async(Game.objects.get)(token=token)
    print(game))



def get_game(token):
    return Game.objects.filter(token=token).select_related("creator").get()

def my_sync_func(token):
    game = get_game(token)
    print(game))

async def my_async_func(game):
    game = sync_to_async(get_game)(token=token)
    print(game))


# urls.py
urlpatterns = [
    path("game/<token>/", views.game_view),
]

# views.py
async def game_view(request, token):
    game = await get_game(token)
    return HttpResponse(f"Welcome to game {game}")


from channels.routing import ProtocolTypeRouter
application = ProtocolTypeRouter({})


class PracticeConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        # when websocket connects
        print("connected", event)
        await self.send({"type": "websocket.accept"})

        await self.send({"type": "websocket.send", "text": 0})

    async def websocket_receive(self, event):
        # when messages is received from websocket
        print("receive", event)
        sleep(1)
        await self.send({"type": "websocket.send",
                         "text": str(randint(0, 100))})

    async def websocket_disconnect(self, event):
        # when websocket disconnects
        print("disconnected", event)



class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
    # [...]


from django.template import loader

class GameHandler:
    def __init__(self, game, loop):
        self.game = game
        self.task = create_task(self.run_forever(loop.queue)
        self.websockets = {}

    async def http_get_index(self, request):
        context = {"game": self.game}
        html = loader.render_to_string("core/game.html", context)
        return Response(text=html, content_type="text/html")

    async def run_forever(self, queue):
        while True:
            message = queue.get()
            if message.player_id:
                await self.send_message_to_player(message.player_id, message)
            else:
                for player_id, ws in self.websockets.values():
                    await self.send_message_to_player(player_id, message)

    async def send_message_to_player(self, player_id, message):
        ws = self.websockets[player_id]
        context = {"game": self.game, "player_id": player_id}
        html = loader.render_to_string("core/game_update.html", context)
        await ws.send_str(html)

    async def ws_handler(self, request):
        await player = get_player(request))
        ws = web.WebSocketResponse()
        self.websockets[player.id] = ws
        async for message in ws:
            data = json.loads(message.data)
            if data["type"] == "click":
                await self.save_click(message.data)
