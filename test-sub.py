#!/usr/bin/env bash
import redis, time, random, datetime, os

taskname =  os.environ['TASKNAME']

r = redis.Redis('redis')
p = r.pubsub(ignore_subscribe_messages=True)

def handler(message):
    print message

p.subscribe(**{taskname: handler})
thread = p.run_in_thread(sleep_time=0.1)