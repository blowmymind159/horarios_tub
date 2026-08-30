import streamlit as st
from datetime import datetime

# DADOS (mesmos dados de antes)
DADOS = [
    # LINHA 212
    ("212", "Braga(Central)", "IDA", "A-U", ["06:30","07:05","08:30","09:30","10:30","14:20","17:30","18:15","19:20"]),
    ("212", "Braga(Central)", "IDA", "A-S", ["08:15","11:45","14:10"]),
    ("212", "Braga(Central)", "IDA", "A-DF", ["08:15","13:00","18:00"]),
    ("212", "Barcelos(Central)", "IDA", "A-U", ["07:25","08:00","09:25","10:26","11:25","15:15","18:26","19:11","20:15"]),
    ("212", "Barcelos(Central)", "IDA", "A-S", ["09:05","12:35","15:00"]),
    ("212", "Barcelos(Central)", "IDA", "A-DF", ["09:05","13:50","18:50"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-U", ["07:00","08:05","08:25","09:30","10:30","13:35","14:15","16:00","16:55","18:00","18:30","19:20"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-S", ["07:25","10:00","12:35","18:30"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-DF", ["10:35","12:00","18:30"]),
    ("212", "Braga(Central)", "VOLTA", "A-U", ["07:55","09:00","09:20","10:25","11:25","14:30","15:10","16:55","17:50","18:55","19:25","20:15"]),
    ("212", "Braga(Central)", "VOLTA", "A-S", ["08:15","10:50","13:25","19:20"]),
    ("212", "Braga(Central)", "VOLTA", "A-DF", ["11:25","12:50","19:20"]),
    
    # LINHA 213
    ("213", "Braga(Central)", "IDA", "A-U", ["06:30","07:00","08:00","09:00","10:00","11:15","12:15","13:05","14:05","15:05","16:05","17:10","18:10","19:10"]),
    ("213", "Braga(Central)", "IDA", "A-S", ["08:00","09:00","12:00","14:30","17:10"]),
    ("213", "Braga(Central)", "IDA", "A-DF", ["13:00","14:45","19:50"]),
    ("213", "Barcelos(Central)", "IDA", "A-U", ["07:30","08:00","09:00","10:00","11:00","12:15","13:15","14:05","15:05","16:05","17:05","18:10","19:10","20:10"]),
    ("213", "Barcelos(Central)", "IDA", "A-S", ["09:00","10:00","13:00","15:30","18:10"]),
    ("213", "Barcelos(Central)", "IDA", "A-DF", ["13:50","15:35","20:40"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-U", ["06:45","07:30","08:50","10:15","11:10","12:15","13:10","14:05","15:05","16:05","17:20","18:15","19:05"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-S", ["07:40","10:30","13:05","16:05","19:15"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-DF", ["13:50","17:00","19:00"]),
    ("213", "Braga(Central)", "VOLTA", "A-U", ["07:45","08:30","09:50","11:15","12:10","13:15","14:10","15:05","16:05","17:05","18:20","19:15","20:05"]),
    ("213", "Braga(Central)", "VOLTA", "A-S", ["08:40","11:30","14:05","17:05","20:15"]),
    ("213", "Braga(Central)", "VOLTA", "A-DF", ["14:40","17:50","19:50"]),
    
    # LINHA 214
    ("214", "Braga(Central)", "IDA", "EUI-U", ["08:25","09:00","10:30","13:35","16:35","17:20","17:55","19:00","21:30","22:30"]),
    ("214", "Barcelos(IPCA)", "IDA", "EUI-U", ["09:00","09:30","11:00","14:00","17:05","17:50","18:25","19:30","21:55","22:55"]),
    ("214", "Barcelos(IPCA)", "VOLTA", "EUI-U", ["08:10","09:00","12:45","13:05","16:05","17:05","17:35","18:05","18:30","20:30","22:00","22:55"]),
    ("214", "Braga(Central)", "VOLTA", "EUI-U", ["09:00","09:50","13:35","16:35","17:50","18:35","19:00","21:00","22:30","23:20"]),
    
    # LINHA 215
    ("215", "Barcelos(Central)", "IDA", "A-U", ["08:15","10:30","12:00","13:35","16:30","17:50","18:35","19:15","19:45"]),
    ("215", "Barcelos(Central)", "IDA", "A-S", ["09:10","12:35","18:00"]),
    ("215", "Apúlia(Praia)", "IDA", "A-U", ["07:52","09:10","11:25","12:55","14:30","17:25","18:45","19:30","20:10"]),
    ("215", "Apúlia(Praia)", "IDA", "A-S", ["10:05","13:30"]),
    ("215", "Apúlia(Praia)", "VOLTA", "A-U", ["07:58","09:17","12:32","14:32","16:02","17:32","19:00","19:45"]),
    ("215", "Apúlia(Praia)", "VOLTA", "A-S", ["11:42","17:31"]),
    ("215", "Barcelos(Central)", "VOLTA", "A-U", ["07:35","08:15","08:56","09:40","10:15","13:30","15:30","17:00","18:30","20:00"]),
    ("215", "Barcelos(Central)", "VOLTA", "A-S", ["08:45","12:26","18:15"]),
    
    # LINHA 216
    ("216", "Barcelos(Central)", "IDA", "A-U", ["11:30","13:30","19:00"]),
    ("216", "Barcelos(Central)", "IDA", "A-S", ["07:40"]),
    ("216", "Esposende(Central)", "IDA", "A-U", ["12:20","14:20","19:50"]),
    ("216", "Esposende(Central)", "IDA", "A-S", ["08:45"]),
    ("216", "Esposende(Central)", "VOLTA", "A-U", ["06:50","12:20","13:30","17:55"]),
    ("216", "Barcelos(Central)", "VOLTA", "A-U", ["14:20","18:45"]),
    ("216", "Esposende(Central)", "VOLTA", "A-S", ["19:15"]),
]

NOMES_LINHAS = {
    "212": "Braga - Barcelos (por Martim)",
    "213": "Braga - Barcelos (por Prado)",
    "214": "Braga - Barcelos IPCA (por A11)",
    "215": "Barcelos - Apúlia (por Esposende)",
    "216": "Barcelos - Esposende (por Vila Seca)"
}

DESCRICOES_TIPOS_DIA = {
    "A-U": "Dias Úteis (Segunda a Sexta)",
    "A-S": "Sábados",
    "A-DF": "Domingos e Feriados",
    "E-U": "Escolar - Dias Úteis",
    "FE-U": "Férias Escolares",
    "EUI-U": "IPCA - Época Escolar",
    "EXI-U": "IPCA - Época de Exames",
    "PPI-U": "IPCA - Pausa Letiva",
    "AXI-S": "IPCA - Sábados"
}

def get_linhas():
    return sorted(list(set([d[0] for d in DADOS])))

def get_paragens(linha, direcao):
    if direcao == "Ambas":
        paragens = sorted(list(set([d[1] for d in DADOS if d[0] == linha])))
    else:
        paragens = sorted(list(set([d[1] for d in DADOS if d[0] == linha and d[2] == direcao])))
    return paragens

def get_direcoes(linha):
    direcoes = sorted(list(set([d[2] for d in DADOS if d[0] == linha])))
    return direcoes

def get_tipos_dia(linha, paragem, direcao):
    if direcao == "Ambas":
        tipos = sorted(list(set([d[3] for d in DADOS if d[0] == linha and d[1] == paragem])))
    else:
        tipos = sorted(list(set([d[3] for d in DADOS if d[0] == linha and d[1] == paragem and d[2] == direcao])))
    return tipos

def tem_fim_de_semana(linha, paragem, direcao):
    """Verifica se a paragem tem horários ao fim de semana"""
    tipos = get_tipos_dia(linha, paragem, direcao)
    tem_sabado = "A-S" in tipos
    tem_domingo = "A-DF" in tipos
    return tem_sabado or tem_domingo

def get_horarios(linha, paragem, direcao, tipo_dia, hora_atual):
    resultados = []
    for d in DADOS:
        if d[0] != linha:
            continue
        if d[1] != paragem:
            continue
        if direcao != "Ambas" and d[2] != direcao:
            continue
        if d[3] != tipo_dia:
            continue
        
        horarios_filtrados = [h for h in d[4] if h >= hora_atual]
        
        if horarios_filtrados:
            resultados.append({
                "linha": d[0],
                "paragem": d[1],
                "direcao": d[2],
                "tipo_dia": d[3],
                "horarios": horarios_filtrados
            })
    
    return resultados

# INTERFACE
st.set_page_config(page_title="Horários TUB", page_icon="🚌", layout="wide")

st.title("🚌 Horários TUB")
st.markdown("Linhas 212, 213, 214, 215 e 216")

agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
dia_semana = agora.strftime("%A")
st.info(f"🕒 Hora atual: **{hora_atual}** | {agora.strftime('%d/%m/%Y')}")

st.markdown("---")

# SELEÇÃO DE LINHA
st.subheader("1️⃣ Escolha a Linha")
linhas = get_linhas()

opcoes_linhas = []
for linha in linhas:
    nome = NOMES_LINHAS.get(linha, linha)
    opcoes_linhas.append(f"{linha} - {nome}")

linha_sel_display = st.selectbox("Qual linha quer consultar?", opcoes_linhas)
linha_codigo = linha_sel_display.split(" - ")[0]

st.success(f"**Linha {linha_codigo}:** {NOMES_LINHAS.get(linha_codigo, '')}")
st.markdown("---")

# SELEÇÃO DE DIREÇÃO
st.subheader("2️⃣ Escolha a Direção")
direcoes = get_direcoes(linha_codigo)

opcoes_direcao = {}
for d in direcoes:
    if d == "IDA":
        opcoes_direcao["IDA (partida do início da linha)"] = "IDA"
    else:
        opcoes_direcao["VOLTA (regresso ao início)"] = "VOLTA"

if len(direcoes) > 1:
    direcao_sel_display = st.selectbox("Qual a direção?", list(opcoes_direcao.keys()))
    direcao_sel = opcoes_direcao[direcao_sel_display]
else:
    direcao_sel = direcoes[0]

st.markdown("---")

# SELEÇÃO DE PARAGEM
st.subheader("3️⃣ Escolha a Paragem")
paragens = get_paragens(linha_codigo, direcao_sel)
paragem_sel = st.selectbox("Onde vai apanhar o autocarro?", paragens)

# Verificar se tem fim de semana
tem_fds = tem_fim_de_semana(linha_codigo, paragem_sel, direcao_sel)

if not tem_fds:
    st.warning(f"⚠️ **Atenção:** A paragem **{paragem_sel}** só tem horários em **dias úteis** (A-U). Não há serviço ao sábado ou domingo.")
    
    # Sugerir paragens com fim de semana
    paragens_fds = [p for p in paragens if tem_fim_de_semana(linha_codigo, p, direcao_sel)]
    if paragens_fds:
        st.info(f"💡 **Paragens com serviço ao fim de semana:** {', '.join(paragens_fds[:3])}")
else:
    st.success(f"✅ Esta paragem tem horários ao **fim de semana**!")

st.markdown("---")

# SELEÇÃO DE TIPO DE DIA
st.subheader("4️⃣ Tipo de Dia")
tipos_dia = get_tipos_dia(linha_codigo, paragem_sel, direcao_sel)

# Mostrar badges com os tipos disponíveis
st.markdown("**Tipos de dia disponíveis para esta paragem:**")
cols = st.columns(len(tipos_dia))
for idx, tipo in enumerate(tipos_dia):
    with cols[idx]:
        descricao = DESCRICOES_TIPOS_DIA.get(tipo, tipo)
        if tipo in ["A-S", "A-DF"]:
            st.markdown(f"""
            <div style="background-color: #28a745; color: white; padding: 0.5rem; border-radius: 5px; text-align: center;">
                <strong>{tipo}</strong><br>
                <small>{descricao}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background-color: #007bff; color: white; padding: 0.5rem; border-radius: 5px; text-align: center;">
                <strong>{tipo}</strong><br>
                <small>{descricao}</small>
            </div>
            """, unsafe_allow_html=True)

opcoes_tipos = []
for tipo in tipos_dia:
    descricao = DESCRICOES_TIPOS_DIA.get(tipo, tipo)
    opcoes_tipos.append(f"{tipo} - {descricao}")

tipo_dia_sel_display = st.selectbox("Que tipo de dia é hoje?", opcoes_tipos)
tipo_dia_codigo = tipo_dia_sel_display.split(" - ")[0]

st.markdown("---")

# RESULTADOS
st.subheader(f"🕐 Próximos Horários - {paragem_sel}")

st.markdown(f"""
<div style="padding: 1rem; border-radius: 8px; background-color: #f0f2f6; margin-bottom: 1rem;">
    <strong>🚌 Linha:</strong> {linha_codigo} - {NOMES_LINHAS.get(linha_codigo, '')}<br>
    <strong>📍 Paragem:</strong> {paragem_sel}<br>
    <strong>🧭 Direção:</strong> {direcao_sel}<br>
    <strong>📅 Tipo:</strong> {tipo_dia_sel_display}<br>
    <strong>🕒 A partir das:</strong> {hora_atual}
</div>
""", unsafe_allow_html=True)

resultados = get_horarios(linha_codigo, paragem_sel, direcao_sel, tipo_dia_codigo, hora_atual)

if resultados:
    total_horarios = sum(len(r["horarios"]) for r in resultados)
    st.success(f"✅ Encontrados {total_horarios} horários disponíveis")
    
    todos_horarios = []
    for r in resultados:
        for hora in r["horarios"]:
            todos_horarios.append({
                "linha": r["linha"],
                "nome_linha": NOMES_LINHAS.get(r["linha"], ""),
                "direcao": r["direcao"],
                "hora": hora
            })
    
    dados_tabela = []
    for h in todos_horarios:
        dados_tabela.append({
            "Linha": f"{h['linha']} - {h['nome_linha']}",
            "Direção": h["direcao"],
            "Hora": h["hora"]
        })
    
    st.table(dados_tabela)
    
    if len(todos_horarios) >= 1:
        st.markdown("### 🎯 Próximas 3 passagens:")
        cols = st.columns(3)
        for i in range(min(3, len(todos_horarios))):
            with cols[i]:
                hora = todos_horarios[i]["hora"]
                linha = todos_horarios[i]["linha"]
                direcao = todos_horarios[i]["direcao"]
                
                st.markdown(f"""
                <div style="background-color: #d4edda; padding: 1rem; border-radius: 8px; text-align: center; margin-bottom: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: bold; color: #155724;">
                        {hora}
                    </div>
                    <div style="color: #155724; font-weight: bold;">
                        Linha {linha}
                    </div>
                    <div style="font-size: 0.9rem; color: #155724;">
                        {direcao}
                    </div>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning(f"⚠️ Não há mais passagens hoje para esta paragem ({tipo_dia_sel_display}) a partir das {hora_atual}.")
    st.info("💡 Tente consultar outro tipo de dia ou outra paragem.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; background-color: #fff3cd; border-radius: 8px;">
    <strong>⚠️ Importante:</strong><br>
    Chegue às paragens com <strong>10 minutos de antecedência</strong>.<br>
    Podem ocorrer alterações devido a acidentes, obras ou outros fatores.<br><br>
    <em>📅 Dados de 28/07/2026</em>
</div>
""", unsafe_allow_html=True)
