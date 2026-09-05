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

foldername = "krnar/"
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

    arr.append(['men_trousers.txt', 0, False, 'https://www.flipkart.com/men/trousers/pr?sid=2oq%2Cs9b%2C9uj&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['men_innerwear.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/innerwear-and-swimwear/~cs-axj382hyd1/pr?sid=clo%2Cqfl&otracker=categorytree&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['men_shorts_brand.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/bottomwear/shorts/mens-shorts/pr?sid=clo%2Cvua%2Ce8g%2Ckc7&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.brand%255B%255D%3DHIGHLANDER&p%5B%5D=facets.brand%255B%255D%3DU.S.%2BPOLO%2BASSN.&p%5B%5D=facets.brand%255B%255D%3DAllen%2BSolly&p%5B%5D=facets.brand%255B%255D%3DRaymond&p%5B%5D=facets.brand%255B%255D%3DARROW&p%5B%5D=facets.brand%255B%255D%3DLOUIS%2BPHILIPPE&p%5B%5D=facets.brand%255B%255D%3DVAN%2BHEUSEN&p%5B%5D=facets.brand%255B%255D%3DFLYING%2BMACHINE&p%5B%5D=facets.brand%255B%255D%3DWROGN&p%5B%5D=facets.brand%255B%255D%3DSpykar&p%5B%5D=facets.brand%255B%255D%3DFOREVER%2B21&p%5B%5D=facets.brand%255B%255D%3DPARX&p%5B%5D=facets.brand%255B%255D%3DBlackberrys&p%5B%5D=facets.brand%255B%255D%3DMUFTI&p%5B%5D=facets.brand%255B%255D%3DArrow%2BSport&p%5B%5D=facets.brand%255B%255D%3DPARK%2BAVENUE&p%5B%5D=facets.brand%255B%255D%3DPepe%2BJeans&p%5B%5D=facets.brand%255B%255D%3DCAMPUS%2BSUTRA&p%5B%5D=facets.brand%255B%255D%3DPeter%2BEngland%2BUniversity&p%5B%5D=facets.brand%255B%255D%3DVAN%2BHEUSEN%2BSPORT&p%5B%5D=facets.brand%255B%255D%3DCalvin%2BKlein%2BJeans&p%5B%5D=facets.brand%255B%255D%3DArrow%2BNewyork&p%5B%5D=facets.brand%255B%255D%3DTOMMY%2BHILFIGER&p%5B%5D=facets.brand%255B%255D%3DUnited%2BColors%2Bof%2BBenetton&p%5B%5D=facets.brand%255B%255D%3DCOLORPLUS&p%5B%5D=facets.brand%255B%255D%3DFabindia&p%5B%5D=facets.brand%255B%255D%3DU.S.%2BPolo%2BAssn.%2BDenim%2BCo.&p%5B%5D=facets.brand%255B%255D%3DPeter%2BEngland&p%5B%5D=facets.brand%255B%255D%3DLEVI%2527S&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D150'])
    arr.append(['menclothing.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&otracker=categorytree&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=nmenu_sub_Men_0_Clothing&sort=price_asc&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['men_ethnic.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/kurtas-ethnic-sets-and-bottoms/pr?sid=clo%2Ccfv&otracker[]=categorytree&otracker[]=nmenu_sub_Men_0_Ethnic%20wear&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100&sort=price_asc'])
    arr.append(['men_fabric.txt', 0, False, 'https://www.flipkart.com/mens-clothing/fabrics/pr?sid=2oq%2Cs9b%2C9hz&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['men_tracksuits.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/tracksuits/pr?sid=clo%2Cnyk&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['men_shorts.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/bottomwear/shorts/mens-shorts/pr?sid=clo%2Cvua%2Ce8g%2Ckc7&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&otracker=categorytree&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D70'])
    arr.append(['laptop_50p_1.txt', 1, False, 'https://www.flipkart.com/laptops/pr?p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&count=40&affid=sriyaz083&sid=6bo%2Cb5g&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['laptop_50p.txt', 1, False, 'https://www.flipkart.com/search?sid=6bo%2Cb5g&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['laptop_15k.txt', 1, False, 'https://www.flipkart.com/search?sid=6bo%2Cb5g&otracker=CLP_Filters&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000'])
    arr.append(['cooler_3k.txt', 1, False, 'https://www.flipkart.com/air-coolers/pr?sid=j9e%2Cabm%2C52j&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D3000'])
    arr.append(['bulb_brand80.txt', 1, False, 'https://www.flipkart.com/all/home-lighting/utility-lighting/pr?sid=all%2Cjhg%2Cyqn&otracker=categorytree&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D80%2525%2Bor%2Bmore&p[]=facets.brand%255B%255D%3DSyska&p[]=facets.brand%255B%255D%3DSyska%2BLed%2BLights&p[]=facets.brand%255B%255D%3DEVEREADY&p[]=facets.brand%255B%255D%3DPHILIPS&p[]=facets.brand%255B%255D%3DCrompton&p[]=facets.brand%255B%255D%3DCrompton%2BGreaves&p[]=facets.brand%255B%255D%3DBAJAJ&p[]=facets.brand%255B%255D%3DHAVELLS&p[]=facets.brand%255B%255D%3DWipro&p[]=facets.brand%255B%255D%3DWipro%2BGarnet&p[]=facets.brand%255B%255D%3DWipro%2BGarnet%2BPlus&p[]=facets.brand%255B%255D%3DHALONIX&p[]=facets.brand%255B%255D%3DHALONIX%25C2%25A0&p[]=facets.brand%255B%255D%3DPolycab&p[]=facets.brand%255B%255D%3DLUMINOUS&p[]=facets.brand%255B%255D%3DGoldmedal&p[]=facets.brand%255B%255D%3DOREVA&p[]=facets.brand%255B%255D%3DMURPHY&p[]=facets.brand%255B%255D%3DTISVA&p[]=facets.brand%255B%255D%3DFINOLEX&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D200'])
    arr.append(['binoculars_500.txt', 0, False, 'https://www.flipkart.com/camera-accessories/binoculars-optics/pr?sid=jek%2C6l2%2Cepu&marketplace=FLIPKART&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D500'])
    arr.append(['assistants_2k.txt', 0, False, 'https://www.flipkart.com/automation-robotics/smart-assistants/pr?sid=igc%2Camm&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D2000'])
    arr.append(['bath_linen150.txt', 0, False, 'https://www.flipkart.com/home-furnishing/bath-linen/pr?sid=jra%2Cjk3&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D150'])
    arr.append(['all_footwear_120.txt', 0, False, 'https://www.flipkart.com/footwear/pr?sid=osp&otracker=categorytree&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D80'])
    arr.append(['dryfruits_500.txt', 0, False, 'https://www.flipkart.com/food-products/dry-fruit-nut-seed/dry-fruits/pr?sid=eat%2Cltb%2Cngb&marketplace=FLIPKART&otracker=product_breadCrumbs_Dry+Fruits&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p%5B%5D=facets.fruit_nut_name%255B%255D%3DAlmonds&p%5B%5D=facets.fruit_nut_name%255B%255D%3DCashews&p%5B%5D=facets.fruit_nut_name%255B%255D%3DWalnuts&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500&p%5B%5D=facets.brand%255B%255D%3DHappilo&p%5B%5D=facets.brand%255B%255D%3DWONDERLAND&p%5B%5D=facets.brand%255B%255D%3DNutraj&p%5B%5D=facets.brand%255B%255D%3DNaturoz&p%5B%5D=facets.brand%255B%255D%3DGranola&p%5B%5D=facets.brand%255B%255D%3DTulsi&p%5B%5D=facets.brand%255B%255D%3DPRO%2BORGANIC%2BLIFE&p%5B%5D=facets.brand%255B%255D%3DNature%2BVit&p%5B%5D=facets.brand%255B%255D%3DNutty%2BGritties&p%5B%5D=facets.brand%255B%255D%3DGlomin&p%5B%5D=facets.brand%255B%255D%3DD%2BNATURE%2BFRESH&p%5B%5D=facets.brand%255B%255D%3DYoung%2BN%2BFit&p%5B%5D=facets.brand%255B%255D%3DKHARAWALA%2527S&p%5B%5D=facets.brand%255B%255D%3DNutty%2BNirvana&p%5B%5D=facets.brand%255B%255D%3DOrganic%2BBasket&p%5B%5D=facets.brand%255B%255D%3DCalifornia%2BGold%2BNutrition&p%5B%5D=facets.brand%255B%255D%3DTrue%2BElements'])
    arr.append(['men_briefs_100.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/innerwear-and-swimwear/briefs-and-trunks/pr?sid=clo%2Cqfl%2Cszr&marketplace=FLIPKART&otracker=product_breadCrumbs_Briefs+and+Trunks&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D100'])
    arr.append(['clothes_brand.txt', 0, False, 'https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&marketplace=FLIPKART&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&sort=price_asc&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D300&p%5B%5D=facets.brand%255B%255D%3DLOUIS%2BPHILIPPE&p%5B%5D=facets.brand%255B%255D%3DADIDAS&p%5B%5D=facets.brand%255B%255D%3DAllen%2BSolly&p%5B%5D=facets.brand%255B%255D%3DARROW&p%5B%5D=facets.brand%255B%255D%3DArrow%2BSport&p%5B%5D=facets.brand%255B%255D%3DBlackberrys&p%5B%5D=facets.brand%255B%255D%3DBIBA&p%5B%5D=facets.brand%255B%255D%3DLEE&p%5B%5D=facets.brand%255B%255D%3DLEVI%2527S&p%5B%5D=facets.brand%255B%255D%3DFLYING%2BMACHINE&p%5B%5D=facets.brand%255B%255D%3DJACK%2B%2526%2BJONES&p%5B%5D=facets.brand%255B%255D%3DNIKE&p%5B%5D=facets.brand%255B%255D%3DMARKS%2B%2526%2BSPENCER&p%5B%5D=facets.brand%255B%255D%3DMONTE%2BCARLO&p%5B%5D=facets.brand%255B%255D%3DHIGHLANDER&p%5B%5D=facets.brand%255B%255D%3DPARK%2BAVENUE&p%5B%5D=facets.brand%255B%255D%3DPepe%2BJeans&p%5B%5D=facets.brand%255B%255D%3DPUMA&p%5B%5D=facets.brand%255B%255D%3DRaymond&p%5B%5D=facets.brand%255B%255D%3DSpykar&p%5B%5D=facets.brand%255B%255D%3DU.S.%2BPOLO%2BASSN.&p%5B%5D=facets.brand%255B%255D%3DUnited%2BColors%2Bof%2BBenetton&p%5B%5D=facets.brand%255B%255D%3DTOMMY%2BHILFIGER&p%5B%5D=facets.brand%255B%255D%3DVAN%2BHEUSEN&p%5B%5D=facets.brand%255B%255D%3DVAN%2BHEUSEN%2BSPORT&p%5B%5D=facets.brand%255B%255D%3DPeter%2BEngland&p%5B%5D=facets.brand%255B%255D%3DMUFTI&p%5B%5D=facets.brand%255B%255D%3DWrangler'])
    arr.append(['WM_6k.txt', 0, False, 'https://www.flipkart.com/search?sid=j9e%2Fabm%2F8qx&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=discount&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D6000'])
    arr.append(['vacc_1500.txt', 0, False, 'https://www.flipkart.com/vacuum-cleaners/pr?sid=j9e%2Cabm%2Cul2&otracker=nmenu_sub_Appliances_0_Vacuum+Cleaners&otracker=nmenu_sub_Appliances_0_Vacuum+Cleaners&otracker=nmenu_sub_TVs+%26+Appliances_0_Vacuum+Cleaners&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D1500'])
    arr.append(['audio_video_100.txt', 0, True, 'https://www.flipkart.com/audio-video/pr?sid=0pm&marketplace=FLIPKART&otracker=product_breadCrumbs_Audio+%26+Video&sort=discount&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D100'])
    arr.append(['mattress_brand.txt', 0, False, 'https://www.flipkart.com/furniture/mattresses/pr?sid=wwe%2Crg9&otracker=categorytree&sort=discount&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D2500&p[]=facets.brand%255B%255D%3DSleepyhead&p[]=facets.brand%255B%255D%3DWakefit&p[]=facets.brand%255B%255D%3DSleepX&p[]=facets.brand%255B%255D%3DFlipkart%2BPerfect%2BHomes&p[]=facets.brand%255B%255D%3DPEPS&p[]=facets.brand%255B%255D%3DKURLON&p[]=facets.brand%255B%255D%3DCOIRFIT&p[]=facets.brand%255B%255D%3DSleepyCat&p[]=facets.brand%255B%255D%3DSLEEP%2BSPA&p[]=facets.brand%255B%255D%3DSleepwell&p[]=facets.brand%255B%255D%3Dduroflex&p[]=facets.brand%255B%255D%3DWakeup%2BIndia&p[]=facets.brand%255B%255D%3DTorque&p[]=facets.brand%255B%255D%3DGodrej%2BInterio&p[]=facets.brand%255B%255D%3DFoams%2BIndia&p[]=facets.brand%255B%255D%3DTwigs%2BDirect&p[]=facets.brand%255B%255D%3DRelaxwell&p[]=facets.brand%255B%255D%3DSPRINGFIT&p[]=facets.brand%255B%255D%3DThe%2BSleep%2BCompany&p[]=facets.brand%255B%255D%3Dkurlonmattress&p[]=facets.brand%255B%255D%3DKURLON%2BDUPLEX&p[]=facets.brand%255B%255D%3DKURLON%2BEVERFIRM&p[]=facets.brand%255B%255D%3DKurlon%2Bmatt&p[]=facets.brand%255B%255D%3DSLEEPFRESH&p[]=facets.brand%255B%255D%3DSleep%2BUniverse&p[]=facets.brand%255B%255D%3DGrassberry&p[]=facets.brand%255B%255D%3DUtsav%2BMattresses&p[]=facets.brand%255B%255D%3DCentuary'])
    arr.append(['memorycard_400.txt', 0, False, 'https://www.flipkart.com/computers/storage/memory-cards/pr?sid=6bo%2Cjdy%2Ctby&otracker=nmenu_sub_Electronics_0_Memory+Cards&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D400&p[]=facets.brand%255B%255D%3DHP&p[]=facets.brand%255B%255D%3DSanDisk&p[]=facets.brand%255B%255D%3DStrontium&p[]=facets.brand%255B%255D%3DSAMSUNG&p[]=facets.brand%255B%255D%3DWD&p[]=facets.brand%255B%255D%3DTOSHIBA&p[]=facets.brand%255B%255D%3DSONY&p[]=facets.brand%255B%255D%3DKingston&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['mob_3k.txt', 1, False, 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D3000&p[]=facets.type%255B%255D%3DSmartphones&p[]=facets.serviceability[]%3Dfalse'])
    arr.append(['mob1.txt', 1, False, 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D3500&p%5B%5D=facets.type%255B%255D%3DSmartphones&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DRealme&p%5B%5D=facets.brand%255B%255D%3DSamsung&p%5B%5D=facets.brand%255B%255D%3DHonor&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.brand%255B%255D%3DAsus&p%5B%5D=facets.brand%255B%255D%3DApple&p%5B%5D=facets.brand%255B%255D%3DBlackberry&p%5B%5D=facets.brand%255B%255D%3DCoolpad&p%5B%5D=facets.brand%255B%255D%3DGionee&p%5B%5D=facets.brand%255B%255D%3DGoogle&p%5B%5D=facets.brand%255B%255D%3DHTC&p%5B%5D=facets.brand%255B%255D%3DHuawei&p%5B%5D=facets.brand%255B%255D%3DInFocus&p%5B%5D=facets.brand%255B%255D%3DIntex&p%5B%5D=facets.brand%255B%255D%3DKarbonn&p%5B%5D=facets.brand%255B%255D%3DLava&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.brand%255B%255D%3DLG&p%5B%5D=facets.brand%255B%255D%3DLYF&p%5B%5D=facets.brand%255B%255D%3DMeizu&p%5B%5D=facets.brand%255B%255D%3DMicromax&p%5B%5D=facets.brand%255B%255D%3DMotorola&p%5B%5D=facets.brand%255B%255D%3DNokia&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DSony&p%5B%5D=facets.brand%255B%255D%3DSwipe&p%5B%5D=facets.brand%255B%255D%3DXOLO&p%5B%5D=facets.brand%255B%255D%3DVivo&p%5B%5D=facets.brand%255B%255D%3DYu&p%5B%5D=facets.brand%255B%255D%3DZen&p%5B%5D=facets.serviceability%5B%5D%3Dfalse'])
    arr.append(['mob2.txt', 1, False, 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mobiles&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DSmartphones&p%5B%5D=facets.ram%255B%255D%3D4%2BGB&p%5B%5D=facets.ram%255B%255D%3D3%2BGB&p%5B%5D=facets.ram%255B%255D%3D2%2BGB&p%5B%5D=facets.ram%255B%255D%3D1%2BGB&p%5B%5D=facets.ram%255B%255D%3D512%2BMB%2B-%2B1%2BGB&p%5B%5D=facets.ram%255B%255D%3DLess%2Bthan%2B512%2BMB&p%5B%5D=facets.ram%255B%255D%3D6%2BGB%2B%2526%2BAbove&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000'])
    arr.append(['mob3.txt', 1, False, 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&marketplace=FLIPKART&otracker=product_breadCrumbs_Mobiles&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.internal_storage%255B%255D%3D256%2BGB%2B%2526%2BAbove&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D64%2B-%2B127.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D32%2B-%2B63.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D16%2B-%2B31.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D8%2B-%2B15.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D4%2B-%2B7.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D2%2BGB%2B-%2B3.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3D1%2BGB%2B-%2B1.9%2BGB&p%5B%5D=facets.internal_storage%255B%255D%3DLess%2Bthan%2B1%2BGB&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.type%255B%255D%3DSmartphones'])
    arr.append(['mob4.txt', 1, False, 'https://www.flipkart.com/mobiles/~smartphones-under-rs15000/pr?sid=tyy%2C4io&sort=price_asc&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.serviceability[]%3Dfalse&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D3200'])
    arr.append(['oven_5k.txt', 0, False, 'https://www.flipkart.com/microwave-ovens/pr?sid=j9e%2Fm38%2Fo49&otracker=CLP_Filters&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D4000'])
    arr.append(['pendrive_300.txt', 0, False, 'https://www.flipkart.com/computers/storage/pen-drives/pr?sid=6bo%2Cjdy%2Cuar&otracker=nmenu_sub_Electronics_0_Pendrives&p%5B%5D=facets.price_range.from%3DMin&sort=price_asc&p%5B%5D=facets.price_range.to%3D300&p%5B%5D=facets.brand%255B%255D%3DHP&p%5B%5D=facets.brand%255B%255D%3DSanDisk&p%5B%5D=facets.brand%255B%255D%3DStrontium&p%5B%5D=facets.brand%255B%255D%3DKingston&p%5B%5D=facets.brand%255B%255D%3DSony'])
    arr.append(['powerbank_500.txt', 0, False, 'https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&sort=price_asc&p[]=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D500&p[]=facets.brand%255B%255D%3DMi&p[]=facets.brand%255B%255D%3DAmbrane&p[]=facets.brand%255B%255D%3DSyska&p[]=facets.brand%255B%255D%3DFlipkart%2BSmartBuy&p[]=facets.brand%255B%255D%3DPHILIPS&p[]=facets.brand%255B%255D%3DZEBRONICS&p[]=facets.brand%255B%255D%3DPortronics&p[]=facets.brand%255B%255D%3DAPPLE&p[]=facets.brand%255B%255D%3DIntex&p[]=facets.brand%255B%255D%3DRedmi'])
    arr.append(['printer_5k.txt', 1, False, 'https://www.flipkart.com/computers/printers-inks/printers/pr?sid=6bo%2Cffn%2Ct64&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&otracker=categorytree&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D2500'])
    arr.append(['RO_2500.txt', 0, False, 'https://www.flipkart.com/water-purifiers/pr?sid=j9e%2Cabm%2Ci45&otracker=nmenu_sub_Appliances_0_Water+Purifiers&otracker=nmenu_sub_TVs+%26+Appliances_0_Water+Purifiers&sort=price_asc&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2500&p%5B%5D=facets.discount_range_v1%255B%255D%3D50%2525%2Bor%2Bmore'])
    arr.append(['smart-bulb_500.txt', 0, False, 'https://www.flipkart.com/automation-robotics/smart-lighting/pr?sid=igc%2Cb4q&otracker=categorytree&sort=price_asc&p%5B%5D=facets.discount_range_v1%255B%255D%3D70%2525%2Bor%2Bmore&p%5B%5D=facets.brand%255B%255D%3DSmitch&p%5B%5D=facets.brand%255B%255D%3DMi&p%5B%5D=facets.brand%255B%255D%3DSyska&p%5B%5D=facets.brand%255B%255D%3DCrompton&p%5B%5D=facets.brand%255B%255D%3DPHILIPS&p%5B%5D=facets.brand%255B%255D%3DHALONIX&p%5B%5D=facets.brand%255B%255D%3DHomehop&p%5B%5D=facets.brand%255B%255D%3DWipro&p%5B%5D=facets.brand%255B%255D%3DCololight&p%5B%5D=facets.brand%255B%255D%3DHelea&p%5B%5D=facets.brand%255B%255D%3DHAVELLS&p%5B%5D=facets.brand%255B%255D%3DHomeMate&p%5B%5D=facets.brand%255B%255D%3DKAMONK&p%5B%5D=facets.brand%255B%255D%3DLifelong&p%5B%5D=facets.brand%255B%255D%3DTP-Link&p%5B%5D=facets.brand%255B%255D%3DMANSAA&p%5B%5D=facets.brand%255B%255D%3DLUMINOUS&p%5B%5D=facets.brand%255B%255D%3Dnanoleaf&p%5B%5D=facets.brand%255B%255D%3Dpolycab&p%5B%5D=facets.brand%255B%255D%3DPolycab%2BHohm&p%5B%5D=facets.brand%255B%255D%3DPanasonic&p%5B%5D=facets.brand%255B%255D%3DYeelight&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D500'])
    arr.append(['smartwatch_1000.txt', 0, False, 'https://www.flipkart.com/search?sid=ajy%2Cbuh&otracker=CLP_Filters&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D800&p[]=facets.brand%255B%255D%3DboAt&p[]=facets.brand%255B%255D%3DAPPLE&p[]=facets.brand%255B%255D%3DNoise&p[]=facets.brand%255B%255D%3Drealme&p[]=facets.brand%255B%255D%3DFire-Boltt&p[]=facets.brand%255B%255D%3DSAMSUNG&p[]=facets.brand%255B%255D%3DGIONEE&p[]=facets.brand%255B%255D%3DFITBIT&p[]=facets.brand%255B%255D%3DGizmore&p[]=facets.brand%255B%255D%3DBoult&p[]=facets.brand%255B%255D%3DGARMIN&p[]=facets.brand%255B%255D%3DAMAZFIT&p[]=facets.brand%255B%255D%3DTitan&p[]=facets.brand%255B%255D%3Dhuami&p[]=facets.brand%255B%255D%3DFastrack&p[]=facets.brand%255B%255D%3DDIZO&p[]=facets.brand%255B%255D%3DNoiseFit&p[]=facets.brand%255B%255D%3DPebble&p[]=facets.discount_range_v1%255B%255D%3D40%2525%2Bor%2Bmore'])
    arr.append(['treadmill_15k.txt', 1, False, 'https://www.flipkart.com/exercise-fitness/fitness-equipment/treadmills/pr?sid=qoc%2Camf%2Coyq&marketplace=FLIPKART&otracker=product_breadCrumbs_Treadmills&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=price_asc&p[]=facets.price_range.from%3DMin&p[]=facets.price_range.to%3D15000'])

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
