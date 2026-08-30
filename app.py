import streamlit as st
from datetime import datetime

# ============================================
# DADOS EMBUTIDOS
# ============================================
DADOS = [
    # LINHA 212
    ("212", "Braga(Central)", "IDA", "A-U", ["06:30","07:05","08:30","09:30","10:30","14:20","17:30","18:15","19:20"]),
    ("212", "Braga(Bairro de Baixo)", "IDA", "A-U", ["06:39","07:14","08:39","09:39","10:39","14:29","17:39","18:24","19:29"]),
    ("212", "Martim(Pousada)", "IDA", "A-U", ["06:49","07:24","08:49","09:49","10:49","14:39","17:49","18:34","19:39"]),
    ("212", "Encourados(Almas)", "IDA", "A-U", ["06:52","07:27","08:52","09:52","10:52","14:42","17:52","18:37","19:42"]),
    ("212", "Gamil(Moinhos)", "IDA", "A-U", ["07:00","07:35","09:00","10:00","11:00","14:50","18:00","18:45","19:50"]),
    ("212", "Barcelinhos(Colégio La Salle)", "IDA", "A-U", ["07:04","07:39","09:04","10:04","11:04","14:54","18:04","18:49","19:54"]),
    ("212", "Vila Frescaínha(R. de São Simão)", "IDA", "A-U", ["07:11","07:46","09:11","10:11","11:11","15:01","18:11","18:56","20:01"]),
    ("212", "Barcelos(São José)", "IDA", "A-U", ["07:14","07:49","09:14","10:15","11:14","15:04","18:15","19:00","20:04"]),
    ("212", "Barcelos(Central)", "IDA", "A-U", ["07:25","08:00","09:25","10:26","11:25","15:15","18:26","19:11","20:15"]),
    ("212", "Braga(Central)", "IDA", "A-S", ["08:15","11:45","14:10"]),
    ("212", "Barcelos(Central)", "IDA", "A-S", ["09:05","12:35","15:00"]),
    ("212", "Braga(Central)", "IDA", "A-DF", ["08:15","13:00","18:00"]),
    ("212", "Barcelos(Central)", "IDA", "A-DF", ["09:05","13:50","18:50"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-U", ["07:00","08:05","08:25","09:30","10:30","13:35","14:15","16:00","16:55","18:00","18:30","19:20"]),
    ("212", "Vila Frescaínha(R. de São Simão)", "VOLTA", "A-U", ["07:09","08:14","08:34","09:39","10:39","13:44","14:24","16:09","17:04","18:09","18:39","19:29"]),
    ("212", "Barcelinhos(Colégio La Salle)", "VOLTA", "A-U", ["07:16","08:21","08:41","09:46","10:46","13:51","14:31","16:16","17:11","18:16","18:46","19:36"]),
    ("212", "Gamil(Moinhos)", "VOLTA", "A-U", ["07:21","08:26","08:46","09:51","10:51","13:56","14:36","16:21","17:16","18:21","18:51","19:41"]),
    ("212", "Martim(Pousada)", "VOLTA", "A-U", ["07:35","08:40","09:00","10:05","11:05","14:10","14:50","16:35","17:30","18:35","19:05","19:55"]),
    ("212", "Braga(Central)", "VOLTA", "A-U", ["07:55","09:00","09:20","10:25","11:25","14:30","15:10","16:55","17:50","18:55","19:25","20:15"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-S", ["07:25","10:00","12:35","18:30"]),
    ("212", "Braga(Central)", "VOLTA", "A-S", ["08:15","10:50","13:25","19:20"]),
    ("212", "Barcelos(Central)", "VOLTA", "A-DF", ["10:35","12:00","18:30"]),
    ("212", "Braga(Central)", "VOLTA", "A-DF", ["11:25","12:50","19:20"]),
    
    # LINHA 213
    ("213", "Braga(Central)", "IDA", "A-U", ["06:30","07:00","08:00","09:00","10:00","11:15","12:15","13:05","14:05","15:05","16:05","17:10","18:10","19:10"]),
    ("213", "Merelim São Paio(Ponte)", "IDA", "A-U", ["06:47","07:17","08:17","09:17","10:17","11:32","12:32","13:22","14:22","15:22","16:22","17:27","18:27","19:27"]),
    ("213", "Prado(Bom Sucesso)", "IDA", "A-U", ["06:48","07:18","08:18","09:18","10:18","11:33","12:33","13:23","14:23","15:23","16:23","17:28","18:28","19:28"]),
    ("213", "Cruto(Faial)", "IDA", "A-U", ["06:53","07:25","08:25","09:25","10:25","11:40","12:40","13:30","14:30","15:30","16:30","17:35","18:35","19:35"]),
    ("213", "Ucha(Igreja)", "IDA", "A-U", ["06:57","07:29","08:29","09:29","10:29","11:44","12:44","13:34","14:34","15:34","16:34","17:39","18:39","19:39"]),
    ("213", "Lama(Igreja)", "IDA", "A-U", ["07:03","07:34","08:34","09:34","10:34","11:49","12:49","13:39","14:39","15:39","16:39","17:44","18:44","19:44"]),
    ("213", "Galegos São Martinho(Padre Paulino)", "IDA", "A-U", ["07:09","07:39","08:39","09:39","10:39","11:54","12:54","13:44","14:44","15:44","16:44","17:49","18:49","19:49"]),
    ("213", "Manhente(EB23)", "IDA", "A-U", ["07:10","07:40","08:40","09:40","10:40","11:55","12:55","13:45","14:45","15:45","16:45","17:50","18:50","19:50"]),
    ("213", "Barcelos(Bagoeira)", "IDA", "A-U", ["07:22","07:50","08:50","09:50","10:50","12:05","13:05","13:55","14:55","15:55","16:55","18:00","19:00","20:00"]),
    ("213", "Barcelos(Central)", "IDA", "A-U", ["07:30","08:00","09:00","10:00","11:00","12:15","13:15","14:05","15:05","16:05","17:05","18:10","19:10","20:10"]),
    ("213", "Braga(Central)", "IDA", "A-S", ["08:00","09:00","12:00","14:30","17:10"]),
    ("213", "Barcelos(Central)", "IDA", "A-S", ["09:00","10:00","13:00","15:30","18:10"]),
    ("213", "Braga(Central)", "IDA", "A-DF", ["13:00","14:45","19:50"]),
    ("213", "Barcelos(Central)", "IDA", "A-DF", ["13:50","15:35","20:40"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-U", ["06:45","07:30","08:50","10:15","11:10","12:15","13:10","14:05","15:05","16:05","17:20","18:15","19:05"]),
    ("213", "Barcelos(Bagoeira)", "VOLTA", "A-U", ["06:52","07:37","08:57","10:22","11:17","12:22","13:17","14:12","15:12","16:12","17:27","18:22","19:12"]),
    ("213", "Lama(Igreja)", "VOLTA", "A-U", ["07:11","07:56","09:16","10:41","11:36","12:41","13:36","14:31","15:31","16:31","17:46","18:41","19:31"]),
    ("213", "Prado(Bom Sucesso)", "VOLTA", "A-U", ["07:28","08:13","09:33","10:58","11:53","12:58","13:53","14:48","15:48","16:48","18:03","18:58","19:48"]),
    ("213", "Braga(Central)", "VOLTA", "A-U", ["07:45","08:30","09:50","11:15","12:10","13:15","14:10","15:05","16:05","17:05","18:20","19:15","20:05"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-S", ["07:40","10:30","13:05","16:05","19:15"]),
    ("213", "Braga(Central)", "VOLTA", "A-S", ["08:40","11:30","14:05","17:05","20:15"]),
    ("213", "Barcelos(Central)", "VOLTA", "A-DF", ["13:50","17:00","19:00"]),
    ("213", "Braga(Central)", "VOLTA", "A-DF", ["14:40","17:50","19:50"]),
    
    # LINHA 214
    ("214", "Braga(Central)", "IDA", "EUI-U", ["08:25","09:00","10:30","13:35","16:35","17:20","17:55","19:00","21:30","22:30"]),
    ("214", "Barcelos(IPCA)", "IDA", "EUI-U", ["09:00","09:30","11:00","14:00","17:05","17:50","18:25","19:30","21:55","22:55"]),
    ("214", "Barcelos(IPCA)", "VOLTA", "EUI-U", ["08:10","09:00","12:45","13:05","16:05","17:05","17:35","18:05","18:30","20:30","22:00","22:55"]),
    ("214", "Braga(Central)", "VOLTA", "EUI-U", ["09:00","09:50","13:35","16:35","17:50","18:35","19:00","21:00","22:30","23:20"]),
    
    # LINHA 215
    ("215", "Barcelos(Central)", "IDA", "A-U", ["08:15","10:30","12:00","13:35","16:30","17:50","18:35","19:15","19:45"]),
    ("215", "Esposende(Central)", "IDA", "A-U", ["07:30","08:48","11:03","12:33","14:08","17:03","18:23","19:08","19:48","20:15"]),
    ("215", "Apúlia(Praia)", "IDA", "A-U", ["07:52","09:10","11:25","12:55","14:30","17:25","18:45","19:30","20:10"]),
    ("215", "Barcelos(Central)", "IDA", "A-S", ["09:10","12:35","18:00"]),
    ("215", "Apúlia(Praia)", "IDA", "A-S", ["10:05","13:30"]),
    ("215", "Apúlia(Praia)", "VOLTA", "A-U", ["07:58","09:17","12:32","14:32","16:02","17:32","19:00","19:45"]),
    ("215", "Esposende(Central)", "VOLTA", "A-U", ["06:59","07:38","08:18","09:02","09:39","12:54","14:52","16:24","17:54","19:21","20:05"]),
    ("215", "Barcelos(Central)", "VOLTA", "A-U", ["07:35","08:15","08:56","09:40","10:15","13:30","15:30","17:00","18:30","20:00"]),
    ("215", "Apúlia(Praia)", "VOLTA", "A-S", ["11:42","17:31"]),
    ("215", "Barcelos(Central)", "VOLTA", "A-S", ["08:45","12:26","18:15"]),
    
    # LINHA 216
    ("216", "Barcelos(Central)", "IDA", "A-U", ["11:30","13:30","19:00"]),
    ("216", "Esposende(Central)", "IDA", "A-U", ["12:20","14:20","19:50"]),
    ("216", "Barcelos(Central)", "IDA", "A-S", ["07:40"]),
    ("216", "Esposende(Central)", "IDA", "A-S", ["08:45"]),
    ("216", "Esposende(Central)", "VOLTA", "A-U", ["06:50","12:20","13:30","17:55"]),
    ("216", "Barcelos(Central)", "VOLTA", "A-U", ["14:20","18:45"]),
    ("216", "Esposende(Central)", "VOLTA", "A-S", ["19:15"]),
]

# ============================================
# NOMES E DESCRIÇÕES
# ============================================
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

# ============================================
# FUNÇÕES
# ============================================
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

# ============================================
# INTERFACE
# ============================================
st.set_page_config(page_title="Horários TUB", page_icon="", layout="wide")

# CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .info-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #f0f2f6;
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="main-header">🚌 Horários TUB</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Linhas 212, 213, 214, 215 e 216</div>', unsafe_allow_html=True)

# Hora atual
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
st.info(f"🕒 Hora atual: **{hora_atual}** | {agora.strftime('%d/%m/%Y')}")

st.markdown("---")

# Instruções rápidas
with st.expander("📖 Como usar esta app", expanded=False):
    st.write("""
    1. **Escolha a linha** que pretende consultar
    2. **Selecione a paragem** onde vai apanhar o autocarro
    3. **Escolha a direção** (IDA ou VOLTA)
    4. **Selecione o tipo de dia** (Dias úteis, Sábados, etc.)
    
    A app mostrará automaticamente os próximos horários a partir da hora atual!
    """)

# ============================================
# SELEÇÃO DE LINHA
# ============================================
st.subheader("1️⃣ Escolha a Linha")
linhas = get_linhas()

opcoes_linhas = []
for linha in linhas:
    nome = NOMES_LINHAS.get(linha, linha)
    opcoes_linhas.append(f"{linha} - {nome}")

linha_sel_display = st.selectbox(
    "Qual linha quer consultar?",
    opcoes_linhas,
    label_visibility="collapsed"
)

linha_codigo = linha_sel_display.split(" - ")[0]

# Mostrar info da linha
st.success(f"**Linha {linha_codigo}:** {NOMES_LINHAS.get(linha_codigo, '')}")

st.markdown("---")

# ============================================
# SELEÇÃO DE DIREÇÃO
# ============================================
st.subheader("2️⃣ Escolha a Direção")
direcoes = get_direcoes(linha_codigo)

opcoes_direcao = {}
for d in direcoes:
    if d == "IDA":
        opcoes_direcao["IDA (partida do início da linha)"] = "IDA"
    else:
        opcoes_direcao["VOLTA (regresso ao início)"] = "VOLTA"

if len(direcoes) > 1:
    direcao_sel_display = st.selectbox(
        "Qual a direção?",
        list(opcoes_direcao.keys()),
        label_visibility="collapsed"
    )
    direcao_sel = opcoes_direcao[direcao_sel_display]
else:
    direcao_sel = direcoes[0]
    st.info(f"Direção disponível: {direcao_sel}")

st.markdown("---")

# ============================================
# SELEÇÃO DE PARAGEM
# ============================================
st.subheader("3️⃣ Escolha a Paragem")
paragens = get_paragens(linha_codigo, direcao_sel)

paragem_sel = st.selectbox(
    "Onde vai apanhar o autocarro?",
    paragens,
    label_visibility="collapsed"
)

st.markdown("---")

# ============================================
# SELEÇÃO DE TIPO DE DIA
# ============================================
st.subheader("4️ Tipo de Dia")
tipos_dia = get_tipos_dia(linha_codigo, paragem_sel, direcao_sel)

opcoes_tipos = []
for tipo in tipos_dia:
    descricao = DESCRICOES_TIPOS_DIA.get(tipo, tipo)
    opcoes_tipos.append(f"{tipo} - {descricao}")

tipo_dia_sel_display = st.selectbox(
    "Que tipo de dia é hoje?",
    opcoes_tipos,
    label_visibility="collapsed"
)

tipo_dia_codigo = tipo_dia_sel_display.split(" - ")[0]

st.markdown("---")

# ============================================
# RESULTADOS
# ============================================
st.subheader(f"🕐 Próximos Horários - {paragem_sel}")

# Resumo da pesquisa
st.markdown(f"""
<div class="info-box">
    <strong>🚌 Linha:</strong> {linha_codigo} - {NOMES_LINHAS.get(linha_codigo, '')}<br>
    <strong>📍 Paragem:</strong> {paragem_sel}<br>
    <strong>🧭 Direção:</strong> {direcao_sel}<br>
    <strong>📅 Tipo:</strong> {tipo_dia_sel_display}<br>
    <strong>🕒 A partir das:</strong> {hora_atual}
</div>
""", unsafe_allow_html=True)

# Obter horários
resultados = get_horarios(linha_codigo, paragem_sel, direcao_sel, tipo_dia_codigo, hora_atual)

if resultados:
    total_horarios = sum(len(r["horarios"]) for r in resultados)
    st.success(f"✅ Encontrados {total_horarios} horários disponíveis")
    
    # Criar tabela
    dados_tabela = []
    for r in resultados:
        for hora in r["horarios"]:
            dados_tabela.append({
                " Linha": f"{r['linha']} - {NOMES_LINHAS.get(r['linha'], '')}",
                "🧭 Direção": r["direcao"],
                "🕐 Hora": hora
            })
    
    # Mostrar tabela
    st.table(dados_tabela)
    
    # Destacar próximos 3 (CORREÇÃO DO ERRO)
    if len(dados_tabela) >= 1:
        st.markdown("### 🎯 Próximas 3 passagens:")
        cols = st.columns(3)
        for i in range(min(3, len(dados_tabela))):
            with cols[i]:
                st.markdown(f"""
                <div style="background-color: #d4edda; padding: 1rem; border-radius: 8px; text-align: center;">
                    <div style="font-size: 1.5rem; font-weight: bold; color: #155724;">
                        {dados_tabela[i]['🕐 Hora']}
                    </div>
                    <div style="color: #155724; margin-top: 0.5rem;">
                        {dados_tabela[i]['🚌 Linha'].split(' - ')[0]}
                    </div>
                    <div style="font-size: 0.9rem; color: #155724;">
                        {dados_tabela[i]['🧭 Direção']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
else:
    st.warning(f"⚠️ Não há mais passagens hoje para esta paragem ({tipo_dia_sel_display}) a partir das {hora_atual}.")
    st.info("💡 Tente consultar outro tipo de dia ou outra paragem.")

# ============================================
# RODAPÉ
# ============================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem; background-color: #fff3cd; border-radius: 8px;">
    <strong>⚠️ Importante:</strong><br>
    Chegue às paragens com <strong>10 minutos de antecedência</strong>.<br>
    Podem ocorrer alterações devido a acidentes, obras ou outros fatores.<br><br>
    <em>📅 Dados de 28/07/2026</em>
</div>
""", unsafe_allow_html=True)

# Link para feedback
st.markdown("""
<div style="text-align: center; margin-top: 1rem;">
    <a href="https://horariostub.streamlit.app" target="_blank" style="color: #1f77b4;">
        🔄 Atualizar página
    </a>
</div>
""", unsafe_allow_html=True)
