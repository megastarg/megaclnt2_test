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
import sync_data
sync_data.start_sync_thread()
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


foldername = "W_appliences_HKPK/"
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
 
    arr.append(['kappliance_microwaveU3k.txt', 1,False,'https://www.flipkart.com/home-kitchen/kitchen-appliances/microwave-ovens/pr?sid=j9e%2Cm38%2Co49&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D3000'])
    arr.append(['kappliance_electrictandooeU500.txt', 1,False,'https://www.flipkart.com/home-kitchen/kitchen-appliances/electric-tandoor/pr?sid=j9e%2Cm38%2Ceun&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['kappliance_mixerjuierU1k.txt', 1,False,'https://www.flipkart.com/home-kitchen/kitchen-appliances/mixer-juicer-grinder/pr?sid=j9e%2Cm38%2C7ek&otracker=categorytree&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000&p%5B%5D=facets.brand%255B%255D%3DButterfly&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DPrestige&p%5B%5D=facets.brand%255B%255D%3DPreethi&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DWONDERCHEF&p%5B%5D=facets.brand%255B%255D%3DGlen&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DSUJATA&p%5B%5D=facets.brand%255B%255D%3DMAHARAJA%2BWHITELINE&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DBOSS&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DBOROSIL&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.brand%255B%255D%3DMorphy%2BRichards&p%5B%5D=facets.brand%255B%255D%3DBMS%2BLifestyle&p%5B%5D=facets.brand%255B%255D%3DPigeon&p%5B%5D=facets.brand%255B%255D%3DGreenchef&p%5B%5D=facets.brand%255B%255D%3DFABER&p%5B%5D=facets.brand%255B%255D%3Dmi%2Bstar&p%5B%5D=facets.brand%255B%255D%3DLifelong&p%5B%5D=facets.brand%255B%255D%3DKenstar&p%5B%5D=facets.brand%255B%255D%3DPadmini%2BEssentia&p%5B%5D=facets.brand%255B%255D%3DKENT&p%5B%5D=facets.brand%255B%255D%3DKhaitan%2BOrfin&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DKuvings&p%5B%5D=facets.brand%255B%255D%3DORPAT&p%5B%5D=facets.brand%255B%255D%3DInalsa&p%5B%5D=facets.brand%255B%255D%3DSinger&p%5B%5D=facets.brand%255B%255D%3Dcello&p%5B%5D=facets.brand%255B%255D%3DACTIVA&p%5B%5D=facets.brand%255B%255D%3DSWISS%2BMILITARY&p%5B%5D=facets.brand%255B%255D%3DImperium&p%5B%5D=facets.brand%255B%255D%3DNutribullet&p%5B%5D=facets.brand%255B%255D%3DKutchina&p%5B%5D=facets.brand%255B%255D%3DSuryaflame&p%5B%5D=facets.brand%255B%255D%3DRico&p%5B%5D=facets.brand%255B%255D%3DORIENT&p%5B%5D=facets.brand%255B%255D%3DAGARO&p%5B%5D=facets.brand%255B%255D%3DTefal&p%5B%5D=facets.brand%255B%255D%3DNutriPro&p%5B%5D=facets.brand%255B%255D%3DMasterChef&p%5B%5D=facets.brand%255B%255D%3DBAJAJ%2BVACCO&p%5B%5D=facets.brand%255B%255D%3DBlack%2B%2526%2BDecker&p%5B%5D=facets.brand%255B%255D%3DPigeon%2Bby%2BStovekraft&p%5B%5D=facets.brand%255B%255D%3DPADMINI&p%5B%5D=facets.brand%255B%255D%3DNutrismart&p%5B%5D=facets.brand%255B%255D%3DSunflame&p%5B%5D=facets.brand%255B%255D%3DBPL&p%5B%5D=facets.brand%255B%255D%3DAtomberg&p%5B%5D=facets.brand%255B%255D%3DKhaitanAvaante&p%5B%5D=facets.brand%255B%255D%3DINALSA%2BMellerware&p%5B%5D=facets.brand%255B%255D%3DEdel%2Bby%2BLifelong&p%5B%5D=facets.brand%255B%255D%3DCrompton%2BGreaves&p%5B%5D=facets.brand%255B%255D%3DChefmaster&p%5B%5D=facets.brand%255B%255D%3DBajaj%2BElectricals&p%5B%5D=facets.brand%255B%255D%3DBlueBerry%2527s&p%5B%5D=facets.brand%255B%255D%3DSmeg&p%5B%5D=facets.brand%255B%255D%3DKITCHEN%2BAID&p%5B%5D=facets.brand%255B%255D%3DGoyal%2BKitchen%2BEquipment&p%5B%5D=facets.brand%255B%255D%3DHafele&p%5B%5D=facets.brand%255B%255D%3DHestia'])
    arr.append(['kappliance_inductioncooktopU1k.txt', 1,False,'https://www.flipkart.com/home-kitchen/kitchen-appliances/induction-cooktops/pr?sid=j9e%2Cm38%2C575&otracker=categorytree&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DPrestige&p%5B%5D=facets.brand%255B%255D%3DPigeon&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DLifelong&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DButterfly&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DBaltra&p%5B%5D=facets.brand%255B%255D%3DPigeon%2Bby%2BStovekraft&p%5B%5D=facets.brand%255B%255D%3Dcello&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DMorphy%2BRichards&p%5B%5D=facets.brand%255B%255D%3DKENT&p%5B%5D=facets.brand%255B%255D%3DGreenchef&p%5B%5D=facets.brand%255B%255D%3DiBELL&p%5B%5D=facets.brand%255B%255D%3DPIGEON%2BBY%2BSTOVE%2BKRAFT&p%5B%5D=facets.brand%255B%255D%3DKenstar&p%5B%5D=facets.brand%255B%255D%3DDivya&p%5B%5D=facets.brand%255B%255D%3Dgoodflame&p%5B%5D=facets.brand%255B%255D%3DWONDERCHEF&p%5B%5D=facets.brand%255B%255D%3DMAHARAJA%2BWHITELINE&p%5B%5D=facets.brand%255B%255D%3DMaplin&p%5B%5D=facets.brand%255B%255D%3DGlen&p%5B%5D=facets.brand%255B%255D%3DSantosh&p%5B%5D=facets.brand%255B%255D%3DGross%2Bchef&p%5B%5D=facets.brand%255B%255D%3DSunflame&p%5B%5D=facets.brand%255B%255D%3DPreethi&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.brand%255B%255D%3DORBIT&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DMasterChef&p%5B%5D=facets.brand%255B%255D%3DBPL&p%5B%5D=facets.brand%255B%255D%3DBlack%2B%2526%2BDecker&p%5B%5D=facets.brand%255B%255D%3DBOROSIL&p%5B%5D=facets.brand%255B%255D%3Dgeneric%2Bbajaj&p%5B%5D=facets.brand%255B%255D%3DWipro&p%5B%5D=facets.brand%255B%255D%3DThomson&p%5B%5D=facets.brand%255B%255D%3DPadmini%2BEssentia&p%5B%5D=facets.brand%255B%255D%3DInalsa&p%5B%5D=facets.brand%255B%255D%3DFABER&p%5B%5D=facets.brand%255B%255D%3DEurofobes&p%5B%5D=facets.brand%255B%255D%3DEVEREST&p%5B%5D=facets.brand%255B%255D%3Dkiran&p%5B%5D=facets.brand%255B%255D%3DHatCo&p%5B%5D=facets.brand%255B%255D%3DEltons&p%5B%5D=facets.brand%255B%255D%3DBOSS&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['kappliance_ChimneyU1500.txt', 1,False,'https://www.flipkart.com/chimney/pr?sid=j9e%2Cm38%2Ctgz&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500'])
    arr.append(['kappliance_dishwasherU4k.txt', 1,False,'https://www.flipkart.com/home-kitchen/kitchen-appliances/dish-washers/pr?sid=j9e%2Cm38%2C58n&otracker=categorytree&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D4000'])
    arr.append(['kappliance_oven_5k.txt', 1,False,'https://www.flipkart.com/microwave-ovens/pr?sid=j9e%2Cm38%2Co49&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D4000'])
    arr.append(['kappliance_refrigrator_U5k.txt', 1,False,'https://www.flipkart.com/refrigerators/pr?sid=j9e%2Cabm%2Chzg&otracker=categorytree&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['kappliance_refrigrator_topbrandU10k.txt', 1,False,'https://www.flipkart.com/refrigerators/pr?sid=j9e%2Cabm%2Chzg&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DHaier&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DVoltas%2BBeko&p%5B%5D=facets.brand%255B%255D%3DLloyd&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DKelvinator&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DHisense&p%5B%5D=facets.brand%255B%255D%3DHitachi&p%5B%5D=facets.brand%255B%255D%3DBPL&p%5B%5D=facets.brand%255B%255D%3DONIDA&p%5B%5D=facets.brand%255B%255D%3DMITASHI&p%5B%5D=facets.brand%255B%255D%3DRockwell&p%5B%5D=facets.brand%255B%255D%3DBlue%2BStar&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_refrigrator_capacity4h5hU25k.txt', 1,False,'https://www.flipkart.com/refrigerators/pr?sid=j9e%2Cabm%2Chzg&otracker=categorytree&p%5B%5D=facets.capacity%255B%255D%3D401%2B-%2B500%2BL&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D501%2B%2BAbove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['kappliance_refrigrator_300lplusU15k.txt', 1,False,'https://www.flipkart.com/refrigerators/pr?sid=j9e%2Cabm%2Chzg&otracker=categorytree&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D301%2B-%2B400%2BL&p%5B%5D=facets.capacity%255B%255D%3D401%2B-%2B500%2BL&p%5B%5D=facets.capacity%255B%255D%3D501%2B%2BAbove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['kappliance_refrigrator_cap2h3hU10k.txt', 1,False,'https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/pr?sid=j9e%2Cabm%2Chzg&otracker=categorytree&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D201%2B-%2B250%2BL&p%5B%5D=facets.capacity%255B%255D%3D251%2B-%2B300%2BL&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_wm_topbrandU5k.txt', 1,False,'https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DGodrej&p%5B%5D=facets.brand%255B%255D%3DVoltas%2BBeko&p%5B%5D=facets.brand%255B%255D%3DHaier&p%5B%5D=facets.brand%255B%255D%3Drealme%2BTechLife&p%5B%5D=facets.brand%255B%255D%3DONIDA&p%5B%5D=facets.brand%255B%255D%3DLloyd&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DThomson&p%5B%5D=facets.brand%255B%255D%3DMOTOROLA&p%5B%5D=facets.brand%255B%255D%3DSiemens&p%5B%5D=facets.brand%255B%255D%3DTCL&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DTOSHIBA&p%5B%5D=facets.brand%255B%255D%3DSansui&p%5B%5D=facets.brand%255B%255D%3DAcer&p%5B%5D=facets.brand%255B%255D%3DKelvinator&p%5B%5D=facets.brand%255B%255D%3DLG%2BElectronics&p%5B%5D=facets.brand%255B%255D%3DVoltas&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['kappliance_wm_allB_3k.txt', 1,False,'https://www.flipkart.com/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D3000'])
    arr.append(['kappliance_wm_ifbboschlgU7k.txt', 1,False,'https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_wm10kg_u7k.txt', 1,False,'https://www.flipkart.com/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.capacity%255B%255D%3D10.1%2Bkg%2B%2BAbove&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D7000'])
    arr.append(['kappliance_wm_frontloadU10k.txt', 1,False,'https://www.flipkart.com/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.function_type%255B%255D%3DFully%2BAutomatic%2BFront%2BLoad&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_wm_fullyautU7k.txt', 1,False,'https://www.flipkart.com/washing-machines/pr?sid=j9e%2Cabm%2C8qx&otracker=categorytree&sort=price_asc&p%5B%5D=facets.function_type%255B%255D%3DFully%2BAutomatic%2BTop%2BLoad&p%5B%5D=facets.function_type%255B%255D%3DFully%2BAutomatic%2BFront%2BLoad&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D7000'])
    arr.append(['kappliance_dishwasheU10k.txt', 1,False,'https://www.flipkart.com/dish-washers/pr?sid=j9e%2Cm38%2C58n&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_dishwasherifboschU25k.txt', 1,False,'https://www.flipkart.com/dish-washers/pr?sid=j9e%2Cm38%2C58n&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D25000'])
    arr.append(['kappliance_vcleanerU1k.txt', 1,False,'https://www.flipkart.com/vacuum-cleaners/pr?sid=j9e%2Cabm%2Cul2&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DAGARO&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DEUREKA%2BFORBES&p%5B%5D=facets.brand%255B%255D%3DInalsa&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DKENT&p%5B%5D=facets.brand%255B%255D%3DPrestige&p%5B%5D=facets.brand%255B%255D%3DDyson&p%5B%5D=facets.brand%255B%255D%3DKarcher&p%5B%5D=facets.brand%255B%255D%3DAmerican%2BMicronic&p%5B%5D=facets.brand%255B%255D%3DBalzano&p%5B%5D=facets.brand%255B%255D%3DBAWALY&p%5B%5D=facets.brand%255B%255D%3DEufy%2Bby%2BAnker&p%5B%5D=facets.brand%255B%255D%3DForbes&p%5B%5D=facets.brand%255B%255D%3DEurocLean&p%5B%5D=facets.brand%255B%255D%3DCPEX&p%5B%5D=facets.brand%255B%255D%3DCHESTON&p%5B%5D=facets.brand%255B%255D%3DCAZAR&p%5B%5D=facets.brand%255B%255D%3DGSCPT&p%5B%5D=facets.brand%255B%255D%3DHPD&p%5B%5D=facets.brand%255B%255D%3DHomevac&p%5B%5D=facets.brand%255B%255D%3DIMPEX&p%5B%5D=facets.brand%255B%255D%3DINGCO&p%5B%5D=facets.brand%255B%255D%3DLyrovo&p%5B%5D=facets.brand%255B%255D%3DPure%2BBot&p%5B%5D=facets.brand%255B%255D%3DPhilips%2BSpeedPro%2BCordless%2BStick%2Bvacuum%2Bcleaner%2B-%2BFC6723%252F01&p%5B%5D=facets.brand%255B%255D%3DMilagrow&p%5B%5D=facets.brand%255B%255D%3DMecTURING&p%5B%5D=facets.brand%255B%255D%3DMcTURING&p%5B%5D=facets.brand%255B%255D%3DMarQ%2BBy%2BFlipkart&p%5B%5D=facets.brand%255B%255D%3DMOSHTU&p%5B%5D=facets.brand%255B%255D%3DM-%2BTREX&p%5B%5D=facets.brand%255B%255D%3DQUFEX&p%5B%5D=facets.brand%255B%255D%3DRoboson&p%5B%5D=facets.brand%255B%255D%3DSTARQ&p%5B%5D=facets.brand%255B%255D%3DSinger&p%5B%5D=facets.brand%255B%255D%3DTAURUS&p%5B%5D=facets.brand%255B%255D%3DTesora&p%5B%5D=facets.brand%255B%255D%3Drealme%2BTechLife&p%5B%5D=facets.brand%255B%255D%3Dhm%2BROBOTS&p%5B%5D=facets.brand%255B%255D%3Dcleanex&p%5B%5D=facets.brand%255B%255D%3Dbosler%2Btools&p%5B%5D=facets.brand%255B%255D%3DWoscher&p%5B%5D=facets.brand%255B%255D%3DTrioflextech&p%5B%5D=facets.brand%255B%255D%3DTomahawk&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3DElectrolux&p%5B%5D=facets.brand%255B%255D%3DHASTHIP&p%5B%5D=facets.brand%255B%255D%3DHEUGOR&p%5B%5D=facets.brand%255B%255D%3DHaier&p%5B%5D=facets.brand%255B%255D%3DInstaCuppa&p%5B%5D=facets.brand%255B%255D%3DROIDMI&p%5B%5D=facets.brand%255B%255D%3DProscenic&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DPRINGLE&p%5B%5D=facets.brand%255B%255D%3DSure%2BFrom%2BForbes&p%5B%5D=facets.brand%255B%255D%3DSweephome&p%5B%5D=facets.brand%255B%255D%3DUpsham&p%5B%5D=facets.brand%255B%255D%3DTriSpear&p%5B%5D=facets.brand%255B%255D%3Daulto&p%5B%5D=facets.brand%255B%255D%3DBUI&p%5B%5D=facets.brand%255B%255D%3DBLACK%252BDECKER&p%5B%5D=facets.brand%255B%255D%3DVOLTZ&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMidea&p%5B%5D=facets.brand%255B%255D%3DLifelong&p%5B%5D=facets.brand%255B%255D%3DFlipkart%2BSmartBuy&p%5B%5D=facets.brand%255B%255D%3DGIGAWATTS&p%5B%5D=facets.brand%255B%255D%3DJCBL%2BAccessories&p%5B%5D=facets.brand%255B%255D%3DOSMON&p%5B%5D=facets.brand%255B%255D%3DTINECO&p%5B%5D=facets.brand%255B%255D%3DiBELL&p%5B%5D=facets.brand%255B%255D%3DEufy&p%5B%5D=facets.brand%255B%255D%3DLAORKOU&p%5B%5D=facets.brand%255B%255D%3Dirobot&p%5B%5D=facets.brand%255B%255D%3DTP-Link&p%5B%5D=facets.brand%255B%255D%3DECOVACS&p%5B%5D=facets.brand%255B%255D%3DILIFE&p%5B%5D=facets.brand%255B%255D%3DDeerma&p%5B%5D=facets.brand%255B%255D%3DBlack%2B%2526%2BDecker&p%5B%5D=facets.brand%255B%255D%3DNP-HVRD&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['kappliance_robotic_vcleanerU5k.txt', 1,False,'https://www.flipkart.com/vacuum-cleaners/pr?sid=j9e%2Cabm%2Cul2&p%5B%5D=facets.type%255B%255D%3DRobotic%2BFloor%2BCleaner&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['speaker_speakertopbranU1k_.txt', 1,False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&q=party+speaker&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DboAt&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DJBL%2BProfessional&p%5B%5D=facets.brand%255B%255D%3DJBL%2BCommercial&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DLogitech&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['speaker_200wU7k_.txt', 1,False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&q=party+speaker&otracker=categorytree&sort=price_asc&p%5B%5D=facets.wattage%255B%255D%3DAbove%2B200%2BW&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DMivi&p%5B%5D=facets.brand%255B%255D%3DGOVO&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DBlaupunkt&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DLogitech&p%5B%5D=facets.brand%255B%255D%3DPortronics&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DZebronics&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D7000'])
    arr.append(['speaker_midwattU2k_.txt', 1,False,'https://www.flipkart.com/audio-video/speakers/pr?sid=0pm%2C0o7&q=party+speaker&otracker=categorytree&sort=price_asc&p%5B%5D=facets.wattage%255B%255D%3D161%2B-%2B200%2BW&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['earphone_BT_earbudU500.txt', 1,False,'https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/pr?sid=0pm%2Cfcn%2C821%2Ca7x&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DOnePlus&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DBoult&p%5B%5D=facets.brand%255B%255D%3DFire-Boltt&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DMivi&p%5B%5D=facets.brand%255B%255D%3DNoise&p%5B%5D=facets.brand%255B%255D%3DPTron&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DZoook&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['earphone_BT_earbudU200.txt', 1,False,'https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/pr?sid=0pm%2Cfcn%2C821%2Ca7x&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DOnePlus&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DboAt&p%5B%5D=facets.brand%255B%255D%3DBoult&p%5B%5D=facets.brand%255B%255D%3DFire-Boltt&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.brand%255B%255D%3DLAVA&p%5B%5D=facets.brand%255B%255D%3DMivi&p%5B%5D=facets.brand%255B%255D%3DNoise&p%5B%5D=facets.brand%255B%255D%3DNu%2BRepublic&p%5B%5D=facets.brand%255B%255D%3DProbus&p%5B%5D=facets.brand%255B%255D%3DPortronics&p%5B%5D=facets.brand%255B%255D%3DPTron&p%5B%5D=facets.brand%255B%255D%3DREDMI&p%5B%5D=facets.brand%255B%255D%3Drealme&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DSkullcandy&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3Dtruke&p%5B%5D=facets.brand%255B%255D%3DTWS&p%5B%5D=facets.brand%255B%255D%3DZEBRONICS&p%5B%5D=facets.brand%255B%255D%3DZoook&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D200'])
    arr.append(['earphone_BT_topbrandU1k.txt', 1,False,'https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/pr?sid=0pm%2Cfcn%2C821%2Ca7x&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.brand%255B%255D%3DSONY&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&p%5B%5D=facets.brand%255B%255D%3DBose&p%5B%5D=facets.brand%255B%255D%3DOnePlus&p%5B%5D=facets.brand%255B%255D%3DSennheiser&p%5B%5D=facets.brand%255B%255D%3DShokz&p%5B%5D=facets.brand%255B%255D%3DJBL&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['cycle_adultgencycleU1000.txt', 1,False,'https://www.flipkart.com/sports/cycling/cycles/adult-cycles/pr?sid=abc%2Culv%2Cixt%2Ci5v&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['cycle_adultcycle50p.txt', 1,False,'https://www.flipkart.com/sports/cycling/cycles/adult-cycles/pr?sid=abc%2Culv%2Cixt%2Ci5v&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500'])
    arr.append(['cycle_gearcycle U1500.txt', 1,False,'https://www.flipkart.com/sports/cycling/cycles/adult-cycles/geared-cycles/pr?sid=abc%2Culv%2Cixt%2Ci5v%2Cyjn&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500'])
    arr.append(['cycle_geardiscountU2500.txt', 1,False,'https://www.flipkart.com/sports/cycling/cycles/adult-cycles/geared-cycles/pr?sid=abc%2Culv%2Cixt%2Ci5v%2Cyjn&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2500'])
    arr.append(['cycle_elctriccycleU10000.txt', 1,False,'https://www.flipkart.com/sports/cycling/electric-cycle/pr?sid=abc%2Culv%2Ctwp&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D10000'])
    arr.append(['cycle_electricd50pU15K.txt', 1,False,'https://www.flipkart.com/sports/cycling/electric-cycle/pr?sid=abc%2Culv%2Ctwp&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D40%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
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
        sleep = random.randint(5, 10)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
    else:
        sleep = random.randint(2, 3)
        print("----------------------- Sleeping for " + str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
