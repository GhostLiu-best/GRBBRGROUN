import urllib .request
import requests,time,os,sys
from urllib.request import urlretrieve

errors=[]
errorpages=[]

satdic = {
    "NSS 9":"177.0°W",
    "Intelsat 14":"45.0°W",
    "KazSat 3":"58.5°E",
    "Yamal 300K":"177.0°W",
    "Intelsat 11":"43.1°W",
    "Intelsat 33e":"60.0°E",
    "Hispasat 143W-1":"143.0°W",
    "Sky Brasil 1":"43.1°W",
    "ABS 4":"61.0°E",
    "AMC 8":"139.0°W",
    "SES 6":"40.5°W",
    "Intelsat 39":"62.0°E",
    "AMC 18":"139.0°W",
    "Telstar 11N":"37.6°W",
    "Astra 1G":"63.2°E",
    "Intelsat 5":"137.0°W",
    "NSS 10":"37.5°W",
    "Intelsat 26":"63.6°E",
    "AMC 4":"134.9°W",
    "Hispasat 36W-1":"36.0°W",
    "Intelsat 12":"64.0°E",
    "Galaxy 15":"133.2°W",
    "Intelsat 35e":"34.5°W",
    "Intelsat 906":"64.2°E",
    "Eutelsat 133 West A":"132.8°W",
    "Hylas 4":"33.5°W",
    "Amos 4":"65.0°E",
    "AMC 11":"131.0°W",
    "Intelsat 903":"31.5°W",
    "Intelsat 17":"66.0°E",
    "AMC 1":"130.9°W",
    "Intelsat 25":"31.5°W",
    "Intelsat 20":"68.5°E",
    "Galaxy 12":"129.0°W",
    "XTAR-LANT":"30.0°W",
    "Intelsat 36":"68.5°E",
    "Ciel 2":"129.0°W",
    "Hispasat 30W-5":"30.0°W",
    "Eutelsat 70B":"70.5°E",
    "SES 15":"129.0°W",
    "Hispasat 30W-6":"30.0°W",
    "Intelsat 22":"72.1°E",
    "Galaxy 13/Horizons 1":"127.0°W",
    "Intelsat 904":"29.5°W",
    "G-Sat 14":"74.0°E",
    "Galaxy 14":"125.0°W",
    "Intelsat 907":"27.5°W",
    "G-Sat 18":"74.0°E",
    "AMC 21":"125.0°W",
    "Alcomsat 1":"24.8°W",
    "G-Sat 11":"74.0°E",
    "Galaxy 18":"123.0°W",
    "Intelsat 905":"24.5°W",
    "ABS 2":"75.0°E",
    "EchoStar 9/Galaxy 23":"121.0°W",
    "SES 4":"22.0°W",
    "ABS 2A":"75.0°E",
    "DirecTV 7S":"119.0°W",
    "NSS 7":"20.0°W",
    "Apstar 7":"76.5°E",
    "EchoStar 14":"119.0°W",
    "Al Yah 3":"20.0°W",
    "Thaicom 5":"78.5°E",
    "Echostar 7":"118.8°W",
    "Intelsat 37e":"18.0°W",
    "Thaicom 6":"78.5°E",
    "Anik F3":"118.8°W",
    "Telstar 12 Vantage":"15.0°W",
    "Thaicom 8":"78.5°E",
    "Eutelsat 117 West B":"117.0°W",
    "Express AM8":"14.0°W",
    "G-Sat 6":"82.1°E",
    "Eutelsat 117 West A":"116.8°W",
    "Eutelsat 12 West B":"12.7°W",
    "Insat 4B":"83.0°E",
    "Sirius FM 6":"116.2°W",
    "Express AM44":"11.0°W",
    "G-Sat 12":"83.0°E",
    "ViaSat 1":"115.1°W",
    "Eutelsat 8 West B":"8.0°W",
    "G-Sat 10":"83.0°E",
    "XM 4":"115.0°W",
    "Eutelsat 7 West A":"7.2°W",
    "G-Sat 31":"83.0°E",
    "Eutelsat 115 West B":"114.9°W",
    "Nilesat 201":"7.0°W",
    "G-Sat 30":"83.0°E",
    "Mexsat Bicentenario":"114.8°W",
    "Eutelsat 5 West A":"5.0°W",
    "Horizons 2":"85.0°E",
    "Eutelsat 113 West A":"113.0°W",
    "Eutelsat 5 West B":"5.0°W",
    "Intelsat 15":"85.2°E",
    "Morelos 3":"113.0°W",
    "Amos 3":"4.0°W",
    "KazSat 2":"86.5°E",
    "Wildblue 1":"111.2°W",
    "Amos 7":"4.0°W",
    "ChinaSat 12":"87.5°E",
    "Anik F2":"111.1°W",
    "ABS 3A":"3.0°W",
    "ST 2":"88.0°E",
    "Echostar T1":"111.0°W",
    "Intelsat 10-02":"1.0°W",
    "Yamal 401":"90.0°E",
    "EchoStar 10":"110.0°W",
    "Thor 5":"0.8°W",
    "Measat 3":"91.5°E",
    "EchoStar 11":"110.0°W",
    "Thor 6":"0.8°W",
    "Measat 3a":"91.5°E",
    "DirecTV 5":"109.8°W",
    "Thor 7":"0.8°W",
    "Measat 3b":"91.5°E",
    "Telstar 12":"109.2°W",
    "BulgariaSat 1":"1.9°E",
    "ChinaSat 9":"92.2°E",
    "Anik F1":"107.3°W",
    "Rascom QAF 1R":"2.8°E",
    "G-Sat 15":"93.5°E",
    "Anik F1R":"107.3°W",
    "Eutelsat 3B":"3.1°E",
    "G-Sat 17":"93.5°E",
    "Anik G1":"107.3°W",
    "Astra 4A":"4.8°E",
    "SES 8":"95.0°E",
    "EchoStar 17":"107.1°W",
    "SES 5":"5.0°E",
    "SES 12":"95.0°E",
    "AMSC 1":"106.5°W",
    "Eutelsat 7B":"7.0°E",
    "Express AM33":"96.5°E",
    "AMC 15":"105.0°W",
    "Eutelsat 7C":"7.0°E",
    "G-Sat 9":"97.3°E",
    "EchoStar 105/SES 11":"105.0°W",
    "Eutelsat Ka-Sat 9A":"9.0°E",
    "ChinaSat 11":"98.0°E",
    "SES 3":"103.0°W",
    "Eutelsat 9B":"9.0°E",
    "Thuraya 3":"98.5°E",
    "DirecTV 10":"102.8°W",
    "Eutelsat 10A":"10.0°E",
    "Astra 2A":"100.0°E",
    "DirecTV 12":"102.8°W",
    "EchoStar 21":"10.3°E",
    "AsiaSat 5":"100.5°E",
    "DirecTV 15":"102.8°W",
    "Hotbird 13E":"13.0°E",
    "ChinaSat 9A":"101.4°E",
    "Skyterra 1":"101.3°W",
    "Hotbird 13B":"13.0°E",
    "Express AM3":"103.0°E",
    "DirecTV 9S":"101.1°W",
    "Hotbird 13C":"13.0°E",
    "AsiaSat 7":"105.5°E",
    "DirecTV 8":"101.0°W",
    "Eutelsat 16A":"16.0°E",
    "Telkom 4":"108.0°E",
    "SES 1":"101.0°W",
    "Amos 17":"17.0°E",
    "SES 7":"108.2°E",
    "T 16":"100.8°W",
    "Astra 1KR":"19.2°E",
    "SES 9":"108.2°E",
    "Spaceway 2":"99.2°W",
    "Astra 1L":"19.2°E",
    "BSAT 3A":"110.0°E",
    "DirecTV 11":"99.2°W",
    "Astra 1M":"19.2°E",
    "BSAT 3B":"110.0°E",
    "DirecTV 14":"99.2°W",
    "Astra 1N":"19.2°E",
    "BSAT 3C/JCSAT 110R":"110.0°E",
    "Galaxy 16":"99.0°W",
    "Astra 2B":"19.4°E",
    "JCSAT 15":"110.0°E",
    "EchoStar 19":"97.1°W",
    "Arabsat 5C":"20.0°E",
    "BSAT 4A":"110.0°E",
    "Galaxy 19":"97.0°W",
    "Eutelsat 21B":"21.5°E",
    "ChinaSat 10":"110.5°E",
    "Galaxy 3C":"95.0°W",
    "Astra 3B":"23.5°E",
    "Chinasat 16":"110.5°E",
    "Hellas Sat 2":"95.0°W",
    "Astra 2C":"23.7°E",
    "Koreasat 5":"113.0°E",
    "Spaceway 3":"95.0°W",
    "Eshail 1":"25.5°E",
    "Palapa D":"113.0°E",
    "Intelsat 30":"95.0°W",
    "Eshail 2":"25.8°E",
    "Koreasat 5A":"113.0°E",
    "Intelsat 31":"95.0°W",
    "Badr 4":"26.0°E",
    "ChinaSat 6B":"115.5°E",
    "Galaxy 11":"93.1°W",
    "Badr 6":"26.0°E",
    "ABS 7":"116.0°E",
    "Brasilsat B4":"92.0°W",
    "Badr 5":"26.0°E",
    "Koreasat 6":"116.0°E",
    "Nimiq 6":"91.1°W",
    "Badr 7":"26.0°E",
    "Koreasat 7":"116.0°E",
    "Galaxy 17":"91.0°W",
    "Astra 2F":"28.2°E",
    "Telkom 3S":"118.0°E",
    "Galaxy 28":"89.0°W",
    "Astra 2E":"28.2°E",
    "Bangabandhu 1":"119.1°E",
    "TKSat 1":"87.2°W",
    "Astra 2G":"28.2°E",
    "Thaicom 4":"119.5°E",
    "NSS 6":"87.0°W",
    "XTAR-EUR":"29.0°E",
    "AsiaSat 6/Thaicom 7":"120.0°E",
    "SES 2":"87.0°W",
    "Arabsat 5A":"30.5°E",
    "AsiaSat 9":"122.0°E",
    "Astra 3A":"86.8°W",
    "Arabsat 6A":"30.5°E",
    "JCSAT 4B":"124.0°E",
    "Sirius FM 5":"86.2°W",
    "Hylas 2":"31.0°E",
    "JCSAT 16":"124.0°E",
    "Sirius XM 5":"85.2°W",
    "EDRS C":"31.0°E",
    "ChinaSat 6A":"125.0°E",
    "XM 3":"85.1°W",
    "Astra 5B":"31.5°E",
    "JCSAT 3A":"128.0°E",
    "AMC 16":"85.0°W",
    "Galaxy 25":"32.9°E",
    "LaoSat 1":"128.5°E",
    "AMC 2":"84.9°W",
    "Eutelsat 33E":"33.0°E",
    "ChinaSat 6C":"130.0°E",
    "Star One D1":"84.0°W",
    "Intelsat 28":"33.0°E",
    "Vinasat 2":"131.8°E",
    "AMC 6":"83.0°W",
    "Eutelsat 36B":"36.0°E",
    "JCSAT 5A":"132.0°E",
    "Nimiq 4":"82.0°W",
    "Express AMU1":"36.0°E",
    "Vinasat 1":"132.0°E",
    "Arsat 2":"81.0°W",
    "Paksat 1R":"37.8°E",
    "Apstar 6D [Q3 2019]":"134.0°E",
    "Hylas 1":"79.0°W",
    "Paksat-MM 1":"38.2°E",
    "Apstar 6C":"134.0°E",
    "Sky Mexico 1":"78.8°W",
    "Hellas Sat 3":"39.0°E",
    "Telstar 18 Vantage":"138.0°E",
    "Simón Bolívar":"78.0°W",
    "Hellas Sat 4":"39.0°E",
    "Express AM5":"140.0°E",
    "QuetzSat 1":"77.0°W",
    "Express AM7":"40.0°E",
    "Express AT2":"140.0°E",
    "Intelsat 16":"76.2°W",
    "Türksat 3A":"42.0°E",
    "Apstar 9":"142.0°E",
    "Star One C3":"75.0°W",
    "Türksat 4A":"42.0°E",
    "Superbird C2":"144.0°E",
    "Hispasat 74W-1":"74.0°W",
    "NigComSat 1R":"42.5°E",
    "Nusantara Satu":"146.0°E",
    "Astra 1D":"73.0°W",
    "Thuraya 2":"44.0°E",
    "AsiaSat 3S":"147.5°E",
    "Nimiq 5":"72.7°W",
    "Astra 1F":"44.3°E",
    "JCSAT 18/Kacific-1":"150.0°E",
    "AMC 3":"72.0°W",
    "AzerSpace 2/Intelsat 38":"45.0°E",
    "BRIsat":"150.5°E",
    "Arsat 1":"71.8°W",
    "AzerSpace 1/Africasat 1a":"46.0°E",
    "Optus D2":"152.0°E",
    "Star One C2":"70.0°W",
    "Intelsat 10":"47.5°E",
    "JCSAT 2B":"154.0°E",
    "Star One C4":"70.0°W",
    "Al Yah 2":"47.5°E",
    "Optus C1":"156.0°E",
    "Viasat 2":"69.9°W",
    "G-Sat 19":"47.8°E",
    "Optus D3":"156.0°E",
    "EchoStar 23":"67.9°W",
    "Insat 4CR":"47.9°E",
    "Optus 10":"156.0°E",
    "SES 10":"67.0°W",
    "Afghansat 1":"48.0°E",
    "Intelsat 1R":"157.0°E",
    "Star One C1":"65.0°W",
    "Eutelsat 70C":"48.1°E",
    "Telkom 2":"157.0°E",
    "Eutelsat 65 West A":"65.0°W",
    "Yamal 601":"49.0°E",
    "ABS 6":"159.0°E",
    "Telstar 14R":"63.0°W",
    "Türksat 4B":"50.0°E",
    "Optus D1":"160.0°E",
    "Telstar 19 Vantage":"63.0°W",
    "NSS 5":"50.5°E",
    "Superbird B3":"162.0°E",
    "EchoStar 15":"61.6°W",
    "Belintersat 1":"51.5°E",
    "Apstar 6":"163.0°E",
    "EchoStar 16":"61.5°W",
    "TurkmenÄlem/MonacoSat":"52.0°E",
    "Yamal 202":"163.5°E",
    "EchoStar 18":"61.3°W",
    "Al Yah 1":"52.5°E",
    "Intelsat 19":"166.0°E",
    "Amazonas 2":"61.0°W",
    "Express AM6":"53.0°E",
    "JCSAT RA":"169.0°E",
    "Amazonas 3":"61.0°W",
    "G-Sat 8":"55.0°E",
    "Horizons 3e":"169.0°E",
    "Amazonas 5":"61.0°W",
    "Yamal 402":"55.0°E",
    "Eutelsat 172B":"172.0°E",
    "Intelsat 21":"58.0°W",
    "G-Sat 16":"55.0°E",
    "Eutelsat 174A":"174.0°E",
    "Intelsat 34":"55.5°W",
    "G-Sat 29":"55.0°E",
    "NSS 11":"176.0°E",
    "Intelsat 23":"53.0°W",
    "Express AT1":"56.0°E",
    "Intelsat 18":"180.0°E",
    "SES 14":"47.5°W",
    "NSS 12":"57.0°E"
}

