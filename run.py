from function import *

client = Client()
poll = client.openPolling()

admin = ["U468b5a4827b5620266b9b11502619be6"]

def contactBroadcast(fr, text):
    c = client.getContactList()
    for i in range(len(c)):
        to = c[i]['contactId']
        time.sleep(1)
        client.sendMessage(to, text)
    client.sendMessage(fr, text)

with poll.getresponse() as response:
    while not response.closed:
        for chunk in response:
            if "data:{" in chunk.decode('utf-8'):
                chunk = json.loads(chunk.decode('utf-8').replace("data:",""))
                event = chunk["event"]
                if event == "chat" and "subEvent" in chunk and chunk["subEvent"] == "message":
                    msg = chunk["payload"]["message"]
                    chatId = chunk["payload"]["source"]["chatId"]
                    if msg["type"] == "text":
                        text = msg["text"]
                        #cmd = text.lower()
                        cmd = text
                        if cmd == "hello":
                            if chatId in admin:
                                client.sendMessage(chatId, "halo")
                            else:
                                client.sendMessage(chatId, "hai")
                        elif cmd.startswith("!ex"):
                            if chatId in admin:
                                com = msg.text.replace("!ex","")
                                try:
                                    exec(com)
                                except Exception as err:
                                    client.sendMessage(chatId, str(err))
                            else:
                                client.sendMessage(chatId, "Hayoo mo ngapain :v")
                        elif cmd.startswith("!cbc: "):
                            tes = cmd.replace("!cbc: ", "")
                            if chatId in admin:
                                try:
                                    contactBroadcast(chatId, str(tes)+"\n\n\nFree BC OA\n[Powered by SDK]")
                                except Exception as asu:
                                    client.sendMessage(chatId, str(asu))
                            else:
                                client.sendMessage(chatId, "Hayoo mo ngapain :v")
                            
                elif event == "chat" and "subEvent" in chunk and chunk["subEvent"] == "chatRead":
                    chatId = chunk["payload"]["source"]["chatId"]
                    # READ DETECTION
                    
                else:
                    print(chunk)
                    # OPERATION
                    # NEED PARSING FOR MORE FEATURE
                    # DO IT WITH URE SELF :D
