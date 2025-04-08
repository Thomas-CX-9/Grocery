from random import randint
from os import system
from time import sleep, time
system("clear")
q={
#Unit5 Text1#
"let alone":"People didn't even use video calls any more, ___ ___ paper and pen",
"It turns out that":"__ __ __ __ the piece of paper had been found on the pavement in front of a house owned by Nicholas King, the richest man in Roseshire.",
"Thanks to":"__ __ robotics engineering, humans no longer had to perform dangerous or tedious tasks in 2050.",
"give away":"He didn't want to __ __ more than he had to.",
"lose marbles":"Lane wondered if the 90-year-old tycoon had finally __ his __, even though better diets and medical care had redefined the concept of aging.",
"smell a rat":"'I __ __ __,'King said uneasily",
"watch over":"Who will be __ __ me while you're waiting for the results?",
"What's even better":"__ __ __, electric cars and planes have made the world a greener place.",
("tedious","adj"):["1. boring, not interesting","2. POS"],
("typcoon","n"):["1. a person who has succeeded in business or industry and has become","2. POS"],
("agile","adj"):["1. able to move your body quickly and easily","2. POS"],
("indignantly","adv"):["1. in an angry way, because of sth that is wrong or not fair","2. POS"],
("confront","v"):["1. to face, meet, or deal with a difficult situation or person","2. POS"],
("affection","n"):["1. a feeling of liking for a person or place","2. POS"],
("persuade","v"):["1. to make sb do something by giving them good reasons for doing it","2. POS"],
("contently","adv"):["1. show content or satisfication","2. POS"],
#Unit 5 Text2#
"at one's fingertips":"Boundaries between virtual and physical worlds are blurred by digital experiences such as augmented reality; and instant access to infinite knowledge is __ __ __.",
"drift apart":"People will eventually __ __ because they no longer share any real-life experiences together.",
"take over":"Social networking is also __ __ real-life social interactions, which are essential for developing empathy, understanding body language and learning about 15 taking turns in conversations.",
"distract from":"Incessant incoming messages and notifications __ us __ more important things in life.",
"take a toll on":"Leading a tech-dominated life is also __ __ __ __ our health.",
"result from":"Mindy's 'text claw, __ __ prolonge periods of time curling her fingers around he smartphone, is unsettling.",
"get on":"technology should do the hard work so that you can __ __ and live your life!",
("radically","adv"):["1. completely or extremely","2. POS"],
("hinder","v"):["1. to limit the ability of sb to do sth, or to limit the development of sth","2. POS"],
("unprecedented","adj"):["1. never having happened or existed in the past","2. POS"],
("concern","n"):["1. a worried or nervous feeling about sth","2. POS"],
("incessant","adj"):["1. never stopping especially in an annoying or unpleasant way","2. POS"],
("accomplish","v"):["1. to finish something","2. POS"],
("exterminate","v"):["1. to kill or destory sb/sth completely","2. POS"],
("outlandish","adj"):["1. strange and unusual and difficult to accept or like","2. POS"],
#Unit6 Text1#
"teem with":"Once vibrantly coloured and __ __ life, many coral reefs around the world now line the shorelines as lifeless skeletons.",
"made up of":"Coral reefs are __ __ __ hundreds and sometimes thousands of tiny colourless creatures called polyps.",
"bring about":"However, overfishing, pollution from household waste and rising sea temperatures __ __ by global warming are putting the corals under great stress.",
"the tip of the iceberg":"Unfortunately, the loss of colour in coral reefs is just __ __ __ __ __.",
"give a boost":"Scientists experimenting with different methods to __ coral reefs __ much needed __.",
"without its risk":"However, interfering with nature isn't __ __ __.",
"serve no purpose":"It __ __ __ to regretfully lament I wish we had done more to save the coral reefs' when they're all dead and gone.",
("marine","adj"):["1. related to the sea","2. POS"],
("vibrantly","adv"):["1. in a way that is full of enthusiasm","2. POS"],
("starve","v"):["1. to (cause someone to) become very weak or die because there is no enough food to eat","2. POS"],
("trigger","v"):["1. to cause something to start","2. POS"],
("vulnerable","adj"):["1. able to be easily physically, emotionally, or mentally hurt, influenced, or attacked","2. POS"],
("restore","v"):["1. to return something to an good condition or position","2. POS"],
("species","n"):["1. a set of animals or plants in which the members have similar characteristics to each other","2. POS"],
("lament","v"):["1. to express sadness and feeling sorry about something","2. POS"],
#Unit6 Text2#
"entangled in":"Many marine creatures, such as whales, turtles and seabirds, have died from ingesting pieces of plastic or getting __ __ abandoned fishing nets.",
"every corner of the planet":"Microplastics can already be found in __ __ __ __ __, from the highest summit to the deepest oceans.",
"wean from":"Environmentalists and scientists around the world are also experimenting with a variety of other solutions to __ us __ our plastic reliance.",
"remain to be seen":"Whether the SoluBag will help the Earth reclaim some of its clean water sources lost to plastic waste __ __ __ __.",
"make an effort to":"The fashion industry is __ __ __ __ reduce plastic waste as well.",
"branch out into":"So far, Rothy's have repurposed around 12 million water bottles and have begun __ __ __ other sustainable fashion accessories.",
"derive from":"Elsewhere, Australian company Team Timbuktu is producing activewear out of a new fabric __ __ recycled plastic bottles.",
("complicated","adj"):["1. involving a lot of different parts, in a way that is difficult to understand","2. POS"],
("equivalent","adj"):["1. having the same amount, value, purpose, qualities, etc.","2. POS"],
("drift","v"):["1. to move slowly, especially as a result of outside force, with no control over direction","2. POS"],
("rapidly","adv"):["1. in a fast way","2. POS"],
("reliance","n"):["1. the state of dependent on something or someone","2. POS"],
("repurpose","v"):["1. to find a new use for an idea, product, or building","2. POS"],
("permeate","v"):["1. to spread through something and be present in every part of it","2. POS"],
("gravity","n"):["1. seriousness","2. POS"]
}
#key of dict q
keys=[
#U5 T1#
"let alone",
"It turns out that",
"Thanks to",
"give away",
"lose marbles",
"smell a rat",
"watch over",
"What's even better",
("tedious","adj"),
("typcoon","n"),
("agile","adj"),
("indignantly","adv"),
("confront","v"),
("affection","n"),
("persuade","v"),
("contently","adv"),
#U5 T2#
"at one's fingertips",
"drift apart",
"take over",
"distract from",
"take a toll on",
"result from",
"get on",
("radically","adv"),
("hinder","v"),
("unprecedented","adj"),
("concern","n"),
("incessant","adj"),
("accomplish","v"),
("exterminate","v"),
("outlandish","adj"),
#U6 T1#
"teem with",
"made up of",
"bring about",
"the tip of the iceberg",
"give a boost",
"without its risk",
"serve no purpose",
("marine","adj"),
("vibrantly","adv"),
("starve","v"),
("trigger","v"),
("vulnerable","adj"),
("restore","v"),
("species","n"),
("lament","v"),
#U6 T2#
"entangled in",
"every corner of the planet",
"wean from",
"remain to be seen",
"make an effort to",
"branch out into",
"derive from",
("complicated","adj"),
("equivalent","adj"),
("drift","v"),
("rapidly","adv"),
("reliance","n"),
("repurpose","v"),
("permeate","v"),
("gravity","n")
]
num=list(range(len(keys)))
score=0
st=time()
dt=0
Qnum=1
while num!=[]:
    randnum=num[randint(0,len(num)-1)]
    ask=q[keys[randnum]]
    if isinstance(ask, list):
        temp=ask
        temp_score=0
        for i in range(len(ask)):
            ask=temp[i]
            ans=input(str(Qnum)+". "+ask+"\n")
            if ans==keys[randnum][i]:
                print(f"T({i+1}/{len(temp)})")
                temp_score+=0.5
                sleep(1)
                dt+=1
                system("clear")
            else:
                temp_score=0
                print(keys[randnum][i])
                break
        if temp_score==0:
            break
        else:
            score+=temp_score
            temp_score=0
            num.remove(randnum)
            Qnum+=1
    else:
        ans=input(str(Qnum)+". "+ask+"\n")
        if ans==keys[randnum]:
                print("T")
                num.remove(randnum)
                score+=1
                sleep(1)
                dt+=1
                system("clear")
                Qnum+=1
        else:
            print(keys[randnum])
            break
print(f"ended, score:{int(score)}/{len(keys)}")
dt+=time()-st
print(f"{dt}({int(dt//60)}:{round(dt%60)})")