header = {
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Mobile Safari/537.36',
     'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' , 
     'Accept-Encoding' : 'gzip, deflate' , 
     'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6' ,
     'Connection' : 'close' ,
     'Host':'www.satstar.net' ,
     'Upgrade-Insecure-Requests': '1',
     'Referer': 'http:://http://www.satstar.net/'
}

def islasttop(url):
    pathlist = url.split("/")
    if pathlist[3] == "beams":
        #print("islasttop is True")
        return True
    else:
        #print("islasttop is False")
        return False

def pictype(pos, code):
    lasttag = code.find(r"<a", pos)
    #print("pos: " + str(pos))
    #print("lasttag: " + str(lasttag))
    #print(code[pos:lasttag])
    if lasttag>0 and lasttag<pos+70:
        #print("pictype is True")
        return True
    else:
        #print("pictype is False")
        return False
def gethref(pos, code):
    lasttag = code.find(r"..", pos)
    return code[lasttag+2:code.find(r"'",lasttag+9)]

def getsatHTML():
    r=urllib.request.urlopen(r"http://www.satstar.net/satellites.html")#获取html代码 
    hCode = r.read().decode('utf-8')
    r.close()
    pos = 0
    Fres = []
    links = []
    hrefs = []
    paths = []
    path = r"D:/beamsPic"
    while(pos>=0):
        pos = hCode.find(r"<td width='138", pos)
        if pos<0 or pos>248000:  #手动设置的上限，如果卫星数量增加，那么必须修改
            break
        else:
            pos = hCode.find(r"<a href='", pos) + 9
        words = hCode[pos:hCode.find(r"""</a>""", pos)]
        #print("words: " + words)
        satname = words[words.find(r"'>")+2:]
        #将卫星名称中包含的/去掉，以免造成有下级目录的误解
        filename = "/" + satdic[satname] + '_' + satname.replace(r"/", "-or-")
        url = r"http://www.satstar.net/" + words[:words.find(r"'>")]
        links.append(url)
        paths.append(path + filename)
        #print("url:" + url)
        #print("path:" + path + filename)
        try:
            os.mkdir(path + filename)
            #print(path + filename + "OK!")
        except:
            pass
            #print(path + filename + "已存在")
    Fres.append(links)
    Fres.append(paths)
    return Fres

