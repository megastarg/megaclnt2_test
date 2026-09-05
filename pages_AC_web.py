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


foldername = "Wextraspl_hkmeg78/"
if not os.path.exists(foldername):
    os.mkdir(foldername)


def creation_time(path_to_file):
    current = time.time()
    try:
        diff = current-float(os.path.getctime(path_to_file))
        print(diff)
        return diff
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

    arr.append(['AC_top4BrandU2ok.txt', 1,False,'https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.type%255B%255D%3DSplit&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DO%2BGeneral&p%5B%5D=facets.brand%255B%255D%3DDaikin&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.brand%255B%255D%3DMitsubishi&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['AC_5starU22k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.energy_rating%255B%255D%3D5Star&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJmcm9tIOKCuTI0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIjUgU3RhciBBQ3MiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJBQ05HWDdVRlVXR1ZRTlZCIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_13b09b93-3632-47e6-98a2-4dc14ed0048a_1.QV6OMOX5VKWI&ppt=clp&ppn=tvs-and-appliances-new-clp-store&ssid=gf8634a4gw0000001714400903571&otracker=dynamic_omu_infinite_Air%2BConditioners_1_1.dealCard.OMU_INFINITE_QV6OMOX5VKWI&cid=QV6OMOX5VKWI&sort=price_asc&p%5B%5D=facets.energy_rating%255B%255D%3D4Star&p%5B%5D=facets.type%255B%255D%3DSplit&p%5B%5D=facets.capacity%255B%255D%3D1.5.Ton&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D22000'])
    arr.append(['AC_2taboveU30k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.energy_rating%255B%255D%3D5Star&otracker=categorytree&sort=price_asc&p%5B%5D=facets.energy_rating%255B%255D%3D4Star&p%5B%5D=facets.type%255B%255D%3DSplit&p%5B%5D=facets.capacity%255B%255D%3D2.Ton%2B%2BAbove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['AC_543starU20k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.energy_rating%255B%255D%3D5Star&sort=price_asc&p%5B%5D=facets.energy_rating%255B%255D%3D4Star&p%5B%5D=facets.energy_rating%255B%255D%3D3Star&p%5B%5D=facets.type%255B%255D%3DSplit&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['AC_ogrneralU30k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DO%2BGeneral&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['AC_daikinU25k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DDaikin&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['AC_mitubishiU30k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DMitsubishi&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['AC_midbrandU25k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DSplit&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DVoltas&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DBlue%2BStar&p%5B%5D=facets.brand%255B%255D%3DLloyd&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.brand%255B%255D%3DCARRIER&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DDaikin&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['AC_belowmidU22k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DSplit&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DHaier&p%5B%5D=facets.brand%255B%255D%3DONIDA&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DTOSHIBA&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D22000'])
    arr.append(['AC_lessthan1tU15k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.capacity%255B%255D%3DLess%2Bthan%2B1%2BTon&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['AC_1pt8tonU30k.txt ', 1, False, 'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D1.8%2BTon&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['AC_1.7tonU30k.txt ', 1, False, 'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D1.7%2BTon&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['AC_1pt456tonU20K.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000&p%5B%5D=facets.capacity%255B%255D%3D1.6%2BTon&p%5B%5D=facets.capacity%255B%255D%3D1.5.Ton&p%5B%5D=facets.capacity%255B%255D%3D1.4%2BTon'])
    arr.append(['AC_voltasU25k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DVoltas&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['AC_lgsamsunU25k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['AC_BCDHU25k.txt', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DDaikin&p%5B%5D=facets.brand%255B%255D%3DBlue%2BStar&p%5B%5D=facets.brand%255B%255D%3DCARRIER&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['AC_others_22k', 1,False,'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DLloyd&p%5B%5D=facets.brand%255B%255D%3DHaier&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DONIDA&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DHisense&p%5B%5D=facets.brand%255B%255D%3DThomson&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DTOSHIBA&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D22000'])
    arr.append(['cooler_bajajdeserU5k.txt', 1,False,'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DDesert&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['cooler_symphonyU5k.txt', 1,False,'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DDesert&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DSymphony&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['cooler_kencromorientU5k.txt', 1,False,'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DDesert&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DHindware&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['cooler_otherstop_5k.txt', 1,False,'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DDesert&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DKenstar&p%5B%5D=facets.brand%255B%255D%3DVoltas&p%5B%5D=facets.brand%255B%255D%3DSansui&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DBlue%2BStar&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['mob_tablet_U3000k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.connectivity%255B%255D%3D4G&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%2BOnly&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%252B4G&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%252B5G&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D3000'])
    arr.append(['mob_tablet_topBU10k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.connectivity%255B%255D%3D4G&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%2BOnly&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%252B4G&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%252B5G&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D3000'])
    arr.append(['mob_tablet_U5k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DAPPLE&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DTCL&p%5B%5D=facets.brand%255B%255D%3DMICROSOFT&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DDELL&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DMaplin&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DWishtel&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DElevn&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DOppo&p%5B%5D=facets.brand%255B%255D%3DLifeDigital&p%5B%5D=facets.brand%255B%255D%3DCornea&p%5B%5D=facets.brand%255B%255D%3DWings&p%5B%5D=facets.brand%255B%255D%3DValve&p%5B%5D=facets.brand%255B%255D%3DFUSION5&p%5B%5D=facets.brand%255B%255D%3Ditel&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DBaatu&p%5B%5D=facets.brand%255B%255D%3DAvita&p%5B%5D=facets.brand%255B%255D%3DCoolpad&p%5B%5D=facets.brand%255B%255D%3DE%2526L&p%5B%5D=facets.brand%255B%255D%3DGIONEE&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DElephone&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['mob_tabSamsung128256U20k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&marketplace=FLIPKART&otracker=product_breadCrumbs_Tablets&p%5B%5D=facets.internal_storage%255B%255D%3D256%2BGB%2B%2526%2BAbove&sort=price_asc&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_tabApple_U20k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_tab256U20k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.internal_storage%255B%255D%3D256%2BGB%2B%2526%2BAbove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_tabw5g_U20k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.connectivity%255B%255D%3DWi-Fi%252B5G&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_tabquadhd_30k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.display%255B%255D%3DQuad%2BHD&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['mob_tabwuxga+_U20k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.display%255B%255D%3DWUXGA%252B&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_tab1416inc_U25k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.display_size%255B%255D%3D15%2Binch%2B-%2B15.9%2Binch&p%5B%5D=facets.display_size%255B%255D%3D14%2Binch%2B-%2B14.9%2Binch&p%5B%5D=facets.display_size%255B%255D%3D13%2Binch%2B-%2B13.9%2Binch&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['mob_tab12inplus_U25k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&p%5B%5D=facets.display_size%255B%255D%3D12%2BInch%2B%2526%2BAbove&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['mob_gentab_U7k.txt', 1,False,'https://www.flipkart.com/tablets/pr?sid=tyy%2Chry&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DTCL&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D7000'])
    arr.append(['mob_tab_appleC_u25k.txt', 1,False,'https://www.flipkart.com/tablets/tablets-with-call-facility/pr?sid=tyy%2Chry%2Cadj&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['laptop_32plus_u95k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&otracker=product_breadCrumbs_Laptops&sort=price_asc&p%5B%5D=facets.system_memory%255B%255D%3D36%2BGB&p%5B%5D=facets.system_memory%255B%255D%3D48%2BGB&p%5B%5D=facets.system_memory%255B%255D%3D64%2BGB&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D95000'])
    arr.append(['laptop_2tb_u50k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&otracker=product_breadCrumbs_Laptops&sort=price_asc&p%5B%5D=facets.ssd_capacity%255B%255D%3D2%2BTB&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D50000'])
    arr.append(['laptop_gr8plus_u60k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&marketplace=FLIPKART&otracker=product_breadCrumbs_Laptops&sort=price_asc&p%5B%5D=facets.dedicated_graphics_memory%255B%255D%3D16%2BGB&p%5B%5D=facets.dedicated_graphics_memory%255B%255D%3D12%2BGB&p%5B%5D=facets.dedicated_graphics_memory%255B%255D%3D8%2BGB&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D60000'])
    arr.append(['laptop_mac_u50k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.operating_system%255B%255D%3DMac%2BOS&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D50000'])
    arr.append(['laptop_gamin_u30k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DGaming%2BLaptop&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['laptop_dualscren_u90k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DDual%2BScreen%2BLaptop&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D90000'])
    arr.append(['laptop_creater_u40k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DCreator%2BLaptop&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D40000'])
    arr.append(['laptop_14gen_u50k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.processor_generation%255B%255D%3D14th%2BGen&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D50000'])
    arr.append(['laptop_business_u20k.txt', 1,False,'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DBusiness%2BLaptop&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_esm_u20k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.sim_type%255B%255D%3DDual%2BSim%2528Physical%2B%252B%2BeSIM%2529&p%5B%5D=facets.sim_type%255B%255D%3DDual%2BSim%2528Nano%2B%252B%2BeSIM%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_moto5gU10k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['mob_smsungU10k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['mob_1plusU15K.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['mob_GphoneU20k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['mob_appleU30k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['mob_iqooU10k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DIQOO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['mob_asusU30k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DASUS&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D30000'])
    arr.append(['mob_nothingU15k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&sort=price_asc&p%5B%5D=facets.network_type%255B%255D%3D5G&p%5B%5D=facets.brand%255B%255D%3DNothing&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['mob_highresoU15k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.resolution_type%255B%255D%3DSuper%2BRetina%2BXDR%2BDisplay&sort=price_asc&p%5B%5D=facets.resolution_type%255B%255D%3DSuper%2BRetina%2BHD%2BDisplay&p%5B%5D=facets.resolution_type%255B%255D%3DLiquid%2BRetina%2BHD%2BDisplay&p%5B%5D=facets.resolution_type%255B%255D%3DRetina%2BHD%2BDisplay&p%5B%5D=facets.resolution_type%255B%255D%3DRetina%2BDisplay&p%5B%5D=facets.resolution_type%255B%255D%3DQuad%2BHD%252B&p%5B%5D=facets.resolution_type%255B%255D%3DQuad%2BHD&p%5B%5D=facets.resolution_type%255B%255D%3DFull%2BHD%252B%2BE3%2BSuper%2BAMOLED%2BDisplay&p%5B%5D=facets.resolution_type%255B%255D%3DUHD%2B4K&p%5B%5D=facets.resolution_type%255B%255D%3DWQHD&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['mob_vivoU8k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.network_type%255B%255D%3D5G&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3Dvivo&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
    arr.append(['mob_oppoU8k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
    arr.append(['mob_realmeU8k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
    arr.append(['mob_pocoU7k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DPOCO&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D7000'])
    arr.append(['mob_infinixU8k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DInfinix&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
    arr.append(['mob_redmiU8k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
    arr.append(['mob_MiU15k.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['mob_otherU8K.txt', 1,False,'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.network_type%255B%255D%3D5G&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DTecno&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D8000'])
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
        #clear()
        dowork()
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())

    d = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    hour = d.hour
    if hour >= 3 and hour <= 7:
        sleep = random.randint(1, 2)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
    else:
        sleep = random.randint(1, 2)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
