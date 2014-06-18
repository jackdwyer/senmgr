#!/usr/bin/env python2
import argparse
from senmgr import app, ws, db

parser = argparse.ArgumentParser(description="Sensor Management")
parser.add_argument("-create_db", action='store_true')
args = parser.parse_args()

if args.create_db:
    def create_db():
        db.create_all()

if __name__ == "__main__":
    ws.run(app)
