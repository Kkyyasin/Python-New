#regex modulu
import  re
cumle="türkiyeyi mustafa kemal atatürk kurdu"
patern="türk"
print(re.search(patern,cumle))
print(re.search(patern,cumle).span())
print(re.search(patern,cumle).start())
print(re.search(patern,cumle).end())
print(re.search(patern,cumle).group(),end="\n\n")
for eslesme in re.findall(patern,cumle):#string ifade olarak alır
    print(eslesme)
for eslesme in re.finditer(patern,cumle):#obje olarak alır
    print(eslesme.span(),eslesme.group())
#Dinamik kullanım
#\d rakam base42== base\d\d
#\w karekter mer==\w\w\w
#\s bosluk mer mer== mer\smer
#\Drakam değil
#\W karekter değil
#\S bosluk değil
cumle1="benim telefon numaram 0551-1667710"
patern=r"\d\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern,cumle1))
print(re.search(patern,cumle1).group())
print(re.search(patern,cumle1).span())
patern="\s"
print(re.search(patern,cumle).span())#bosluk bulır
######## Ifade ####### Aciklama ######## Örnek ############# Patern ############
####### ---------------------------------------------------------------- #######
#######  {5}   ########  adet  #######  aaaaa  #########    \w{5}     ##########
#######  {3,4} #######   veya  #######   abc  ##########   \w{3,4}     #########
#######  {2,}  ########  en az  ##### 198721321 ########    \d{2,}     #########
#######    *   ###  0 ya da fazla #######  x  ##########     \w*        ########
#######    +   ### 1 ya da fazla ######  Ahmet1  #######    \w+\d+     #########
#######    ?   #####  ya 1 ya hic ####### Mura #########     Murat?       ######
####### --------------------------------------------------------------- ########
################################################################################
patern="\d{3,4}-\d{7}"
print(re.search(patern,cumle1).span())
print(re.search(patern,cumle1).group())
patern="\s\w*|\w*\s"
for eslesme in re.finditer(patern,cumle):
    print(eslesme.span(),eslesme.group())
def gsm_bul(cumle):
    patern="(\d{3})-(\d{7})"
    num=re.search(patern,cumle)
    if num:
        if num[0].startswith("54"):
            return "Vodofone"
        elif num[0].startswith("505") or num[0].startswith("501") or num[0].startswith("506"):
            return "Avea"
        elif num[0].startswith("53"):
            return "Turkcell"
        else:
            return "Şebeke bulunamadı"
    else:
        return "patern bulunamadi"
cumle2="benim telefon numaram 0535-1667710"
print(gsm_bul(cumle2))
######## Ifade ####### Aciklama ######## Örnek ############# Patern ############
####### ---------------------------------------------------------------- #######
#######    |   ########  veya  #######  slm  #########    selam|slm   ##########
#######    ^    ####### baslar  #######  Ahmet  ##########   ^\w+      #########
#######    $   ########  biter   ##### base42   ########     \d$       #########
#######    .   ######  herhangi  #####  abcdef  ########      .*       #########
#######    \   ########  esc     #####  (not)   ########   \(\w{3}\)   #########
####### --------------------------------------------------------------- ########
################################################################################
patern=r"(slm)|(selam)|(merhaba)"
cumleler=["selam efendim","yasin bey merhaba","naber usta","slm usta"]
for cumlee in cumleler:
    a=re.search(patern,cumlee)
    if a:
        print(a.span(),a.group())
patern="^\d+"
cumle="15aa"#sayıyla basladığını ifade ediyor
print(re.search(patern,cumle))
cumle="a4aa5"
patern="^\w+"#karekterle basladığını ifade eder
print(re.search(patern,cumle))
patern="\w*$"
print(re.search(patern,cumle))#neyle bittiği soylenir

