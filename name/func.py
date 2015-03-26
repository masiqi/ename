#-*-coding:utf8;-*-
import urllib
import urllib2
#from cjklib.characterlookup import CharacterLookup
#from cjklib.reading import ReadingFactory
from libs.BeautifulSoup import BeautifulSoup
from django.conf import settings
from django.core.files.base import ContentFile
from name.models import Name, Pinyin


"""
def chinese_to_gr(chinese):
    cl = CharacterLookup('T')
    f = ReadingFactory()
    rt = []
    t_list = []
    for i in range(len(chinese)):
        t_list = []
        py_list = cl.getReadingForCharacter(chinese[i], 'Pinyin')
        for j in py_list:
            try:
                k = f.convert(j, 'Pinyin', 'GR')
                t_list.append(k)
            except:
                pass
        if len(rt) == 0:
            rt = t_list
        else:
            tt_list = []
            for x in rt:
                for y in t_list:
                    tt_list.append(x + '|' + y)
            rt = tt_list
    return rt
"""

def chinese_to_gr(string=""):                                         
    rt = []                                                            
    if not isinstance(string, unicode):                                    
        string = string.decode("utf-8")                                    

    t_list = []
    for char in string:                                                    
        t_list = []
        key = '%X' % ord(char)                                             
        try:
            pinyin = Pinyin.objects.get(name=key)
            for j in pinyin.roma.split('|'):
                t_list.append(j)
            if len(rt) == 0:
                rt = t_list
            else:
                tt_list = []
                for x in rt:
                    for y in t_list:
                        tt_list.append(x + '|' + y)
                rt = tt_list
        except:
            pass
        #result.append(self.word_dict.get(key, char).split()[0].lower())
    return rt

def load_dict():
    fp = file(settings.ROMA_FILE)
    roma_dict = {}
    for line in fp.readlines():
        i = line.replace('\n', '').split(' ')
        for j in range(1,5):
            key = i[0] + str(j)
            val = i[j]
            roma_dict[key] = val
    fp.close()
    fp = file(settings.PINYIN_DICT)
    for line in fp.readlines():
        i = line.replace('\n', '').replace('    ', '   ').split('   ')
        tmp_list = []
        for j in  i[1].split(' '):
            try:
                tmp_list.append(roma_dict[j.lower()])
            except:
                pass
        roma = '|'.join(tmp_list)
        p, created = Pinyin.objects.get_or_create(name=i[0], defaults={'name':i[0], 'roma':roma})
        if not created:
            p.roma = roma
        p.save()
    return ''

def fetch_name():
    for url in settings.ENAME_URLS:
        soup = BeautifulSoup(urllib.urlopen(url).read())
        for div in soup.findAll('div', {'class':'browsename'}):
            name = div.find('b').text.capitalize().split('(')[0]
            gender = 0
            if div.find('span', {'class':'masc'})  and div.find('span', {'class':'fem'}):
                gender = 2
            else:
                if div.find('span', {'class':'masc'}):
                    gender = 0
                if div.find('span', {'class':'fem'}):
                    gender = 1
            if name.find('&') != -1:
                continue
            n, created = Name.objects.get_or_create(name=name, defaults={'name':name, 'gender':gender})
            if not created:
                n.gender = gender
            n.save()
            print name, gender
    return "ok"

def query_name():
    names = Name.objects.all()
    for name in names:
        headers = {'User-Agent' : 'Mozilla/5.0' }                              
        request = urllib2.Request(settings.TRANSLATE_URL + name.name, None, headers)                    
        soup = BeautifulSoup(urllib2.urlopen(request).read())
        try:
            pronounce = soup.find('span', {'class':'phonetic'}).text
            name.pronounce = pronounce
            print pronounce
        except:
            pass
        try:
            description = soup.find('div', {'class':'trans-container'}).text
            name.description = description 
            print description
        except:
            pass
        request = urllib2.Request(settings.MP3_URL + name.name, None, headers)                    
        mp3 = urllib2.urlopen(request)
        myfile = ContentFile(mp3.read())
        name.mp3.save(name.name + '.mp3', myfile)
        #institution.image.save(str(institution.id) +'.' + postfix, urllib.urlopen(logo))
        name.save()
        """
        headers = {'User-Agent' : 'Mozilla/5.0' }                              
        request = urllib2.Request(audio_url, None, headers)                    
        mp3file = urllib2.urlopen(request)                                     
        with open(mp3_name, 'wb') as output_mp3:                               
            output_mp3.write(mp3file.read()) 
        """
    return "ok"

def cname_name():
    #names = Name.objects.all()
    names = Name.objects.filter(cname=None)
    for name in names:
        url = 'http://www.iciba.com/' + name.name
        headers = {'User-Agent' : 'Mozilla/5.0', 'Cookie':'ICIBA_OUT_SEARCH_USER_ID=698657378%40221.218.126.202; iciba_u_rand=b7049aea387d6b14d2926bb468b32933%40221.218.126.202; iciba_u_rand_t=1385863025; iciba_history_v2=a%3A11%3A%7Bi%3A0%3Bs%3A7%3A%22Abegail%22%3Bi%3A1%3Bs%3A5%3A%22Kyler%22%3Bi%3A2%3Bs%3A6%3A%22Kylerr%22%3Bi%3A3%3Bs%3A4%3A%22Zeph%22%3Bi%3A4%3Bs%3A6%3A%22Zinnia%22%3Bi%3A5%3Bs%3A4%3A%22Zoey%22%3Bi%3A6%3Bs%3A4%3A%22Zoie%22%3Bi%3A7%3Bs%3A4%3A%22Zola%22%3Bi%3A8%3Bs%3A5%3A%22Zowie%22%3Bi%3A9%3Bs%3A4%3A%22Zula%22%3Bi%3A10%3Bs%3A5%3A%22Aidan%22%3B%7D; www-results1=0; ICIBA_HUAYI_COOKIE=1; _kds2_uName=1385863027735250488015; _kds2_times=10; iciba_suggest_power=1; cbj=1; uid=1386065534610067; WEB_POP_SHOW_UV_www_42=1' }                              
        request = urllib2.Request(url, None, headers)                    
        soup = BeautifulSoup(urllib2.urlopen(request).read())
        try:
            n2 = soup.find('h1', {'id':'word_name_h1'}).text
            if n2.lower() == name.name.lower():
                print name.name, n2, soup.find('span', {'class':'label_list'}).text
        except:
            pass

        """
        headers = {'User-Agent' : 'Mozilla/5.0' }                              
        request = urllib2.Request(settings.CNAME_URL+ name.name, None, headers)                    
        soup = BeautifulSoup(urllib2.urlopen(request).read())
        try:
            mean = soup.find('div', {'class':'forsearch'}).find('li')
            cname = mean.find('span').text
            description = mean.findNextSibling().find('span').text
            pronounce = soup.find('div', {'class':'forsearch'}).find('em')
            if name.pronounce == None:
                name.pronounce = pronounce
            name.cname = cname
            name.description = description
            name.save()
            print name.name, cname 
        except:
            print name.name, "None"
            pass

        """
