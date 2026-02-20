from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = "segredo"



personagens = {
    "Tanjiro Kamado": {
        "personagem": "Tanjiro Kamado",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Hinokami Kagura",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "tanjiro.png"
    },
    "Nezuko Kamado": {
        "personagem": "Nezuko Kamado",
        "genero": "Mulher",
        "especie": "Demônio",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Arte Demoníaca",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "nezuko.png"
    },
    "Zenitsu Agatsuma": {
        "personagem": "Zenitsu Agatsuma",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Trovão",
        "patente": "Caçador",
        "cabelo": "Amarelo",
        "status": "Vivo",
        "img": "zenitsu.png"
    },
    "Inosuke Hashibira": {
        "personagem": "Inosuke Hashibira",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Fera",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "inosuke.png"
    },
    "Giyu Tomioka": {
        "personagem": "Giyu Tomioka",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "giyu.png"
    },
    "Shinobu Kocho": {
        "personagem": "Shinobu Kocho",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Inseto",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "shinobu.png"
    },
    "Kyojuro Rengoku": {
        "personagem": "Kyojuro Rengoku",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração das Chamas",
        "patente": "Hashira",
        "cabelo": "Amarelo",
        "status": "Morto",
        "img": "kyojuro.png"
    },
    "Tengen Uzui": {
        "personagem": "Tengen Uzui",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Som",
        "patente": "Hashira",
        "cabelo": "Branco",
        "status": "Vivo",
        "img": "tengen.png"
    },
    "Muichiro Tokito": {
        "personagem": "Muichiro Tokito",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Névoa",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "muichiro.png"
    },
    "Mitsuri Kanroji": {
        "personagem": "Mitsuri Kanroji",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Amor",
        "patente": "Hashira",
        "cabelo": "Rosa",
        "status": "Morto",
        "img": "mitsuri.png"
    },
    "Obanai Iguro": {
        "personagem": "Obanai Iguro",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Serpente",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "obanai.png"
    },
    "Sanemi Shinazugawa": {
        "personagem": "Sanemi Shinazugawa",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Vento",
        "patente": "Hashira",
        "cabelo": "Branco",
        "status": "Vivo",
        "img": "sanemi.png"
    },
    "Gyomei Himejima": {
        "personagem": "Gyomei Himejima",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Rocha",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "gyomei.png"
    },
    "Kanao Tsuyuri": {
        "personagem": "Kanao Tsuyuri",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Flor",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "kanao.png"
    },
    "Genya Shinazugawa": {
        "personagem": "Genya Shinazugawa",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Repetição",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "genya.png"
    },
    "Muzan Kibutsuji": {
        "personagem": "Muzan Kibutsuji",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Rei",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "muzan.png"
    },
    "Kokushibo": {
        "personagem": "Kokushibo",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Respiração da Lua",
        "patente": "Lua Superior",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "kokushibo.png"
    },
    "Douma": {
        "personagem": "Douma",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Loiro",
        "status": "Morto",
        "img": "douma.png"
    },
    "Akaza": {
        "personagem": "Akaza",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Rosa",
        "status": "Morto",
        "img": "akaza.png"
    },
    "Hantengu": {
        "personagem": "Hantengu",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "hantengu.png"
    },
    "Gyokko": {
        "personagem": "Gyokko",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "gyokko.png"
    },
    "Gyutaro": {
        "personagem": "Gyutaro",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Verde",
        "status": "Morto",
        "img": "gyutaro.png"
    },
    "Daki": {
        "personagem": "Daki",
        "genero": "Mulher",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Superior",
        "cabelo": "Branco",
        "status": "Morto",
        "img": "daki.png"
    },
    "Enmu": {
        "personagem": "Enmu",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Inferior",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "enmu.png"
    },
    "Rui": {
        "personagem": "Rui",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Doze Kizuki",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Inferior",
        "cabelo": "Branco",
        "status": "Morto",
        "img": "rui.png"
    },
    "Tamayo": {
        "personagem": "Tamayo",
        "genero": "Mulher",
        "especie": "Demônio",
        "afiliacao": "Independente",
        "estilo": "Arte Demoníaca",
        "patente": "Nenhuma",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "tamayo.png"
    },
    "Yoriichi Tsugikuni": {
        "personagem": "Yoriichi Tsugikuni",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração do Sol",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "yoriichi.png"
    },
    "Sakonji Urokodaki": {
        "personagem": "Sakonji Urokodaki",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Hashira",
        "cabelo": "Cinza",
        "status": "Vivo",
        "img": "urokodaki.png"
    },
    "Kanae Kocho": {
        "personagem": "Kanae Kocho",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Flor",
        "patente": "Hashira",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "kanae.png"
    },
    "Aoi Kanzaki": {
        "personagem": "Aoi Kanzaki",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "aoi.png"
    },
    "Murata": {
        "personagem": "Murata",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "murata.png"
    },
    "Sabito": {
        "personagem": "Sabito",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Caçador",
        "cabelo": "Rosa",
        "status": "Morto",
        "img": "sabito.png"
    },
    "Makomo": {
        "personagem": "Makomo",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Respiração da Água",
        "patente": "Caçador",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "makomo.png"
    },
    "Hotaru Haganezuka": {
        "personagem": "Hotaru Haganezuka",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Ferreiros",
        "estilo": "Nenhum",
        "patente": "Ferreiro",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "haganezuka.png"
    },
    "Kotetsu": {
        "personagem": "Kotetsu",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Ferreiros",
        "estilo": "Nenhum",
        "patente": "Ferreiro",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "kotetsu.png"
    },
    "Amane Ubuyashiki": {
        "personagem": "Amane Ubuyashiki",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Nenhum",
        "patente": "Líder",
        "cabelo": "Branco",
        "status": "Morto",
        "img": "amane.png"
    },
    "Kiriya Ubuyashiki": {
        "personagem": "Kiriya Ubuyashiki",
        "genero": "Homem",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Nenhum",
        "patente": "Líder",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "kiriya.png"
    },
    "Makio": {
        "personagem": "Makio",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Nenhum",
        "patente": "Apoio",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "makio.png"
    },
    "Suma": {
        "personagem": "Suma",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Nenhum",
        "patente": "Apoio",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "suma.png"
    },
    "Hinatsuru": {
        "personagem": "Hinatsuru",
        "genero": "Mulher",
        "especie": "Humano",
        "afiliacao": "Caçadores de Demônios",
        "estilo": "Nenhum",
        "patente": "Apoio",
        "cabelo": "Preto",
        "status": "Vivo",
        "img": "hinatsuru.png"
    },
    "Kyogai": {
        "personagem": "Kyogai",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Independente",
        "estilo": "Arte Demoníaca",
        "patente": "Lua Inferior",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "kyogai.png"
    },
    "Susamaru": {
        "personagem": "Susamaru",
        "genero": "Mulher",
        "especie": "Demônio",
        "afiliacao": "Independente",
        "estilo": "Arte Demoníaca",
        "patente": "Nenhuma",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "susamaru.png"
    },
    "Yahaba": {
        "personagem": "Yahaba",
        "genero": "Homem",
        "especie": "Demônio",
        "afiliacao": "Independente",
        "estilo": "Arte Demoníaca",
        "patente": "Nenhuma",
        "cabelo": "Preto",
        "status": "Morto",
        "img": "yahaba.png"
    },
};




