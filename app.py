import streamlit as st
import random

# Sayfa Konfigürasyonu
st.set_page_config(page_title="PAEM 50 Soru Deneme", page_icon="👮‍♂️")

# CSS Düzenleme
st.markdown("""
    <style>
    .stRadio [role="radiogroup"] { background-color: #f1f3f6; padding: 15px; border-radius: 10px; }
    .stButton>button { width: 100%; font-weight: bold; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 50 SORULUK TAM VERİ SETİ
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # MEVZUAT & RÜTBELER
        {"soru": "3201 ETK'ya göre Komiser Yardımcısı rütbesinde bekleme süresi?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "3201 ETK'ya göre Komiser rütbesinde bekleme süresi?", "secenekler": ["2", "4", "6", "3", "5"], "cevap": "4"},
        {"soru": "3201 ETK'ya göre Başkomiser rütbesinde bekleme süresi?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "3201 ETK'ya göre Emniyet Amiri rütbesinde bekleme süresi?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "2559 PVSK'ya göre durdurulan kişinin üzerinden silah çıkması durumunda polisin yetkisi nedir?", "secenekler": ["Sadece el koyar", "Muhafaza altına alır", "Kişiyi serbest bırakır", "Tutanak tutmaz", "Amire sorar"], "cevap": "Muhafaza altına alır"},
        {"soru": "PVSK Madde 4/A'ya göre durdurma yetkisi neye dayanmalıdır?", "secenekler": ["Makul Sebep", "Yeterli Şüphe", "İhbar", "Somut Delil", "Amir Emri"], "cevap": "Makul Sebep"},
        {"soru": "7068 Disiplin Kanunu'na göre 'Amire Saygısızlık' cezası nedir?", "secenekler": ["Kınama", "Aylıktan Kesme", "Durdurma", "İhraç", "Uyarma"], "cevap": "Aylıktan Kesme"},
        {"soru": "Emniyet Genel Müdürlüğü Yüksek Disiplin Kurulu Başkanı kimdir?", "secenekler": ["İçişleri Bakanı", "EGM", "Personel Daire Bşk", "Teftiş Kurulu Bşk", "Hukuk Müşaviri"], "cevap": "EGM"},
        {"soru": "Polis Akademisi Başkanı kim tarafından atanır?", "secenekler": ["Cumhurbaşkanı", "Bakan", "EGM", "YÖK", "MEB"], "cevap": "Cumhurbaşkanı"},
        {"soru": "657 DMK'ya göre aday memurluk süresi en fazla ne kadardır?", "secenekler": ["1 yıl", "2 yıl", "3 yıl", "4 yıl", "5 yıl"], "cevap": "2 yıl"},
        
        # HUKUK & CMK & TCK
        {"soru": "CMK'ya göre yakalanan kişi kaç saat içinde hakim önüne çıkarılmalıdır?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "24"},
        {"soru": "CMK'ya göre toplu suçlarda gözaltı süresi en fazla kaç gün olabilir?", "secenekler": ["2", "4", "7", "10", "15"], "cevap": "4"},
        {"soru": "TCK'ya göre
