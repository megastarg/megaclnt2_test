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
from multiprocessing import Process, Queue
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
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

foldername = "krnar1/"
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

    arr.append(['tv_6k.txt', 0, False, 'https://www.flipkart.com/search?sid=czl&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=discount&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D5000'])
    arr.append(['jacket_350.txt', 0, True, 'https://www.flipkart.com/mens-clothing/winter-seasonal-wear/jackets/pr?sid=2oq%2Cs9b%2Cqgu%2C8cd&otracker=nmenu_sub_Men_0_Jackets&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D350'])
    arr.append(['homekitchen_500.txt', 0, False, 'https://www.flipkart.com/home-kitchen/pr?sid=j9e&marketplace=FLIPKART&otracker=product_breadCrumbs_Home+%26+Kitchen&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D130&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2BMore'])
    arr.append(['hdd_3k.txt', 0, False, 'https://www.flipkart.com/computers/storage/external-hard-disks/pr?sid=6bo%2Cjdy%2Cnl6&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&wid=9.productCard.PMU_V2_6&sort=price_asc&p[]=facets.price_range.from%3D2010&p[]=facets.price_range.to%3D3000'])
    arr.append(['gasstoveB_2000.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/gas-stove-accessories/gas-stoves/pr?sid=upp%2Cd7m%2Cuhm&marketplace=FLIPKART&otracker=product_breadCrumbs_Gas+Stoves&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.brand%255B%255D%3DPrestige&p%5B%5D=facets.brand%255B%255D%3DPigeon&p%5B%5D=facets.brand%255B%255D%3DButterfly&p%5B%5D=facets.brand%255B%255D%3DSunflame&p%5B%5D=facets.brand%255B%255D%3DLifelong&p%5B%5D=facets.brand%255B%255D%3DElica&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DBalaji&p%5B%5D=facets.brand%255B%255D%3DBalajiflame&p%5B%5D=facets.brand%255B%255D%3DBOROSIL&p%5B%5D=facets.brand%255B%255D%3DBOSCH&p%5B%5D=facets.brand%255B%255D%3Dcello&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DFaber&p%5B%5D=facets.brand%255B%255D%3DHindware&p%5B%5D=facets.brand%255B%255D%3DIFB&p%5B%5D=facets.brand%255B%255D%3DIMPEX&p%5B%5D=facets.brand%255B%255D%3DKhaitan&p%5B%5D=facets.brand%255B%255D%3DMAHARAJA%2BWHITELINE&p%5B%5D=facets.brand%255B%255D%3DMILTON&p%5B%5D=facets.brand%255B%255D%3DPIGEON%2BBY%2BSTOVE%2BKRAFT&p%5B%5D=facets.brand%255B%255D%3DPigeon%2Bby%2BStovekraft&p%5B%5D=facets.brand%255B%255D%3DSinger&p%5B%5D=facets.brand%255B%255D%3DSun%2BFlame&p%5B%5D=facets.brand%255B%255D%3DSURYA&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DWhirlpool&p%5B%5D=facets.brand%255B%255D%3DWONDERCHEF&p%5B%5D=facets.brand%255B%255D%3DUrban%2BFlame&p%5B%5D=facets.brand%255B%255D%3DKaff&p%5B%5D=facets.brand%255B%255D%3DKraft%2BItaly&p%5B%5D=facets.brand%255B%255D%3DHafele&p%5B%5D=facets.brand%255B%255D%3DMeglio&p%5B%5D=facets.brand%255B%255D%3DGlen&p%5B%5D=facets.brand%255B%255D%3DALSTORM&p%5B%5D=facets.brand%255B%255D%3DSunblaze&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['fridge_7k.txt', 0, False, 'https://www.flipkart.com/search?sid=j9e%2Fabm%2Fhzg&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=discount&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D7000'])
    arr.append(['fans_1000.txt', 0, False, 'https://www.flipkart.com/fans/pr?sid=j9e%2Cabm%2Clbz&otracker=categorytree&sort=price_asc&p%5B%5D=facets.brand%255B%255D%3DAtomberg&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DPolycab&p%5B%5D=facets.brand%255B%255D%3DLUMINOUS&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DVenus&p%5B%5D=facets.brand%255B%255D%3DHindware&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['dslr_20k.txt', 0, False, 'https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D20000'])
    arr.append(['dinnerset_400.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/tableware-dinnerware/dinner-sets/pr?sid=upp%2Ci7t%2Clha&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D400'])
    arr.append(['cycles_2500.txt', 1, False, 'https://www.flipkart.com/sports/cycling/cycles/pr?sid=abc%2Culv%2Cixt&marketplace=FLIPKART&otracker=product_breadCrumbs_Cycles&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2500&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'])
    arr.append(['cycles_5000.txt', 1, False, 'https://www.flipkart.com/sports/cycling/cycles/pr?sid=abc%2Culv%2Cixt&marketplace=FLIPKART&otracker=product_breadCrumbs_Cycles&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['cookware_300.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/cookware/pr?sid=upp%2Ctnx&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D200'])
    arr.append(['cooker_500.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/cookware/pressure-cookers/pr?sid=upp%2Ctnx%2Cgsl&marketplace=FLIPKART&otracker=product_breadCrumbs_Pressure+Cookers&sort=price_asc&affid=harishank6&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D500&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured'])
    arr.append(['caserole_500.txt', 0, False, 'https://www.flipkart.com/kitchen-cookware-serveware/tableware-dinnerware/casseroles/pr?sid=upp%2Ci7t%2Cgka&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D250&sort=price_asc'])
    arr.append(['appliances_500.txt', 0, False, 'https://www.flipkart.com/home-kitchen/~appliances-for-a-healthy-living/pr?sid=j9e&otracker=nmenu_sub_TVs+%26+Appliances_0_Healthy+Living+Appliances&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D600'])
    arr.append(['AC_20k.txt', 0, False, 'https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&marketplace=FLIPKART&otracker=product_breadCrumbs_Air+Conditioners&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['suitcases800.txt', 0, False, 'https://www.flipkart.com/bags-wallets-belts/luggage-travel/suitcases/pr?sid=reh%2Cplk%2Ctvv&p[]=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D800'])
    arr.append(['tube_1000.txt', 0, False, 'https://www.flipkart.com/home-lighting/utility-lighting/tube-lights/pr?sid=jhg%2Cyqn%2C4ms&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.brand%255B%255D%3DWipro&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DHALONIX&p%5B%5D=facets.brand%255B%255D%3DEVEREADY&p%5B%5D=facets.brand%255B%255D%3DGold%2BMedal&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DMURPHY&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DLUMINOUS&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DWipro%2BGarnet%2BPlus&p%5B%5D=facets.brand%255B%255D%3DWipro%2BGarnet&p%5B%5D=facets.brand%255B%255D%3DPigeon%2BLED&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.brand%255B%255D%3DELIANTE&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['cycle_5k.txt', 0, False, 'https://www.flipkart.com/sports/cycling/cycles/pr?sid=abc%2Culv%2Cixt&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['ecycle_10k.txt', 0, False, 'https://www.flipkart.com/sports/cycling/electric-cycle/pr?sid=abc%2Culv%2Ctwp&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D10000'])
    arr.append(['traking_bags_200.txt', 0, False, 'https://www.flipkart.com/sports/camping-hiking/camping-hiking-bags/pr?sid=abc%2Cfvf%2Cv2h&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D200'])
    arr.append(['inverter_3k.txt', 0, False, 'https://www.flipkart.com/home-kitchen/home-appliances/inverters-and-accessories/pr?sid=j9e%2Cabm%2Cve9&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D3000'])
    arr.append(['iron_250.txt', 0, False, 'https://www.flipkart.com/iron/pr?sid=j9e%2Cabm%2Ca0u&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D250'])
    arr.append(['Ro_3k.txt', 0, False, 'https://www.flipkart.com/water-purifiers/pr?sid=j9e%2Cabm%2Ci45&marketplace=FLIPKART&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.capacity%255B%255D%3D7%2BL%2Band%2BBelow&p[]=facets.capacity%255B%255D%3D7.1%2BL%2B-%2B14%2BL&p[]=facets.capacity%255B%255D%3D14.1%2BL%2Band%2BAbove&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D3000'])
    arr.append(['geyser_2k.txt', 0, False, 'https://www.flipkart.com/water-geysers/pr?sid=j9e%2Cabm%2Cbfm&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D2000&p[]=facets.type%255B%255D%3DStorage'])
    arr.append(['heater_500.txt', 0, False, 'https://www.flipkart.com/room-heaters/pr?sid=j9e%2Cabm%2Cxie&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D300'])
    arr.append(['Washingmachine_5k.txt', 0, False, 'https://www.flipkart.com/washing-machines/pr?sid=j9e%2Cabm%2C8qx&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D5000'])
    arr.append(['fridge_6k.txt', 0, False, 'https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/pr?sid=j9e%2Cabm%2Chzg&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D6000'])
    arr.append(['ac_20k.txt', 0, False, 'https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000'])
    arr.append(['landline_500.txt', 0, False, 'https://www.flipkart.com/landline-phones/pr?sid=j9e%2Cabm%2Cn0f&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['coolers_4k.txt', 0, False, 'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D4000&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['fan_1500.txt', 0, False, 'https://www.flipkart.com/fans/pr?sid=j9e%2Cabm%2Clbz&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D40%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1500&p%5B%5D=facets.brand%255B%255D%3DUSHA&p%5B%5D=facets.brand%255B%255D%3DBAJAJ&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DOrient%2BElectric&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DV-Guard&p%5B%5D=facets.brand%255B%255D%3DPolycab&p%5B%5D=facets.brand%255B%255D%3DAtomberg&p%5B%5D=facets.brand%255B%255D%3DVenus&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529'])
    arr.append(['vacc_1k.txt', 0, False, 'https://www.flipkart.com/vacuum-cleaners/pr?sid=j9e%2Cabm%2Cul2&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D1000'])
    arr.append(['surge_150.txt', 0, False, 'https://www.flipkart.com/spike-guards-surge-protectors/pr?sid=j9e%2Cabm%2C0c4&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D150'])
    arr.append(['stabilizers_500.txt', 0, False, 'https://www.flipkart.com/voltage-stabilizers/pr?sid=j9e%2Cabm%2Cxf4&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['seasonal_appliances_1k.txt', 0, False, 'https://www.flipkart.com/all/~cs-vtyvjd8ofm/pr?sid=all&collection-tab-name=Fans+and+Air+Coolers&otracker=clp_creative_card_2_7.creativeCard.CREATIVE_CARD_tvs-and-appliances-new-clp-store_PU58CXPC1SDX&fm=neo%2Fmerchandising&iid=M_e5492390-982a-4391-867c-95aca836acd9_7.PU58CXPC1SDX&ppt=clp&ppn=tvs-and-appliances-new-clp-store&ssid=ndibd7oe7regyghs1662902480615&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D1000'])
    arr.append(['seasonal_appliances_5k.txt', 0, False, 'https://www.flipkart.com/all/~cs-vtyvjd8ofm/pr?sid=all&collection-tab-name=Fans+and+Air+Coolers&otracker=clp_creative_card_2_7.creativeCard.CREATIVE_CARD_tvs-and-appliances-new-clp-store_PU58CXPC1SDX&fm=neo%2Fmerchandising&iid=M_e5492390-982a-4391-867c-95aca836acd9_7.PU58CXPC1SDX&ppt=clp&ppn=tvs-and-appliances-new-clp-store&ssid=ndibd7oe7regyghs1662902480615&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D5000'])
    arr.append(['mixergrinder_1500.txt', 0, False, 'https://www.flipkart.com/mixerjuicergrinders/~cs-vo2m188kg2/pr?sid=j9e%2Cm38%2C7ek&otracker=hp_banner_1_43.bannerX3.BANNER_5BXSJ6OUN04R&fm=neo%2Fmerchandising&iid=M_2b7568ec-bb1e-47a6-8585-30bd49ffaf1e_43.5BXSJ6OUN04R&ppt=hp&ppn=homepage&ssid=7doqpb1c9psyups01681451932857&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D1500'])

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
        process = Thread(target=flipkart_parse, args=[
                         filename, telegram, force, url, res_queue, notassured])
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
            item = res_queue.get()
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
        print("----------------------- Sleeping for " +
              str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
    else:
        sleep = random.randint(2, 3)
        print("----------------------- Sleeping for " +
              str(sleep) + " Seconds ------------------------")
        time.sleep(sleep)
