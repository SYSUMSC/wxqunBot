
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
    xml_string1 = """<?xml version="1.0"?>
<msg>
        <appmsg appid="wxcb8d4298c6a09bcb" sdkver="0">
                <title>2分44秒教你如何过四级⚡</title>
                <des>UP主：不太抽象
播放：101.2万</des>
                <action />
                <type>4</type>
                <showtype>0</showtype>
                <soundtype>0</soundtype>
                <mediatagname />
                <messageext />
                <messageaction />
                <content />
                <contentattr>0</contentattr>
                <url>https://b23.tv/R6P3BC3</url>
                <lowurl />
                <dataurl />
                <lowdataurl />
                <songalbumurl />
                <songlyric />
                <template_id />
                <appattach>
                        <totallen>0</totallen>
                        <attachid />
                        <emoticonmd5 />
                        <fileext />
                        <cdnthumburl>3057020100044b30490201000204763ec9b702032f5d03020476bee8b70204675e6753042437346130363464642d353762372d343236312d383461302d3064383130313534376236350204051808030201000405004c4e6300</cdnthumburl>
                        <cdnthumbmd5>e25b18a155770eb1e3f7786a54ec9038</cdnthumbmd5>
                        <cdnthumblength>24437</cdnthumblength>
                        <cdnthumbwidth>160</cdnthumbwidth>
                        <cdnthumbheight>160</cdnthumbheight>
                        <cdnthumbaeskey>2017951eec915ac68eac1848deee68f3</cdnthumbaeskey>
                        <aeskey>2017951eec915ac68eac1848deee68f3</aeskey>
                        <encryver>0</encryver>
                </appattach>
                <extinfo />
                <sourceusername />
                <sourcedisplayname />
                <thumburl />
                <md5>e25b18a155770eb1e3f7786a54ec9038</md5>
                <statextstr>GhQKEnd4Y2I4ZDQyOThjNmEwOWJjYg==</statextstr>
        </appmsg>
        <fromusername>wxid_3zcnbha3j2v922</fromusername>
        <scene>0</scene>
        <appinfo>
                <version>9</version>
                <appname>哔哩哔哩</appname>
        </appinfo>
        <commenturl></commenturl>
</msg>"""
    xml_string = """<msg>
        <appmsg appid="wxd8a2750ce9d46980" sdkver="0">
                <title>大家是怎么对男博士祛魅的🤔 #有想法轻松发  #男博士  #女博士  #研究生</title>
                <des>大家是怎么对男博士祛魅的🤔 #有想法轻松发  #男博士  #女博士  #研究生</des>
                <username />
                <action>view</action>
                <type>5</type>
                <showtype>0</showtype>
                <content />
                <url>https://www.xiaohongshu.com/discovery/item/67471802000000000201b42f?app_platform=android&amp;ignoreEngage=true&amp;app_version=8.65.0&amp;share_from_user_hidden=true&amp;xsec_source=app_share&amp;type=normal&amp;xsec_token=CBd7fKrQuz3O0el1j2TfUs9Ws67HwnJnNyIBoBaMknVo0=&amp;author_share=1&amp;xhsshare=WeixinSession&amp;shareRedId=ODlDRkU6Nk42NzUyOTgwNjg4OTlJSzZK&amp;apptime=1734240150&amp;share_id=2eb5c42a9e464ec59a7fe9bc25c05eb7</url>
                <lowurl />
                <forwardflag>0</forwardflag>
                <dataurl />
                <lowdataurl />
                <contentattr>0</contentattr>
                <streamvideo>
                        <streamvideourl />
                        <streamvideototaltime>0</streamvideototaltime>
                        <streamvideotitle />
                        <streamvideowording />
                        <streamvideoweburl />
                        <streamvideothumburl />
                        <streamvideoaduxinfo />
                        <streamvideopublishid />
                </streamvideo>
                <canvasPageItem>
                        <canvasPageXml><![CDATA[]]></canvasPageXml>
                </canvasPageItem>
                <appattach>
                        <attachid />
                        <cdnthumburl>3057020100044b304902010002046134addf02032f56c2020476aaa2740204675e679e042438656639633363632d396463302d346537352d626166642d6439626435303938323064330204051408030201000405004c54a200</cdnthumburl>
                        <cdnthumbmd5>ab8b719f6a4d566fecc4989ded65a1df</cdnthumbmd5>
                        <cdnthumblength>6284</cdnthumblength>
                        <cdnthumbheight>88</cdnthumbheight>
                        <cdnthumbwidth>66</cdnthumbwidth>
                        <cdnthumbaeskey>090cbd60f7c5f0683b63c7a15cf206af</cdnthumbaeskey>
                        <aeskey>090cbd60f7c5f0683b63c7a15cf206af</aeskey>
                        <encryver>1</encryver>
                        <fileext />
                        <islargefilemsg>0</islargefilemsg>
                </appattach>
                <extinfo />
                <androidsource>2</androidsource>
                <thumburl />
                <mediatagname />
                <messageaction><![CDATA[]]></messageaction>
                <messageext><![CDATA[]]></messageext>
                <emoticongift>
                        <packageflag>0</packageflag>
                        <packageid />
                </emoticongift>
                <emoticonshared>
                        <packageflag>0</packageflag>
                        <packageid />
                </emoticonshared>
                <designershared>
                        <designeruin>0</designeruin>
                        <designername>null</designername>
                        <designerrediretcturl><![CDATA[null]]></designerrediretcturl>
                </designershared>
                <emotionpageshared>
                        <tid>0</tid>
                        <title>null</title>
                        <desc>null</desc>
                        <iconUrl><![CDATA[null]]></iconUrl>
                        <secondUrl>null</secondUrl>
                        <pageType>0</pageType>
                        <setKey>null</setKey>
                </emotionpageshared>
                <webviewshared>
                        <shareUrlOriginal />
                        <shareUrlOpen />
                        <jsAppId />
                        <publisherId />
                        <publisherReqId />
                </webviewshared>
                <template_id />
                <md5>ab8b719f6a4d566fecc4989ded65a1df</md5>
                <websearch>
                        <rec_category>0</rec_category>
                        <channelId>0</channelId>
                </websearch>
                <weappinfo>
                        <username />
                        <appid />
                        <appservicetype>0</appservicetype>
                        <secflagforsinglepagemode>0</secflagforsinglepagemode>
                        <videopageinfo>
                                <thumbwidth>66</thumbwidth>
                                <thumbheight>88</thumbheight>
                                <fromopensdk>0</fromopensdk>
                        </videopageinfo>
                </weappinfo>
                <statextstr>GhQKEnd4ZDhhMjc1MGNlOWQ0Njk4MA==</statextstr>
                <musicShareItem>
                        <musicDuration>0</musicDuration>
                </musicShareItem>
                <finderLiveProductShare>
                        <finderLiveID><![CDATA[]]></finderLiveID>
                        <finderUsername><![CDATA[]]></finderUsername>
                        <finderObjectID><![CDATA[]]></finderObjectID>
                        <finderNonceID><![CDATA[]]></finderNonceID>
                        <liveStatus><![CDATA[]]></liveStatus>
                        <appId><![CDATA[]]></appId>
                        <pagePath><![CDATA[]]></pagePath>
                        <productId><![CDATA[]]></productId>
                        <coverUrl><![CDATA[]]></coverUrl>
                        <productTitle><![CDATA[]]></productTitle>
                        <marketPrice><![CDATA[0]]></marketPrice>
                        <sellingPrice><![CDATA[0]]></sellingPrice>
                        <platformHeadImg><![CDATA[]]></platformHeadImg>
                        <platformName><![CDATA[]]></platformName>
                        <shopWindowId><![CDATA[]]></shopWindowId>
                        <flashSalePrice><![CDATA[0]]></flashSalePrice>
                        <flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>
                        <ecSource><![CDATA[]]></ecSource>
                        <sellingPriceWording><![CDATA[]]></sellingPriceWording>
                        <platformIconURL><![CDATA[]]></platformIconURL>
                        <firstProductTagURL><![CDATA[]]></firstProductTagURL>
                        <firstProductTagAspectRatioString><![CDATA[0.0]]></firstProductTagAspectRatioString>
                        <secondProductTagURL><![CDATA[]]></secondProductTagURL>
                        <secondProductTagAspectRatioString><![CDATA[0.0]]></secondProductTagAspectRatioString>
                        <firstGuaranteeWording><![CDATA[]]></firstGuaranteeWording>
                        <secondGuaranteeWording><![CDATA[]]></secondGuaranteeWording>
                        <thirdGuaranteeWording><![CDATA[]]></thirdGuaranteeWording>
                        <isPriceBeginShow>false</isPriceBeginShow>
                        <lastGMsgID><![CDATA[]]></lastGMsgID>
                        <promoterKey><![CDATA[]]></promoterKey>
                        <discountWording><![CDATA[]]></discountWording>
                        <priceSuffixDescription><![CDATA[]]></priceSuffixDescription>
                        <productCardKey><![CDATA[]]></productCardKey>
                        <isWxShop><![CDATA[]]></isWxShop>
                        <brandIconUrl><![CDATA[]]></brandIconUrl>
                        <showBoxItemStringList />
                </finderLiveProductShare>
                <finderOrder>
                        <appID><![CDATA[]]></appID>
                        <orderID><![CDATA[]]></orderID>
                        <path><![CDATA[]]></path>
                        <priceWording><![CDATA[]]></priceWording>
                        <stateWording><![CDATA[]]></stateWording>
                        <productImageURL><![CDATA[]]></productImageURL>
                        <products><![CDATA[]]></products>
                        <productsCount><![CDATA[0]]></productsCount>
                </finderOrder>
                <finderShopWindowShare>
                        <finderUsername><![CDATA[]]></finderUsername>
                        <avatar><![CDATA[]]></avatar>
                        <nickname><![CDATA[]]></nickname>
                        <commodityInStockCount><![CDATA[]]></commodityInStockCount>
                        <appId><![CDATA[]]></appId>
                        <path><![CDATA[]]></path>
                        <appUsername><![CDATA[]]></appUsername>
                        <query><![CDATA[]]></query>
                        <liteAppId><![CDATA[]]></liteAppId>
                        <liteAppPath><![CDATA[]]></liteAppPath>
                        <liteAppQuery><![CDATA[]]></liteAppQuery>
                        <platformTagURL><![CDATA[]]></platformTagURL>
                        <saleWording><![CDATA[]]></saleWording>
                        <lastGMsgID><![CDATA[]]></lastGMsgID>
                        <profileTypeWording><![CDATA[]]></profileTypeWording>
                        <saleWordingExtra><![CDATA[]]></saleWordingExtra>
                        <isWxShop><![CDATA[]]></isWxShop>
                        <platformIconUrl><![CDATA[]]></platformIconUrl>
                        <brandIconUrl><![CDATA[]]></brandIconUrl>
                        <description><![CDATA[]]></description>
                        <backgroundUrl><![CDATA[]]></backgroundUrl>
                        <darkModePlatformIconUrl><![CDATA[]]></darkModePlatformIconUrl>
                        <reputationInfo>
                                <hasReputationInfo>0</hasReputationInfo>
                                <reputationScore>0</reputationScore>
                                <reputationWording />
                                <reputationTextColor />
                                <reputationLevelWording />
                                <reputationBackgroundColor />
                        </reputationInfo>
                        <productImageURLList />
                </finderShopWindowShare>
                <findernamecard>
                        <username />
                        <avatar><![CDATA[]]></avatar>
                        <nickname />
                        <auth_job />
                        <auth_icon>0</auth_icon>
                        <auth_icon_url />
                        <ecSource><![CDATA[]]></ecSource>
                        <lastGMsgID><![CDATA[]]></lastGMsgID>
                </findernamecard>
                <finderGuarantee>
                        <scene><![CDATA[0]]></scene>
                </finderGuarantee>
                <directshare>0</directshare>
                <gamecenter>
                        <namecard>
                                <iconUrl />
                                <name />
                                <desc />
                                <tail />
                                <jumpUrl />
                        </namecard>
                </gamecenter>
                <patMsg>
                        <chatUser />
                        <records>
                                <recordNum>0</recordNum>
                        </records>
                </patMsg>
                <secretmsg>
                        <issecretmsg>0</issecretmsg>
                </secretmsg>
                <referfromscene>0</referfromscene>
                <gameshare>
                        <liteappext>
                                <liteappbizdata />
                                <priority>0</priority>
                        </liteappext>
                        <appbrandext>
                                <litegameinfo />
                                <priority>-1</priority>
                        </appbrandext>
                        <gameshareid />
                        <sharedata />
                        <isvideo>0</isvideo>
                        <duration>-1</duration>
                        <isexposed>0</isexposed>
                        <readtext />
                </gameshare>
                <mpsharetrace>
                        <hasfinderelement>0</hasfinderelement>
                        <lastgmsgid />
                </mpsharetrace>
                <wxgamecard>
                        <framesetname />
                        <mbcarddata />
                        <minpkgversion />
                        <clientextinfo />
                        <mbcardheight>0</mbcardheight>
                        <isoldversion>0</isoldversion>
                </wxgamecard>
                <liteapp>
                        <id>null</id>
                        <path />
                        <query />
                </liteapp>
        </appmsg>
        <fromusername>wxid_3zcnbha3j2v922</fromusername>
        <scene>0</scene>
        <appinfo>
                <version>46</version>
                <appname>小红书</appname>
        </appinfo>
        <commenturl></commenturl>
</msg>"""
    root = parse_xml(xml_string1)
    print(root)
    appname = root.find("appinfo").find("appname").text
    print(appname)
    title = root.find("appmsg").find("title").text
    print(title)