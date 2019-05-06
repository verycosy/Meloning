from scapy.all import *


def http_header(packet):
    http_packet = str(packet)
    GET_pos = http_packet.find('GET')
    if GET_pos and "stop" in http_packet:
        pos = http_packet.find("p3cu=")
        return GET_print(http_packet[GET_pos:pos])


def GET_print(packet1):
    ret = "[Info]\n"
    result = packet1.split('|')

    # [2] p3mid = sts.melon.com/umps67/08/005/07/874/0800507874.mp3
    # [3] p3playtime = 1253
    # [4] p3servicetime = 229000

    # umps420/08/313/45/333/0831345333.mp3

    pos = result[2].find("umps")
    songResult = result[2][pos:].split("/")
    songId = songResult[5].replace(songResult[1], "").replace(".mp3", "")
    playTime = result[3].split('=')[1]
    serviceTime = result[4].split('=')[1]

    ret += "Song ID : " + songId
    ret += "\nPlay Time : " + playTime
    ret += "\nService Time : " + serviceTime
    ret += "\nPlay Rate : " + str((int(playTime) / int(serviceTime)*100))
    ret += "\n[---]\n"
    return ret


print("START")
sniff(prn=http_header, filter="tcp port 80", count=0)
