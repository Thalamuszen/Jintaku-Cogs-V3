import discord
from redbot.core import commands, Config
from random import randint
import aiohttp
import logging

log = logging.getLogger("Roleplay")  # Thanks to Sinbad for the example code for logging
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()

if logging.getLogger("red").isEnabledFor(logging.DEBUG):
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)
log.addHandler(console)

BaseCog = getattr(commands, "Cog", object)


class Roleplay(BaseCog):
    """Interact with people!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)
        default_global = {
            "fuck": [
                "https://cdn.discordapp.com/attachments/610429582415364116/670260329736830986/ezgif.com-video-to-gif.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619115152605214/AnimeFuck.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913704909930516/FuckAna.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726746517176380/FuckAna2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726764150030347/FuckAna3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726777164955648/FuckAna4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913718050684958/FuckAshe.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913723729772568/FuckAshe2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913751496065024/FuckAshe3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913753131974667/FuckAshe4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913759729483777/FuckAshe5.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619146165157908/AsheFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619187747487744/AsheFuck2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308666459684910/FuckAshe8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726794466721802/FuckAshe9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726811516436580/FuckAshe10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726841749110835/FuckAshe11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913760258097171/FuckBrig.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676913761390690305/FuckBrig2.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670289020365963264/BrigDoggy.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619197432266765/BrigFuck.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474409010692126/FuckBrig5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474510001143819/FuckBrig6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726901471674458/FuckBrig7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709726924766838865/FuckBrig8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676914977390460965/FuckDVa.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676914979651452938/FuckDVa2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676914982452985888/FuckDVa3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915000807391260/FuckDVa4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915006339809300/FuckDVa5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915011867901965/FuckDVa6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915029022474263/FuckDVa7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915029903147043/FuckDVa8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915039088934952/FuckDVa9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915059242303555/FuckDVa10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915066020298795/FuckDVa11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915079135887410/FuckDVa12.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915082508369941/FuckDVa13.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915092482293768/FuckDVa14.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915109234475009/FuckDVa15.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676915111142883358/FuckDVa16.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670283970402844712/dvachoke.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670342078982651905/DvaPound.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670605349081972736/DvaFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619195490435072/DvaFuck2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/672207488216465440/DvaFuck3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474550514188288/FuckDVa22.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474619069956096/FuckDVa23.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474636870582282/FuckDVa24.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474652683108362/FuckDVa25.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474668894224414/FuckDVa26.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/681921503851577436/FuckDva27.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308675481763841/FuckDVa28.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308689465573407/FuckDVa29.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728157741350982/FuckDVa30.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728167950155806/FuckDVa31.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728191899762758/FuckDVa32.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728218319683595/FuckDVa33.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728237135200266/FuckDVa34.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728253488791582/FuckDVa35.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728275228000326/FuckDVa36.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728287382962206/FuckDVa37.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728315044528178/FuckDVa38.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728329921724426/FuckDVa39.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728341166391346/FuckDVa40.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728357322850344/FuckDVa41.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709728372275544134/FuckDVa42.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676916876869238799/FuckMei.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/675438251552669696/FuckMercy.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676916888185471006/FuckMercy.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676916891423473664/FuckMercy2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676916973963051030/FuckMercy3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917010512347146/FuckMercy4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917124114939905/FuckMercy5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917118268211230/FuckMercy6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917200480895011/FuckMercy7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917141584216064/FuckMercy8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917243753529344/FuckMercy9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917057580957726/FuckMercy10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917215878184977/FuckMercy11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917242688045066/FuckMercy12.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917245988831242/FuckMercy13.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917246668439562/FuckMercy14.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676917247540854826/FuckMercy15.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282197912158228/FuckMercy22.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282212814651403/FuckMercy23.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282228614594590/FuckMercy24.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282241428062228/FuckMercy25.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282262815080448/FuckMercy26.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282278631800856/FuckMercy27.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282303763808307/FuckMercy28.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282322021744660/FuckMercy29.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677282326400466944/FuckMercy30.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/680093867911151620/FuckMercy31.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/681159175572553728/FuckMercy32.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308701062823938/FuckMercy33.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729616402579526/FuckMercy34.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729625068142643/FuckMercy35.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729634182365226/FuckMercy36.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729651509166130/FuckMercy37.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670605386188849153/MercyFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619184945823749/MercyFuck2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/672207493736169503/MercyFuck3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/672207494499794954/MercyFuck4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729656013586492/FuckMoira.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729667070033960/FuckMoira2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919430672023572/FuckMulti.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919461634113595/FuckMulti2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919497361195008/FuckMulti3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258322973425694/FuckMulti4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308718431305873/FuckMulti5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729685650669598/FuckMulti6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729697545846805/FuckMulti7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709729709289766912/FuckMulti8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919529447751742/FuckPharah.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919551035703348/FuckPharah2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919578739081216/FuckPharah3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919618211676170/FuckPharah4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919659844599813/FuckPharah5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919696842555432/FuckPharah6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676919733630795805/FuckPharah7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677158960721035275/FuckPharah9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677158971122909205/FuckPharah10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677158982007128074/FuckPharah11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677158994376261692/FuckPharah12.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159002903150592/FuckPharah13.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159016895479838/FuckPharah14.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159040400359455/FuckPharah15.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159063779540992/FuckPharah16.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159079197671484/FuckPharah17.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159103122112512/FuckPharah18.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159109346459658/FuckPharah19.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159119421046809/FuckPharah20.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677159139801169949/FuckPharah21.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308728242176015/FuckPharah22.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730549631287357/FuckPharah23.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730561320550400/FuckPharah24.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730573371047936/FuckPharah25.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619906386952202/PharahFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619208081604618/SombraFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619200309428224/SombraFuck2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183464948236289/FuckSombra3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183471818506242/FuckSombra4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183477858435125/FuckSombra5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183493817630720/FuckSombra6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183505641373706/FuckSombra7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183515514896394/FuckSombra8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183524100374528/FuckSombra9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183539648659456/FuckSombra10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677183551464013831/FuckSombra11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677474694018105354/SymFuck.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730579872219176/FuckSym2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730596775133214/FuckSym3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676921210042581012/FuckTracer.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676921213704208404/FuckTracer2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676921239079485465/FuckTracer3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676921260974014495/FuckTracer4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676921274873675776/FuckTracer5.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619209088368678/TracerFuck.gif", 
                "https://cdn.discordapp.com/attachments/670618563912007681/677194816018317342/FuckTracer7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677194870401663031/FuckTracer8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677194886675562592/FuckTracer9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677194918300614686/FuckTracer10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677194931806273555/FuckTracer11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/681921485413416980/FuckTracer12.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730606799519824/FuckTracer13.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922194433146880/FuckWidow.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922231317725196/FuckWidow2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922241778319405/FuckWidow4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922273168621578/FuckWidow5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922299789737994/FuckWidow6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922311823327233/FuckWidow7.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922326582820890/FuckWidow8.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922333126197282/FuckWidow9.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922346191323140/FuckWidow10.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922363262009384/FuckWidow11.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922372535615507/FuckWidow12.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922381947764746/FuckWidow13.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922402097070090/FuckWidow14.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922412796739626/FuckWidow15.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/676922430471798814/FuckWidow16.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258329512345610/FuckWidow20.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258347522818088/FuckWidow21.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258362131447808/FuckWidow22.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258390761766985/FuckWidow23.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258415999025192/FuckWidow24.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258450547376167/FuckWidow25.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258471196065823/FuckWidow26.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258493132144644/FuckWidow27.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258508651200512/FuckWidow28.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258531170287667/FuckWidow29.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/677258553723191303/FuckWidow30.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682308740799791126/FuckWidow31.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730621190307870/FuckWidow32.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730628555243581/FuckWidow33.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619191061118986/WidowFuck.gif",
                "https://cdn.discordapp.com/attachments/610429582415364116/670619208593440788/WidowFuck2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/672207496362065939/WidowFuck3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309509175181362/LesDVaTracer.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309521732927551/LesMercyAna.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709730641327161365/LesMercyDVa.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309538346434572/LesMercyPharah.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309551445508186/LesMercyPharah2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309570525397082/LesMercyWidow.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309575839580194/LesWidowSombra.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309586937446426/LesWidowSombra2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/682309602364489758/LesWidowTracer.gif",
            ],
            "fuckself": [
                "https://cdn.discordapp.com/attachments/670618563912007681/709732065045643313/SelfDVa.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732081932173383/SelfDVa2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732091910422548/SelfDVa3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/710796073353871360/SelfDVa4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/719888426278846475/SelfDVa5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732107370364979/SelfMercy.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732123090616413/SelfMercy2.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732135002701884/SelfMercy3.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732161124827166/SelfMercy4.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732173749682196/SelfMercy5.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/710796087006461972/SelfMercy6.gif",
                "https://cdn.discordapp.com/attachments/670618563912007681/709732185359515658/SelfWidow.gif",
            ],
            "hugs": [
                "https://img2.gelbooru.com/images/ff/63/ff63a3c4329fda2bf1e9704d4e150fea.gif",
                "https://img2.gelbooru.com/images/2c/e8/2ce81403e0279f1a570711f7472b3abb.gif",
                "https://img2.gelbooru.com/images/e2/05/e205e349535e22c07865913770dcad5f.gif",
                "https://img2.gelbooru.com/images/09/f6/09f63a79f70700abb2593862525ade10.gif",
                "https://safebooru.org//images/1174/5ebeacd87b22a0c5949ecb875667ae75702c2fed.gif",
                "https://safebooru.org//images/848/4828fc43e39f52abd5bac6b299e822ae02786974.gif",
                "https://safebooru.org//images/160/ba09bc95bc05b4f47af22671950e66f085c7ea9e.gif",
                "https://img2.gelbooru.com/images/3f/73/3f73b1c3703d91a9300aebdaab6e26c0.gif",
                "https://img2.gelbooru.com/images/7d/7c/7d7c8ce0c4e561804f16adc7907a78e8.gif",
                "https://img2.gelbooru.com/images/5e/8c/5e8c1a33470c62f6907d0ea5a03ae644.gif",
                "https://img2.gelbooru.com/images/2b/b9/2bb9dc89cf991181bce06279d8d5f0f4.gif",
                "https://cdn.weeb.sh/images/rJaog0FtZ.gif",
                "https://cdn.weeb.sh/images/Hyv6uOQPZ.gif",
                "https://cdn.weeb.sh/images/BJx2l0ttW.gif",
                "https://media.giphy.com/media/iviBUyNqP46Aw/giphy.gif",
                "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif",
                "https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
                "https://media.giphy.com/media/3ZnBrkqoaI2hq/giphy.gif",
                "https://media.giphy.com/media/3o6ZsTopjMRVkJXAWI/giphy.gif",
                "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
                "https://media.giphy.com/media/vVA8U5NnXpMXK/giphy.gif",
                "https://media.giphy.com/media/aVmEsdMmCTqSs/giphy.gif",
                "https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif",
                "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif",
                "https://media.giphy.com/media/ba92ty7qnNcXu/giphy.gif",
                "https://media.giphy.com/media/C4gbG94zAjyYE/giphy.gif",
                "https://i.imgur.com/4Y50gzE.gif",
                "https://i.imgur.com/OrpyAfa.gif",
                "https://i.imgur.com/aA8mTuX.gif",
                "https://i.imgur.com/fm9PHyr.gif",
                "https://i.imgur.com/tCuAWNW.gif",
                "https://i.imgur.com/BPMTcq7.gif",
                "https://i.imgur.com/V1fd9oP.gif",
                "https://i.imgur.com/OSDidQJ.gif",
                "https://i.imgur.com/1RlShE9.gif",
                "https://i.imgur.com/hM1LcZf.gif",
                "https://i.imgur.com/cRfX87T.gif",
                "https://cdn.weeb.sh/images/HyNJIaVCb.gif",
                "https://cdn.weeb.sh/images/ryMqdOXvZ.gif",
                "https://cdn.weeb.sh/images/Hk4qu_XvZ.gif",
                "https://cdn.weeb.sh/images/ByuHsvu8z.gif",
                "https://cdn.weeb.sh/images/Hy4hxRKtW.gif",
                "https://cdn.weeb.sh/images/Sk2gmRZZG.gif",
                "https://cdn.weeb.sh/images/HkfgF_QvW.gif",
                "https://cdn.weeb.sh/images/HJTWcTNCZ.gif",
                "https://cdn.weeb.sh/images/rko9O_mwW.gif",
                "https://cdn.weeb.sh/images/rkx1dJ25z.gif",
                "https://media.giphy.com/media/KMQoRt68bFei4/giphy.gif",
                "https://cdn.weeb.sh/images/BkZngAYtb.gif",
            ],
            "cuddle": [
                "https://cdn.weeb.sh/images/BkTe8U7v-.gif",
                "https://cdn.weeb.sh/images/SykzL87D-.gif",
                "https://cdn.weeb.sh/images/BywGX8caZ.gif",
                "https://cdn.weeb.sh/images/SJceIU7wZ.gif",
                "https://cdn.weeb.sh/images/SJn18IXP-.gif",
                "https://cdn.weeb.sh/images/B1Qb88XvW.gif",
                "https://cdn.weeb.sh/images/r1XEOymib.gif",
                "https://cdn.weeb.sh/images/SJLkLImPb.gif",
                "https://cdn.weeb.sh/images/SyUYOJ7iZ.gif",
                "https://cdn.weeb.sh/images/rkBl8LmDZ.gif",
                "https://cdn.weeb.sh/images/Byd1IUmP-.gif",
                "https://cdn.weeb.sh/images/B1S1I87vZ.gif",
                "https://cdn.weeb.sh/images/r1s9RqB7G.gif",
                "https://cdn.weeb.sh/images/Hy5y88mPb.gif",
                "https://cdn.weeb.sh/images/rkA6SU7w-.gif",
                "https://cdn.weeb.sh/images/r1A77CZbz.gif",
                "https://cdn.weeb.sh/images/SJYxIUmD-.gif",
                "https://cdn.weeb.sh/images/H1SfI8XwW.gif",
                "https://cdn.weeb.sh/images/rJCAH8XPb.gif",
                "https://cdn.weeb.sh/images/By03IkXsZ.gif",
                "https://cdn.weeb.sh/images/ryfyLL7D-.gif",
                "https://cdn.weeb.sh/images/BJwpw_XLM.gif",
                "https://cdn.weeb.sh/images/r1VzDkmjW.gif",
                "https://cdn.weeb.sh/images/BJkABImvb.gif",
                "https://cdn.weeb.sh/images/HkzArUmvZ.gif",
                "https://cdn.weeb.sh/images/r1A77CZbz.gif",
            ],
            "kiss": [
                "https://cdn.discordapp.com/attachments/670618563912007681/673248796276293652/KissGenjiMercy.gif",
                "https://78.media.tumblr.com/7255f36b2c31fac77542e8fe6837b408/tumblr_mokq94dAXR1s05qslo1_500.gif",
            ],
            "slap": [
                "https://cdn.weeb.sh/images/H16aQJFvb.gif",
                "https://img2.gelbooru.com/images/d2/2c/d22c2eedd00914ce38efb46d797be031.gif",
                "https://safebooru.org//images/192/fb1c45872a172ab384a22b9d9089b861d366564c.gif",
                "https://safebooru.org//images/118/968c5b9f042a5262c8c8628cd52a7a6a557e525d.gif",
                "https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
                "https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
                "https://media1.tenor.com/images/4a6b15b8d111255c77da57c735c79b44/tenor.gif?itemid=10937039",
                "https://media1.tenor.com/images/153b2f1bfd3c595c920ce60f1553c5f7/tenor.gif?itemid=10936993",
                "https://media1.tenor.com/images/4fa82be21ffd18c99a9708ba209d56ad/tenor.gif?itemid=5318916",
                "https://media1.tenor.com/images/1ba1ea1786f0b03912b1c9138dac707c/tenor.gif?itemid=5738394",
                "https://i.imgur.com/EO8udG1.gif",
                "https://i.imgur.com/lMmn1wy.gif",
                "https://i.imgur.com/TuSUTg5.gif",
                "https://i.imgur.com/9Ql97mO.gif",
                "https://i.imgur.com/VBGqeIU.gif",
                "https://i.imgur.com/uPZwGFQ.gif",
                "https://i.imgur.com/Su0X9iF.gif",
                "https://i.imgur.com/eNiOIMB.gif",
                "https://i.imgur.com/gsAGyoI.gif",
                "https://cdn.weeb.sh/images/HyPjmytDW.gif",
                "https://cdn.weeb.sh/images/BJ8o71tD-.gif",
                "https://cdn.weeb.sh/images/BJLCX1Kw-.gif",
                "https://cdn.weeb.sh/images/rJvR71KPb.gif",
                "https://cdn.weeb.sh/images/SkZTQkKPZ.gif",
                "https://cdn.weeb.sh/images/Hkw1VkYP-.gif",
                "https://cdn.weeb.sh/images/BkxEo7ytDb.gif",
                "https://cdn.weeb.sh/images/B1fnQyKDW.gif",
                "https://cdn.weeb.sh/images/Bkj-oaV0Z.gif",
                "https://cdn.weeb.sh/images/r1siXJKw-.gif",
                "https://cdn.weeb.sh/images/r1VF-lcyz.gif",
                "https://cdn.weeb.sh/images/BJgsX1Kv-.gif",
                "https://cdn.weeb.sh/images/SkKn-xc1f.gif",
                "https://cdn.weeb.sh/images/Sk9mfCtY-.gif",
                "https://cdn.weeb.sh/images/ry_RQkYDb.gif",
                "https://cdn.weeb.sh/images/HkK2mkYPZ.gif",
                "https://cdn.weeb.sh/images/S1ylxxc1M.gif",
                "https://cdn.weeb.sh/images/SJdXoVguf.gif",
                "https://cdn.weeb.sh/images/ByHUMRNR-.gif",
                "https://cdn.weeb.sh/images/SkdyfWCSf.gif",
                "https://cdn.weeb.sh/images/rknn7Jtv-.gif",
                "https://cdn.weeb.sh/images/rJgTQ1tvb.gif",
                "https://cdn.weeb.sh/images/rkaqm1twZ.gif",
                "https://cdn.weeb.sh/images/ryn_Zg5JG.gif",
                "https://cdn.weeb.sh/images/SJ-CQytvW.gif",
            ],
            "pat": [
                "https://cdn.weeb.sh/images/r180y1Yvb.gif",
                "https://img2.gelbooru.com/images/56/b9/56b9297e70fd0312aba34e7ed1608b27.gif",
                "https://img2.gelbooru.com/images/ce/ea/ceea3600c9de0fb5a2452d1e9f2d714b.gif",
                "https://img2.gelbooru.com/images/4e/08/4e0895594994c5eedf5a1991f02bd4dc.gif",
                "https://img2.gelbooru.com/images/c7/41/c741fec81ea5eceb8ebcc7b4dc2bedd5.gif",
                "http://i.imgur.com/10VrpFZ.gif",
                "http://i.imgur.com/x0u35IU.gif",
                "http://i.imgur.com/0gTbTNR.gif",
                "http://i.imgur.com/hlLCiAt.gif",
                "http://i.imgur.com/sAANBDj.gif",
                "https://i.imgur.com/10VrpFZ.gif"
                "https://i.imgur.com/x0u35IU.gif",
                "https://i.imgur.com/sAANBDj.gif",
                "https://i.imgur.com/wtxwpm1.gif",
                "https://i.imgur.com/3eR7weH.gif",
                "https://i.imgur.com/cK8Ro3x.gif",
                "https://i.imgur.com/qtHlt3n.gif",
                "https://i.imgur.com/bzzodCZ.gif",
                "https://cdn.weeb.sh/images/r180y1Yvb.gif",
                "https://cdn.weeb.sh/images/Sky1x1YwW.gif",
                "https://cdn.weeb.sh/images/r1Y5L6NCZ.gif",
                "https://cdn.weeb.sh/images/HJGQlJYwb.gif",
                "https://cdn.weeb.sh/images/rkBZkRttW.gif",
                "https://cdn.weeb.sh/images/rJavp1KVM.gif",
                "https://cdn.weeb.sh/images/r1AsJ1twZ.gif",
                "https://cdn.weeb.sh/images/ry1tlj2AW.gif",
                "https://cdn.weeb.sh/images/HyqTkyFvb.gif",
                "https://cdn.weeb.sh/images/H1jnJktPb.gif",
                "https://cdn.weeb.sh/images/ryLKqTVCW.gif",
                "https://cdn.weeb.sh/images/rJJXgJFDW.gif",
                "https://i.imgur.com/grAHcaB.gif",
                "https://cdn.weeb.sh/images/SJS1lyYwW.gif",
                "https://cdn.weeb.sh/images/rkbblkYvb.gif",
                "https://cdn.weeb.sh/images/H1s5hx0Bf.gif",
                "https://cdn.weeb.sh/images/rkSN7g91M.gif",
                "https://cdn.weeb.sh/images/rktsca40-.gif",
                "https://cdn.weeb.sh/images/ryh6x04Rb.gif",
                "https://cdn.weeb.sh/images/rkTC896_f.gif",
                "https://cdn.weeb.sh/images/SJudB96_f.gif",
                "https://cdn.weeb.sh/images/SJudB96_f.gif",
                "https://cdn.weeb.sh/images/r1lVQgcyG.gif",
            ],
            "lick": [
                "https://media1.tenor.com/images/c4f68fbbec3c96193386e5fcc5429b89/tenor.gif?itemid=13451325",
                "https://media1.tenor.com/images/ec2ca0bf12d7b1a30fea702b59e5a7fa/tenor.gif?itemid=13417195",
                "https://cdn.weeb.sh/images/HkEqiExdf.gif",
                "https://media1.tenor.com/images/5f73f2a7b302a3800b3613095f8a5c40/tenor.gif?itemid=10005495",
                "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727",
                "https://media1.tenor.com/images/069076cc8054bb8b114c5a37eec70a1f/tenor.gif?itemid=13248504",
                "https://media1.tenor.com/images/fc0ef2ba03d82af0cbd6c5815c3c83d5/tenor.gif?itemid=12141725",
                "https://media1.tenor.com/images/d702fa41028207c6523b831ec2db9467/tenor.gif?itemid=5990650",
                "https://media1.tenor.com/images/81769ee6622b5396d1489fb4667fd20a/tenor.gif?itemid=14376074",
                "https://media1.tenor.com/images/feeef4685f9307b76c78a22ba0a69f48/tenor.gif?itemid=8413059",
                "https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773",
            ],
            "highfive": [
                "https://media1.tenor.com/images/0ae4995e4eb27e427454526c05b2e3dd/tenor.gif?itemid=12376992",
                "https://media1.tenor.com/images/7b1f06eac73c36721912edcaacddf666/tenor.gif?itemid=10559431",
                "https://media1.tenor.com/images/c3263b8196afc25ddc1d53a4224347cd/tenor.gif?itemid=9443275",
                "https://media1.tenor.com/images/56d6725009312574e4798c732cebc5fe/tenor.gif?itemid=12312526",
                "https://media1.tenor.com/images/e96d2396570a2fadd9c83e284a1ca675/tenor.gif?itemid=5390726",
                "https://media1.tenor.com/images/106c8e64e864230341b59cc892b5a980/tenor.gif?itemid=5682921",
                "https://media1.tenor.com/images/b714d7680f8b49d69b07bc2f1e052e72/tenor.gif?itemid=13400356",
                "https://media1.tenor.com/images/0c23b320822afd5b1ce3faf01c2b9b69/tenor.gif?itemid=14137078",
                "https://media1.tenor.com/images/e2f299d05a7b1832314ec7a331440d4e/tenor.gif?itemid=5374033",
                "https://media1.tenor.com/images/16267f3a34efb42598bd822effaccd11/tenor.gif?itemid=14137081",
                "https://media1.tenor.com/images/9730876547cb3939388cf79b8a641da9/tenor.gif?itemid=8073516",
                "https://media1.tenor.com/images/ce85a2843f52309b85515f56a0a49d06/tenor.gif?itemid=14137077",
            ],
            "feed": [
                "https://media1.tenor.com/images/93c4833dbcfd5be9401afbda220066ee/tenor.gif?itemid=11223742",
                "https://media1.tenor.com/images/33cfd292d4ef5e2dc533ff73a102c2e6/tenor.gif?itemid=12165913",
                "https://media1.tenor.com/images/72268391ffde3cd976a456ee2a033f46/tenor.gif?itemid=7589062",
                "https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977",
                "https://media1.tenor.com/images/187ff5bc3a5628b6906935232898c200/tenor.gif?itemid=9340097",
                "https://media1.tenor.com/images/15e7d9e1eb0aad2852fabda1210aee95/tenor.gif?itemid=12005286",
                "https://media1.tenor.com/images/d08d0825019c321f21293c35df8ed6a9/tenor.gif?itemid=9032297",
                "https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244",
                "https://media1.tenor.com/images/6bde17caa5743a22686e5f7b6e3e23b4/tenor.gif?itemid=13726430",
                "https://media1.tenor.com/images/fd3616d34ade61e1ac5cd0975c25a917/tenor.gif?itemid=13653906",
                "https://imgur.com/v7jsPrv",
            ],
            "tickle": [
                "https://img2.gelbooru.com/images/c4/41/c441cf1fce1fe51420796f6bd0e420e1.gif",
                "https://img2.gelbooru.com/images/00/a8/00a8b5ad3ceb7b063ed8a4a59f7c8bdf.gif",
                "https://img2.gelbooru.com/images/51/63/516318277e9438626c12d0543eb5808b.gif",
                "https://img2.gelbooru.com/images/0c/e4/0ce45bee2e1aaed9f1e650438f1e2867.gif",
                "https://img2.gelbooru.com/images/11/74/1174ccbee672bd3f1129f5dc36964926.gif",
                "https://media1.tenor.com/images/02f62186ccb7fa8a2667f3216cfd7e13/tenor.gif?itemid=13269751",
                "https://media1.tenor.com/images/d38554c6e23b86c81f8d4a3764b38912/tenor.gif?itemid=11379131",
                "https://media1.tenor.com/images/05a64a05e5501be2b1a5a734998ad2b2/tenor.gif?itemid=11379130",
            ],
            "poke": [
                "https://img2.gelbooru.com/images/07/86/078690a58e0b816e8e00cc58e090b499.gif",
                "https://img2.gelbooru.com/images/b7/89/b789369db69022afde47a1ed62598ec6.gif",
                "https://img2.gelbooru.com/images/49/ec/49ecc543b7b0b680ad0c27c29e942a21.gif",
                "https://img2.gelbooru.com/images/91/ef/91ef340231f6d537836e23c8ab90a255.gif",
                "https://img2.gelbooru.com/images/62/d9/62d9a16a640bfcd25dd6159e53fc50d2.gif",
                "https://img2.gelbooru.com/images/1d/8b/1d8b77bf65858101a82d195deaa39252.gif",
                "https://img2.gelbooru.com/images/c0/22/c022dc318c7f014d7bac6c2300b9f7a2.gif",
                "https://media1.tenor.com/images/3b2bfd09965bd77f2a8cb9ba59cedbe4/tenor.gif?itemid=5607667",
                "https://media1.tenor.com/images/514efe749cb611eb382713596e3427d8/tenor.gif?itemid=13054528",
                "https://media1.tenor.com/images/8795ff617de989265907eed8029a99a3/tenor.gif?itemid=14629871",
                "https://media1.tenor.com/images/1e0ea8b241a7db2b9c03775133138733/tenor.gif?itemid=10064326",
                "https://media1.tenor.com/images/90f68d48795c51222c60afc7239c930c/tenor.gif?itemid=8701034",
                "https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763",
                "https://media1.tenor.com/images/f8a48a25f47d5d12342705c7c87368bb/tenor.gif?itemid=14134415",
                "https://media.tenor.com/images/6b5c1554a6ee9d48ab0392603bab8a8e/tenor.gif",
            ],
            "smug": [
                "https://cdn.nekos.life/v3/sfw/gif/smug/smug_027.gif",
                "https://cdn.nekos.life/v3/sfw/gif/smug/smug_057.gif",
                "https://i.kym-cdn.com/photos/images/original/001/087/562/93c.gif",
                "https://i.kym-cdn.com/photos/images/newsfeed/001/161/167/eda.gif",
                "https://media1.tenor.com/images/d9b3127da3f9419cbb28f9f7c00860d8/tenor.gif?itemid=9588226",
                "https://media1.tenor.com/images/0097fa7f957477f9edc5ff147bb9a5ad/tenor.gif?itemid=12390496",

            ],
        }
        self.config.register_global(**default_global)
        
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def fuck(self, ctx, *, user: discord.Member):
        """Fucks a user!"""

        author = ctx.message.author
        images = await self.config.fuck()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} wants to fuck you, {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def fuckself(self, ctx, *, user: discord.Member):
        """Fucks yourself!"""

        author = ctx.message.author
        images = await self.config.fuckself()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} is fucking themselves.. lewd!**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hugs a user!"""

        author = ctx.message.author
        images = await self.config.hugs()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddles a user!"""

        author = ctx.message.author
        images = await self.config.cuddle()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} cuddles {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss a user!"""

        author = ctx.message.author
        images = await self.config.kiss()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slaps a user!"""

        author = ctx.message.author
        images = await self.config.slap()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} slaps {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, user: discord.Member):
        """Pats a user!"""

        author = ctx.message.author
        images = await self.config.pat()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx, *, user: discord.Member):
        """Licks a user!"""

        author = ctx.message.author
        images = await self.config.lick()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} licks {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def highfive(self, ctx, *, user: discord.Member):
        """Highfives a user!"""

        author = ctx.message.author
        images = await self.config.highfive()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} highfives {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feeds a user!"""

        author = ctx.message.author
        images = await self.config.feed()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user!"""

        author = ctx.message.author
        images = await self.config.tickle()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, *, user: discord.Member):
        """Pokes a user!"""

        author = ctx.message.author
        images = await self.config.poke()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug towards someone!"""

        author = ctx.message.author
        images = await self.config.smug()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour=discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} is smug**"
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    async def fetch_nekos_life(self, ctx, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nekos.dev/api/v3/images/sfw/gif/{rp_action}/?count=20") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError) as ex:
                    log.debug("Pruned by exception, error below:")
                    log.debug(ex)
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]

