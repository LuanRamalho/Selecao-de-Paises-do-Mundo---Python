import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from svgpathtools import svg2paths

# Dicionário de países e bandeiras
countries = {
    'África': {
        'África do Sul': 'https://flagpedia.net/data/flags/w580/za.webp',
        'Angola': 'https://flagpedia.net/data/flags/w580/ao.webp',
        'Argélia': 'https://flagpedia.net/data/flags/w580/dz.webp',
        'Benin': 'https://flagpedia.net/data/flags/w580/bj.webp',
        'Botsuana': 'https://flagpedia.net/data/flags/w580/bw.webp',
        'Burkina Faso': 'https://flagpedia.net/data/flags/w580/bf.webp',
        'Burundi': 'https://flagpedia.net/data/flags/w580/bi.webp',
        'Camarões': 'https://flagpedia.net/data/flags/w580/cm.webp',
        'Cabo Verde': 'https://flagpedia.net/data/flags/w580/cv.webp',
        'República Centro Africana': 'https://flagpedia.net/data/flags/w580/cf.webp',
        'Chade': 'https://flagpedia.net/data/flags/w580/td.webp',
        'Comoros': 'https://flagpedia.net/data/flags/w580/km.webp',
        'República do Congo': 'https://flagpedia.net/data/flags/w580/cg.webp',
        'República Democrática do Congo': 'https://flagpedia.net/data/flags/w580/cd.webp',
        'Costa do Marfim': 'https://flagpedia.net/data/flags/w580/ci.webp',
        'Djibuti': 'https://flagpedia.net/data/flags/w580/dj.webp',
        'Egito': 'https://flagpedia.net/data/flags/w580/eg.webp',
        'Eritreia': 'https://flagpedia.net/data/flags/w580/er.webp',
        'Eswatini': 'https://flagpedia.net/data/flags/w580/sz.webp',
        'Etiópia': 'https://flagpedia.net/data/flags/w580/et.webp',
        'Gabão': 'https://flagpedia.net/data/flags/w580/ga.webp',
        'Gâmbia': 'https://flagpedia.net/data/flags/w580/gm.webp',
        'Gana': 'https://flagpedia.net/data/flags/w580/gh.webp',
        'Guiné': 'https://flagpedia.net/data/flags/w580/gn.webp',
        'Guiné-Bissau': 'https://flagpedia.net/data/flags/w580/gw.webp',
        'Guiné Equatorial': 'https://flagpedia.net/data/flags/w580/gq.webp',
        'Lesoto': 'https://flagpedia.net/data/flags/w580/ls.webp',
        'Libéria': 'https://flagpedia.net/data/flags/w580/lr.webp',
        'Líbia': 'https://flagpedia.net/data/flags/w580/ly.webp',
        'Madagascar': 'hhttps://flagpedia.net/data/flags/w580/mg.webp',
        'Malauí': 'https://flagpedia.net/data/flags/w580/mw.webp',
        'Mali': 'https://flagpedia.net/data/flags/w580/ml.webp',
        'Mauritânia': 'https://flagpedia.net/data/flags/w580/mr.webp',
        'Maurício': 'https://flagpedia.net/data/flags/w580/mu.webp',
        'Mayotte': 'https://flagpedia.net/data/flags/w580/yt.webp',
        'Marrocos': 'https://flagpedia.net/data/flags/w580/ma.webp',
        'Moçambique': 'https://flagpedia.net/data/flags/w580/mz.webp',
        'Namíbia': 'https://flagpedia.net/data/flags/w580/na.webp',
        'Níger': 'https://flagpedia.net/data/flags/w580/ne.webp',
        'Nigéria': 'https://flagpedia.net/data/flags/w580/ng.webp',
        'Quênia': 'https://flagpedia.net/data/flags/w580/ke.webp',
        'Reunião': 'https://flagpedia.net/data/flags/w580/re.webp',
        'Ruanda': 'https://flagpedia.net/data/flags/w580/rw.webp',
        'Saara do Oeste': 'https://flagpedia.net/data/flags/w580/eh.webp',
        'Santa Helena': 'https://flagpedia.net/saint-helena-ascension-and-tristan-da-cunha',
        'São Tomé e Príncipe': 'https://flagpedia.net/data/flags/w580/st.webp',
        'Senegal': 'https://flagpedia.net/data/flags/w580/sn.webp',
        'Seychelles': 'https://flagpedia.net/data/flags/w580/sc.webp',
        'Serra Leoa': 'https://flagpedia.net/data/flags/w580/sl.webp',
        'Somália': 'https://flagpedia.net/data/flags/w580/so.webp',
        'Sudão': 'https://flagpedia.net/data/flags/w580/sd.webp',
        'Sudão do Sul': 'https://flagpedia.net/data/flags/w580/ss.webp',
        'Tanzânia': 'https://flagpedia.net/data/flags/w580/tz.webp',
        'Togo': 'https://flagpedia.net/data/flags/w580/tg.webp',
        'Tunísia': 'https://flagpedia.net/data/flags/w580/tn.webp',
        'Uganda': 'https://flagpedia.net/data/flags/w580/ug.webp',
        'Zâmbia': 'https://flagpedia.net/data/flags/w580/zm.webp',
        'Zimbábue': 'https://flagpedia.net/data/flags/w580/zw.webp'
    },
    'Ásia': {
        'Afeganistão': 'https://flagpedia.net/data/flags/w580/af.webp?v=un',
        'Arábia Saudita': 'https://flagpedia.net/data/flags/w580/sa.webp',
        'Armênia': 'https://flagpedia.net/data/flags/w580/am.webp',
        'Azerbaijão': 'https://flagpedia.net/data/flags/w580/az.webp',
        'Bahrein': 'https://flagpedia.net/data/flags/w580/bh.webp',
        'Bangladesh': 'https://flagpedia.net/data/flags/w580/bd.webp',
        'Brunei': 'https://flagpedia.net/data/flags/w580/bn.webp',
        'Butão': 'https://flagpedia.net/data/flags/w580/bt.webp',
        'Camboja': 'https://flagpedia.net/data/flags/w580/kh.webp',
        'Cazaquistão': 'https://flagpedia.net/data/flags/w580/kz.webp',
        'Coréia do Norte': 'https://flagpedia.net/data/flags/w580/kp.webp',
        'Coréia do Sul': 'https://flagpedia.net/data/flags/w580/kr.webp',
        'China': 'https://flagpedia.net/data/flags/w580/cn.webp',
        'Emirados Árabes Unidos': 'https://flagpedia.net/data/flags/w580/ae.webp',
        'Filipinas': 'https://flagpedia.net/data/flags/w580/ph.webp',
        'Hong Kong': 'https://flagpedia.net/data/flags/w580/hk.webp',
        'Iemen': 'https://flagpedia.net/data/flags/w580/ye.webp',
        'Índia': 'https://flagpedia.net/data/flags/w580/in.webp',
        'Indonésia': 'https://flagpedia.net/data/flags/w580/id.webp',
        'Irã': 'https://flagpedia.net/data/flags/w580/ir.webp',
        'Iraque': 'https://flagpedia.net/data/flags/w580/iq.webp',
        'Israel': 'https://flagpedia.net/data/flags/w580/il.webp',
        'Japão': 'https://flagpedia.net/data/flags/w580/jp.webp',
        'Jordânia': 'https://flagpedia.net/data/flags/w580/jo.webp',
        'Kuwait': 'https://flagpedia.net/data/flags/w580/kw.webp',
        'Laos': 'https://flagpedia.net/data/flags/w580/la.webp',
        'Líbano': 'https://flagpedia.net/data/flags/w580/lb.webp',
        'Macau': 'https://flagpedia.net/data/flags/w580/mo.webp',
        'Malásia': 'https://flagpedia.net/data/flags/w580/my.webp',
        'Maldivas': 'https://flagpedia.net/data/flags/w580/mv.webp',
        'Mianmar': 'https://flagpedia.net/data/flags/w580/mm.webp',
        'Mongólia': 'https://flagpedia.net/data/flags/w580/mn.webp',
        'Nepal': 'https://flagpedia.net/data/flags/w580/np.webp',
        'Omã': 'https://flagpedia.net/data/flags/w580/om.webp',
        'Palestina': 'https://flagpedia.net/data/flags/w580/ps.webp',
        'Paquistão': 'https://flagpedia.net/data/flags/w580/pk.webp',
        'Qatar': 'https://flagpedia.net/data/flags/w580/qa.webp',
        'Quirguistão': 'https://flagpedia.net/data/flags/w580/kg.webp',
        'Singapura': 'https://flagpedia.net/data/flags/w580/sg.webp',
        'Síria': 'https://flagpedia.net/data/flags/w580/sy.webp',
        'Sri Lanka': 'https://flagpedia.net/data/flags/w580/lk.webp',
        'Tadjiquistão': 'https://flagpedia.net/data/flags/w580/tj.webp',
        'Tailândia': 'https://flagpedia.net/data/flags/w580/th.webp',
        'Taiwan': 'https://flagpedia.net/data/flags/w580/tw.webp',
        'Timor Leste': 'https://flagpedia.net/data/flags/w580/tl.webp',
        'Turcomenistão': 'https://flagpedia.net/data/flags/w580/tm.webp',
        'Turquia': 'https://flagpedia.net/data/flags/w580/tr.webp',
        'Uzbequistão': 'https://flagpedia.net/data/flags/w580/uz.webp',
        'Vietnã': 'https://flagpedia.net/data/flags/w580/vn.webp'
    },
    'Europa': {
        'Albânia': 'https://flagpedia.net/data/flags/w580/al.webp',
        'Alemanha': 'https://flagpedia.net/data/flags/w580/de.webp',
        'Andorra': 'https://flagpedia.net/data/flags/w580/ad.webp',
        'Áustria': 'https://flagpedia.net/data/flags/w580/at.webp',
        'Belarus': 'https://flagpedia.net/data/flags/w580/by.webp',
        'Bélgica': 'https://flagpedia.net/data/flags/w580/be.webp',
        'Bósnia-Herzegovina': 'https://flagpedia.net/data/flags/w580/ba.webp',
        'Bulgária': 'https://flagpedia.net/data/flags/w580/bg.webp',
        'Chipre': 'https://flagpedia.net/data/flags/w580/cy.webp',
        'Croácia': 'https://flagpedia.net/data/flags/w580/hr.webp',
        'República Tcheca': 'https://flagpedia.net/data/flags/w580/cz.webp',
        'Dinamarca': 'https://flagpedia.net/data/flags/w580/dk.webp',
        'Escócia': 'https://flagpedia.net/data/flags/w580/gb-sct.webp',
        'Eslováquia': 'https://flagpedia.net/data/flags/w580/sk.webp',
        'Eslovênia': 'https://flagpedia.net/data/flags/w580/si.webp',
        'Espanha': 'https://flagpedia.net/data/flags/w580/es.webp',
        'Estônia': 'https://flagpedia.net/data/flags/w580/ee.webp',
        'Finlândia': 'https://flagpedia.net/data/flags/w580/fi.webp',
        'França': 'https://flagpedia.net/data/flags/w580/fr.webp',
        'Geórgia': 'https://flagpedia.net/data/flags/w580/ge.webp',
        'Gibraltar': 'https://flagpedia.net/data/flags/w580/gi.webp',
        'Grécia': 'https://flagpedia.net/data/flags/w580/gr.webp',
        'Groenlândia': 'https://flagpedia.net/data/flags/w580/gl.webp',
        'Holanda': 'https://flagpedia.net/data/flags/w580/nl.webp',
        'Hungria': 'https://flagpedia.net/data/flags/w580/hu.webp',
        'Inglaterra': 'https://flagpedia.net/data/flags/w580/gb-eng.webp',
        'Irlanda': 'https://flagpedia.net/data/flags/w580/ie.webp',
        'Irlanda do Norte': 'https://flagpedia.net/data/flags/w580/gb-nir.webp',
        'Islândia': 'https://flagpedia.net/data/flags/w580/is.webp',
        'Itália': 'https://flagpedia.net/data/flags/w580/it.webp',
        'Kosovo': 'https://flagpedia.net/data/flags/w580/xk.webp',
        'Letônia': 'https://flagpedia.net/data/flags/w580/lv.webp',
        'Liechtenstein': 'https://flagpedia.net/data/flags/w580/li.webp', 
        'Lituânia': 'https://flagpedia.net/data/flags/w580/lt.webp',
        'Luxemburgo': 'https://flagpedia.net/data/flags/w580/lu.webp',
        'Macedônia': 'https://flagpedia.net/data/flags/w580/mk.webp',
        'Malta': 'https://flagpedia.net/data/flags/w580/mt.webp',
        'Moldávia': 'https://flagpedia.net/data/flags/w580/md.webp',
        'Mônaco': 'https://flagpedia.net/data/flags/w580/mc.webp',
        'Montenegro': 'https://flagpedia.net/data/flags/w580/me.webp',
        'Noruega': 'https://flagpedia.net/data/flags/w580/no.webp',
        'País de Gales': 'https://flagpedia.net/data/flags/w580/gb-wls.webp',
        'Polônia': 'https://flagpedia.net/data/flags/w580/pl.webp',
        'Portugal': 'https://flagpedia.net/data/flags/w580/pt.webp',
        'Reino Unido': 'https://flagpedia.net/data/flags/w580/gb.webp',
        'Romênia': 'https://flagpedia.net/data/flags/w580/ro.webp',
        'Rússia': 'https://flagpedia.net/data/flags/w580/ru.webp',
        'San Marino': 'https://flagpedia.net/data/flags/w580/sm.webp',
        'Sérvia': 'https://flagpedia.net/data/flags/w580/rs.webp',
        'Suécia': 'https://flagpedia.net/data/flags/w580/se.webp',
        'Suiça': 'https://flagpedia.net/data/flags/w580/ch.webp', 
        'Ucrânia': 'https://flagpedia.net/data/flags/w580/ua.webp',
        'Vaticano': 'https://flagpedia.net/data/flags/w580/va.webp',
        'Ilhas Aland': 'https://flagpedia.net/data/flags/w580/ax.webp',
        'Ilhas Faroe': 'https://flagpedia.net/data/flags/w580/fo.webp'
    },
    'América do Norte': {
        'Canadá': 'https://flagpedia.net/data/flags/w580/ca.webp',
        'Estados Unidos': 'https://flagpedia.net/data/flags/w580/us.webp',
        'México': 'https://flagpedia.net/data/flags/w580/mx.webp'
    },
    'América Central': {
        'Anguilla': 'https://flagpedia.net/data/flags/w580/ai.webp',
        'Antígua e Barbuda': 'https://flagpedia.net/data/flags/w580/ag.webp',
        'Aruba': 'https://flagpedia.net/data/flags/w580/aw.webp',
        'Bahamas': 'https://flagpedia.net/data/flags/w580/bs.webp',
        'Barbados': 'https://flagpedia.net/data/flags/w580/bb.webp',
        'Belize': 'https://flagpedia.net/data/flags/w580/bz.webp',
        'Costa Rica': 'https://flagpedia.net/data/flags/w580/cr.webp',
        'Cuba': 'https://flagpedia.net/data/flags/w580/cu.webp',
        'Curaçao': 'https://flagpedia.net/data/flags/w580/cw.webp',
        'Dominica': 'https://flagpedia.net/data/flags/w580/dm.webp',
        'República Dominicana': 'https://flagpedia.net/data/flags/w580/do.webp',
        'El Salvador': 'https://flagpedia.net/data/flags/w580/sv.webp',
        'Granada': 'https://flagpedia.net/data/flags/w580/gd.webp',
        'Guadalupe': 'https://flagpedia.net/data/flags/w580/gp.webp',
        'Guatemala': 'https://flagpedia.net/data/flags/w580/gt.webp',
        'Haiti': 'https://flagpedia.net/data/flags/w580/ht.webp',
        'Honduras': 'https://flagpedia.net/data/flags/w580/hn.webp',
        'Jamaica': 'https://flagpedia.net/data/flags/w580/jm.webp',
        'Martinica': 'https://flagpedia.net/data/flags/w580/mq.webp',
        'Montserrat': 'https://flagpedia.net/data/flags/w580/ms.webp',
        'Nicarágua': 'https://flagpedia.net/data/flags/w580/ni.webp',
        'Panamá': 'https://flagpedia.net/data/flags/w580/pa.webp',
        'Porto Rico': 'https://flagpedia.net/data/flags/w580/pr.webp',
        'São Bartolomeu': 'https://flagpedia.net/data/flags/w580/bl.webp',
        'São Cristóvão e Nevis': 'https://flagpedia.net/data/flags/w580/kn.webp',
        'Santa Lucia': 'https://flagpedia.net/data/flags/w580/lc.webp',
        'São Martinho': 'https://flagpedia.net/data/flags/w580/sx.webp',
        'São Vicente e Granadinas': 'https://flagpedia.net/data/flags/w580/vc.webp',
        'Trinidad e Tobago': 'https://flagpedia.net/data/flags/w580/tt.webp',
        'Ilhas Bermudas': 'https://flagpedia.net/data/flags/w580/bm.webp',
        'Ilhas Cayman': 'https://flagpedia.net/data/flags/w580/ky.webp',
        'Ilhas Turks e Caicos': 'https://flagpedia.net/data/flags/w580/tc.webp',
        'Ilhas Virgens Britânicas': 'https://flagpedia.net/data/flags/w580/vg.webp',
        'Ilhas Virgens Americanas': 'https://flagpedia.net/data/flags/w580/vi.webp'
    },
    'América do Sul': {
        'Argentina': 'https://flagpedia.net/data/flags/w580/ar.webp',
        'Bolivia': 'https://flagpedia.net/data/flags/w580/bo.webp',
        'Brasil': 'https://flagpedia.net/data/flags/w580/br.webp',
        'Chile': 'https://flagpedia.net/data/flags/w580/cl.webp',
        'Colômbia': 'https://flagpedia.net/data/flags/w580/co.webp',
        'Equador': 'https://flagpedia.net/data/flags/w580/ec.webp',
        'Guiana': 'https://flagpedia.net/data/flags/w580/gy.webp',
        'Guiana Francesa': 'https://flagpedia.net/data/flags/w580/gf.webp',
        'Paraguai': 'https://flagpedia.net/data/flags/w580/py.webp',
        'Peru': 'https://flagpedia.net/data/flags/w580/pe.webp',
        'Suriname': 'https://flagpedia.net/data/flags/w580/sr.webp',
        'Uruguai': 'https://flagpedia.net/data/flags/w580/uy.webp',
        'Venezuela': 'https://flagpedia.net/data/flags/w580/ve.webp',
        'Ilhas Falkland (Ilhas Malvinas)': 'https://flagpedia.net/data/flags/w580/fk.webp'
    },
    'Oceania': {
        'Austrália': 'https://flagpedia.net/data/flags/w580/au.webp',
        'Fiji': 'https://flagpedia.net/data/flags/w580/fj.webp',
        'Guam': 'https://flagpedia.net/data/flags/w580/gu.webp',
        'kiribati': 'https://flagpedia.net/data/flags/w580/ki.webp',
        'Micronésia': 'https://flagpedia.net/data/flags/w580/fm.webp',
        'Nauru': 'https://flagpedia.net/data/flags/w580/nr.webp',
        'Niue': 'https://flagpedia.net/data/flags/w580/nu.webp',
        'Nova Caledônia': 'https://flagpedia.net/data/flags/w580/nc.webp',
        'Nova Zelândia': 'https://flagpedia.net/data/flags/w580/nz.webp',
        'Palau': 'https://flagpedia.net/data/flags/w580/pw.webp',
        'Papua Nova Guiné': 'https://flagpedia.net/data/flags/w580/pg.webp', 
        'Polinésia Francesa': 'https://flagpedia.net/data/flags/w580/pf.webp',
        'Samoa': 'https://flagpedia.net/data/flags/w580/ws.webp',
        'Samoa Americana': 'https://flagpedia.net/data/flags/w580/as.webp',
        'Tokelau': 'https://flagpedia.net/data/flags/w580/tk.webp',
        'Tonga': 'https://flagpedia.net/data/flags/w580/to.webp',
        'Tuvalu': 'https://flagpedia.net/data/flags/w580/tv.webp',
        'Vanuatu': 'https://flagpedia.net/data/flags/w580/vu.webp',
        'Wallis e Futuna': 'https://flagpedia.net/data/flags/w580/wf.webp',
        'Ilhas Christmas': 'https://flagpedia.net/data/flags/w580/cx.webp',
        'Ilhas Cocos': 'https://flagpedia.net/data/flags/w580/cc.webp',
        'Ilhas Cook': 'https://flagpedia.net/data/flags/w580/ck.webp',
        'Ilhas Mariana do Norte': 'https://flagpedia.net/data/flags/w580/mp.webp',
        'Ilhas Marshall': 'https://flagpedia.net/data/flags/w580/mh.webp',
        'Ilhas Norfolk': 'https://flagpedia.net/data/flags/w580/nf.webp',
        'Ilhas Pitcairn': 'https://flagpedia.net/data/flags/w580/pn.webp',
        'Ilhas Salomão': 'https://flagpedia.net/data/flags/w580/sb.webp'
    },
    'Antarctica': {
        'Antártida': 'https://flagpedia.net/data/flags/w580/aq.webp'
    }
}

