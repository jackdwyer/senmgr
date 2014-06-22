#!/usr/bin/env python2
import argparse
from senmgr import app, ws, db

parser = argparse.ArgumentParser(description="Sensor Management")
parser.add_argument("--createdb", action='store_true')
parser.add_argument("--world", action='store_true')
parser.add_argument("--database", type=str, default="/tmp/senmgr.db")
args = parser.parse_args()

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + args.database

if args.createdb:
    db.create_all()


if __name__ == "__main__":
    if args.world:
        ws.run(app, host="0.0.0.0")
    else:
        ws.run(app)