def getHTML(tarurl):
    print("checking in " + tarurl)
    times = 5
    while(times>0):
        times = times - 1
        try:
            #获取html代码
            with urllib.request.urlopen(tarurl, timeout=5) as r:
                #print("req OK!")
                hCode = r.read().decode('utf-8')
            break;
        except:
            print("Check Page Fail!" + str(times) + "times left!")
            if times == 0:
                errorpages.append(tarurl)
                return 0
    
    #print("work in : " + tarurl)
    pos = 0
    links = []
    hrefs = []
    while(pos>=0):
        pos = hCode.find(r"<img src='", pos)
        if pos<0:
            break
        else:
            pos = pos + 10
        link = hCode[pos:hCode.find(r"""'""", pos)]

        url = r"http://www.satstar.net" + link[2:]
        
        if not islasttop(tarurl):
            if pictype(pos-70, hCode):
                #print("newPage:  " + r"http://www.satstar.net" + gethref(pos-70,hCode))
                getHTML(r"http://www.satstar.net" + gethref(pos-70,hCode))
            else:
                #print("Downloading---" + url)
                links.append(url)
        else:
            #print("topDownloading---" + url)
            links.append(url)
    downPic(links)
    
def downPic(links):
    for x in links:
        picname = x[x.find(r"/images")+8:]
        print("Downloading---" + x)
        time.sleep(1)
        times = 3
        while(times>0):
            times = times - 1
            try:
                with requests.get(url=x, headers=header,timeout=5) as r:
                    #print("req OK!")
                    res =  r.content
                    with open(picname, "wb") as f:
                        f.write(res)
                #print("save done!")
                break;
            except:
                print("Download Pic Fail!" + str(times) + "times left!")
                if times == 0:
                    errors.append(x)
            
        

if __name__=="__main__":
    Mylinks = getsatHTML()#无波束图的卫星未处理
    times = 0
    tar = 38
    for x,y in zip(Mylinks[0], Mylinks[1]):
        print("下载进程： " + str(times) + "/" + str(len(Mylinks[0])))
        if times>=tar:
            try:
                os.chdir(y)
            except:
                os.chdir(r"""D:/beamsPic/""")
                os.mkdir(y)
                os.chdir(y)
            getHTML(x)
        times = times + 1
    print(errors)
    print(errorpages)
