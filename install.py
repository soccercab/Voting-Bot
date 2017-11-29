import urllib
import os
import time
print "Installing..."
urllib.urlretrieve ("https://bootstrap.pypa.io/get-pip.py", "runpip.py")
os.startfile("runpip.py")

urllib.urlretrieve ("https://github.com/SPMNJ/Currentbot/raw/master/proxy.txt", "proxy.txt")
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
text = ['import requests, re, json, time, random, os', 'requests.packages.urllib3.disable_warnings()', 'if os.path.exists("install.py"):', '    os.remove("install.py")', 'if os.path.exists("install.py"):', '    os.remove("runpip.py")', 'base_url = "https://polldaddy.com/poll/"', 'redirect = ""', '', 'useragents = []', 'current_useragent = ""', '', 'proxies = []', 'current_proxy = {"http":""}', 'current_proxy_num = -1', '', '', 'def get_all_useragents():', '    f = open("useragent.txt", "r")', '    for line in f:', "        useragents.append(line.rstrip('\\n').rstrip('\\r'))", '    f.close()', '', 'def choose_useragent():', '    k = random.randint(0, len(useragents)-1)', '    current_useragent = useragents[k]', '    #print current_useragent', '', 'def get_all_proxies():', '    f = open("proxy.txt", "r")', '    for line in f:', "        proxies.append(line.rstrip('\\n').rstrip('\\r'))", '    f.close()', '', 'def choose_proxy():', '    k = random.randint(0, len(proxies)-1)', '    current_num = k', '    current_proxy["http"] = proxies[k]', '', '', 'def vote_once(form, value):', '    c = requests.Session()', '    #Chooses useragent randomly', '    choose_useragent()', '    redirect = {"Referer": base_url + str(form) + "/", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "User-Agent": current_useragent, "Upgrade-Insecure-Requests":"1", "Accept-Encoding": "gzip, deflate, sdch", "Accept-Language": "en-US,en;q=0.8"}', '', '    # Chooses proxy randomly', '    choose_proxy()', '    try:', '        init = c.get(base_url + str(form) + "/", headers=redirect, verify=False, proxies=current_proxy)', '    except:', '        print "error with proxy, don\'t worry its been trashed!"', '        proxies.remove(current_proxy_num)', '        return None', '', '    # Search for the data-vote JSON object', '    data = re.search("data-vote=\\"(.*?)\\"",init.text).group(1).replace(\'&quot;\',\'"\')', '    data = json.loads(data)', '    # Search for the hidden form value', '    pz = re.search("type=\'hidden\' name=\'pz\' value=\'(.*?)\'",init.text).group(1)', '    # Build the GET url to vote', '    request = "https://polldaddy.com/vote.php?va=" + str(data[\'at\']) + "&pt=0&r=0&p=" + str(form) + "&a=" + str(value) + "%2C&o=&t=" + str(data[\'t\']) + "&token=" + str(data[\'n\']) + "&pz=" + str(pz)', '    try:', '        send = c.get(request, headers=redirect, verify=False, proxies=current_proxy)', '    except:', '        print "error with proxy"', '        proxies.remove(current_proxy_num)', '        return None', '', '    return ("revoted" in send.url)', '', 'def vote(form, value, times, wait_min = None, wait_max = None):', '    global redirect', '    # For each voting attempt', '    i = 1', '    while i < times+1:', '        b = vote_once(form, value)', '        # If successful, print that out, else try waiting for 60 seconds (rate limiting)', '        if not b:', '            # Randomize timing if set', '            if wait_min and wait_max:', '                seconds = random.randint(wait_min, wait_max)', '            else:', '                seconds = 3', '', '            print "Voted (time number " + str(i) + ")!"', '            time.sleep(seconds)', '        else:', '            print "Locked.  Sleeping for 60 seconds."', '            i-=1', '            time.sleep(60)', '        i += 1', '', '# Initialize these to the specific form and how often you want to vote', 'poll_id = 9884284', 'answer_id = 45266278', 'print """RV VOTING SOFTWARE', 'PLEASE DON\'T USE THIS IF WE ARE CLOSE TO WINNING"""', 'number_of_votes = int(raw_input("How Many Votes> "))', 'wait_min = int(raw_input("Min Vote Waiting> "))', 'if wait_min == 0:', '    wait_min = 1', 'wait_max = int(raw_input("Max Vote Waiting> "))', '', 'get_all_proxies()', 'get_all_useragents()', 'vote(poll_id, answer_id, number_of_votes, wait_min, wait_max)']
code = open("AutoVote.py","w+")
for i in range(len(text)):
    code.write(text[i]+"\n")
code.close()
time.sleep(3)
os.startfile("AutoVote.py")


