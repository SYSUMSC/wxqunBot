
import xml.etree.ElementTree as ET
def parse_xml(xml_string:str):
    try:
        root = ET.fromstring(xml_string)
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None
if __name__ == "__main__":
    #python -m utils.xml
    xml_string = """<msg><emoji fromusername = "wxid_3zcnbha3j2v922" tousername = "wxid_th8wamjjmc9u22" type="2" idbuffer="media:0_0" md5="6cd389c713563e9ee42d74dbfb29efa4" len = "846196" productid="" androidmd5="6cd389c713563e9ee42d74dbfb29efa4" androidlen="846196" s60v3md5 = "6cd389c713563e9ee42d74dbfb29efa4" s60v3len="846196" s60v5md5 = "6cd389c713563e9ee42d74dbfb29efa4" s60v5len="846196" cdnurl = "http://vweixinf.tc.qq.com/110/20401/stodownload?m=6cd389c713563e9ee42d74dbfb29efa4&amp;filekey=30440201010430302e02016e040253480420366364333839633731333536336539656534326437346462666232396566613402030ce974040d00000004627466730000000132&amp;hy=SH&amp;storeid=26597bc240008ce8fc9995fc60000006e01004fb1534802465b01e7df0a2eb&amp;ef=1&amp;bizid=1022" designerid = "" thumburl = "" encrypturl = "http://vweixinf.tc.qq.com/110/20402/stodownload?m=22d74b10c8d5a67099d10eb926219955&amp;filekey=30440201010430302e02016e040253480420323264373462313063386435613637303939643130656239323632313939353502030ce980040d00000004627466730000000132&amp;hy=SH&amp;storeid=26597bc24000ac874c9995fc60000006e02004fb2534802465b01e7df0a2f6&amp;ef=2&amp;bizid=1022" aeskey= "2cb2ea7a5a484d3f87eb81245e630b25" externurl = "http://vweixinf.tc.qq.com/110/20403/stodownload?m=8e7e0441790bc648549c50e8fde68255&amp;filekey=30440201010430302e02016e0402534804203865376530343431373930626336343835343963353065386664653638323535020301c300040d00000004627466730000000132&amp;hy=SH&amp;storeid=26597bc24000cbf6dc9995fc60000006e03004fb3534802465b01e7df0a316&amp;ef=3&amp;bizid=1022" externmd5 = "64558af8ce7d698ee28a148b54f733cc" width= "280" height= "280" tpurl= "" tpauthkey= "" attachedtext= "" attachedtextcolor= "" lensid= "" emojiattr= "" linkid= "" desc= "" ></emoji> <gameext type="0" content="0" ></gameext></msg>"""
    root = parse_xml(xml_string)
    print(root)
    #获取emoji cdnurl
    cdnurl = root.find("emoji").get("cdnurl")
    print(cdnurl)