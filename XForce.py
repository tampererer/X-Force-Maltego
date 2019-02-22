# -*- coding: utf-8 -*-
from MaltegoTransform import *
import requests
import json

apiurl = "https://api.xforce.ibmcloud.com/"

apikey = "<Your API Key>"
apipass = "<Your API Pass>"


# url_to_categ
def url_to_categ():
    try:
        headers = {'Accept': 'application/json', 'Host': 'api.xforce.ibmcloud.com'}
        response = requests.get(apiurl + 'url/' + data, auth=(apikey, apipass), headers=headers)
        response_json = response.json()

        if 'cats' in response_json['result']:
            for r in response_json['result']['cats']:
                me = mt.addEntity("maltego.Phrase", '%s' % r)
                me.setLinkLabel("X-Force url_category")

    except:
        pass

    return mt

# url_to_malware
def url_to_malware():
    try:
        headers = {'Accept': 'application/json', 'Host': 'api.xforce.ibmcloud.com'}
        response = requests.get(apiurl + 'url/malware/' + data, auth=(apikey, apipass), headers=headers)
        response_json = response.json()

        if 'malware' in response_json:
            for r in response_json['malware']:
                if 'family' in r:
                    for item in r['family']:
                        me = mt.addEntity("maltego.Avdetection", '%s' % item)
                        me.setLinkLabel("X-Force malware_family")

                if 'md5' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['md5'].lower())
                    me.setLinkLabel("md5")

                if 'host' in r:
                    me = mt.addEntity("maltego.Domain", '%s' % r['host'] + "." + r['domain'])

                if 'ip' in r:
                    me = mt.addEntity("maltego.IPv4Address", '%s' % r['ip'])

    except:
        pass

    return mt

# ip_to_malware
def ip_to_malware():
    try:
        headers = {'Accept': 'application/json', 'Host': 'api.xforce.ibmcloud.com'}
        response = requests.get(apiurl + 'ipr/malware/' + data, auth=(apikey, apipass), headers=headers)
        response_json = response.json()

        if 'malware' in response_json:
            for r in response_json['malware']:
                if 'family' in r:
                    for item in r['family']:
                        me = mt.addEntity("maltego.Avdetection", '%s' % item)
                        me.setLinkLabel("X-Force malware")

                if 'md5' in r:
                    me = mt.addEntity("maltego.Hash", '%s' % r['md5'].lower())

                if 'host' in r:
                    me = mt.addEntity("maltego.Domain", '%s' % r['host'] + "." + r['domain'])

                if 'domain' in r:
                    me = mt.addEntity("maltego.Domain", '%s' % r['domain'])


    except:
        pass

    return mt

# hash_to_malware
def hash_to_malware():
    try:
        headers = {'Accept': 'application/json', 'Host': 'api.xforce.ibmcloud.com'}
        response = requests.get(apiurl + 'malware/' + data, auth=(apikey, apipass), headers=headers)
        response_json = response.json()

        if 'malware' in response_json:
            for r in response_json['malware']['family']:
                me = mt.addEntity("maltego.Avdetection", '%s' % r)
                me.setLinkLabel("X-Force malware")

            for r in response_json['malware']['origins']['CnCServers']['rows']:
                if 'host' in r:
                    me = mt.addEntity("maltego.Domain", '%s' % r['host'] + "." + r['domain'])

                if 'domain' in r:
                    me = mt.addEntity("maltego.Domain", '%s' % r['domain'])


    except:
        pass

    return mt

# domain_to_whois
def domain_to_whois():
    try:
        headers = {'Accept': 'application/json', 'Host': 'api.xforce.ibmcloud.com'}
        response = requests.get(apiurl + 'whois/' + data, auth=(apikey, apipass), headers=headers)
        response_json = response.json()

        if 'createdDate' in response_json:
            me = mt.addEntity("maltego.Phrase", '%s' % response_json['createdDate'])
            me.setLinkLabel("createdDate")

        if 'updatedDate' in response_json:
            me = mt.addEntity("maltego.Phrase", '%s' % response_json['updatedDate'])
            me.setLinkLabel("updatedDate")

        if 'contactEmail' in response_json:
            me = mt.addEntity("maltego.EmailAddress", '%s' % response_json['contactEmail'])

        if 'registrarName' in response_json:
            me = mt.addEntity("maltego.Phrase", '%s' % response_json['registrarName'])
            me.setLinkLabel("registrarName")

    except:
        pass

    return mt


# 

# 

# main
func = sys.argv[1]
data = sys.argv[2]

mt = MaltegoTransform()
mresult = eval(func)()
mresult.returnOutput()


