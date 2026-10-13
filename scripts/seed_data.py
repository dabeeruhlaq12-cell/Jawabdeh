#!/usr/bin/env python3
"""One-time seed: writes data/states.json and data/cities/*.json.
After seeding, edit the JSON files directly; this script is kept as a record of sources."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWED = "2026-10-13"
CH = "https://citizen.complainthub.org/t/"
W = "https://en.wikipedia.org/wiki/"
V, NV = "verified", "needs_verification"


def ch(type_, value, en, hi, status=NV, source=None):
    d = {"type": type_, "value": value, "label_en": en, "label_hi": hi, "status": status}
    if source:
        d["source"] = source
    return d


HELP = ("Citizen helpline", "नागरिक हेल्पलाइन")
TOLL = ("Toll-free helpline", "टोल-फ़्री हेल्पलाइन")
WA = ("WhatsApp complaints", "WhatsApp पर शिकायत")
WEB = ("Online complaint / official website", "ऑनलाइन शिकायत / आधिकारिक वेबसाइट")
SEW = ("Sewer / septic tank", "सीवर / सेप्टिक टैंक")

# ---------------------------------------------------------------- states
STATES = {
 "up": dict(en="Uttar Pradesh", hi="उत्तर प्रदेश", g_en="Jansunwai (IGRS) – UP CM grievance system", g_hi="जनसुनवाई (IGRS) – उ.प्र. मुख्यमंत्री शिकायत प्रणाली",
   ch=[ch("phone","1076","CM Helpline","मुख्यमंत्री हेल्पलाइन",V), ch("web","jansunwai.up.nic.in","Jansunwai portal","जनसुनवाई पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")],
   muni=[ch("phone","1533","Urban local body helpline (all UP cities)","नगर निकाय हेल्पलाइन (उ.प्र. के सभी शहर)",V,CH+"how-can-you-file-civic-complaints-of-kanpur-municipal-corporation-kmc/1787")]),
 "uk": dict(en="Uttarakhand", hi="उत्तराखंड", g_en="Uttarakhand CM Helpline", g_hi="उत्तराखंड मुख्यमंत्री हेल्पलाइन",
   ch=[ch("phone","1905","CM Helpline","मुख्यमंत्री हेल्पलाइन",V,CH+"how-can-i-file-civic-complaints-of-dehradun-municipal-corporation/237"), ch("web","cmhelpline.uk.gov.in","CM Helpline portal","सीएम हेल्पलाइन पोर्टल",V)]),
 "pb": dict(en="Punjab", hi="पंजाब", g_en="Connect Punjab – public grievance system", g_hi="कनेक्ट पंजाब – जन शिकायत प्रणाली",
   ch=[ch("phone","1100","CM Helpline (e-Sewa)","सीएम हेल्पलाइन (ई-सेवा)",NV,CH+"how-can-i-file-complaints-about-government-offices-to-department-of-public-grievance-of-punjab-cm-helpline/1713"), ch("web","connect.punjab.gov.in","Connect Punjab portal","कनेक्ट पंजाब पोर्टल",V)]),
 "ch": dict(en="Chandigarh (UT)", hi="चंडीगढ़ (केंद्र शासित)", g_en="Chandigarh Administration e-grievance / CPGRAMS", g_hi="चंडीगढ़ प्रशासन ई-शिकायत / CPGRAMS",
   ch=[ch("web","eservices.chd.gov.in","UT grievance registration","केंद्र शासित प्रदेश शिकायत पंजीकरण",NV), ch("web","pgportal.gov.in","CPGRAMS (appellate route for MC Chandigarh)","CPGRAMS (नगर निगम की अपील के लिए)",V,CH+"where-can-i-file-civic-complaints-of-chandigarh-municipal-corporation-mcc/1374")]),
 "rj": dict(en="Rajasthan", hi="राजस्थान", g_en="Rajasthan Sampark", g_hi="राजस्थान संपर्क",
   ch=[ch("phone","181","Rajasthan Sampark helpline","राजस्थान संपर्क हेल्पलाइन",V,CH+"how-can-you-file-civic-complaints-of-greater-jaipur-municipal-corporation-jmc/1682"), ch("web","sampark.rajasthan.gov.in","Rajasthan Sampark portal","राजस्थान संपर्क पोर्टल",V)]),
 "mp": dict(en="Madhya Pradesh", hi="मध्य प्रदेश", g_en="MP CM Helpline (Jan Setu)", g_hi="मुख्यमंत्री हेल्पलाइन (जन सेतु)",
   ch=[ch("phone","181","CM Helpline","सीएम हेल्पलाइन",V), ch("web","cmhelpline.mp.gov.in","CM Helpline portal","सीएम हेल्पलाइन पोर्टल",V)]),
 "cg": dict(en="Chhattisgarh", hi="छत्तीसगढ़", g_en="Jan Shikayat – CG public grievance system", g_hi="जन शिकायत – छ.ग. लोक शिकायत प्रणाली",
   ch=[ch("web","janshikayat.cg.nic.in","Jan Shikayat portal","जन शिकायत पोर्टल",V,CH+"how-can-i-file-complaints-about-government-offices-to-public-grievance-redressal-department-jan-shikayat-chhattisgarh/1585"), ch("phone","1100","Grievance helpline","शिकायत हेल्पलाइन",NV)]),
 "mh": dict(en="Maharashtra", hi="महाराष्ट्र", g_en="Aaple Sarkar – Maharashtra grievance system", g_hi="आपले सरकार – महाराष्ट्र शिकायत प्रणाली",
   ch=[ch("web","grievances.maharashtra.gov.in","Aaple Sarkar grievance portal","आपले सरकार शिकायत पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
 "gj": dict(en="Gujarat", hi="गुजरात", g_en="Gujarat CMO Samadhan", g_hi="गुजरात सीएमओ समाधान",
   ch=[ch("web","cmogujarat.gov.in/en/write-to-cmo","Write to CMO (Samadhan)","सीएमओ को लिखें (समाधान)",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
 "br": dict(en="Bihar", hi="बिहार", g_en="Bihar Lok Shikayat (Right to Public Grievance Redressal)", g_hi="बिहार लोक शिकायत (लोक शिकायत निवारण अधिकार)",
   ch=[ch("web","lokshikayat.bihar.gov.in","Lok Shikayat portal","लोक शिकायत पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")],
   note_en="Under Bihar's public grievance law the officer must give a hearing and a written decision within a fixed time.",
   note_hi="बिहार के लोक शिकायत क़ानून के तहत अधिकारी को तय समय में सुनवाई कर लिखित फ़ैसला देना होता है।"),
 "jh": dict(en="Jharkhand", hi="झारखंड", g_en="Jharkhand CMO grievance", g_hi="झारखंड मुख्यमंत्री कार्यालय शिकायत",
   ch=[ch("web","cm.jharkhand.gov.in","CMO Jharkhand grievance","मुख्यमंत्री कार्यालय शिकायत",NV), ch("phone","181","CM Jansamvad helpline","सीएम जनसंवाद हेल्पलाइन",NV)]),
 "od": dict(en="Odisha", hi="ओडिशा", g_en="Jana Sunani – Odisha grievance system", g_hi="जन सुनानी – ओडिशा शिकायत प्रणाली",
   ch=[ch("web","janasunani.odisha.gov.in","Jana Sunani portal","जन सुनानी पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
 "as": dict(en="Assam", hi="असम", g_en="Assam CM Grievance Cell", g_hi="असम मुख्यमंत्री शिकायत प्रकोष्ठ",
   ch=[ch("web","cm.assam.gov.in/write-to-cm","Write to the CM","मुख्यमंत्री को लिखें",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
 "tn": dict(en="Tamil Nadu", hi="तमिलनाडु", g_en="Tamil Nadu CM Helpline", g_hi="तमिलनाडु मुख्यमंत्री हेल्पलाइन",
   ch=[ch("phone","1100","CM Helpline","सीएम हेल्पलाइन",V), ch("web","cmhelpline.tnega.org","CM Helpline portal","सीएम हेल्पलाइन पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
 "ka": dict(en="Karnataka", hi="कर्नाटक", g_en="Janaspandana IPGRS – Karnataka", g_hi="जनस्पंदन IPGRS – कर्नाटक",
   ch=[ch("web","ipgrs.karnataka.gov.in","Janaspandana portal","जनस्पंदन पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104"), ch("phone","1902","Janaspandana helpline","जनस्पंदन हेल्पलाइन",NV)]),
 "ap": dict(en="Andhra Pradesh", hi="आंध्र प्रदेश", g_en="AP Public Grievance Redressal System (PGRS)", g_hi="आं.प्र. लोक शिकायत निवारण प्रणाली (PGRS)",
   ch=[ch("web","pgrs.ap.gov.in","PGRS portal","PGRS पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104"), ch("phone","1100","State call centre","राज्य कॉल सेंटर",NV,"https://www.indiacustomercare.com/vijayawada-municipal-corporation-contact-no")]),
 "kl": dict(en="Kerala", hi="केरल", g_en="Kerala CM's Public Grievance Redressal Cell", g_hi="केरल मुख्यमंत्री लोक शिकायत निवारण प्रकोष्ठ",
   ch=[ch("web","complaints.cmo.kerala.gov.in","CMO grievance portal","मुख्यमंत्री कार्यालय शिकायत पोर्टल",V,CH+"where-can-you-file-complaints-against-government-offices-departments-and-public-services/104")]),
}

# ---------------------------------------------------------------- cities
def city(id_, en, hi, state, muni_en, channels, discom, mps, mlas, *, mla_status=V, mla_src=None,
         escalation=None, website=None, extra=None, note_en=None, note_hi=None, mla_note_en=None, mla_note_hi=None):
    d = {"id": id_, "name_en": en, "name_hi": hi, "state": state, "last_reviewed": REVIEWED,
         "municipal": {"name_en": muni_en, "name_hi": f"{hi} नगर निगम", "channels": channels},
         "discom": {"name_en": discom},
         "reps": {"mps": [{"name": n, "seat": s} for n, s in mps],
                  "mlas": [{"seat": s, "name": n} for s, n in mlas],
                  "mla_status": mla_status}}
    if website: d["municipal"]["channels"].append(ch("web", website, *WEB, V))
    if escalation: d["municipal"]["escalation"] = escalation
    if mla_src: d["reps"]["mla_source"] = mla_src
    if mla_note_en: d["reps"]["mla_note_en"], d["reps"]["mla_note_hi"] = mla_note_en, mla_note_hi
    if note_en: d["note_en"], d["note_hi"] = note_en, note_hi
    if extra: d.update(extra)
    return d

C = []
s = CH+"where-can-i-file-civic-complaints-to-lucknow-municipal-corporation-lmc/1417"
C.append(city("lucknow","Lucknow","लखनऊ","up","Lucknow Nagar Nigam",
  [ch("phone","1533",*TOLL,V,s), ch("phone","9219902911",*WA,NV,s), ch("web","lucknow.everythingcivic.com","Lucknow Nagar Nigam 311 (online complaint)","लखनऊ नगर निगम 311 (ऑनलाइन शिकायत)",NV,s)],
  "Madhyanchal Vidyut Vitran Nigam (MVVNL)", [("Rajnath Singh","Lucknow")],
  [("Lucknow West","Armaan Khan"),("Lucknow North","Neeraj Bora"),("Lucknow East","O. P. Srivastava"),("Lucknow Central","Ravidas Mehrotra"),("Lucknow Cantt.","Brajesh Pathak")],
  mla_src=W+"Lucknow_Lok_Sabha_constituency", website="lmc.up.nic.in",
  escalation="Municipal Commissioner, Public Grievance Cell, Lucknow Nagar Nigam, Trilokinath Road, Lalbagh, Lucknow 226001"))
s = CH+"how-can-you-file-civic-complaints-of-kanpur-municipal-corporation-kmc/1787"
C.append(city("kanpur","Kanpur","कानपुर","up","Kanpur Nagar Nigam",
  [ch("phone","1533",*TOLL,V,s), ch("phone","18001805124","Toll-free general complaints","टोल-फ़्री सामान्य शिकायत",NV,s), ch("phone","18001805159","Garbage collection","कचरा उठान",NV,s), ch("web","online.kanpursmartcity.org","Online grievance system","ऑनलाइन शिकायत प्रणाली",NV,s)],
  "KESCo (Kanpur Electricity Supply Company)", [("Ramesh Awasthi","Kanpur")],
  [("Govind Nagar","Surendra Maithani"),("Sishamau","Naseem Solanki"),("Arya Nagar","Amitabh Bajpai"),("Kidwai Nagar","Mahesh Trivedi"),("Kanpur Cantt.","Mohammad Hassan Roomi")],
  mla_src=W+"Kanpur_Lok_Sabha_constituency", website="kmc.up.nic.in",
  escalation="Municipal Commissioner, Public Grievance Cell, Kanpur Nagar Nigam, Moti Jheel, Harsh Nagar, Kanpur 208002"))
s = CH+"how-can-i-file-civic-complaints-of-varanasi-nagar-nigam/1781"
C.append(city("varanasi","Varanasi","वाराणसी","up","Varanasi Nagar Nigam",
  [ch("phone","1533",*TOLL,V,s), ch("phone","18001805567",*TOLL,NV,s), ch("phone","05422720005","Complaint registration","शिकायत दर्ज",NV,s)],
  "Purvanchal Vidyut Vitran Nigam (PuVVNL)", [("Narendra Modi","Varanasi")],
  [("Varanasi North","Ravindra Jaiswal"),("Varanasi South","Neelkanth Tiwari"),("Varanasi Cantt.","Saurabh Srivastava")],
  mla_src=W+"Varanasi_Lok_Sabha_constituency", website="nnvns.org.in",
  escalation="Public Grievance Cell, Varanasi Nagar Nigam, Sigra, Varanasi 221002"))
s = CH+"where-can-i-file-civic-complaints-of-agra-municipal-corporation-amc/1789"
C.append(city("agra","Agra","आगरा","up","Agra Nagar Nigam",
  [ch("phone","1533",*TOLL,V,s), ch("phone","18004197788",*TOLL,NV,s), ch("phone","18001803580","Streetlights","स्ट्रीटलाइट",NV,s), ch("phone","14420",*SEW,NV,s)],
  "Torrent Power (Agra city distribution franchise)", [("S. P. Singh Baghel","Agra")],
  [("Agra Cantt.","Girraj Singh Dharmesh"),("Agra South","Yogendra Upadhyaya"),("Agra North","Purshottam Khandelwal")],
  mla_src=W+"Agra_Lok_Sabha_constituency", website="nagarnigamagra.com",
  escalation="Municipal Commissioner, Agra Nagar Nigam, M.G. Road, Sanjay Place, Agra 282002"))
s = CH+"how-can-i-file-civic-complaints-of-dehradun-municipal-corporation/237"
C.append(city("dehradun","Dehradun","देहरादून","uk","Dehradun Nagar Nigam",
  [ch("phone","18001802525",*TOLL,NV,s), ch("phone","01352714074",*HELP,NV,s)],
  "Uttarakhand Power Corporation (UPCL)", [("Mala Rajya Laxmi Shah","Tehri Garhwal"),("Trivendra Singh Rawat","Haridwar (part of city)")],
  [("Rajpur Road","Khajan Dass"),("Dehradun Cantt.","Savita Kapoor"),("Raipur","Umesh Sharma 'Kau'"),("Mussoorie","Ganesh Joshi")],
  mla_src=W+"Tehri_Garhwal_Lok_Sabha_constituency", website="nagarnigamdehradun.com",
  escalation="Municipal Commissioner, Public Grievance Cell, Nagar Nigam Dehradun, near Doon Hospital, Race Course, Dehradun 248001",
  extra={"water": {"name_en":"Uttarakhand Jal Sansthan","name_hi":"उत्तराखंड जल संस्थान","channels":[ch("phone","18001804100","Drinking water & sewerage","पेयजल और सीवरेज",NV,s)]}},
  mla_note_en="Dharampur and other southern parts of the city fall in Haridwar Lok Sabha.", mla_note_hi="धरमपुर और शहर के दक्षिणी हिस्से हरिद्वार लोकसभा में आते हैं।"))
s = CH+"where-can-i-file-civic-complaints-of-chandigarh-municipal-corporation-mcc/1374"
C.append(city("chandigarh","Chandigarh","चंडीगढ़","ch","Municipal Corporation Chandigarh",
  [ch("phone","01722787200",*HELP,NV,s)],
  "Chandigarh Power Distribution Ltd", [("Manish Tewari","Chandigarh")], [],
  mla_status="none", website="mcchandigarh.gov.in",
  escalation="Municipal Commissioner Cell, Municipal Corporation, Sector 17, Chandigarh",
  mla_note_en="Chandigarh is a Union Territory with no legislative assembly, so there are no MLAs. Escalate to the UT Administration or the MP.",
  mla_note_hi="चंडीगढ़ केंद्र शासित प्रदेश है, यहाँ विधानसभा नहीं है, इसलिए विधायक नहीं हैं। प्रशासन या सांसद तक शिकायत ले जाएँ।"))
C.append(city("ludhiana","Ludhiana","लुधियाना","pb","Municipal Corporation Ludhiana",
  [ch("web","mcludhiana.gov.in",*WEB)], "Punjab State Power Corporation (PSPCL)", [("Amrinder Singh Raja Warring","Ludhiana")],
  [("Ludhiana East","Daljit Singh Grewal"),("Ludhiana South","Rajinder Pal Kaur Chhina"),("Atam Nagar","Kulwant Singh Sidhu"),("Ludhiana Central","Ashok Prashar Pappi"),("Ludhiana West","Sanjeev Arora"),("Ludhiana North","Madan Lal Bagga")],
  mla_src=W+"Ludhiana_Lok_Sabha_constituency",
  note_en="A verified municipal helpline for Ludhiana has not been added yet. Use the Connect Punjab portal meanwhile.", note_hi="लुधियाना नगर निगम की पुष्ट हेल्पलाइन अभी नहीं जोड़ी गई है। तब तक कनेक्ट पंजाब पोर्टल का उपयोग करें।"))
s = CH+"how-can-you-file-civic-complaints-of-greater-jaipur-municipal-corporation-jmc/1682"
C.append(city("jaipur","Jaipur","जयपुर","rj","Nagar Nigam Jaipur",
  [ch("phone","01412747400",*HELP,NV,s), ch("phone","01412742900","Control room","कंट्रोल रूम",NV,s), ch("phone","14420",*SEW,NV,s), ch("web","samadhan.jaipurmc.org","Online complaint","ऑनलाइन शिकायत",NV,s)],
  "Jaipur Vidyut Vitran Nigam (JVVNL)", [("Manju Sharma","Jaipur")],
  [("Hawa Mahal","Balmukund Acharya"),("Vidhyadhar Nagar","Diya Kumari"),("Civil Lines","Gopal Sharma"),("Kishanpole","Aminuddin Kagzi"),("Adarsh Nagar","Rafeek Khan"),("Malviya Nagar","Kali Charan Saraf"),("Sanganer","Bhajan Lal Sharma")],
  mla_src=W+"Jaipur_Lok_Sabha_constituency", website="jaipurmc.org"))
C.append(city("jodhpur","Jodhpur","जोधपुर","rj","Nagar Nigam Jodhpur",
  [], "Jodhpur Vidyut Vitran Nigam (JdVVNL)", [("Gajendra Singh Shekhawat","Jodhpur")],
  [("Sardarpura","Ashok Gehlot"),("Jodhpur","Atul Bhansali"),("Soorsagar","Devendra Joshi")],
  mla_src=W+"Jodhpur_Lok_Sabha_constituency",
  note_en="A verified municipal helpline for Jodhpur has not been added yet. Rajasthan Sampark (181) accepts municipal complaints.", note_hi="जोधपुर नगर निगम की पुष्ट हेल्पलाइन अभी नहीं जोड़ी गई है। राजस्थान संपर्क (181) पर नगर निगम की शिकायत दर्ज होती है।"))
C.append(city("udaipur","Udaipur","उदयपुर","rj","Nagar Nigam Udaipur",
  [], "Ajmer Vidyut Vitran Nigam (AVVNL)", [("Manna Lal Rawat","Udaipur")],
  [("Udaipur","Tarachand Jain"),("Udaipur Rural","Phool Singh Meena")],
  mla_src=W+"Udaipur_Lok_Sabha_constituency",
  note_en="A verified municipal helpline for Udaipur has not been added yet. Rajasthan Sampark (181) accepts municipal complaints.", note_hi="उदयपुर नगर निगम की पुष्ट हेल्पलाइन अभी नहीं जोड़ी गई है। राजस्थान संपर्क (181) पर नगर निगम की शिकायत दर्ज होती है।"))
s = CH+"where-can-you-file-civic-complaints-of-indore-municipal-corporation-imc/1744"
C.append(city("indore","Indore","इंदौर","mp","Indore Municipal Corporation",
  [ch("phone","18002335522",*TOLL,NV,s), ch("phone","07314071717",*HELP,NV,s), ch("app","Indore 311","Indore 311 app (photo + location)","Indore 311 ऐप (फ़ोटो + लोकेशन)",V,"https://apps.apple.com/app/id1135167189")],
  "MP Paschim Kshetra Vidyut Vitaran Co. (West DISCOM)", [("Shankar Lalwani","Indore")],
  [("Indore-1","Kailash Vijayvargiya"),("Indore-2","Ramesh Mendola"),("Indore-3","Golu (Rakesh) Shukla"),("Indore-4","Malini Gaur"),("Indore-5","Mahendra Hardia"),("Rau","Madhu Verma")],
  mla_src=W+"Indore_Lok_Sabha_constituency",
  escalation="Deputy Commissioner, Public Grievance Cell, Indore Nagar Palika Nigam, Shivaji Market, Nagar Nigam Square, Indore 452001"))
s = CH+"how-can-i-file-civic-complaints-of-bhopal-municipal-corporation-bmc/1788"
C.append(city("bhopal","Bhopal","भोपाल","mp","Bhopal Municipal Corporation",
  [ch("phone","155304",*HELP,NV,s), ch("phone","18002330014",*TOLL,NV,s), ch("phone","9424401548",*WA,NV,s)],
  "MP Madhya Kshetra Vidyut Vitaran Co. (Central DISCOM)", [("Alok Sharma","Bhopal")],
  [("Bhopal Uttar","Atif Arif Aqueel"),("Narela","Vishvas Sarang"),("Bhopal Dakshin-Paschim","Bhagwandas Sabnani"),("Bhopal Madhya","Arif Masood"),("Govindpura","Krishna Gaur"),("Huzur","Rameshwar Sharma")],
  mla_src=W+"Bhopal_Lok_Sabha_constituency", website="bmconline.gov.in",
  escalation="Municipal Commissioner, Public Grievance Cell, BMC HQ, ISBT Campus, Dr. Ambedkar Marg, Bhopal 462023"))
C.append(city("jabalpur","Jabalpur","जबलपुर","mp","Jabalpur Municipal Corporation",
  [ch("phone","07612637500","Smart City helpline","स्मार्ट सिटी हेल्पलाइन",NV,"https://www.indiacustomercare.com/jabalpur-municipal-corporation-contact-no"), ch("app","JAN (Jabalpur Apna Nigam)","JAN app","JAN ऐप (जबलपुर अपना निगम)",NV,"https://www.indiacustomercare.com/jabalpur-municipal-corporation-contact-no")],
  "MP Poorv Kshetra Vidyut Vitaran Co. (East DISCOM)", [("Ashish Dubey","Jabalpur")],
  [("Jabalpur East","Lakhan Ghanghoriya"),("Jabalpur North","Abhilash Pandey"),("Jabalpur Cantt.","Ashok Rohani"),("Jabalpur West","Rakesh Singh")],
  mla_src=W+"Jabalpur_Lok_Sabha_constituency"))
C.append(city("raipur","Raipur","रायपुर","cg","Raipur Municipal Corporation",
  [ch("phone","07712535790",*HELP,NV,"https://www.indiacustomercare.com/raipur-municipal-corporation-rmc-contact-no")],
  "CG State Power Distribution Co. (CSPDCL)", [("Brijmohan Agrawal","Raipur")],
  [("Raipur City West","Rajesh Munat"),("Raipur City North","Purandar Mishra"),("Raipur City South","Sunil Kumar Soni"),("Raipur Rural","Motilal Sahu")],
  mla_src=W+"Raipur_Lok_Sabha_constituency"))
s1 = "https://thehitavada.com/Encyc/2025/2/8/Devendra-Fadnavis-launchesNMC-s-helpline-155304.html"
C.append(city("nagpur","Nagpur","नागपुर","mh","Nagpur Municipal Corporation",
  [ch("phone","155304","NMC grievance helpline (8am–8pm)","मनपा शिकायत हेल्पलाइन (सुबह 8–रात 8)",V,s1), ch("phone","14420",*SEW,NV),
   ch("in_person","","Zone grievance day: 2nd & 4th Friday, 10am–1pm","ज़ोन शिकायत दिवस: दूसरा और चौथा शुक्रवार, सुबह 10–दोपहर 1",V,"https://www.thehitavada.com/Encyc/2026/7/4/nmc-to-hold-grievances-redressal-days-on-second-and-fourth-fridays-.html")],
  "Maharashtra State Electricity Distribution (MSEDCL / Mahavitaran)", [("Nitin Gadkari","Nagpur")],
  [("Nagpur South West","Devendra Fadnavis"),("Nagpur South","Mohan Mate"),("Nagpur East","Krishna Khopde"),("Nagpur Central","Pravin Datke"),("Nagpur West","Vikas Thakre"),("Nagpur North","Nitin Raut")],
  mla_src=W+"Nagpur_Lok_Sabha_constituency", website="nmcnagpur.gov.in",
  escalation="Public Grievance Cell, NMC Head Office, Mahanagar Palika Marg, Civil Lines, Nagpur 440001",
  extra={"dev_authority": {"name_en":"Nagpur Improvement Trust (NIT)","name_hi":"नागपुर सुधार प्रन्यास (NIT)","channels":[ch("phone","07122531431","NIT complaints (areas under NIT)","NIT शिकायत (NIT वाले इलाक़े)",V,"https://www.nitnagpur.org/contact/complaint-grievances")]}}))
C.append(city("nashik","Nashik","नासिक","mh","Nashik Municipal Corporation",
  [ch("phone","7030300300","NMC grievance helpline","मनपा शिकायत हेल्पलाइन",V,"https://nmc.gov.in/home/index/E"), ch("phone","18002677953","Streetlight complaints","स्ट्रीटलाइट शिकायत",V,"https://nmc.gov.in/home/index/E")],
  "Maharashtra State Electricity Distribution (MSEDCL / Mahavitaran)", [("Rajabhau Waje","Nashik")],
  [("Nashik East","Rahul Dhikale"),("Nashik Central","Devyani Pharande"),("Nashik West","Seema Hiray"),("Deolali","Saroj Ahire")],
  mla_src=W+"2024_Maharashtra_Legislative_Assembly_election", website="nmc.gov.in"))
s = CH+"how-can-i-file-civic-complaints-of-surat-municipal-corporation-smc/1671"
C.append(city("surat","Surat","सूरत","gj","Surat Municipal Corporation",
  [ch("phone","18001238000",*TOLL,NV,s), ch("phone","7623838000",*WA,NV,s), ch("web","suratmunicipal.gov.in","Online complaint (Online Services)","ऑनलाइन शिकायत (ऑनलाइन सेवाएँ)",V,s)],
  "DGVCL (Dakshin Gujarat Vij Co.); Torrent Power in parts of the city", [("Mukesh Dalal","Surat"),("C. R. Patil","Navsari (part of city)")],
  [("Surat East","Arvind Rana"),("Surat North","Kanti Balar"),("Varachha Road","Kishor Kanani"),("Karanj","Pravin Ghoghari"),("Katargam","Vinu Moradiya"),("Surat West","Purnesh Modi"),("Majura","Harsh Sanghavi"),("Udhna","Manu Patel"),("Limbayat","Sangita Patil")],
  mla_status=NV, escalation="Public Grievance Cell, Surat Municipal Corporation, Muglisara, Surat 395003"))
s = CH+"where-can-i-file-civic-complaints-of-vadodara-municipal-corporation-vmc/1551"
C.append(city("vadodara","Vadodara","वडोदरा","gj","Vadodara Municipal Corporation",
  [ch("phone","18002330265",*TOLL,NV,s), ch("phone","9913166666",*WA,NV,s)],
  "MGVCL (Madhya Gujarat Vij Co.)", [("Hemang Joshi","Vadodara")],
  [("Vadodara City","Manisha Vakil"),("Sayajigunj","Keyur Rokadia"),("Akota","Chaitanya Desai"),("Raopura","Balkrishna Shukla")],
  mla_status=NV, website="vmc.gov.in", escalation="Municipal Commissioner, Vadodara Municipal Corporation, Khanderao Market, Vadodara 390001",
  mla_note_en="Manjalpur had a by-election; its current MLA has not been added yet.", mla_note_hi="मांजलपुर में उपचुनाव हुआ था; वहाँ के मौजूदा विधायक का नाम अभी नहीं जोड़ा गया है।"))
s = CH+"how-can-i-file-civic-complaints-of-rajkot-municipal-corporation-rmc/1642"
C.append(city("rajkot","Rajkot","राजकोट","gj","Rajkot Municipal Corporation",
  [ch("phone","18001231973",*TOLL,NV,s), ch("phone","9512301973",*WA,NV,s), ch("web","rmc.gov.in/ComplaintRegistration","Online complaint","ऑनलाइन शिकायत",NV,s)],
  "PGVCL (Paschim Gujarat Vij Co.)", [("Parshottam Rupala","Rajkot")],
  [("Rajkot East","Uday Kangad"),("Rajkot West","Darshita Shah"),("Rajkot South","Ramesh Tilala"),("Rajkot Rural","Bhanuben Babariya")],
  mla_status=NV, escalation="Municipal Commissioner, Rajkot Municipal Corporation, Dhebarbhai Main Road, Rajkot 360001"))
C.append(city("patna","Patna","पटना","br","Patna Municipal Corporation",
  [ch("phone","155304","24×7 toll-free helpline","24×7 टोल-फ़्री हेल्पलाइन",V,"https://patnapress.com/patna-drainage-operations-heavy-rain-august-2025/")],
  "South Bihar Power Distribution Co. (SBPDCL)", [("Ravi Shankar Prasad","Patna Sahib"),("Misa Bharti","Pataliputra (part of city)")],
  [("Digha","Sanjeev Chaurasiya"),("Bankipur","Prashant Kishor"),("Kumhrar","Sanjay Kumar Gupta"),("Patna Sahib","Ratnesh Kumar Kushwaha")],
  mla_src=W+"Patna_Sahib_Lok_Sabha_constituency",
  mla_note_en="Bankipur's MLA was elected in a by-election after the 2025 general election.", mla_note_hi="बांकीपुर के विधायक 2025 के आम चुनाव के बाद हुए उपचुनाव में चुने गए।"))
C.append(city("ranchi","Ranchi","रांची","jh","Ranchi Municipal Corporation",
  [ch("phone","18001202929",*TOLL,NV,"https://www.indiacustomercare.com/node/16804"), ch("phone","18005701235","Connect Centre (toll-free)","कनेक्ट सेंटर (टोल-फ़्री)",NV,"https://www.indiacustomercare.com/node/16804")],
  "Jharkhand Bijli Vitran Nigam (JBVNL)", [("Sanjay Seth","Ranchi")],
  [("Ranchi","C. P. Singh"),("Hatia","Navin Jaiswal"),("Kanke","Suresh Kumar Baitha")],
  mla_src=W+"Ranchi_Lok_Sabha_constituency"))
C.append(city("bhubaneswar","Bhubaneswar","भुवनेश्वर","od","Bhubaneswar Municipal Corporation",
  [ch("phone","18003450061","Unified helpline (BMC, BDA, Smart City, buses)","एकीकृत हेल्पलाइन (BMC, BDA, स्मार्ट सिटी, बस)",NV,"https://www.orissapost.com/24x7-helpline-for-citizens-grievances/amp/")],
  "TP Central Odisha Distribution Ltd (TPCODL)", [("Aparajita Sarangi","Bhubaneswar")],
  [("Bhubaneswar Central","Ananta Narayan Jena"),("Bhubaneswar North","Susant Kumar Rout"),("Ekamra-Bhubaneswar","Babu Singh")],
  mla_src=W+"Bhubaneswar_Lok_Sabha_constituency"))
C.append(city("guwahati","Guwahati","गुवाहाटी","as","Guwahati Municipal Corporation",
  [ch("phone","8811007000","Call or WhatsApp","कॉल या WhatsApp",NV,"https://sentinelassam.com/news/guwahati-municipal-corporation-gmc-helpline-for-public-grievances")],
  "Assam Power Distribution Co. (APDCL)", [("Bijuli Kalita Medhi","Guwahati")],
  [("Dispur","Pradyut Bordoloi"),("New Guwahati","Diplu Ranjan Sarmah"),("Guwahati Central","Vijay Kumar Gupta"),("Jalukbari","Himanta Biswa Sarma")],
  mla_src=W+"2026_Assam_Legislative_Assembly_election", website="gmc.assam.gov.in"))
C.append(city("coimbatore","Coimbatore","कोयंबटूर","tn","Coimbatore City Municipal Corporation",
  [ch("web","ccmc.gov.in",*WEB)], "TN Power Distribution Corporation (TNPDCL)", [("Ganapathi P. Rajkumar","Coimbatore")],
  [("Coimbatore North",""),("Coimbatore South",""),("Singanallur",""),("Kavundampalayam","")],
  mla_status="to_be_contributed",
  note_en="A verified municipal helpline for Coimbatore has not been added yet. The TN CM Helpline (1100) accepts civic complaints.", note_hi="कोयंबटूर नगर निगम की पुष्ट हेल्पलाइन अभी नहीं जोड़ी गई है। तमिलनाडु सीएम हेल्पलाइन (1100) पर नागरिक शिकायत दर्ज होती है।",
  mla_note_en="MLAs elected in the May 2026 election have not been added yet.", mla_note_hi="मई 2026 चुनाव में चुने गए विधायकों के नाम अभी नहीं जोड़े गए हैं।"))
s = "https://maduraicorporation.co.in/contact-us"
C.append(city("madurai","Madurai","मदुरै","tn","Madurai City Municipal Corporation",
  [ch("phone","7871661787","Phone / WhatsApp","फ़ोन / WhatsApp",V,s), ch("web","maduraicorporation.co.in","Register Your Complaint (online)","ऑनलाइन शिकायत दर्ज करें",V,s)],
  "TN Power Distribution Corporation (TNPDCL)", [("S. Venkatesan","Madurai")],
  [("Madurai East",""),("Madurai North",""),("Madurai South",""),("Madurai Central",""),("Madurai West","")],
  mla_status="to_be_contributed",
  mla_note_en="MLAs elected in the May 2026 election have not been added yet.", mla_note_hi="मई 2026 चुनाव में चुने गए विधायकों के नाम अभी नहीं जोड़े गए हैं।"))
C.append(city("mysuru","Mysuru","मैसूरु","ka","Mysuru City Corporation",
  [ch("phone","18002005822",*TOLL,NV,"https://www.deccanherald.com/content/522031/mcc-launches-toll-free-helpline.html")],
  "Chamundeshwari Electricity Supply Corp. (CESC Mysore)", [("Yaduveer Krishnadatta Chamaraja Wadiyar","Mysore")],
  [("Krishnaraja","T. S. Srivatsa"),("Chamaraja","K. Harish Gowda"),("Narasimharaja","Tanveer Sait"),("Chamundeshwari","G. T. Devegowda")],
  mla_src=W+"Mysore_Lok_Sabha_constituency"))
s = CH+"how-can-i-file-civic-complaints-of-greater-visakhapatnam-municipal-corporation-gvmc/1791"
C.append(city("visakhapatnam","Visakhapatnam","विशाखापत्तनम","ap","Greater Visakhapatnam Municipal Corporation (GVMC)",
  [ch("phone","1913",*TOLL,NV,s), ch("phone","180042500009",*TOLL,NV,s), ch("phone","9666909192",*WA,NV,s)],
  "AP Eastern Power Distribution Co. (APEPDCL)", [("Sribharat Mathukumilli","Visakhapatnam")],
  [("Visakhapatnam East","Velagapudi Ramakrishna Babu"),("Visakhapatnam South","Vamsi Krishna Srinivas"),("Visakhapatnam North","Penmetsa Vishnu Kumar Raju"),("Visakhapatnam West","P. G. V. R. Naidu"),("Gajuwaka","Palla Srinivas Rao"),("Bheemili","Ganta Srinivasa Rao")],
  mla_src=W+"Visakhapatnam_Lok_Sabha_constituency", website="gvmc.gov.in",
  escalation="Chief Municipal Commissioner, GVMC HQ, Tenneti Bhavanam, Asilmetta, Visakhapatnam 530002"))
C.append(city("vijayawada","Vijayawada","विजयवाड़ा","ap","Vijayawada Municipal Corporation",
  [ch("phone","08662421058","VMC support (Mon–Sat, 9:30–5:30)","VMC सहायता (सोम–शनि, 9:30–5:30)",NV,"https://www.indiacustomercare.com/vijayawada-municipal-corporation-contact-no")],
  "AP Central Power Distribution Co. (APCPDCL)", [("Kesineni Sivanath","Vijayawada")],
  [("Vijayawada West","Sujana Chowdary"),("Vijayawada Central","Bonda Umamaheswara Rao"),("Vijayawada East","Gadde Rama Mohan")],
  mla_src=W+"Vijayawada_Lok_Sabha_constituency"))
s = CH+"how-can-i-file-civic-complaints-of-kochi-municipal-corporation-kmc/1550"
C.append(city("kochi","Kochi","कोच्चि","kl","Kochi Municipal Corporation",
  [ch("phone","04842369007",*HELP,NV,s), ch("web","citizen.lsgkerala.gov.in","Online grievance (K-SMART / LSG portal)","ऑनलाइन शिकायत (LSG पोर्टल)",NV,s)],
  "Kerala State Electricity Board (KSEB)", [("Hibi Eden","Ernakulam")],
  [("Kochi","Mohammad Shiyas"),("Ernakulam","T. J. Vinod"),("Thrikkakara","Uma Thomas"),("Thrippunithura","Deepak Joy"),("Kalamassery","V. E. Abdul Gafoor"),("Vypin","Tony Chammany")],
  mla_src=W+"2026_Kerala_Legislative_Assembly_election",
  escalation="Municipal Commissioner, Kochi Municipal Corporation, PB No 1016, Ernakulam 682011"))
s = "https://smarttvm.tmc.lsgkerala.gov.in/default/index/contactus"
C.append(city("thiruvananthapuram","Thiruvananthapuram","तिरुवनंतपुरम","kl","Thiruvananthapuram Corporation",
  [ch("phone","04712377700","General helpline (24×7)","सामान्य हेल्पलाइन (24×7)",V,s), ch("phone","9496434488","Water / septage help desk","पानी / सेप्टेज हेल्प डेस्क",V,s), ch("phone","9447060134","Streetlights","स्ट्रीटलाइट",V,s), ch("web","smarttvm.tmc.lsgkerala.gov.in","Online complaint (gives tracking number)","ऑनलाइन शिकायत (ट्रैकिंग नंबर मिलता है)",V,s)],
  "Kerala State Electricity Board (KSEB)", [("Shashi Tharoor","Thiruvananthapuram")],
  [("Kazhakootam","V. Muraleedharan"),("Vattiyoorkavu","K. Muraleedharan"),("Thiruvananthapuram","C. P. John"),("Nemom","Rajeev Chandrasekhar"),("Kovalam","M. Vincent")],
  mla_src=W+"2026_Kerala_Legislative_Assembly_election"))

states = {k: {"id": k, "name_en": v["en"], "name_hi": v["hi"],
              "grievance": {"name_en": v["g_en"], "name_hi": v["g_hi"], "channels": v["ch"]},
              **({"municipal_shared": v["muni"]} if "muni" in v else {}),
              **({"note_en": v["note_en"], "note_hi": v["note_hi"]} if "note_en" in v else {})}
          for k, v in STATES.items()}

out = ROOT / "data"
(out / "cities").mkdir(parents=True, exist_ok=True)
for old in (out / "cities").glob("*.json"):
    old.unlink()
(out / "states.json").write_text(json.dumps(states, ensure_ascii=False, indent=2), encoding="utf-8")
for c in C:
    assert c["state"] in states, c["id"]
    (out / "cities" / f"{c['id']}.json").write_text(json.dumps(c, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{len(C)} cities, {len(states)} states")
