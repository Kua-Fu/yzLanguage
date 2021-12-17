import json
import random

from tqdm import tqdm

MAX_NUM = 10000000*3


def create_data():
    num = MAX_NUM
    for i in tqdm(range(num)):
        geonameid = random.randint(1, 100)
        latitude = random.uniform(10, 20)
        name = random.sample('zyxwvutsrqponmlkjihgfedcba', 5)
        name = ''.join(name)
        longitude = random.uniform(20, 30)
        population = random.randint(1, 10000)
        data = {"geonameid": geonameid, "latitude": latitude,
                "name": name, "longitude": longitude, "population": population}
        print(json.dumps(data, ensure_ascii=False))


if __name__ == "__main__":
    create_data()