def populate_countries(event):
    continent = continent_combobox.get()
    country_combobox['values'] = list(countries[continent].keys())
    country_combobox.set('')

def display_flag(event):
    country = country_combobox.get()
    continent = continent_combobox.get()
    
    if country:
        url = countries[continent][country]
        response = requests.get(url)
        img_data = Image.open(BytesIO(response.content)).resize((200, 120))
        img = ImageTk.PhotoImage(img_data)
        
        flag_label.config(image=img)
        flag_label.image = img

# Criação da janela principal
root = tk.Tk()
root.title("Exibição de Bandeiras")
root.geometry("400x400")

# Criação dos elementos da interface
continent_label = tk.Label(root, text="Selecione o Continente:", font=("Times new Roman", 14))
continent_label.pack(pady=5)

continent_combobox = ttk.Combobox(root, values=list(countries.keys()), state="readonly")
continent_combobox.pack(pady=5)
continent_combobox.bind("<<ComboboxSelected>>", populate_countries)

country_label = tk.Label(root, text="Selecione o País:" , font=("Times new Roman", 14))
country_label.pack(pady=5)

country_combobox = ttk.Combobox(root, state="readonly")
country_combobox.pack(pady=5)
country_combobox.bind("<<ComboboxSelected>>", display_flag)

flag_label = tk.Label(root)
flag_label.pack(pady=20)

# Inicia o loop da interface
root.mainloop()
