# Pilotní řešení řízených slovníků/taxonomií pro Národní repozitář – dokumentace
Seznam taxonomií je [na GitHubu](https://github.com/Narodni-repozitar/nr-vocabularies/tree/main/nr_vocabularies/fixtures)

## Obsah
### [Access-Rights](#acccess-rights) 
### [Community-Types](#community-types) 
### [Contributor-Types](#contributor-types) 
### [Countries](#countries) 
### [Degree-Grantors](#degree-grantors) 
### [Funders](#funders) 
### [Institutions](#institutions) 
### [Item-Relation-Types](#item-relation-types) 
### [Languages](#languages) 
### [Resource-Types](#resource-types) 
### [Rights (dříve Licenses)](#rights) 
### [Subject-Categories](#subject-categories) 
### [Přehled struktury jednotlivých slovníků/taxonomií](#struktura-taxonomii)

### Obecné informace
Slovníky pro Národní repozitář (dále NR) byly původně připraveny v roce 2020, a to pouze pro jeho dokumentovou část. 
V trochu pozměněné podobě byly použity pro pilotní datový repozitář v roce 2021. Na konci roku 2021 vyšla nová verze Invenia 3.5, 
která výrazně ovlivnila i podobu slovníků. Tato verze byla vývojáři NR aplikována na začátku roku 2022. 
Slovníky bylo třeba upravit, a to z těchto důvodů:
1.	Bylo třeba, aby stejné položky v různých slovnících byly stejného typu.
2.	Slovníky v rámci Invenia 3 nedovolují hierarchické uspořádání (kromě afiliací).

První problém byl odstraněn sjednocením názvů záhlaví, jejich přejmenováním. Při úpravách názvů záhlaví jsme se snažili vycházet 
z modelu pro slovníky v Inveniu 3. Některé položky (sloupce) byly vypuštěny jako zbytečné.

Druhý problém byl řešen na koncepční schůzce s vývojáři a bylo rozhodnuto, že pro slovníky si vytvoříme vlastní model, 
aby hierarchické uspořádání bylo možné vždy, když je potřeba.

Diskutován byl také problém slugů (id), zda je vhodnější, aby zůstaly jako písmenné stringy nebo by měly být vyjádřené ve formě id kódu. 
Zatím zůstávají stringy, které vychází buď z názvu (title_cs/title_en) s pomlčkami nebo se jedná o převzaté numerické, 
alfabetické nebo alfanumerické kódy z původních třídění a řízených slovníků (identifikátory jednotlivých položek).

Při definování slovníku byla zohledňována existence relevantních (mezinárodních) slovníků vhodných pro repozitáře. 
Vycházelo se z praxe NUŠL, pokynů OpenAIRE, slovníků od COAR, pokynů od DataCite (agentury přidělující DOI převážně datům 
a šedé literatuře) a dalších.

Další úprava struktury slovníků byla provedena na přelomu let 2023 a 2024, opět došlo ke změně struktury 
a slovníky byly také zaktualizovány podle nové verze schématu DataCite 4.5 z března 2024, která obsahuje i obsah řízených slovníků, 
ze kterých některé slovníky NR přebírají hodnoty. V roce 2024 by tuto verzi slovníků měla začít využívat i datová část NR.


## <a name="acccess-rights"></a>Access-Rights
Úrovně přístupu k plným textům (dokumentům, souborům) pro koncového uživatele, nerozlišuje se kde, tj. ať už přímo 
v prohlíženém zdroji nebo v jiném, z kterého byl záznam sklizen. Jedná se o aplikaci slovníku COAR (Coalition for OA repositories), 
tedy slovníku vytvořeného přímo pro potřeby repozitářů. Pro účely Národního repozitáře byl tento slovník rozšířen o české překlady. 
Zároveň byl v roce 2020 do COAR zaslán požadavek o publikování překladu do češtiny, zatím tento požadavek nebyl zpracován.

Stejný slovník využívá i OpenAIRE, mělo by tedy být usnadněné mapování z NR do OpenAIRE. 
Tato úprava slovníku obsahuje český a anglický termín a URI COAR slovníku.

[Dokumentace COAR slovníku](http://vocabularies.coar-repositories.org/documentation/access_rights/) \
[Slovník v RDF z github](https://github.com/coar-repositories/vocabularies/tree/master/access_rights)

Hodnoty: 
- open access
  - cz: otevřený přístup
  - Volně dostupný dokument.


- embargoed access
  - cz: odložené zpřístupnění
  - Odložený přístup definovaný datem, po jehož uplynutí se soubory zveřejní. Většinou se týká akademických článků, 
  kde vydavatel umožňuje autorovi volně zpřístupnit článek až po určité době. Po vypršení stanoveného času se práva 
  změní na open access.
 

- restricted access
  - cz: omezený přístup
  - Dokument je přístupný pouze vybrané skupině uživatelů (např. zaměstnancům a studentům univerzity) nebo za určitých 
  podmínek (např. registrace do systému); většinou se jedná o omezený přístup pro zaměstnance konkrétní instituce; 
  přístup může být udělen po přihlášení, registraci nebo žádosti přes email.


- metadata only access
  - cz: pouze metadata
  - Neexistuje elektronický soubor nebo není veřejně dostupný. V podstatě pokud nelze použít nějakou možnost výše, 
  tak bude užita tato možnost. 
  - Bude se týkat převážně tištěných dokumentů nebo dokumentů vyloučených ze zveřejnění 
  (např. z důvodu patentového řízení nebo ochrany osobních údajů).


## <a name="community-types"></a>Community-Types
Jednoduchý slovník pro odlišení typů komunit.


## <a name="contributor-types"></a>Contributor-Types
Jedná se o slovník hodnot, kterých může nabývat role přispěvatele.

Náš slovník je kombinací výběru položek z těchto schémat/seznamů: DataCite, MARC21 a EVSKP-MS. 
Výběr probíhal na základě praxe s existujícími daty v NUŠL a užití v jiných repozitářích. 

**DataCite** posloužil jako základ a většina termínů byla převzata. Vyřazeny byly takové, které prozatím nenajdou 
v repozitáři využití. Kompletní DataCite slovník převzal OpenAIRE. Pro předávání dat do OpenAIRE budou hodnoty převzaté 
z jiných systémů nahrazeny hodnotou „Other“, která je součástí slovníku DataCite. 
Definice hodnot v DataCite jsou dostupné [v Apendixu 1](https://schema.datacite.org/meta/kernel-4.4/doc/DataCite-MetadataKernel_v4.4.pdf), 
nemají však trvalé identifikátory jako slovníky COAR.

| **Popis**              | **Kód v MARC** |
|------------------------|:--------------:|
| ContactPerson          |                |
| DataCollector          |                |
| DataCurator            |                |
| DataManager            |                |
| Distributor            |      dst       |
| Editor                 |      edt       |
| Producer               |      pro       |
| ProjectLeader          |      rth       |
| ProjectManager         |                |
| ProjectMember          |      rtm       |
| Researcher             |      res       |
| ResearchGroup          |                |
| RightsHolder           |      asg       |
| Supervisor             |                |
| hosting institution    |                |
| registration agency    |                |
| registration authority |                |
| related person         |                |
| sponsor                |      spn       |
| work package leader    |      rth       |
| consultant             |      csl       |
| other                  |      oth       |

Z **EVŠKP-M** byl převzat termín advisor a referee (vedoucí a oponent práce) [více zde](http://www.evskp.cz/standardy/evskp/#_Toc203923576). 
Definice Supervisora v DataCite by nezahrnula i roli vedoucího práce, přestože se tento termín často užívá, 
a roli oponenta neobsahuje vůbec. Z těchto důvodů byly obě hodnoty převzaty z evškp-ms.

| **Popis** | **Kód v MARC** |
|-----------|:--------------:|
| Referee   |      opn       |
| Advisor   |      ths       |

**MARC 21** obsahuje velmi obsáhlý seznam kódů rolí tvůrců, který by jako celek pro záběr Národního repozitáře 
pro výstupy VaVaI neměl smysl, jako např. iluminátor rukopisů, dřevorytec apod. Byly tedy vybrány pouze hodnoty 
považované za relevantní. V katalozích (a jejich OAI-PMH) jsou pak zaznamenány třímístné písmenné kódy. 
Kódy a definice jednotlivých rolí v MARC 21 [naleznete zde](https://text.nkp.cz/o-knihovne/odborne-cinnosti/zpracovani-fondu/informativni-materialy/kody-roli) 

| **Popis**        | **Kód v MARC** |
|------------------|:--------------:|
| ilustrátor       |      ill       |
| kurátor výstavy  |      cur       |
| moderátor        |      mod       |
| překladatel      |      trl       |
| fotograf         |      pht       |
| recenzent        |      rev       |
| spolupracovník   |      clb       |
| umělec           |      art       |
| dotazovaný       |      ive       |
| dotazovatel      |      ivr       |
| organizátor akce |      orm       |
| spíkr            |      spk       |
| panelista        |      pan       |
| nakladatel       |      pbl       |
| proofreader      |      pfr       |
| owner            |      own       |
| former owner     |      fmo       |
| respondent       |      rsp       |


## <a name="countries"></a>Countries
Slovník zemí (countries) vychází ze standardu ISO 3166 pro země, obsahuje dvoumístné kódy zemí (ve slugu), 
název země v českém a anglickém jazyce a třímístné kódy zemí. [Seznam zde](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). 
V záznamech v UI repozitáře se zobrazují dvoumístné kódy.


## <a name="degree-grantors"></a>Degree-Grantors
Tento hierarchický slovník vznikl později a byly do něj vybrány pouze vysoké školy a univerzity, přičemž byla zachována 
hierarchie s fakultami, katedrami a ústavy. Užívá ho pouze model pro dokumenty, konkrétně metadatové pole degreeGrantor, 
čili vysoká škola udělující titul.

Obsahuje následující údaje o VŠ, přičemž na úrovni fakult a kateder jsou obvykle vyplněné jen názvy v češtině a angličtině:
- Názvové údaje: 
  - Název instituce, v českém a anglickém jazyce (title_cs a title_en). 
  - Zkratky názvů institucí (acronym).
  - Další známé názvy institucí i organizačních jednotek (nonpreferredLabels v čj a aj).
- URL odkaz na webové stránky instituce.
- Identifikace instituce:
  - ROR, 
  - IČO instituce (bude sloužit jako její identifikátor).
- Pole pro účely technického řešení:
  - „tags_0“ s hodnotou „deprecated“ označující zaniklé instituce, které byly buď zrušené bez náhrady nebo sloučené 
  s jinou institucí pod jiný název. Týká se zejména soukromých vysokých škol.
  - „nameType“ s hodnotou organizational pro rozlišení institucí a osob coby autorů v záznamech, při importech.

## <a name="funders"></a>Funders
Slovník funders (poskytovatelé financí) je vytvořený na míru českému prostředí a Národnímu repozitáři. 
Hodnoty slovníku jsou převzaty zejména z Informačního systému pro výzkum, vývoj a inovace (IS VaVaI), 
doplněni jsou někteří nejčastější poskytovatelé ze zahraničí. Do budoucna se počítá s komplexnějším řešením 
vytěžování databází o financování jako je např. IS VaVaI a OpenAIRE, aby se eliminovalo riziko překlepů a duplicitní 
vyplňování všech údajů o financování VaVaI.

Obsahuje následující informace o poskytovatelích:
- název poskytovatele v češtině a angličtině, popřípadě dalších jazycích,
- předchozí názvy nebo nepreferovaná zkratka názvu instituce (označení záhlaví jako nonpreferredLabels),
- acronym (nejznámější česká zkratka názvu instituce),
- relatedURI (identifikátory ROR a DOI z Crossref)

Slovník se podle potřeby doplňuje novými hodnotami.


## <a name="institutions"></a>Institutions
Slovník institucí evidovaných v Národním repozitáři – jedná se převážně o výzkumné organizace, neziskové organizace, 
muzea, galerie, knihovny apod. Vycházelo se ze seznamu partnerských institucí Národního úložiště šedé literatury, 
slovník tedy obsahuje zejména instituce, poskytující data do NUŠL, včetně zaniklých ústavů AV ČR. Přidány byly instituce, 
které jsou členy EduID a dá se od nich očekávat zájem o ukládání výzkumných dat. Slovník je doplňován dle potřeb uživatelů 
novými položkami. Slovník byl vytvořen pro české prostředí, tvoří ho převážně české instituce. 

Zpočátku se jednalo o hierarchickou taxonomii, která obsahovala nejen celé instituce, ale i jejich organizační jednotky. 
To značně znesnadňovalo údržbu slovníku. Navíc uživatelé často volili afiliaci až na úrovni fakult a kateder, 
což není žádoucí z hlediska indexace a vyhledávání. Proto v roce 2024 vznikla další specifická taxonomie degree-grantors, 
která obsahuje pro potřeby popisu VŠKP pouze vysoké školy a univerzity se zachováním hierarchie (fakulty, katedry atd.) 
a z taxonomie institutions se tedy stal slovník bez hierarchie, který obsahuje pouze organizace (včetně VŠ) na nejvyšší úrovni. 

Obsahuje následující údaje o instituci:
- Názvové údaje: 
  - Název instituce, v českém a anglickém jazyce (title_cs a title_en). 
  - Zkratky názvů institucí (acronym).
  - Další známé názvy institucí i organizačních jednotek (nonpreferredLabels v čj a aj).
- URL odkaz na webové stránky instituce.
- Identifikace instituce:
  - ROR, 
  - IČO instituce (bude sloužit jako její identifikátor).
- Pole pro účely technického řešení:
  - „tags_0“ s hodnotou „deprecated“ označující zaniklé instituce, které byly buď zrušené bez náhrady nebo sloučené 
  s jinou institucí pod jiný název. Týká se zejména soukromých vysokých škol.
  - „nameType“ s hodnotou organizational pro rozlišení institucí a osob coby autorů v záznamech, při importech.


Slovník původně obsahoval také rozřazení institucí do kategorií (galerie, knihovna, VVI, státní VŠ atd.), 
tato kategorizace byla v roce 2024 zrušena jako nevyhovující. S různými typy institucí byla kategorizace čím dál 
nepřesnější a nebyla využívána v UI NR pro fasety či jiný účel. Zrušen byl také identifikátor RID pro VŠ. 
Naopak přidána byla položka tags_0, která slouží pro označení institucí, které už zanikly nebo byly sloučeny 
s jinou institucí (hodnota deprecated).


## <a name="item-relation-types"></a>Item-Relation-Types
Slovník popisuje vztah popisovaného zdroje k připojené jednotce, např. kapitola odkazuje na knihu. 
Do slovníku byly převzaty kompletně hodnoty z [DataCite](https://datacite-metadata-schema.readthedocs.io/en/4.5/). 
Hodnoty jsou podle slovníku a verze schématu DataCite průběžně doplňovány.

Slovník obsahuje název vztahu v češtině a angličtině. Pokud se jedná o párovou vazbu (př. Je verzí/Má verzi), 
je uvedena rovněž párová vazba. Slovník obsahuje také nápovědu pro jednotlivé vazby (příklady jejich užití) 
pro účely budoucího zobrazení uživateli ve vkládacím formuláři v rozhraní repozitáře, pokud to bude technicky možné. 
Nápověda je zatím jen v angličtině, převzatá z dokumentace schématu DataCite


## <a name="languages"></a>Languages
Slovník jazyků vychází ze standardu ISO 639-2 B (určen pro bibliografický popis. K jednomu záznamu lze přiřadit více jazyků. 
[Seznam zde](https://cs.wikipedia.org/wiki/Seznam_k%C3%B3d%C5%AF_ISO_639-2) 

Slovník obsahuje dvoumístné kódy (v id), název jazyka v češtině a angličtině a třímístné kódy jazyka v angličtině 
a v originálním jazyce. V záznamech v UI repozitáře se zobrazují dvoumístné kódy.

Ve slovníku je také zavedena položka tags_0 s hodnotou featured, která označuje jazyky, které se ve vkládacím formuláři 
mají vkladatelům zobrazovat prioritně.


## <a name="resource-types"></a>Resource-Types
Taxonomie resourceType (typ dokumentu) byla vytvořená na míru českému prostředí a Národnímu repozitáři. Taxonomie slouží 
jednak k označení typů dokumentů, přijímaných do Národního repozitáře, ale také k označení typů souvisejícího zdroje 
(relatedItem). Jedná se o další speciální typy zdrojů, jejichž přijímání do Národního repozitáře se zatím neočekává, 
ale bude pravděpodobné, že jejich metadata budou připojována k přijímaným dokumentům coby související zdroje přes pole 
relatedItem.

Při tvorbě položek byly vzaty v potaz Definice druhů výsledků pro IS VaVaI (RIV), 
slovník [Resource Types od COAR](https://vocabularies.coar-repositories.org/resource_types/3.0/) (použitá též v OpenAIRE), 
typologie DataCite Resource Type General, typologie Národního úložiště šedé literatury a obdobné typologie užité 
v jiných repozitářích (ASEP, Zenodo aj.). Cílem bylo dosáhnout co nejvyššího souladu mezi používanými typologiemi, 
proto taxonomie obsahuje rovněž mapování na hodnoty slovníku COAR a DataCite. To by následně mělo usnadnit mapování 
a výměnu dat u datových i dokumentových repozitářů.

Jedná se o hierarchický slovník, proto je označován jako taxonomie. Taxonomie má dvě úrovně a obsahuje termíny v českém 
a anglickém jazyce, v případě potřeby také alternativní označení typů dokumentů (jako např. knihy a monografie) 
obsahuje též mapování na hodnoty slovníku [COAR Resource Types](https://vocabularies.coar-repositories.org/resource_types/) 
(včetně trvalých identifikátorů) a na hodnoty slovníku DataCite Resource Type General.

K odlišení položek, které slouží jako typy přijímaných dokumentů do repozitáře a položek sloužících 
pouze jako typologie souvisejících zdrojů, bylo vytvořeno pole props.submission s hodnotami „true“ 
(přijímané typy dokumentů, zobrazují se ve vkládacím formuláři) nebo „false“ (užívají se pouze k označení typu 
souvisejícího zdroje).


## <a name="rights"></a>Rights (dříve Licenses)
Taxonomie obsahuje licence, které je možné dílům udělit. Zatím se jedná pouze o Creative Commons licence, 
známé pod zkratkou CC licence. Položky bude nutné do budoucna rozšířit o další typy licencí. Vycházeli jsme 
z modelu Zenoda a NUŠL, kde jsou přidělovány rovněž CC licence. Slovník CC licencí je zatím pojatý hierarchicky (proto je opět označován jako taxonomie), aby bylo možné při vyhledávání v repozitáři podle licencí filtrovat výsledky. Na první úrovni je název sady licencí 
(zatím tedy pouze CC). Na druhé úrovni je verze licencí (pro CC 1 – 4). Na třetí úrovni se pak nachází konkrétní licence. 

Teprve nejnižší úroveň nese následující informace:
- název česky a anglicky,
- odkaz do prohlášení k dané licenci CC, které je povinné uvádět, ve struktuře https://creativecommons.org/licenses/by-nc/2.5/,
- kvůli technickému řešení slovník obsahuje také odkaz do obrázku, který by měl následně v záznamech představovat ikonu, 
reprezentující informaci o licenci,
- zkratka licence – užívá se pro zobrazení licencí ve fasetě v UI NR,
- slovní popis typu licence v češtině a angličtině,
- položku tags_0 s hodnotou featured pro prioritní zobrazení licencí ve verzi 4.0.

Více o verzích licencí [zde](https://wiki.creativecommons.org/wiki/License_Versions) 

Celé detailní znění konkrétní licence lze získat přes odkaz s legalcode, který má následující strukturu - 
https://creativecommons.org/licenses/by-nd-nc/1.0/legalcode 

**Poznámka pro užití**
- Udělení licence je nevratné.
- Každé dílo by mělo být publikováno pouze pod jedním typem licencí CC.
- U licence 1.0 jsou u poslední možnosti prohozena písmena oproti jiným verzím. Tj. ve verzi 1.0 je BY-ND-NC, 
ve zbylých verzích je to BY-NC-ND.
- Verze 3 vyšla v národních mutacích, lze ji použít obecně  pro mezinárodní organizace, 
více lze dohledat na wiki creativecommons; v tomto slovníku se prozatím pracuje jen s českou národní verzí, 
s možností pozdějšího rozšíření, pokud to bude potřeba.


## <a name="subject-categories"></a>Subject-Categories
Taxonomie byla vytvořena a zařazena pro potřebu oborové klasifikace zejména datových sad. Byla přejata klasifikace 
Struktura oborů OECD (Frascati manual) jako celek. Jeho základ (první tři úrovně) jsou užívány také jako číselník oborů 
v IS VaVai. Zvažována byla ještě klasifikace, užívána pro systém re3data, vytvořena původně 
v [Deutsche Forschungsgemeinschaft](https://www.dfg.de/en/dfg_profile/statutory_bodies/review_boards/subject_areas/index.jsp), 
nakonec byla ale vybrána obecnější klasifikace FRASCATI, důvodem bylo především užití v IS VaVaI.

Taxonomie obsahuje název předmětové kategorie v angličtině a jeho překlad do češtiny, provedený pracovníky NTK, 
částečně převzatý ze [struktury oborů FORD](https://www.tacr.cz/wp-content/uploads/documents/2019/09/27/1569592365_Struktura_oboru_FORD.pdf).

Třídění a označování datových sad a případně dalších zdrojů pomůže k lepší práci s nimi v rámci systému (poskytování 
specifických oborových popisů) a k lepší a přesnější diseminaci (předávání relevantních záznamů do oborových repozitářů).

K jednomu zdroji/záznamu může být přiřazeno více oborových kategorií.


## <a name="struktura-taxonomii"></a>Přehled struktury jednotlivých taxonomií

### access-rights
| **Název sloupce**  | **Typ hodnoty**                 |
|--------------------|---------------------------------|
| id                 | identifikátor přístupových práv |
| title_cs           | označení práv v češtině         |
| title_en           | označení práv v angličtině      |
| relatedURI_COAR    | COAR PURL                       |

### community-types
| **Název sloupce**       | **Typ hodnoty**    |
|-------------------------|--------------------|
| id                      | id typu komunity   |
| title_cs                | název v češtině    |
| title_en                | název v angličtině |

### contributor-types
| **Název sloupce**   | **Typ hodnoty**                 |
|---------------------|---------------------------------|
| id                  | id role přispěvatele            |
| title_cs            | název v češtině                 |
| title_en            | název v angličtině              |
| props.marcCode      | odpovídající kód v MARC         |
| props.dataCiteCode  | odpovídající hodnota v DataCite |

### countries 
| **Název sloupce** | **Typ hodnoty**     |
|-------------------|---------------------|
| id                | dvoumístný kód země |
| title_cs          | název v češtině     |
| title_en          | název v angličtině  |
| props.alpha3Code  | třímístný kód země  |

### degree-grantors 
| **Název sloupce**         | **Typ hodnoty**                                                      |
|---------------------------|----------------------------------------------------------------------|
| hierarchy_parent          | id mateřské vysoké školy/univerzity                                  |
| id                        | id instituce/organizační jednotky                                    |
| title_cs                  | název v češtině                                                      |
| title_en                  | název v angličtině                                                   |
| tags_0                    | hodnota „deprecated“ označuje zaniklé instituce                      |
| props.acronym             | zkratka názvu instituce/organizační jednotky (Akronym)               |
| props.ICO                 | IČO instituce                                                        |
| relatedURI_ROR            | ROR instituce                                                        |
| relatedURI_URL            | webová stránka organizace                                            |
| props.nameType            | hodnota "organizational" pro rozlišení institucí od osob coby autorů |
| nonpreferredLabels_cs_0-5 | další známé názvy instituce/organizační jednotky v češtině           |
| nonpreferredLabels_en_0-5 | další známé názvy instituce/organizační jednotky v angličtině        |

### funders
| **Název sloupce**           | **Typ hodnoty**                                            |
|-----------------------------|------------------------------------------------------------|
| id                          | id poskytovatele financí                                   |
| title_cs                    | název v češtině                                            |
| title_en                    | název v angličtině                                         |
| onpreferredLables_en_0      | předchozí názvy nebo nepreferovaná zkratka názvu instituce |
| title_fr                    | název ve francouzštině                                     |
| title_sk                    | název ve slovenštině                                       |
| title_pl                    | název v polštině                                           |
| title_de                    | název v němčině                                            |
| props.acronym               | acronym (nejznámější česká zkratka názvu instituce         |
| relatedURI_CrossrefFunderID | DOI z Crossref                                             |
| relatedURI_ROR              | ROR identifikátor                                          |

### institutions
| **Název sloupce**         | **Typ hodnoty**                                                      |
|---------------------------|----------------------------------------------------------------------|
| id                        | id instituce                                                         |
| title_cs                  | název instituce v češtině                                            |
| title_en                  | název instituce v angličtině                                         |
| tags_0                    | hodnota „deprecated“ označuje zaniklé instituce                      |
| props.acronym             | zkratka názvu instituce (Akronym)                                    |
| props.ICO                 | IČO instituce                                                        |
| relatedURI_ROR            | ROR instituce                                                        |
| relatedURI_URL            | webová stránka organizace                                            |
| props.nameType            | hodnota "organizational" pro rozlišení institucí od osob coby autorů |
| nonpreferredLabels_cs_0-5 | další známé názvy instituce v češtině                                |
| nonpreferredLabels_en_0-5 | další známé názvy instituce v angličtině                             |

### item-relation-types
| **Název sloupce** | **Typ hodnoty**                                                   |
|-------------------|-------------------------------------------------------------------|
| id                | identifikátor vztahu                                              |
| title_cs          | název vztahu v češtině                                            |
| title_en          | název vztahu v angličtině                                         |
| props.pair        | identifikátor párového vztahu, který je k tomuto významově opačný |
| hint_en           | vysvětlení vztahu                                                 |

### languages 
| **Název sloupce**      | **Typ hodnoty**                                                                 |
|------------------------|---------------------------------------------------------------------------------|
| id                     | dvoumístný kód jazyka                                                           |
| title_cs               | název v češtině                                                                 |
| title_en               | název v angličtině                                                              |
| props.alpha3CodeENG    | třímístný kód jazyka v angličtině                                               |
| props.alpha3CodeNative | třímístný kód jazyka v originálním jazyce                                       |
| tags_0                 | hodnota "featured" označuje prioritně zobrazované jazyky ve vkládacím formuláři |

### resource-types
| **Název sloupce**       | **Typ hodnoty**                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| hierarchy_parent        | id mateřského typu dokumentu                                                                                          |
| id                      | id typu dokumentu                                                                                                     |
| title_cs                | název v češtině                                                                                                       |
| title_en                | název v angličtině                                                                                                    |
| nonpreferredLables_cs_0 | další známé názvy typu dokumentu v češtině                                                                            |
| onpreferredLables_en_0  | další známé názvy typu dokumentu v angličtině                                                                         |
| props.coarType          | odpovýdající typ dokumentu dle COAR                                                                                   |
| relatedURI_COAR         | COAR PURL                                                                                                             |
| props.dataCiteType      | odpovýdající typ dokumentu dle DataCite                                                                               |
| props.submission        | „true“ (přijímané typy dokumentů, zobrazení ve vkládacím formuláři) nebo „false“ (označení typu souvisejícího zdroje) |

### rights
| **Název sloupce**   | **Typ hodnoty**                                                |
|---------------------|----------------------------------------------------------------|
| id                  | id licence                                                     |
| hierarchy_parent    | id mateřské licence                                            |
| title_cs            | název v češtině                                                |
| title_en            | název v angličtině                                             |
| icon                | odkaz na ikonu licence                                         |
| relatedURI_URL      | odkaz do prohlášení k dané licenci CC, které je povinné uvádět |
| props.acronym       | zkratka licence                                                |
| description_cs      | slovní popis typu licence v češtině                            |
| description_en      | slovní popis typu licence v angličtině                         |
| tags_0              | hodnota "featured" pro prioritní zobrazení licencí (verzi 4.0) |

### subject-categories
| **Název sloupce**       | **Typ hodnoty**       |
|-------------------------|-----------------------|
| hierarchy_parent        | id mateřské kategorie |
| id                      | id kategorie          |
| title_cs                | název v češtině       |
| title_en                | název v angličtině    |
