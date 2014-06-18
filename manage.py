#!/usr/bin/env python2
import argparse
from senmgr import app, ws, db, config

parser = argparse.ArgumentParser(description="Sensor Management")
parser.add_argument("-create_db", action='store_true')
parser.add_argument("-world", action='store_true')
args = parser.parse_args()

if args.create_db:
    db.create_all()

if __name__ == "__main__":
    if args.world:
        ws.run(app, host="0.0.0.0")
    else:
        ws.run(app)
