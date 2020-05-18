from xml.dom.minidom import *


xml_quelltext = """
<Musikliste>
    <Medium nummer="4710" typ="CD">
        <Titel>Abbey Road</Titel>
        <Interpret>The Beatles</Interpret>
        <Jahr>1969</Jahr>
        <Laufzeit>44</Laufzeit>
    </Medium>
    <Medium nummer="4711" typ="DVD">
        <Titel>The Wall</Titel>
        <Interpret>Pink Floyd</Interpret>
        <Jahr>1979</Jahr>
        <Laufzeit>81</Laufzeit>
        <BluRay />
    </Medium>
    <Medium nummer="4712" typ="CD">
        <Titel>Verschiedene Songs 1</Titel>
        <MP3 />
    </Medium>
    <Medium nummer="4713" typ="CD">
        <Titel>A Kind of Magic</Titel>
        <Interpret>Queen</Interpret>
        <Jahr>1986</Jahr>
        <Laufzeit>53</Laufzeit>
    </Medium>
    <Medium nummer="4714" typ="CD">
        <Titel>The Concert in Central Park</Titel>
        <Interpret>Paul Simon</Interpret>
        <Interpret>Art Garfunkel</Interpret>
        <Jahr>1981</Jahr>
        <Laufzeit>76</Laufzeit>
    </Medium>
    <Medium nummer="4715" typ="CD">
        <Titel>Face Value</Titel>
        <Interpret>Phil Collins</Interpret>
        <Jahr>1981</Jahr>
        <Laufzeit>48</Laufzeit>
    </Medium>
    <Medium nummer="4716" typ="CD">
        <Titel>The Dark Side of the Moon</Titel>
        <Interpret>Pink Floyd</Interpret>
        <Jahr>1973</Jahr>
        <Laufzeit>43</Laufzeit>
        <MP3 />
    </Medium>
    <Medium nummer="4717" typ="CD">
        <Titel>Graceland</Titel>
        <Interpret>Paul Simon</Interpret>
        <Jahr>1986</Jahr>
        <Laufzeit>45</Laufzeit>
    </Medium>
    <Medium nummer="4718" typ="CD">
        <Titel>.But Seriously</Titel>
        <Interpret>Phil Collins</Interpret>
        <Jahr>1989</Jahr>
        <Laufzeit>60</Laufzeit>
    </Medium>
    <Medium nummer="4730" typ="CD">
        <Titel>21</Titel>
        <Interpret>Adele</Interpret>
        <Jahr>2011</Jahr>
        <Laufzeit>46</Laufzeit>
    </Medium>
    <Medium nummer="4735" typ="CD">
        <Titel>Live At The Royal Albert Hall</Titel>
        <Interpret>Adele</Interpret>
        <Jahr>2011</Jahr>
        <Laufzeit>100</Laufzeit>
        <BluRay />
    </Medium>


</Musikliste>
"""
document = parseString(xml_quelltext)
node = document

def task1():
    for medium in node.getElementsByTagName("Medium"):
        titleTag = medium.getElementsByTagName("Titel")
        title = titleTag[0].firstChild.nodeValue

        mediumType = ""
        if not medium.getElementsByTagName("MP3") == []:
            mediumType = "MP3"
        elif not medium.getElementsByTagName("BluRay") == []:
            mediumType = "BluRay"
            
        print(title, ("- " + mediumType) if mediumType != "" else "")

def task2(wanted):
    titles = []
    for medium in node.getElementsByTagName("Medium"):
        for interpret in medium.getElementsByTagName("Interpret"):
            interpret = interpret.firstChild
            
            if interpret.nodeValue == wanted:
                titleTag = medium.getElementsByTagName("Titel")
                titles.append(titleTag[0].firstChild.nodeValue)

    print(*titles, sep=", ")

def task3():
    interprets = []
    for interpret in node.getElementsByTagName("Interpret"):
        interpret = interpret.firstChild.nodeValue
        
        if not interpret in interprets:
            interprets.append(interpret)

    print(*interprets, sep=", ")

def task4(dsf):
    time = 0
    for medium in node.getElementsByTagName("Medium"):
        if medium.attributes.getNamedItem("typ").value == dsf and not medium.getElementsByTagName("Laufzeit") == []:
            runningTime = medium.getElementsByTagName("Laufzeit")
            time += int(runningTime[0].firstChild.nodeValue)

    print("Die Laufzeit gespeichert in", dsf, "beträgt", str(time) + ".")
            




    


