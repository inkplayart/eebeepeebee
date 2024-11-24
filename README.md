# eebeepeebee
An extremely minimal self-hosted pastebin for a small number of users, tested on Linux

## Quickstart: Run EBPB and have it accessible to all machines on your network
1. pip install fastapi uvicorn jinja2 python-multipart (a virtual environment would do nicely here...)
2. Install uvicorn for your distro (apt install uvicorn)
3. clone the repository
4. cd to the repository
5. uvicorn main:app --host 0.0.0.0 --port 2345
6. Access is via <your_server_ip>:2345

Change the port if you want, it really doesn't matter

## How does it work?
Navigate to http://<your_server_ip>:<whichever_port_you_chose> on your favorite web browser. It will open up the text box. Put text in that and hit "Generate URL". It will create a random URL made up of two fruits. Go to http://<your_server_ip>:<whichever_port_you_chose>/<fruit1>-<fruit2> to see the text. That's it.

The text persists in RAM for as long as the app is running. However, if the random generator creates the same URL it will overwrite what's already there. Therefore, don't rely on this to store text forever. That's not the purpose at all.

## Running in the background
The quickstart command will stop the app once you log out. To avoid that, use the command: nohup uvicorn main:app --host 0.0.0.0 --port 2345 > output.log 2>&1 &

## FAQ
**Why does this exist?**
I was using my phone, my friend was using their computer, and we had no easy way to share links. By making the URL two fruits, we could easily share the URL just by saying it out loud without sending a string of random characters like the real pastebin does.
**Really you had no easy way to do this?  What about all the other pastebin apps out there like...**
I like making my own stuff and hosting my own stuff.
**Is this secure?**
I doubt it. Like, it's about 100 lines of code. I'm sure it can be broken to pieces.
**Will this run on...**
Probably. I'll bet you can get it running on the last dregs of toothpaste in the tube it's so lightweight. If it can serve FastAPI apps, it can serve this.
**I want a new feature. Can you add...**
No. But feel free to change it yourself.
