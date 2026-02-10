import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="PAEM 100 Soru Bankası", page_icon="👮")

# --- 100 SORULUK TAM VERİ SETİ ---
if 'questions' not in st.session_state:
    st.session_state.questions = [
        # MEVZUAT & RÜTBELER (1-25)
        {"soru": "3201 ETK'ya göre Komiser Yardımcısı rütbe bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "3201 ETK'ya göre Komiser rütbe bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "3201 ETK'ya göre Başkomiser rütbe bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "3"},
        {"soru": "3201 ETK'ya göre Emniyet Amiri rütbe bekleme süresi kaçtır?", "secenekler": ["2", "3", "4", "5", "6"], "cevap": "4"},
        {"soru": "PVSK Madde 4/A'ya göre durdurma yetkisi neye dayanır?", "secenekler": ["Tecrübe ve Makul Sebep", "Yeterli Şüphe", "Somut Delil", "Amir Emri", "İhbar"], "cevap": "Tecrübe ve Makul Sebep"},
        {"soru": "7068 Disiplin Kanunu'na göre 'Amire Saygısızlık' cezasının karşılığı nedir?", "secenekler": ["Kınama", "Aylıktan Kesme", "Durdurma", "Meslekten Çıkarma", "Uyarma"], "cevap": "Aylıktan Kesme"},
        {"soru": "657 DMK'ya göre aday memurluk süresi en fazla kaçtır?", "secenekler": ["1 yıl", "2 yıl", "3 yıl", "4 yıl", "6 ay"], "cevap": "2 yıl"},
        {"soru": "Polis Akademisi Başkanı kim tarafından atanır?", "secenekler": ["Emniyet Genel Müdürü", "İçişleri Bakanı", "Cumhurbaşkanı", "YÖK Başkanı", "Milli Eğitim Bakanı"], "cevap": "Cumhurbaşkanı"},
        {"soru": "PVSK'ya göre önleme araması kararı mülki amir tarafından verilirse kaç saat içinde hakime sunulur?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "24"},
        {"soru": "7068 sayılı Kanun'a göre disiplin cezalarına karşı kaç gün içinde dava açılabilir?", "secenekler": ["15", "30", "45", "60", "90"], "cevap": "60"},
        {"soru": "EGM Yüksek Disiplin Kurulu Başkanı kimdir?", "secenekler": ["Emniyet Genel Müdürü", "Personel Başkanı", "Teftiş Kurulu Başkanı", "Bakan Yardımcısı", "Hukuk Müşaviri"], "cevap": "Emniyet Genel Müdürü"},
        {"soru": "Polis memurlarının yıllık izin süresi 1-10 yıl arası hizmette kaç gündür?", "secenekler": ["15", "20", "30", "45", "10"], "cevap": "20"},
        {"soru": "657 DMK'ya göre mazeret izni (doğum sonrası) kaç haftadır?", "secenekler": ["4", "8", "12", "16", "20"], "cevap": "16"},
        {"soru": "Emniyet hizmetleri sınıfı mensuplarının emeklilik yaş haddi kural olarak kaçtır?", "secenekler": ["50", "55", "60", "65", "62"], "cevap": "55"},
        {"soru": "7068'e göre uyarma cezasının zamanaşımı süresi ne kadardır?", "secenekler": ["1 ay", "6 ay", "1 yıl", "2 yıl", "5 yıl"], "cevap": "6 ay"},
        {"soru": "Polisin kıyafet yönetmeliğini hangi makam çıkarır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "İçişleri Bakanlığı", "EGM", "Polis Akademisi"], "cevap": "İçişleri Bakanlığı"},
        {"soru": "Çarşı ve Mahalle Bekçileri kime bağlıdır?", "secenekler": ["Belediye", "Valilik", "Emniyet Genel Müdürlüğü", "Jandarma", "İçişleri Bakanlığı"], "cevap": "Emniyet Genel Müdürlüğü"},
        {"soru": "3201'e göre Polis Bakım ve Yardım Sandığı'nın kısa adı nedir?", "secenekler": ["POLSAN", "POLVAK", "EGMVAK", "POYAS", "POLBYS"], "cevap": "POLSAN"},
        {"soru": "7068'e göre 'Yalan beyanda bulunmak' cezası nedir?", "secenekler": ["Kınama", "Durdurma", "Maaş Kesme", "İhraç", "Uyarma"], "cevap": "Durdurma"},
        {"soru": "PVSK'ya göre adli arama kararı gecikmesinde sakınca bulunan hallerde kimden alınır?", "secenekler": ["Vali", "Emniyet Müdürü", "Cumhuriyet Savcısı", "İçişleri Bakanı", "Kaymakam"], "cevap": "Cumhuriyet Savcısı"},
        {"soru": "657'ye göre devlet memuru hediye alabilir mi?", "secenekler": ["Evet", "Hayır", "Amir izniyle", "Sadece bayramda", "Düşük bedelliyse"], "cevap": "Hayır"},
        {"soru": "PVSK Madde 16'ya göre polisin silah kullanma yetkisi hangi durumda doğar?", "secenekler": ["Kaçan her kişiye", "Meşru Müdafaa", "Sözlü uyarıya uymayan her durumda", "Sadece terör suçlarında", "Amir emriyle"], "cevap": "Meşru Müdafaa"},
        {"soru": "Emniyet teşkilatında en üst rütbe hangisidir?", "secenekler": ["Emniyet Müdürü", "Sınıf Üstü Emniyet Müdürü", "Birinci Sınıf Emniyet Müdürü", "Genel Müdür", "Kurul Başkanı"], "cevap": "Sınıf Üstü Emniyet Müdürü"},
        {"soru": "7068'e göre 'Görevin yerine getirilmesinde dil, din, ırk ayrımı yapmak' cezası?", "secenekler": ["Kınama", "Aylıktan Kesme", "Durdurma", "Meslekten Çıkarma", "Uyarma"], "cevap": "Meslekten Çıkarma"},
        {"soru": "Polis Akademisi hangi yıla kadar Emniyet Genel Müdürlüğü'ne bağlıydı?", "secenekler": ["1937", "1984", "2015", "2001", "1990"], "cevap": "1937"},

        # ANAYASA & HUKUK (26-50)
        {"soru": "Anayasa Mahkemesi üye sayısı kaçtır?", "secenekler": ["11", "13", "15", "17", "19"], "cevap": "15"},
        {"soru": "AYM üyelerinin görev süresi kaç yıldır?", "secenekler": ["4", "6", "9", "12", "15"], "cevap": "12"},
        {"soru": "RTÜK üyelerini aşağıdakilerden hangisi seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "İletişim Başkanlığı", "YÖK", "Danıştay"], "cevap": "TBMM"},
        {"soru": "Milli Güvenlik Kurulu'nun başkanı kimdir?", "secenekler": ["Cumhurbaşkanı", "İçişleri Bakanı", "Genelkurmay Başkanı", "MSB", "Cumhurbaşkanı Yardımcısı"], "cevap": "Cumhurbaşkanı"},
        {"soru": "CMK'ya göre gözaltı süresi toplu suçlarda en fazla kaç gündür?", "secenekler": ["2", "4", "7", "12", "15"], "cevap": "4"},
        {"soru": "Yüksek Seçim Kurulu (YSK) kaç asıl üyeden oluşur?", "secenekler": ["5", "7", "9", "11", "13"], "cevap": "7"},
        {"soru": "HSK'nın başkanı kimdir?", "secenekler": ["Yargıtay Başkanı", "Adalet Bakanı", "Danıştay Başkanı", "Cumhurbaşkanı", "AYM Başkanı"], "cevap": "Adalet Bakanı"},
        {"soru": "CMK'ya göre el koyma kararını hakim kaç saat içinde onaylar?", "secenekler": ["12", "24", "48", "72", "96"], "cevap": "48"},
        {"soru": "Tanıklıktan çekinme hakkı CMK'nın kaçıncı maddesinde düzenlenmiştir?", "secenekler": ["45", "50", "60", "75", "100"], "cevap": "45"},
        {"soru": "OHAL süresi bir seferde en fazla kaç ay olabilir?", "secenekler": ["2", "4", "6", "9", "12"], "cevap": "6"},
        {"soru": "TBMM seçimleri kaç yılda bir yapılır?", "secenekler": ["3", "4", "5", "6", "7"], "cevap": "5"},
        {"soru": "Milletvekili seçilme yaşı kaçtır?", "secenekler": ["18", "21", "25", "30", "40"], "cevap": "18"},
        {"soru": "Anayasaya göre HSK kaç üyeden oluşur?", "secenekler": ["11", "13", "15", "17", "21"], "cevap": "13"},
        {"soru": "Siyasi partilerin kapatılması davasını kim açar?", "secenekler": ["Yargıtay Başsavcısı", "AYM Başkanı", "Adalet Bakanı", "Cumhurbaşkanı", "TBMM Başkanı"], "cevap": "Yargıtay Başsavcısı"},
        {"soru": "Devlet Denetleme Kurulu kime bağlıdır?", "secenekler": ["TBMM", "Cumhurbaşkanı", "Sayıştay", "Danıştay", "YÖK"], "cevap": "Cumhurbaşkanı"},
        {"soru": "AYM üyelerinin yaş haddi kaçtır?", "secenekler": ["60", "65", "67", "70", "72"], "cevap": "65"},
        {"soru": "Kamu Başdenetçisini kim seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "Danıştay", "Yargıtay", "HSK"], "cevap": "TBMM"},
        {"soru": "Uyuşmazlık Mahkemesi Başkanı hangi kurumdan seçilir?", "secenekler": ["AYM", "Yargıtay", "Danıştay", "Sayıştay", "Askeri Yargıtay"], "cevap": "AYM"},
        {"soru": "TCK'ya göre 'Kasten Öldürme' suçunun temel cezası nedir?", "secenekler": ["Ağırlaştırılmış Müebbet", "Müebbet", "20 Yıl", "25 Yıl", "Müebbet Hapis"], "cevap": "Müebbet"},
        {"soru": "CMK 100. madde konusu nedir?", "secenekler": ["Gözaltı", "Tutuklama", "Arama", "Tanıklık", "El koyma"], "cevap": "Tutuklama"},
        {"soru": "Savunma hakkı anayasanın kaçıncı maddesinde düzenlenmiştir?", "secenekler": ["36", "38", "40", "42", "45"], "cevap": "36"},
        {"soru": "Bakanlıkların kurulması ne ile olur?", "secenekler": ["Kanun", "Yönetmelik", "CB Kararnamesi", "Tüzük", "Genelge"], "cevap": "CB Kararnamesi"},
        {"soru": "Sayıştay üyelerini kim seçer?", "secenekler": ["Cumhurbaşkanı", "TBMM", "Yargıtay", "Danıştay", "Sayıştay Genel Kurulu"], "cevap": "TBMM"},
        {"soru": "CMK'ya göre adli tatil ne zaman biter?", "secenekler": ["20 Temmuz", "31 Ağustos", "1 Eylül", "5 Eylül", "15 Ağustos"], "cevap": "31 Ağustos"},
        {"soru": "Cumhurbaşkanı seçilme yaşı kaçtır?", "secenekler": ["18", "25", "30", "40", "45"], "cevap": "40"},

        # TARİH, GÜNCEL & GENEL KÜLTÜR (51-100)
        {"soru": "Alper Gezeravcı'nın rütbesi nedir?", "secenekler": ["Binbaşı", "Yarbay", "Albay", "Yüzbaşı", "Astsubay"], "cevap": "Albay"},
        {"soru": "2024 Avrupa Futbol Şampiyonası nerede yapıldı?", "secenekler": ["Türkiye", "Almanya", "Fransa", "İngiltere", "İtalya"], "cevap": "Almanya"},
        {"soru": "Lozan Antlaşması hangi yıl imzalanmıştır?", "secenekler": ["1920", "1921", "1922", "1923", "1924"], "cevap": "1923"},
        {"soru": "İstiklal Marşı'nın bestecisi kimdir?", "secenekler": ["M. Akif Ersoy", "Osman Zeki Üngör", "Ziya Gökalp", "Cemal Reşit Rey", "Yahya Kemal"], "cevap": "Osman Zeki Üngör"},
        {"soru": "Türkiye'nin en yüksek dağı hangisidir?", "secenekler": ["Erciyes", "Süphan", "Ağrı", "Kaçkar", "Nemrut"], "cevap": "Ağrı"},
        {"soru": "Nutuk hangi yılları kapsar?", "secenekler": ["1919-1923", "1919-1927", "1923-1938", "1915-1920", "1920-1930"], "cevap": "1919-1927"},
        {"soru": "Türk Bayrağı Kanunu yılı?", "secenekler": ["1923", "1936", "1983", "1924", "1950"], "cevap": "1983"},
        {"soru": "Mavi Vatan doktrini neyi kapsar?", "secenekler": ["Kara suları", "Kıta Sahanlığı", "Münhasır Ekonomik Bölge", "Hepsi", "Sadece adalar"], "cevap": "Hepsi"},
        {"soru": "Savunma sanayi projesi 'KAAN' nedir?", "secenekler": ["Tank", "İHA", "Savaş Uçağı", "Gemi", "Füze"], "cevap": "Savaş Uçağı"},
        {"soru": "Türkiye'nin en büyük gölü hangisidir?", "secenekler": ["Van Gölü", "Tuz Gölü", "Beyşehir", "Eğirdir", "İznik"], "cevap": "Van Gölü"},
        {"soru": "Hatay'ın ana vatana katıldığı yıl?", "secenekler": ["1923", "1938", "1939", "1940", "1924"], "cevap": "1939"},
        {"soru": "Dünyanın en derin noktası neresidir?", "secenekler": ["Mariana Çukuru", "Hazar Denizi", "Buz Denizi", "Nil Deltası", "Atlas Okyanusu"], "cevap": "Mariana Çukuru"},
        {"soru": "İlk kadın vali kimdir?", "secenekler": ["Lale Aytaman", "Tansu Çiller", "Meral Akşener", "Fatma Şahin", "Güler İleri"], "cevap": "Lale Aytaman"},
        {"soru": "İstiklal Yolu hangi iller arasındadır?", "secenekler": ["Ankara-İzmir", "İnebolu-Ankara", "İstanbul-Ankara", "Samsun-Erzurum", "Sivas-Ankara"], "cevap": "İnebolu-Ankara"},
        {"soru": "UNESCO Dünya Mirası listesine en son giren yerimiz (2023)?", "secenekler": ["Gordion", "Göbeklitepe", "Efes", "Ani Harabeleri", "Arslantepe"], "cevap": "Gordion"},
        {"soru": "Karasuları genişliği kural olarak kaç mildir?", "secenekler": ["3", "6", "12", "24", "200"], "cevap": "6"},
        {"soru": "İlk Türk kadın opera sanatçısı?", "secenekler": ["Semiha Berksoy", "Safiye Ayla", "Müzeyyen Senar", "Leyla Gencer", "Suna Kan"], "cevap": "Semiha Berksoy"},
        {"soru": "Nobel Edebiyat Ödülü alan ilk Türk yazar?", "secenekler": ["Yaşar Kemal", "Orhan Pamuk", "Aziz Nesin", "Elif Şafak", "Nazım Hikmet"], "cevap": "Orhan Pamuk"},
        {"soru": "2024 Avrupa Konseyi Dönem Başkanı?", "secenekler": ["Macaristan", "Belçika", "İspanya", "Türkiye", "Polonya"], "cevap": "Macaristan"},
        {"soru": "En çok sınır komşumuz olan ülke?", "secenekler": ["Irak", "İran", "Suriye", "Yunanistan", "Bulgaristan"], "cevap": "Suriye"},
        {"soru": "TC'nin ilk Cumhurbaşkanı?", "secenekler": ["İsmet İnönü", "M. Kemal Atatürk", "Celal Bayar", "Fevzi Çakmak", "Kazım Karabekir"], "cevap": "M. Kemal Atatürk"},
        {"soru": "Türkiye'nin ilk yerli otomobili?", "secenekler": ["Anadol", "Devrim", "Togg", "Murat 124", "Şahin"], "cevap": "Devrim"},
        {"soru": "Milli Mücadele'de ilk kurşunu kim atmıştır?", "secenekler": ["Hasan Tahsin", "Kara Fatma", "Sütçü İmam", "Mehmet Çavuş", "Şahin Bey"], "cevap": "Mehmet Çavuş"},
        {"soru": "Atatürk'ün naaşının Anıtkabir'e nakledildiği yıl?", "secenekler": ["1938", "1945", "1953", "1960", "1939"], "cevap": "1953"},
        {"soru": "İzmir'de Yunanlılara ilk kurşunu kim atmıştır?", "secenekler": ["Hasan Tahsin", "Sütçü İmam", "Şahin Bey", "Yörük Ali Efe", "Demirci Efe"], "cevap": "Hasan Tahsin"},
        {"soru": "Erzurum Kongresi Başkanı kimdir?", "secenekler": ["Mustafa Kemal", "Rauf Orbay", "Kazım Karabekir", "İsmet İnönü", "Refet Bele"], "cevap": "Mustafa Kemal"},
        {"soru": "Dünya Sağlık Örgütü (WHO) merkezi neresidir?", "secenekler": ["New York", "Paris", "Cenevre", "Londra", "Roma"], "cevap": "Cenevre"},
        {"soru": "G-20 zirvesi 2024 yılında nerede yapılmıştır?", "secenekler": ["Brezilya", "Hindistan", "Türkiye", "ABD", "Endonezya"], "cevap": "Brezilya"},
        {"soru": "TC Anayasası'na göre mülkiyet hakkı ne ile kısıtlanabilir?", "secenekler": ["CB Kararnamesi", "Kanun", "Yönetmelik", "Tüzük", "Genelge"], "cevap": "Kanun"},
        {"soru": "NATO'ya en son katılan üye ülke hangisidir?", "secenekler": ["Finlandiya", "İsveç", "Ukrayna", "Makedonya", "Arnavutluk"], "cevap": "İsveç"},
        {"soru": "Türk lirasından 6 sıfır ne zaman atıldı?", "secenekler": ["2000", "2005", "2010", "1995", "2002"], "cevap": "2005"},
        {"soru": "Türkiye'nin en uzun nehri (kendi topraklarımızda)?", "secenekler": ["Fırat", "Dicle", "Kızılırmak", "Sakarya", "Seyhan"], "cevap": "Kızılırmak"},
        {"soru": "İlk kadın Başbakanımız?", "secenekler": ["Lale Aytaman", "Tansu Çiller", "Meral Akşener", "Güler Sabancı", "Türkan Saylan"], "cevap": "Tansu Çiller"},
        {"soru": "Sinekli Bakkal romanının yazarı?", "secenekler": ["Halide Edip Adıvar", "Reşat Nuri", "Yakup Kadri", "Peyami Safa", "Orhan Kemal"], "cevap": "Halide Edip Adıvar"},
        {"soru": "Dede Korkut hikayeleri kaç tanedir?", "secenekler": ["10", "12", "13", "15", "20"], "cevap": "13"},
        {"soru": "TBMM kaç yılında açılmıştır?", "secenekler": ["1919", "1920", "1921", "1922", "1923"], "cevap": "1920"},
        {"soru": "Mudanya Ateşkes Antlaşması'na kim katılmamıştır?", "secenekler": ["İngiltere", "Fransa", "İtalya", "Yunanistan", "Türkiye"], "cevap": "Yunanistan"},
        {"soru": "Cumhuriyetçilik ilkesinin en önemli tamamlayıcısı nedir?", "secenekler": ["Milliyetçilik", "Laiklik", "Halkçılık", "Ulusal Egemenlik", "Devletçilik"], "cevap": "Ulusal Egemenlik"},
        {"soru": "Anayasa Mahkemesi ne zaman kurulmuştur?", "secenekler": ["1924", "1961", "1982", "1945", "1950"], "cevap": "1961"},
        {"soru": "Sayıştay Başkanı kaç yıl için seçilir?", "secenekler": ["4", "5", "6", "10", "12"], "cevap": "5"},
        {"soru": "Uluslararası Ceza Mahkemesi (UCM) nerededir?", "secenekler": ["Lahey", "Strazburg", "Brüksel", "Viyana", "Berlin"], "cevap": "Lahey"},
        {"soru": "Modern Olimpiyatlar ilk kez nerede yapıldı?", "secenekler": ["Atina", "Paris", "Londra", "Roma", "Berlin"], "cevap": "Atina"},
        {"soru": "İnsan Hakları Evrensel Bildirgesi hangi yıl kabul edildi?", "secenekler": ["1945", "1948", "1950", "1954", "1960"], "cevap": "1948"},
        {"soru": "Ayasofya hangi yıl müze statüsünden çıkarılıp cami oldu?", "secenekler": ["2018", "2019", "2020", "2021", "2022"], "cevap": "2020"},
        {"soru": "TC'de tek dereceli seçim sistemine ne zaman geçildi?", "secenekler": ["1923", "1946", "1950", "1924", "1930"], "cevap": "1946"},
        {"soru": "TC'nin ilk anayasası hangisidir?", "secenekler": ["1876", "1921", "1924", "1961", "1982"], "cevap": "1921"},
        {"soru": "Sivil Savunma Teşkilatı kime bağlıdır?", "secenekler": ["EGM", "AFAD", "Jandarma", "TSK", "Milli Savunma"], "cevap": "AFAD"},
        {"soru": "Emniyet Genel Müdürlüğü hangi bakanlığa bağlıdır?", "secenekler": ["MSB", "Adalet", "İçişleri", "Dışişleri", "CB"], "cevap": "İçişleri"},
        {"soru": "Sevr Antlaşması nerede imzalanmıştır?", "secenekler": ["Paris", "Sévres", "Londra", "Lozan", "Versay"], "cevap": "Sévres"},
        {"soru": "Mustafa Kemal'e 'Atatürk' soyadı hangi yıl verildi?", "secenekler": ["1923", "1930", "1934", "1938", "1924"], "cevap": "1934"}
    ]
    random.shuffle(st.session_state.questions)

# --- UYGULAMA MOTORU ---
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'skor' not in st.session_state: st.session_state.skor = 0

st.title("🚓 PAEM 100 SORU BANKASI")

if st.session_state.idx < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.idx]
    st.progress((st.session_state.idx + 1) / len(st.session_state.questions))
    
    st.subheader(f"Soru {st.session_state.idx + 1} / 100")
    st.info(q['soru'])
    
    secim = st.radio("Cevap Şıkları:", q['secenekler'], key=f"q_{st.session_state.idx}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Cevabı Onayla ✅"):
            if secim == q['cevap']:
                st.success("Tebrikler, Doğru! ✨")
                st.session_state.skor += 1
            else:
                st.error(f"Yanlış! ❌ Doğru: {q['cevap']}")
    
    with col2:
        if st.button("Sonraki Soru ➡️"):
            st.session_state.idx += 1
            st.rerun()
else:
    st.balloons()
    st.header("🏁 Sınav Tamamlandı!")
    st.metric("Toplam Puan", f"{st.session_state.skor} / 100")
    st.write(f"Başarı Oranı: %{(st.session_state.skor / 100) * 100:.2f}")
    if st.button("Sınavı Baştan Başlat 🔄"):
        st.session_state.idx = 0
        st.session_state.skor = 0
        random.shuffle(st.session_state.questions)
        st.rerun()
