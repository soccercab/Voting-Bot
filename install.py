import urllib
import os
import time
os.chdir(os.path.expanduser("~")+"/Downloads/")
print "Installing..."
urllib.urlretrieve ("https://bootstrap.pypa.io/get-pip.py", "runpip.py")
os.startfile("runpip.py")
time.sleep(20)
print "Downloading needed files"
urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/proxy.txt", "proxy.txt")
urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/useragent.txt", "useragent.txt")
urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/version.txt", "version.txt")
time.sleep(5)
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('requests')
print "Building Auto Vote Software"
time.sleep(1)
text = ['import requests, re, json, time, random, os, urllib', 'requests.packages.urllib3.disable_warnings()', 'if os.path.exists("install.py"):', '    os.remove("install.py")', 'if os.path.exists("runpip.py"):', '    os.remove("runpip.py")', 'base_url = "https://polldaddy.com/poll/"', 'redirect = ""', 'useragents = []', 'current_useragent = ""', '', 'proxies = []', 'current_proxy = {"http":""}', 'current_proxy_num = -1', '', '', 'def get_all_useragents():', '    f = open("useragent.txt", "r")', '    for line in f:', "        useragents.append(line.rstrip('\\n').rstrip('\\r'))", '    f.close()', '', 'def choose_useragent():', '    k = random.randint(0, len(useragents)-1)', '    current_useragent = useragents[k]', '    #print current_useragent', '', 'def get_all_proxies():', '    f = open("proxy.txt", "r")', '    for line in f:', "        proxies.append(line.rstrip('\\n').rstrip('\\r'))", '    f.close()', '', 'def choose_proxy():', '    k = random.randint(0, len(proxies)-1)', '    current_num = k', '    current_proxy["http"] = proxies[k]', '    #print current_proxy["http"]', 'def vote_once(form, value):', '    c = requests.Session()', '    #Chooses useragent randomly', '    choose_useragent()', '    redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": current_useragent, "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}', '', '    # Chooses proxy randomly', '    choose_proxy()', '    try:', '        init = c.get(base_url + str(form) + "/", headers=redirect, verify=True, proxies=current_proxy)', '    except:', '        print "Error with proxy, Report at www.rvautovote.ga with error message below"', '        print current_proxy', '        proxies.remove(current_proxy_num)', '        return None', '', '    # Search for the data-vote JSON object', '    data = re.search("data-vote=\\"(.*?)\\"",init.text).group(1).replace(\'&quot;\',\'"\')', '    data = json.loads(data)', '    # Search for the hidden form value', '    pz = re.search("type=\'hidden\' name=\'pz\' value=\'(.*?)\'",init.text).group(1)', '    # Build the GET url to vote', '    request = "https://polldaddy.com/vote.php?va=" + str(data[\'at\']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data[\'t\']) + "&token=" + str(data[\'n\']) + "&pz=" + str(pz)', '    try:', '        send = c.get(request, headers=redirect, verify=True, proxies=current_proxy)', '    except:', '        print "Error with request, please report at www.rvautovote.ga and close application"', '        proxies.remove(current_proxy_num)', '        return None', '', '    return ("revoted" in send.url)', '', 'def vote(form, value, times, wait_min = None, wait_max = None):', '    global redirect', '    # For each voting attempt', '    i = 1', '    while i < times+1:', '        b = vote_once(form, value)', '        # If successful, print that out, else try waiting for 60 seconds (rate limiting)', '        if not b:', '            # Randomize timing if set', '            if wait_min and wait_max:', '                seconds = random.randint(wait_min, wait_max)', '            else:', '                seconds = 3', '', '            print "Voted (time number " + str(i) + ")!"', '            time.sleep(seconds)', '        else:', '            print "Locked.  Sleeping for 10 seconds."', '            print "If locks are happening please use pisphon3 or change pisphon3 server"', '            i-=1    ', '            time.sleep(10)', '        i += 1', '', '# Initialize these to the specific form and how often you want to vote', 'def pisphon():', '    print """In case you are at using this at school is it recommended that you use a vpn.', 'Fortually, pisphon3 (vpn) is free and easy to install/use"""', "    pisphon_question = raw_input('Would you like to install/use pisphon3[y/n]> ')", '    if pisphon_question.startswith("y"):', '        print "Installing pisphon3"', '        urllib.urlretrieve("https://s3.amazonaws.com/0ubz-2q11-gi9y/psiphon3.exe","psiphon3.exe")', "        os.startfile('psiphon3.exe')", '        time.sleep(3)', 'def update():', '    urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/version.txt", "version_test.txt")', '    testfile = open("version_test.txt")', "    if not os.path.exists('version.txt'):", '        testfile.close()', '        urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/install.py", "install.py")', '        os.startfile("install.py")', '        raise "Updating!"', '    else:', '        testfile2 = open("version.txt")', '        if testfile.read() != testfile2.read():', '            testfile.close()', '            testfile2.close()', '            urllib.urlretrieve ("https://github.com/SPMNJ/Voting-Bot/raw/master/install.py", "install.py")', '            os.startfile("install.py")', '            raise "Updating!"', '        testfile.close()', '        testfile2.close()', 'poll_id = 9884284', 'answer_id = 45266278', 'get_all_proxies()', 'get_all_useragents()', 'while True:', '    update()', '    print """RV VOTING SOFTWARE', 'FOR RVFANCLUB"""', '    time.sleep(2)', '    pisphon()', '    number_of_votes = int(raw_input("How Many Votes> "))', '    wait_min = int(raw_input("Min Vote Waiting> "))', '    if wait_min == 0:', '        wait_min = 1.', '    wait_max = int(raw_input("Max Vote Waiting> "))', '    try:', '        vote(poll_id, answer_id, number_of_votes, wait_min, wait_max)', '    except Exception as inst:', '        print inst', '        print "CRITICAL ERROR REPORT AT www.rvautovote.ga"', '        time.sleep(120)']
code = open("AutoVote.py","w+")
for i in range(len(text)):
    code.write(text[i]+"\n")
code.close()
time.sleep(3)
os.startfile("AutoVote.py")
print "File started"
time.sleep(1)
