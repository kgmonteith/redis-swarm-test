#!/usr/bin/env bash
import redis, time, random, datetime, os, json

taskname =  os.environ['TASKNAME']

example = {
    'name': taskname,
    'score': 87.33,
    'time': datetime.datetime.now().isoformat()
}
print example

r = redis.Redis('redis')

while True:
    value = r.hgetall('stats.%s' % taskname)
    example['score'] = random.randint(1,100)
    example['time'] = datetime.datetime.now().isoformat()
    pipe = r.pipeline()
    pipe.hmset('stats.%s' % taskname, example).publish(taskname, json.dumps(example)).execute()
    print(value)
    time.sleep(5)