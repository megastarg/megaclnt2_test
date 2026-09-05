import json
import time
import os
import gc
import psutil
import datetime
import pytz
import logging
import traceback
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Queue
from threading import Thread

# Import both parsers
from main import flipkart_parse as flipkart_parse_web
from mainmob import flipkart_parse as flipkart_parse_mob

from block import block
from fkrdplog import updatetoserver
import extrafiles
import sync_data

# Initialize extra threads
extrafiles.start()
sync_data.start_sync_thread()

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='log.txt')
logger = logging.getLogger("ScraperEngine")

def get_parser(source_script):
    mob_scripts = ['pages_7.py', 'pages_8.py', 'pages_9_1.py', 'pages_AC.py', 'appliances_M.py']
    if source_script in mob_scripts:
        return flipkart_parse_mob
    return flipkart_parse_web

def creation_time(path_to_file):
    current = time.time()
    try:
        diff = current - float(os.path.getctime(path_to_file))
        return diff
    except Exception as e:
        return 0

def run_group(foldername, tasks):
    if not os.path.exists(foldername):
        os.mkdir(foldername)
        
    res_queue = Queue()
    
    if creation_time(foldername) < 1200:
        telegram = "off"
    else:
        telegram = "on"
        
    print(f"[{datetime.datetime.now()}] Starting group: {foldername} with {len(tasks)} tasks.")
    
    futures = []
    # Use ThreadPoolExecutor to limit concurrency to 80 (similar to existing logic)
    with ThreadPoolExecutor(max_workers=80) as executor:
        for task in tasks:
            filename = foldername + task['filename']
            force = task['force']
            notassured = task['notassured']
            url = task['url']
            parser = get_parser(task['source_script'])
            
            futures.append(executor.submit(parser, filename, telegram, force, url, res_queue, notassured))
            
        # We also need to run block and updatetoserver
        block_future = executor.submit(block, foldername)
        update_future = executor.submit(updatetoserver, foldername)
        
        for future in as_completed(futures + [block_future, update_future]):
            try:
                future.result()
            except Exception as e:
                logger.error(f"Error in task: {e}")
                logger.error(traceback.format_exc())

    # Write output
    with open(foldername.strip("/") + '_output.txt', 'w+') as fall:
        res_queue.put(None)
        while True:
            item = res_queue.get()
            if item is None:
                break
            fall.write(item + "\r\n")
        fall.write("Telegram = " + telegram)
        
    print(f"[{datetime.datetime.now()}] Completed group: {foldername}")

def main_loop(group_name=None):
    with open('config.json', 'r') as f:
        config = json.load(f)
        
    while True:
        try:
            for foldername, tasks in config.items():
                if group_name and foldername != group_name:
                    continue
                run_group(foldername, tasks)
                
                # Manual garbage collection between groups
                collected = gc.collect()
                print(f"Garbage collector: collected {collected} objects.")
                
                # Memory check
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 2. ** 20
                print('memory use:', round(memoryUse, 2), "MB")
                if memoryUse > 500:
                    print("Restarting memory usage exceeds ...........")
                    os.system("python3 " + __file__)
                    os._exit(0)
                    
        except Exception as e:
            logger.error(str(e))
            logger.error(traceback.format_exc())

        d = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        hour = d.hour
        if 3 <= hour <= 7:
            sleep = random.randint(5, 10)
        else:
            sleep = random.randint(2, 3)
        time.sleep(sleep)

import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main_loop(sys.argv[1])
    else:
        main_loop()