# FUNÇÃO COMPARAR CORRIGIDA
def comparar(p, alvo):
    resultado = {}
    for campo in ["genero","especie","afiliacao","estilo","patente","cabelo","status"]:
        valor_p = str(p[campo]).strip().lower()
        valor_alvo = str(alvo[campo]).strip().lower()
        resultado[campo] = "verde" if valor_p == valor_alvo else "vermelho"
    return resultado






@app.route("/", methods=["GET", "POST"])
def home():
    # Se não existir personagem do dia, cria um
    if "personagem" not in session:
        session["personagem"] = random.choice(list(personagens.keys()))
    # Cria lista de tentativas caso não exista
    if "tentativas" not in session:
        session["tentativas"] = []

    # POST — adicionar tentativa
    if request.method == "POST":
        nome = request.form.get("personagem")
        if nome in personagens:
            p = personagens[nome]
            alvo = personagens[session["personagem"]]
            session["tentativas"].insert(0, {
                "dados": p,
                "resultado": comparar(p, alvo)
            })

    return render_template(
        "index.html",
        personagens=personagens.values(),
        tentativas=session["tentativas"]
    )
def get_personagem_digitado(nome):
    nome_lower = nome.strip().lower()
    mapeamento = {
        "tanjiro": "Tanjiro Kamado",
        "tanjiro kamado": "Tanjiro Kamado",
        "kamado": "Tanjiro Kamado",
        "nezuko": "Nezuko Kamado",
        "nezuko kamado": "Nezuko Kamado",
        "zenitsu": "Zenitsu Agatsuma",
        "zenitsu agatsuma": "Zenitsu Agatsuma",
        "agatsuma": "Zenitsu Agatsuma",
        "inosuke": "Inosuke Hashibira",
        "inosuke hashibira": "Inosuke Hashibira",
        "hashibira": "Inosuke Hashibira",
        "kanao": "Kanao Tsuyuri",
        "kanao tsuyuri": "Kanao Tsuyuri",
        "tsuyuri": "Kanao Tsuyuri",
        "genya": "Genya Shinazugawa",
        "genya shinazugawa": "Genya Shinazugawa",
        "giyu": "Giyu Tomioka",
        "tomioka": "Giyu Tomioka",
        "giyu tomioka": "Giyu Tomioka",
        "shinobu": "Shinobu Kocho",
        "kocho": "Shinobu Kocho",
        "shinobu kocho": "Shinobu Kocho",
        "kyojuro": "Kyojuro Rengoku",
        "rengoku": "Kyojuro Rengoku",
        "kyojuro rengoku": "Kyojuro Rengoku",
        "tengen": "Tengen Uzui",
        "uzui": "Tengen Uzui",
        "tengen uzui": "Tengen Uzui",
        "muichiro": "Muichiro Tokito",
        "tokito": "Muichiro Tokito",
        "muichiro tokito": "Muichiro Tokito",
        "mitsuri": "Mitsuri Kanroji",
        "kanroji": "Mitsuri Kanroji",
        "mitsuri kanroji": "Mitsuri Kanroji",
        "obanai": "Obanai Iguro",
        "iguro": "Obanai Iguro",
        "obanai iguro": "Obanai Iguro",
        "sanemi": "Sanemi Shinazugawa",
        "sanemi shinazugawa": "Sanemi Shinazugawa",
        "gyomei": "Gyomei Himejima",
        "himejima": "Gyomei Himejima",
        "gyomei himejima": "Gyomei Himejima",
        "sakonji": "Sakonji Urokodaki",
        "urokodaki": "Sakonji Urokodaki",
        "sakonji urokodaki": "Sakonji Urokodaki",
        "jigoro": "Jigoro Kuwajima",
        "kuwajima": "Jigoro Kuwajima",
        "jigoro kuwajima": "Jigoro Kuwajima",
        "shinjuro": "Shinjuro Rengoku",
        "shinjuro rengoku": "Shinjuro Rengoku",
        "kanae": "Kanae Kocho",
        "kanae kocho": "Kanae Kocho",
        "yoriichi": "Yoriichi Tsugikuni",
        "tsugikuni": "Yoriichi Tsugikuni",
        "yoriichi tsugikuni": "Yoriichi Tsugikuni",
        "muzan": "Muzan Kibutsuji",
        "kibutsuji": "Muzan Kibutsuji",
        "muzan kibutsuji": "Muzan Kibutsuji",
        "kokushibo": "Kokushibo",
        "douma": "Douma",
        "akaza": "Akaza",
        "hantengu": "Hantengu",
        "gyokko": "Gyokko",
        "gyutaro": "Gyutaro",
        "daki": "Daki",
        "enmu": "Enmu",
        "rui": "Rui",
        "tamayo": "Tamayo",
        "yushiro": "Yushiro"
    }
    nome_completo = mapeamento.get(nome_lower)
    if nome_completo:
        return personagens[nome_completo]
    return None



if __name__ == "__main__":

    app.run(debug=True)
