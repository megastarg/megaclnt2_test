import datetime
import random
import logging
import threading
from logging.handlers import RotatingFileHandler
import traceback
from threading import Thread
import os
from os import path
import psutil
import sys
from multiprocessing import Process,Queue
import time
import pytz
from fkrdplog import updatetoserver
import gc
import extrafiles
extrafiles.start()
from main import flipkart_parse
from block import block
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.ERROR)
handler = RotatingFileHandler("log.txt", maxBytes=10000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

foldername = "guj/"
if not os.path.exists(foldername):
    os.mkdir(foldername)


def creation_time(path_to_file):
    current = time.time()
    try:
        return current-float(os.path.getctime(path_to_file))
    except Exception as e:
        print(str(e))
        return 0

def pcmemory():
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0] / 2. ** 20  # memory use in GB...I think
    print('memory use:', round(memoryUse, 2), "MB")
    if memoryUse > 300:
        os.system("python " + __file__)
        print("Restarting memory usage exceeds ...........")
        sys.exit()

def dowork():
    arr = []
    res_queue = Queue()

    arr.append(['kitchenstorage_50.txt', 0, False,'https://www.flipkart.com/kitchen-cookware-serveware/kitchen-storage-containers/pr?sid=upp%2C5ix&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D50'])
    arr.append(['barware_100.txt', 0, False,'https://www.flipkart.com/kitchen-cookware-serveware/barware/pr?sid=upp%2Cta2&otracker=categorytree&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D100&sort=price_asc'])
    arr.append(['hddbrand_disc2000.txt', 0, False,'https://www.flipkart.com/computers/storage/hdd/pr?sid=6bo%2Cjdy%2Cnl6&otracker=categorytree&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DSeagate&p%5B%5D=facets.brand%255B%255D%3DWD&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['ssdbrand_disc2000.txt', 0, False,'https://www.flipkart.com/computers/storage/ssd/pr?sid=6bo%2Cjdy%2Cdus&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000&p%5B%5D=facets.brand%255B%255D%3DWD&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DSeagate&p%5B%5D=facets.brand%255B%255D%3DKINGSTON&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DWESTERN%2BDIGITAL&p%5B%5D=facets.brand%255B%255D%3DSanDisk'])
    arr.append(['memcapacity_disc250.txt', 0, False,'https://www.flipkart.com/computers/storage/memory-cards/pr?sid=6bo%2Cjdy%2Ctby&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D250&p%5B%5D=facets.capacity%255B%255D%3D1%2BTB&p%5B%5D=facets.capacity%255B%255D%3D128&p%5B%5D=facets.capacity%255B%255D%3D128%2BGB&p%5B%5D=facets.capacity%255B%255D%3D256%2BGB&p%5B%5D=facets.capacity%255B%255D%3D512&p%5B%5D=facets.capacity%255B%255D%3D512%2BGB&p%5B%5D=facets.capacity%255B%255D%3D64&p%5B%5D=facets.capacity%255B%255D%3D64%2BGB'])
    arr.append(['pdcapacity_disc200.txt', 0, False,'https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D200&p%5B%5D=facets.capacity%255B%255D%3D1%2BTB&p%5B%5D=facets.capacity%255B%255D%3D128&p%5B%5D=facets.capacity%255B%255D%3D128%2BGB&p%5B%5D=facets.capacity%255B%255D%3D256%2BGB&p%5B%5D=facets.capacity%255B%255D%3D512&p%5B%5D=facets.capacity%255B%255D%3D512%2BGB&p%5B%5D=facets.capacity%255B%255D%3D64&p%5B%5D=facets.capacity%255B%255D%3D64%2BGB'])
    arr.append(['printerbrand_disc4000.txt', 0, False,'https://www.flipkart.com/computers/computer-peripherals/printers-inks/printers/pr?sid=6bo%2Ctia%2Cffn%2Ct64&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.brand%255B%255D%3DSAMSUNG&p[]=facets.brand%255B%255D%3DHP&p[]=facets.brand%255B%255D%3DEpson&p[]=facets.brand%255B%255D%3DCanon&p[]=facets.brand%255B%255D%3Dbrother&p[]=facets.brand%255B%255D%3DXerox&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D4000'])
    arr.append(['laptop_disc20000.txt', 0, False,'https://www.flipkart.com/computers/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['monitorbrand_disc2000.txt', 0, False,'https://www.flipkart.com/computers/monitors/pr?sid=6bo%2C9no&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DDELL&p%5B%5D=facets.brand%255B%255D%3Dacer&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DBenQ&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DMSI&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DMarQ%2Bby%2BFlipkart&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['pcbrand_disc6000.txt', 0, False,'https://www.flipkart.com/computers/desktop-pcs/pr?sid=6bo%2Cnl4&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.brand%255B%255D%3DHP&p[]=facets.brand%255B%255D%3DLenovo&p[]=facets.brand%255B%255D%3DAssembled&p[]=facets.brand%255B%255D%3DAssembled%2BTower%2BPC&p[]=facets.brand%255B%255D%3DASUS&p[]=facets.brand%255B%255D%3Diball&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D6000'])
    arr.append(['routertype_disc2000.txt', 0, False,'https://www.flipkart.com/computers/routers/pr?sid=6bo%2C2a2&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.frequency_band%255B%255D%3DDual%2BBand&p%5B%5D=facets.frequency_band%255B%255D%3DTri%2BBand&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['routersbrand_disc2000.txt', 0, False,'https://www.flipkart.com/computers/routers/pr?sid=6bo%2C2a2&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DTP-Link&p%5B%5D=facets.brand%255B%255D%3DD-Link&p%5B%5D=facets.brand%255B%255D%3DTENDA&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DNETGEAR&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DLINKSYS&p%5B%5D=facets.brand%255B%255D%3DMikroTik&p%5B%5D=facets.brand%255B%255D%3DSyrotech&p%5B%5D=facets.brand%255B%255D%3DT%2BP%2BLINK&p%5B%5D=facets.brand%255B%255D%3DAirtel&p%5B%5D=facets.brand%255B%255D%3DJio&p%5B%5D=facets.brand%255B%255D%3DJioFi&p%5B%5D=facets.brand%255B%255D%3DDlink&p%5B%5D=facets.brand%255B%255D%3Dmercusys&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['keyboardbrand_disc500.txt', 0, False,'https://www.flipkart.com/laptop-accessories/keyboards/pr?sid=6bo%2Cai3%2C3oe&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DLogitech&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DFlipkart%2BSmartBuy&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DPortronics&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3Dacer&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DDell&p%5B%5D=facets.brand%255B%255D%3DZebronics&p%5B%5D=facets.brand%255B%255D%3DMicrosoft&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['wirelessmouse_disc200.txt', 0, False,'https://www.flipkart.com/laptop-accessories/mouse/pr?sid=6bo%2Cai3%2C2ay&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.interface%255B%255D%3D2.4GHz%2BWireless&p[]=facets.interface%255B%255D%3DBluetooth&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D200'])
    arr.append(['laptopbags_disc100.txt', 0, False,'https://www.flipkart.com/bags-wallets-belts/bags-backpacks/laptop-bags/pr?sid=reh%2C4d7%2Cx9i&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['speakersbrand_disc1000.txt', 0, False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.price_range.from%3DMin&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.to%3D1000&p%5B%5D=facets.brand%255B%255D%3DPhilips&p%5B%5D=facets.brand%255B%255D%3DSony&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DMarQ%2Bby%2BFlipkart&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DBlaupunkt&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DPolk%2BAudio&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DThomson&p%5B%5D=facets.brand%255B%255D%3DSansui&p%5B%5D=facets.brand%255B%255D%3DF%2526D&p%5B%5D=facets.brand%255B%255D%3DCreative&p%5B%5D=facets.brand%255B%255D%3DAmkette&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.brand%255B%255D%3DDENON&p%5B%5D=facets.brand%255B%255D%3DGIZMORE&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DBoult%2BAudio&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DJBL%2BCommercial&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['soundbarbrand_disc1000.txt', 0, False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&param=10&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNvdW5kYmFycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=1.productCard.PMU_V2_1&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000&p%5B%5D=facets.type%255B%255D%3DSoundbar&p%5B%5D=facets.brand%255B%255D%3DPhilips&p%5B%5D=facets.brand%255B%255D%3DSony&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DMarQ%2Bby%2BFlipkart&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DBlaupunkt&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DZebronics&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DPortronics&p%5B%5D=facets.brand%255B%255D%3DPolk%2BAudio&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DThomson&p%5B%5D=facets.brand%255B%255D%3DSansui&p%5B%5D=facets.brand%255B%255D%3DF%2526D&p%5B%5D=facets.brand%255B%255D%3DCreative&p%5B%5D=facets.brand%255B%255D%3DAnt%2BAudio&p%5B%5D=facets.brand%255B%255D%3DAmkette&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DIball&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.brand%255B%255D%3DGIZMORE&p%5B%5D=facets.brand%255B%255D%3DDENON&p%5B%5D=facets.brand%255B%255D%3DPanasonic'])
    arr.append(['hometheatrebrand_disc1500.txt', 0, False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&param=3&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkhvbWUgVGhlYXRyZXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=3.productCard.PMU_V2_2&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.type%255B%255D%3DHome%2BTheatre&p%5B%5D=facets.type%255B%255D%3DTower%2BSpeaker&p%5B%5D=facets.brand%255B%255D%3DF%2526D&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DBlaupunkt&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DMarQ%2Bby%2BFlipkart&p%5B%5D=facets.brand%255B%255D%3DLogitech&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DSony&p%5B%5D=facets.brand%255B%255D%3DZebronics&p%5B%5D=facets.brand%255B%255D%3DPhilips&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DIball&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500'])
    arr.append(['cctvbrand_disc1000.txt', 0, False,'https://www.flipkart.com/automation-robotics/surveillance-devices/security-cameras/pr?sid=igc%2Cj69%2Cagd&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.brand%255B%255D%3DCP%2BPLUS&p[]=facets.brand%255B%255D%3DMi&p[]=facets.brand%255B%255D%3DHik%2BVision&p[]=facets.brand%255B%255D%3DHIKVISION&p[]=facets.brand%255B%255D%3DTP-Link&p[]=facets.brand%255B%255D%3DZEBRONICS&p[]=facets.brand%255B%255D%3DHALONIX&p[]=facets.brand%255B%255D%3DHawkvision&p[]=facets.brand%255B%255D%3DD-Link&p[]=facets.brand%255B%255D%3Dhawkeye&p[]=facets.brand%255B%255D%3Dcpplus&p[]=facets.brand%255B%255D%3DXiaomi&p[]=facets.brand%255B%255D%3DWipro&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D1000'])
    arr.append(['dslrbrand_10000.txt', 0, False,'https://www.flipkart.com/search?sid=jek%2Cp31%2Ctrv&otracker=CLP_Filters&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DCanon&p%5B%5D=facets.brand%255B%255D%3DNIKON&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DFUJIFILM&p%5B%5D=facets.brand%255B%255D%3DOLYMPUS&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['smartbulbbrand_disc500.txt', 0, False,'https://www.flipkart.com/automation-robotics/smart-lighting/pr?sid=igc%2Cb4q&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_6b5ae26f-c9d6-400b-9d53-b888b7d92f00_1_372UD5BXDFYS_MC.SVYH9PFY273Y&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics%7ESmart%2BHome%2Bautomation%7ESmart%2BLights_SVYH9PFY273Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=SVYH9PFY273Y&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DSmitch&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['smartwatchbrand_disc1000.txt', 0, False,'https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy%2Cbuh&p%5B%5D=facets.discount_range_v1%255B%255D%3D40%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DNoise&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DFire-Boltt&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DFITBIT&p%5B%5D=facets.brand%255B%255D%3DAmbrane&p%5B%5D=facets.brand%255B%255D%3DAmazfit&p%5B%5D=facets.brand%255B%255D%3DTitan&p%5B%5D=facets.brand%255B%255D%3DFastrack&p%5B%5D=facets.brand%255B%255D%3DFOSSIL&p%5B%5D=facets.brand%255B%255D%3DGARMIN&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DGOQii&p%5B%5D=facets.brand%255B%255D%3DDIZO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['diapersbrand_disc100.txt', 0, False,'https://www.flipkart.com/baby-care/diaper-potty-training/baby-diapers/pr?sid=kyh%2Cfdp%2Cyvf&p%5B%5D=facets.discount_range_v1%255B%255D%3D30%2525%2Bor%2Bmore&otracker=categorytree&otracker=nmenu_sub_Baby+%26+Kids_0_Diapers&otracker=nmenu_sub_Baby+%26+Kids_0_Diapers&otracker=nmenu_sub_Baby+%26+Kids_0_Diapers&otracker=nmenu_sub_Baby+%26+Kids_0_Diapers&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DMamypoko&p%5B%5D=facets.brand%255B%255D%3DPampers&p%5B%5D=facets.brand%255B%255D%3DHuggies&p%5B%5D=facets.brand%255B%255D%3DLittle%2BAngel&p%5B%5D=facets.brand%255B%255D%3DHIMALAYA&p%5B%5D=facets.brand%255B%255D%3DMiss%2B%2526%2BChief&p%5B%5D=facets.brand%255B%255D%3DLittle%2527s&p%5B%5D=facets.brand%255B%255D%3DMAMY%2BPOKO%2BPANTS&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D100'])
    arr.append(['mobilebrand_disc50.txt', 0, False,'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000&p%5B%5D=facets.type%255B%255D%3DSmartphones&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DAPPLE&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DInfocus&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3Dvivo'])
    arr.append(['mobile_disc5000.txt', 0, False,'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.type%255B%255D%3DSmartphones&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D5000'])
    arr.append(['tvsize_disc12000.txt', 0, False,'https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIjQwLTQzIEluY2ggVFZzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=16.productCard.PMU_V2_7&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D30%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.screen_size%255B%255D%3D39%2B-%2B43%2Binch&p[]=facets.screen_size%255B%255D%3D48%2B-%2B55%2Binch&p[]=facets.screen_size%255B%255D%3D60%2Binch%2B%2BAbove&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D12000'])
    arr.append(['tv_disc5000.txt', 0, False,'https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIjQwLTQzIEluY2ggVFZzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=16.productCard.PMU_V2_7&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D5000&p[]=facets.discount_range_v1%255B%255D%3D30%2525%2Bor%2Bmore'])
    arr.append(['voltagestab.txt', 0, False, 'https://www.flipkart.com/computers/tv-video-accessories/voltage-stabilizers/pr?sid=6bo%2Cul6%2Cv9r&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.serviceability[]%3Dtrue&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D1000'])
    arr.append(['ebikes.txt', 0, False, 'https://www.flipkart.com/exercise-fitness/fitness-equipment/exercise-bikes/pr?sid=qoc%2Camf%2Ceut&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['crosstrainers.txt', 0, False, 'https://www.flipkart.com/exercise-fitness/fitness-equipment/cross-trainers/pr?sid=qoc%2Camf%2Cgci&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.serviceability[]%3Dtrue&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D9000'])
    arr.append(['fitnessequip.txt', 0, False, 'https://www.flipkart.com/exercise-fitness/fitness-equipment/pr?sid=qoc%2Camf&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.serviceability[]%3Dtrue&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D150'])
    arr.append(['fitness_accessories.txt', 0, False, 'https://www.flipkart.com/exercise-fitness/fitness-accessories/pr?sid=qoc%2Cacb&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.serviceability[]%3Dtrue&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D80'])
    arr.append(['sports.txt', 0, False, 'https://www.flipkart.com/search?sid=abc&otracker=CLP_Filters&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D60&p[]=facets.serviceability[]%3Dtrue&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc'])
    arr.append(['kitchenstorage.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/kitchen-storage-containers/pr?sid=upp%2C5ix&otracker=nmenu_sub_Home+%26+Furniture_0_Kitchen+Storage&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D50&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529'])
    arr.append(['mop.txt', 0, False, 'https://www.flipkart.com/home-cleaning-bathroom-accessories/cleaning-supplies/mops/pr?sid=rja%2Cz2d%2Cxrz&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D100'])
    arr.append(['washingpowder.txt', 0, False, 'https://www.flipkart.com/home-cleaning-bathroom-accessories/household-supplies/washing-powders/pr?sid=rja%2Cplv%2Cbwz&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DSurf%2Bexcel&p%5B%5D=facets.brand%255B%255D%3DAriel&p%5B%5D=facets.brand%255B%255D%3DTide&p%5B%5D=facets.brand%255B%255D%3DGhadi&p%5B%5D=facets.brand%255B%255D%3DRin&p%5B%5D=facets.brand%255B%255D%3DDescalers&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DDettol&p%5B%5D=facets.brand%255B%255D%3DFlipkart%2BSupermart&p%5B%5D=facets.brand%255B%255D%3DGhadi%2BDetergent%2BPowder&p%5B%5D=facets.brand%255B%255D%3DSurf&p%5B%5D=facets.brand%255B%255D%3DWheel'])
    arr.append(['homedecor.txt', 0, False, 'https://www.flipkart.com/home-decor/pr?sid=arb&marketplace=FLIPKART&otracker=nmenu_sub_Home+%26+Furniture_0_Home+Decor&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D50'])
    arr.append(['homefurnishing.txt', 0, False, 'https://www.flipkart.com/home-furnishing/pr?sid=jra&marketplace=FLIPKART&otracker=nmenu_sub_Home+%26+Furniture_0_Furnishing&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D90'])
    arr.append(['furniture.txt', 0, False, 'https://www.flipkart.com/furniture/pr?sid=wwe&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D100'])

    if creation_time(foldername)<1200:
        telegram = "off"
    else:
        telegram = "on"
    threads = []

    for i in arr:
        filename = foldername + i[0]
        force = i[1]
        notassured = i[2]
        url = i[3]
        process = Thread(target=flipkart_parse, args=[filename, telegram, force, url, res_queue, notassured])
        process.setDaemon(True)
        process.start()
        threads.append(process)

    process = Thread(target=block, args=[foldername])
    process.start()
    threads.append(process)

    process = Thread(target=updatetoserver, args=[foldername])
    process.start()
    threads.append(process)

    for process in threads:
        process.join()

    print("\nTotal Active Threads : " + str(threading.active_count()))
    print("Telegram = " + telegram)
    #pcmemory()

    with open(foldername.strip("/") + '_output.txt', 'w+') as fall:
        res_queue.put(None)
        while True:
            item=res_queue.get()
            if item is None:
                break
            fall.write(item + "\r\n")
        fall.write("Telegram = " + telegram)
    res_queue.empty()
    del res_queue
    collected = gc.collect()
    print("Garbage collector: collected", "%d objects." % collected)

while True:
    try:
        clear()
        dowork()
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())

    d = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    hour = d.hour
    if hour >= 3 and hour <= 7:
        sleep = random.randint(5, 10)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
    else:
        sleep = random.randint(1, 3)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
