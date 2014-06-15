from senmgr import app, ws

if __name__ == "__main__":
    app.debug = True
    ws.run(app, host='0.0.0.0')
