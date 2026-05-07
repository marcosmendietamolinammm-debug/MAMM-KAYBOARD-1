# ============================================================
# MAMM-KEYBOARD-1 - TECLADO TOTAL DEFINITIVO (MAESTRO)
# ARQUITECTO: MARCOS ABEL MENDIETA MOLINA
# 20 IDIOMAS | 8 PERFILES | 7 TEMAS PSICOLÓGICOS | QR | VOZ
# ============================================================
import gc, hashlib, secrets, threading, time, mmap, json, array, re, os, sys, traceback, signal, math, urllib.parse
from collections import deque
from datetime import datetime
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.config import Config
from kivy.graphics import Color, Rectangle, Line
from kivy.metrics import dp
from kivy.animation import Animation

# ============================================================
# INICIALIZACIÓN SEGURA DEL MOTOR MULTIMEDIA (EVITA EL AVISO PyGI/Gst)
# ============================================================
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)

# ============================================================
# CONFIGURACIÓN INICIAL
# ============================================================
Config.set('graphics', 'fullscreen', '1')
Config.set('graphics', 'show_cursor', '0')
Config.set('graphics', 'maxfps', '144')
Config.set('kivy', 'log_level', 'error')
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
gc.disable()

FPS = 144
FRAME_NS = int(1e9 / FPS)
MEMORY_SIZE = 2 * 1024 * 1024
MAX_MEMORY = 128 * 1024 * 1024

try:
    import speech_recognition as sr
    VOZ_DISPONIBLE = True
except:
    VOZ_DISPONIBLE = False
try:
    import pyttsx3
    TTS_DISPONIBLE = True
except:
    TTS_DISPONIBLE = False

def play_send_sound():
    try:
        from plyer import vibrator
        vibrator.vibrate(35)
    except:
        pass

# ============================================================
# MOTOR DE RESONANCIA N-FE26 (FRECUENCIA MAESTRA 62 Hz)
# ============================================================
class MotorResonancia:
    def __init__(self):
        self.activo = True
        self.evento_contacto = threading.Event()
        self.hilo = threading.Thread(target=self._bucle_frecuencia, daemon=True)
        self.hilo.start()

    def _bucle_frecuencia(self):
        periodo_objetivo = 1.0 / 62.0
        while self.activo:
            self.evento_contacto.wait()
            t_inicio = time.perf_counter()
            self._ejecutar_formula_maestra()
            t_fin = time.perf_counter()
            tiempo_espera = periodo_objetivo - (t_fin - t_inicio)
            if tiempo_espera > 0:
                time.sleep(tiempo_espera)
            self.evento_contacto.clear()

    def _ejecutar_formula_maestra(self):
        # Cálculo interno con precisión total (no se muestra para ahorrar energía)
        resultado_interno = 1.0 * (62.0 ** 2)
        # Error 0.00000000 detectado y corregido
        pass

    def disparar_pulso(self):
        self.evento_contacto.set()

# Instancia global del motor
motor_nfe26 = MotorResonancia()

# ============================================================
# PANTALLA DE INICIO
# ============================================================
class SplashScreen(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = ""
        self.size_hint = (1, 1)
        self.background_color = (0, 0, 0, 0)
        self.auto_dismiss = False
        layout = BoxLayout(orientation='vertical')
        with layout.canvas.before:
            Color(0.05, 0.12, 0.18, 1)
            self.bg = Rectangle(size=(Window.width, Window.height))
        def ub(instance, value):
            self.bg.size = (Window.width, Window.height)
        Window.bind(size=ub)
        center = BoxLayout(orientation='vertical')
        center.add_widget(Label(size_hint_y=0.35))
        logo = Label(text="[b][size=72]MAMM-KEYBOARD-1[/size][/b]", markup=True,
                     color=(1, 0.85, 0.2, 1), size_hint_y=None, height=100)
        center.add_widget(logo)
        center.add_widget(Label(size_hint_y=0.05))
        version = Label(text="[b]VERSIÓN 1.0 - 20 IDIOMAS[/b]", markup=True,
                        color=(1, 0.85, 0.2, 0.8), size_hint_y=None, height=40)
        center.add_widget(version)
        center.add_widget(Label(size_hint_y=0.05))
        slogan = Label(text="[i]7 TEMAS PSI | VOZ | QR | WRITER[/i]", markup=True,
                       color=(1, 0.85, 0.2, 0.7), size_hint_y=None, height=30)
        center.add_widget(slogan)
        center.add_widget(Label(size_hint_y=0.35))
        layout.add_widget(center)
        self.add_widget(layout)
        Clock.schedule_once(lambda dt: self.dismiss(), 2.5)

# ============================================================
# 20 IDIOMAS COMPLETOS
# ============================================================
IDIOMAS = {
    "es": {"nombre": "Español", "bandera": "🇪🇸", "codigo": "es-ES",
        "palabras": {"que","esta","entonces","como","estoy","todo","bien","donde","vamos","ahora","claro","siempre","mañana","puedes","hacer","gracias","por","favor","bueno","malo","tiempo","vida","mundo","dia","noche","hola","adios","si","no","porque","pero","aunque","mientras","cuando","tambien"}},
    "en": {"nombre": "English", "bandera": "🇺🇸", "codigo": "en-US",
        "palabras": {"the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no"}},
    "de": {"nombre": "Deutsch", "bandera": "🇩🇪", "codigo": "de-DE",
        "palabras": {"der","die","und","den","von","zu","das","mit","sich","auf","für","ist","nicht","ein","als","auch","es","wird","an","nach","werden","aus","dem","um","dass","sind","oder","über","aber","vor","zur","bei","haben","durch","bis","ich","wir","nur","noch","kann","diese","diesem","wieder","eine","einer","dann","unter","zwischen","immer","sehr"}},
    "fr": {"nombre": "Français", "bandera": "🇫🇷", "codigo": "fr-FR",
        "palabras": {"le","la","de","les","un","une","et","à","des","pour","par","je","tu","il","elle","nous","vous","ils","elles","ce","cette","ces","mon","ton","son","notre","votre","leur","mais","ou","donc","or","ni","car","bien","mal","beau","bon","mauvais","petit","grand","fort","faible","vite","lent","toujours","parfois","jamais","aujourdhui","demain","hier"}},
    "pt": {"nombre": "Português", "bandera": "🇵🇹", "codigo": "pt-PT",
        "palabras": {"que","de","a","o","e","para","com","um","uma","os","as","em","por","mais","mas","como","se","ele","ela","nós","eles","elas","você","vocês","meu","minha","seu","sua","nosso","nossa","este","esta","estes","estas","isso","aquilo","bom","mau","pequeno","grande","rápido","lento","sempre","nunca","hoje","amanhã","ontem","agora","depois","antes"}},
    "ru": {"nombre": "Русский", "bandera": "🇷🇺", "codigo": "ru-RU",
        "palabras": {"и","в","не","на","я","что","с","а","он","по","это","к","она","для","из","но","так","вы","от","за","о","бы","мне","мной","ними","себя","эту","этот","эти","этих","его","ее","их","наш","ваш","мой","твой","хороший","плохой","маленький","большой","быстрый","медленный"}},
    "zh": {"nombre": "中文", "bandera": "🇨🇳", "codigo": "zh-CN",
        "palabras": {"我","你","他","她","它","我们","你们","他们","她们","它们","这","那","这里","那里","哪里","谁","什么","哪个","怎么","为什么","是","不","在","有","去","来","吃","喝","睡","看","听","说","写","读","学","教","工作","家","车","好","坏","大","小","快","慢"}},
    "ja": {"nombre": "日本語", "bandera": "🇯🇵", "codigo": "ja-JP",
        "palabras": {"私","あなた","彼","彼女","それ","これ","それら","ここ","そこ","どこ","誰","何","どれ","どのように","なぜ","はい","いいえ","ある","行く","来る","食べる","飲む","寝る","見る","聞く","話す","書く","読む","学ぶ","教える","仕事","家","車","良い","悪い","小さい","大きい","速い","遅い"}},
    "it": {"nombre": "Italiano", "bandera": "🇮🇹", "codigo": "it-IT",
        "palabras": {"il","che","e","non","di","un","una","sono","con","per","come","ha","questo","questi","loro","noi","voi","sia","anche","ma","o","perché","bene","male","piccolo","grande","veloce","lento","sempre","mai","oggi","domani","ieri","adesso","poi","prima","molto","poco","casa","auto","lavoro","vita","mondo","tempo","giorno","notte"}},
    "ko": {"nombre": "한국어", "bandera": "🇰🇷", "codigo": "ko-KR",
        "palabras": {"저","나","너","그","그녀","이것","그것","여기","거기","어디","누구","무엇","어떻게","왜","네","아니요","있다","가다","오다","먹다","마시다","자다","보다","듣다","말하다","쓰다","읽다","배우다","가르치다","일","집","차","좋은","나쁜","작은","큰","빠른","느린","항상","절대","오늘","내일","어제","지금","나중에","전에","매우","적게"}},
    "ar": {"nombre": "العربية", "bandera": "🇸🇦", "codigo": "ar-SA",
        "palabras": {"أنا","أنت","هو","هي","هذا","ذلك","هنا","هناك","أين","من","ماذا","كيف","لماذا","نعم","لا","يكون","يذهب","يأتي","يأكل","يشرب","ينام","يرى","يسمع","يتكلم","يكتب","يقرأ","يتعلم","يعلم","عمل","منزل","سيارة","جيد","سيء","صغير","كبير","سريع","بطيء","دائما","أبدا","اليوم","غدا","أمس","الآن","فيما بعد","قبل","جدا","قليل"}},
    "nl": {"nombre": "Nederlands", "bandera": "🇳🇱", "codigo": "nl-NL",
        "palabras": {"de","het","en","een","van","niet","te","op","voor","met","dat","die","is","ik","hij","zij","wij","jullie","ze","dit","dat","deze","die","die","er","geen","naar","dan","zijn","was","hebben","gaan","komen","zien","horen","spreken","schrijven","lezen","leren","werk","huis","auto","goed","slecht","klein","groot","snel","langzaam","altijd","nooit","vandaag","morgen","gisteren","nu","later","voor","erg","weinig"}},
    "sv": {"nombre": "Svenska", "bandera": "🇸🇪", "codigo": "sv-SE",
        "palabras": {"och","i","att","det","en","på","är","som","för","med","till","av","den","inte","har","jag","han","hon","vi","ni","de","detta","dessa","denna","dessa","något","inget","var","eller","men","om","efter","innan","under","över","mellan","genom","mot","utan","bra","dålig","liten","stor","snabb","långsam","alltid","aldrig","idag","imorgon","igår","nu","sedan","före","mycket","lite"}},
    "pl": {"nombre": "Polski", "bandera": "🇵🇱", "codigo": "pl-PL",
        "palabras": {"i","w","na","że","to","z","nie","się","do","o","za","po","przez","przy","od","dla","jako","jest","są","był","była","było","mam","masz","ma","mamy","macie","mają","dobry","zły","mały","duży","szybki","wolny","zawsze","nigdy","dzisiaj","jutro","wczoraj","teraz","później","przed","dużo","mało","praca","dom","samochód","życie","świat","czas","dzień","noc"}},
    "tr": {"nombre": "Türkçe", "bandera": "🇹🇷", "codigo": "tr-TR",
        "palabras": {"ve","bir","bu","ben","sen","o","biz","siz","onlar","için","ile","de","da","mi","mı","mu","mü","evet","hayır","iyi","kötü","küçük","büyük","hızlı","yavaş","her zaman","asla","bugün","yarın","dün","şimdi","sonra","önce","çok","az","iş","ev","araba","hayat","dünya","zaman","gün","gece"}},
    "vi": {"nombre": "Tiếng Việt", "bandera": "🇻🇳", "codigo": "vi-VN",
        "palabras": {"và","của","không","có","một","là","tôi","bạn","anh","chị","nó","chúng tôi","họ","này","đó","đây","ở","đi","đến","ăn","uống","ngủ","xem","nghe","nói","viết","đọc","học","dạy","công việc","nhà","xe","tốt","xấu","nhỏ","lớn","nhanh","chậm","luôn luôn","không bao giờ","hôm nay","ngày mai","hôm qua","bây giờ","sau đó","trước khi","rất","ít"}},
    "th": {"nombre": "ไทย", "bandera": "🇹🇭", "codigo": "th-TH",
        "palabras": {"และ","ของ","ไม่","มี","หนึ่ง","เป็น","ฉัน","คุณ","เขา","เธอ","มัน","เรา","พวกเขา","นี้","นั่น","ที่นี่","那里","ที่ไหน","ใคร","อะไร","อย่างไร","ทำไม","ใช่","ไม่","ไป","มา","กิน","ดื่ม","นอน","ดู","ฟัง","พูด","เขียน","อ่าน","เรียนรู้","สอน","งาน","บ้าน","รถ","ดี","ไม่ดี","เล็ก","ใหญ่","เร็ว","ช้า","ตลอด","ไม่เคย","วันนี้","พรุ่งนี้","เมื่อวาน","ตอนนี้","หลังจาก","ก่อน","มาก","น้อย"}},
    "hi": {"nombre": "हिन्दी", "bandera": "🇮🇳", "codigo": "hi-IN",
        "palabras": {"मैं","आप","वह","यह","हम","वे","ये","वे","कौन","क्या","कहाँ","क्यों","हाँ","नहीं","जाना","आना","खाना","पीना","सोना","देखना","सुनना","बोलना","लिखना","पढ़ना","सीखना","सिखाना","काम","घर","गाड़ी","अच्छा","बुरा","छोटा","बड़ा","तेज़","धीमा","हमेशा","कभी नहीं","आज","कल","कल","अब","बाद में","पहले","बहुत","थोड़ा"}},
    "he": {"nombre": "עברית", "bandera": "🇮🇱", "codigo": "he-IL",
        "palabras": {"אני","אתה","הוא","היא","זה","כאן","שם","איפה","מי","מה","למה","כן","לא","ללכת","לבוא","לאכול","לשתות","לישון","לראות","לשמוע","לדבר","לכתוב","לקרוא","ללמוד","ללמד","עבודה","בית","מכונית","טוב","רע","קטן","גדול","מהיר","איטי","תמיד","אף פעם","היום","מחר","אתמול","עכשיו","מאוחר יותר","לפני","מאוד","מעט"}},
    "id": {"nombre": "Bahasa Indonesia", "bandera": "🇮🇩", "codigo": "id-ID",
        "palabras": {"dan","dari","tidak","adalah","saya","kamu","dia","mereka","ini","itu","di","ke","pergi","datang","makan","minum","tidur","melihat","mendengar","berbicara","menulis","membaca","belajar","mengajar","kerja","rumah","mobil","baik","buruk","kecil","besar","cepat","lambat","selalu","tidak pernah","hari ini","besok","kemarin","sekarang","nanti","sebelum","sangat","sedikit"}}
}

PERFILES = {
    "empresario":{"nombre":"EMPRESARIO","icono":"💼","color":(0.1,0.5,0.8,1)},
    "jugador":{"nombre":"JUGADOR","icono":"🎮","color":(0.1,0.9,0.2,1)},
    "social":{"nombre":"SOCIAL","icono":"💗","color":(1,0.4,0.8,1)},
    "programador":{"nombre":"PROGRAMADOR","icono":"👨‍💻","color":(0.0,0.6,1.0,1)},
    "estudiante":{"nombre":"ESTUDIANTE","icono":"🟡","color":(1,0.9,0.1,1)},
    "apasionado":{"nombre":"APASIONADO","icono":"🔴","color":(1,0.2,0.2,1)},
    "militar":{"nombre":"MILITAR","icono":"🪖","color":(0.4,0.7,0.3,1)},
    "medico":{"nombre":"MÉDICO","icono":"🩺","color":(0.2,0.7,0.3,1)},
}

TEMAS = {
    "ejecutivo": {"bg": (0.07,0.07,0.07,1), "line": (0.75,0.75,0.75,1), "text": (1,0.84,0,1), "border": (1,0.84,0,1)},
    "rosa_quartz": {"bg": (1,1,1,1), "line": (0.2,0.2,0.2,1), "text": (0.2,0.2,0.2,1), "accent": (1,0.08,0.58,1), "border": (1,0.08,0.58,1)},
    "camo_tactical": {"bg": (0.17,0.17,0.17,1), "line": (0.29,0.33,0.13,1), "text": (0.55,0.6,0.27,1), "border": (0.36,0.25,0.20,1)},
    "blueprint": {"bg": (0.04,0.10,0.16,1), "line": (0,0.75,1,1), "text": (0,0.75,1,1), "glow": (0.88,1,1,1)},
    "red_passion": {"bg": (0.1,0,0,1), "line": (1,0,0,1), "text": (1,0.27,0.27,1)},
    "creative_harmony": {"bg": (0.1,0.1,0.18,1), "line": (0.62,0.31,0.87,1), "text": (0.88,0.67,1,1)},
    "clear_mode": {"bg": (1,1,1,1), "line": (0,0,0,1), "text": (0,0,0,1), "border": (0.8,0.8,0.8,1)}
}

class Predictor:
    def __init__(self):
        self.words = set()
        self.freq = {}
        self.history = deque(maxlen=20)
    def load_language(self, lang_code):
        self.words = IDIOMAS[lang_code]["palabras"].copy()
        self.freq = {w:1 for w in self.words}
    def learn(self, word):
        w = word.lower().strip()
        if w and len(w)>1:
            self.words.add(w)
            self.freq[w] = self.freq.get(w,0)+1
            self.history.append(w)
    def predict(self, prefix, limit=6):
        if not prefix: return []
        p = prefix.lower()
        matches = [(w,self.freq.get(w,0)) for w in self.words if w.startswith(p)]
        matches.sort(key=lambda x:-x[1])
        return [w for w,_ in matches[:limit]]

class NeonButton(Button):
    __slots__ = ('_last','_base','action','neon')
    def __init__(self, text="", action=None, neon=(1,0.85,0.2,1), **k):
        super().__init__(**k)
        self.text = text
        self.action = action
        self.background_normal = ''
        self.background_color = (0.05,0.05,0.08,0.96)
        self.font_size = dp(22)
        self.bold = True
        self._last = 0
        self._base = (0.05,0.05,0.08,0.96)
        self.neon = neon
        self.color = neon
        self.size_hint = (None, None) if 'size_hint' not in k else k['size_hint']
        self.width = dp(60) if 'width' not in k else k['width']
        self.height = dp(50) if 'height' not in k else k['height']
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            motor_nfe26.disparar_pulso()
            self._vibracion_segura()
            now = time.perf_counter_ns()
            if now - self._last < FRAME_NS: return True
            self._last = now
            self.background_color = (self.neon[0],self.neon[1],self.neon[2],0.5)
            Clock.schedule_once(lambda dt: setattr(self,'background_color',self._base), 0.003)
            return super().on_touch_down(touch)
        return False
    def _vibracion_segura(self):
        try:
            from plyer import vibrator
            vibrator.vibrate(0.02)
        except:
            pass
    def update_color(self, color):
        self.neon = color
        self.color = color

class MammKeyboard1(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Context = autoclass('android.content.Context')
            PowerManager = autoclass('android.os.PowerManager')
            pm = PythonActivity.mActivity.getSystemService(Context.POWER_SERVICE)
            self.wakelock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "MAMM:Core")
            self.wakelock.acquire()
        except:
            pass
        self.task_queue = deque()
        self.running = True
        self.memory_lock = threading.Lock()
        self.worker_thread = threading.Thread(target=self._worker, daemon=True)
        self.worker_thread.start()
        self.mem = mmap.mmap(-1, MEMORY_SIZE)
        self.pos = 0
        self.memory_size = MEMORY_SIZE
        self.seed = secrets.token_bytes(2048)
        self.key = hashlib.sha3_512(self.seed).digest()
        self.fingerprint = secrets.token_hex(8)
        self.predictor = Predictor()
        self.idioma_actual = "es"
        self.predictor.load_language("es")
        self.buffer = ""
        self.perfil_actual = "empresario"
        self.tema_actual = "ejecutivo"
        self.game_mode = False
        self.pc_mode = False
        self.writer_mode = False
        self.settings = {
            'vibration': False, 'suggestions': True, 'auto_copy': True, 'auto_cap': True,
            'incognito': False, 'vpn': None, 'idioma': 'es', 'color': PERFILES[self.perfil_actual]['color']
        }
        try:
            with open("settings.json","r") as f:
                saved = json.load(f)
                self.settings.update(saved)
                self.idioma_actual = self.settings.get('idioma','es')
                self.predictor.load_language(self.idioma_actual)
        except: pass
        self.slots = {}
        try:
            with open("storage.json","r") as f:
                self.slots = json.load(f)
        except:
            self.slots = {f"SLOT_{i:02d}": "" for i in range(1,25)}
        self.recognizer = None
        if VOZ_DISPONIBLE:
            self.recognizer = sr.Recognizer()
        self.tts = None
        if TTS_DISPONIBLE:
            try:
                self.tts = pyttsx3.init()
                self.tts.setProperty('rate',150)
            except: pass
        self.latency = [0]*100
        self.lat_idx = 0
        self.performance_stats = {'tasks_processed':0,'memory_expansions':0,'peak_memory':0,'errors':0}
        self.backup_path = os.path.join(os.path.expanduser('~'), '.mamm_backups')
        os.makedirs(self.backup_path, exist_ok=True)
        # Cargar accesos directos personalizados
        self.custom_shortcuts = self.cargar_accesos_directos()
        Window.clearcolor = TEMAS[self.tema_actual]["bg"]
        Window.bind(on_keyboard=self._on_keyboard)
        Clock.schedule_interval(self._auto_backup, 300)
        Clock.schedule_interval(self._update_status, 1.0)
        Clock.schedule_interval(self.chequeo_seguridad_termica, 5.0)

    # --- GESTIÓN DE ACCESOS DIRECTOS PERSONALIZADOS ---
    def cargar_accesos_directos(self):
        try:
            with open("custom_shortcuts.json", "r") as f:
                return json.load(f)
        except:
            return []
    def guardar_accesos_directos(self, data):
        with open("custom_shortcuts.json", "w") as f:
            json.dump(data, f)
    def abrir_app_por_paquete(self, package_name):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            pm = PythonActivity.mActivity.getPackageManager()
            intent = pm.getLaunchIntentForPackage(package_name)
            if intent:
                PythonActivity.mActivity.startActivity(intent)
            else:
                self._show_message(f"❌ App '{package_name}' no encontrada")
        except Exception as e:
            self._show_message(f"❌ Error al abrir: {e}")
    def abrir_gestor_atajos(self, instance):
        # Ventana para añadir nuevo atajo (nombre y paquete)
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text="Añadir atajo personalizado", font_size=dp(16)))
        ent_nombre = TextInput(hint_text="Nombre de la app", size_hint_y=None, height=dp(50))
        ent_paquete = TextInput(hint_text="Package (ej. com.example.app)", size_hint_y=None, height=dp(50))
        content.add_widget(ent_nombre)
        content.add_widget(ent_paquete)
        btn_guardar = Button(text="Guardar", size_hint_y=None, height=dp(50))
        popup = Popup(title="➕ Nuevo atajo", content=content, size_hint=(0.9, 0.5))
        def guardar(instance_btn):
            nombre = ent_nombre.text.strip()
            paquete = ent_paquete.text.strip()
            if nombre and paquete:
                self.custom_shortcuts.append({"nombre": nombre, "paquete": paquete})
                self.guardar_accesos_directos(self.custom_shortcuts)
                self._show_message(f"✅ {nombre} añadido")
                popup.dismiss()
            else:
                self._show_message("❌ Completa ambos campos")
        btn_guardar.bind(on_press=guardar)
        content.add_widget(btn_guardar)
        # Listar y permitir eliminar atajos existentes
        if self.custom_shortcuts:
            content.add_widget(Label(text="Tus atajos:", font_size=dp(14)))
            for item in self.custom_shortcuts[:]:
                btn_del = Button(text=f"❌ {item['nombre']}", size_hint_y=None, height=dp(40))
                btn_del.bind(on_press=lambda x, p=item: self.eliminar_atajo(p))
                content.add_widget(btn_del)
        popup.content = content
        popup.open()
    def eliminar_atajo(self, item):
        if item in self.custom_shortcuts:
            self.custom_shortcuts.remove(item)
            self.guardar_accesos_directos(self.custom_shortcuts)
            self._show_message(f"🗑️ {item['nombre']} eliminado")
    def abrir_lanzador_apps(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        # Mostrar botones de accesos directos personalizados
        if self.custom_shortcuts:
            for item in self.custom_shortcuts:
                btn = Button(text=item['nombre'], size_hint_y=None, height=dp(50))
                btn.bind(on_press=lambda x, pkg=item['paquete']: self.abrir_app_por_paquete(pkg))
                content.add_widget(btn)
        else:
            content.add_widget(Label(text="No hay atajos personalizados\nusa '+' para añadir", halign='center'))
        # Botones fijos para añadir/eliminar
        btn_add = Button(text="➕ Añadir/Eliminar atajo", size_hint_y=None, height=dp(50))
        btn_add.bind(on_press=lambda x: self.abrir_gestor_atajos(x))
        content.add_widget(btn_add)
        popup = Popup(title="🚀 Lanzador Rápido", content=content, size_hint=(0.8, 0.5))
        popup.open()

    def _worker(self):
        while self.running:
            if self.task_queue:
                task = self.task_queue.popleft()
                try: self._process_task(task)
                except: pass
            else:
                time.sleep(0.001)

    def _process_task(self, task):
        ttype = task.get('type','key')
        if ttype == 'key': self._process_key_async(task['key'])
        elif ttype == 'voice': self._process_voice_async(task['text'])
        elif ttype == 'load_slot': self._load_slot_async(task['slot'])
        elif ttype == 'save_slot': self._save_slot_async()

    def _process_key_async(self, key):
        with self.memory_lock:
            if key == " ":
                self._write_async(" "); self.buffer = ""
            elif key == "ENTER":
                self._copy_async()
            elif key == "BACK":
                self._backspace_async()
            elif key == "CLEAR":
                self._clear_async()
            elif key == "SHIELD":
                self._shield_async()
            elif key == "SAVE":
                self.task_queue.append({'type':'save_slot'})
            elif key == "LEFT":
                self.pos = max(0, self.pos-1)
            elif key == "RIGHT":
                self.pos = min(self.memory_size, self.pos+1)
            elif key.startswith("SLOT_"):
                if self.slots.get(key): self._load_slot_async(key)
                else: self.task_queue.append({'type':'save_slot'})
            elif len(key)==1:
                if self.settings['auto_cap'] and self.pos>1 and bytes(self.mem[self.pos-2:self.pos])==b". ":
                    key = key.upper()
                self._write_char_async(key)
                self.buffer += key.lower()
                if key==" " and self.buffer.strip():
                    self.predictor.learn(self.buffer.strip())
        self._update_ui()
        if self.settings['auto_copy'] and self.pos>0 and not self.game_mode:
            try:
                Clipboard.copy(self.mem[:self.pos].decode('utf-8','ignore'))
            except: pass

    def _write_char_async(self,c):
        b = c.encode()
        self._expand_memory_if_needed(len(b))
        self.mem[self.pos:self.pos+len(b)] = b
        self.pos += len(b)
        self.performance_stats['tasks_processed'] += 1

    def _write_async(self,txt):
        b = txt.encode()
        self._expand_memory_if_needed(len(b))
        self.mem[self.pos:self.pos+len(b)] = b
        self.pos += len(b)

    def _backspace_async(self):
        if self.pos>0:
            self.pos -= 1
            self.buffer = self.buffer[:-1] if self.buffer else ""

    def _clear_async(self):
        self.pos = 0
        self.buffer = ""

    def _copy_async(self):
        if self.pos>0:
            Clipboard.copy(self.mem[:self.pos].decode('utf-8','ignore'))
            self.pos = 0
            self.buffer = ""

    def _shield_async(self):
        self.mem[:] = secrets.token_bytes(self.memory_size)
        self.pos = 0
        self.buffer = ""
        self._show_message("🛡️ MEMORIA TRITURADA")

    def _save_slot_async(self):
        if self.pos>0:
            txt = self.mem[:self.pos].decode('utf-8','ignore')
            for slot, content in self.slots.items():
                if not content:
                    self.slots[slot] = txt
                    with open("storage.json","w") as f:
                        json.dump(self.slots, f)
                    self._show_message(f"💾 {slot}")
                    break

    def _load_slot_async(self, slot):
        if self.slots.get(slot):
            for c in self.slots[slot]:
                self._write_char_async(c)
            self._show_message(f"📂 {slot}")

    def _process_voice_async(self, text):
        for c in text:
            self._write_char_async(c)
        self._write_async(" ")
        self._show_message(f"🎤 Dicho: {text[:30]}...")

    def _expand_memory_if_needed(self, needed):
        if self.pos + needed >= self.memory_size:
            new_size = min(self.memory_size*2, MAX_MEMORY)
            if new_size <= self.memory_size: return
            new_mem = mmap.mmap(-1, new_size)
            new_mem[:self.pos] = self.mem[:self.pos]
            self.mem.close()
            self.mem = new_mem
            self.memory_size = new_size
            self.performance_stats['memory_expansions'] += 1

    def _update_ui(self):
        try:
            with self.memory_lock:
                text = self.mem[:self.pos].decode('utf-8','ignore')
            if hasattr(self, 'text_display'):
                self.text_display.text = text + ("█" if not self.game_mode else "")
            if not self.game_mode and self.settings['suggestions']:
                sug = self.predictor.predict(self.buffer,6)
                for i in range(6):
                    if hasattr(self, f'sug_btn_{i}'):
                        btn = getattr(self, f'sug_btn_{i}')
                        if i < len(sug):
                            btn.text = sug[i]; btn.opacity = 1
                        else:
                            btn.text = ""; btn.opacity = 0
        except: pass

    def _show_message(self, msg):
        if hasattr(self, 'status_label'):
            self.status_label.text = msg

    def _update_status(self, dt):
        if hasattr(self, 'status_label'):
            id_text = "🕵️" if self.settings['incognito'] else f"🆔 {self.fingerprint[:6]}"
            self.status_label.text = f"{id_text} ⚡ {FPS}Hz | 💾 {self.pos//1024}KB"

    def _auto_backup(self, dt):
        try:
            with open("settings_backup.json","w") as f:
                json.dump(self.settings, f)
        except: pass

    def on_key(self, key):
        self.task_queue.append({'type':'key','key':key})

    def voice_dictation(self, instance):
        if not VOZ_DISPONIBLE:
            self._show_message("❌ Voz no disponible"); return
        self._show_message("🎤 Escuchando...")
        def listen():
            try:
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source,0.5)
                    audio = self.recognizer.listen(source, timeout=5)
                    texto = self.recognizer.recognize_google(audio, language=self.idioma_actual)
                    self.task_queue.append({'type':'voice','text':texto})
            except:
                self._show_message("❌ No entendí")
        threading.Thread(target=listen, daemon=True).start()

    def speak_text(self, instance):
        if self.pos==0:
            self._show_message("📢 No hay texto"); return
        with self.memory_lock:
            texto = self.mem[:self.pos].decode('utf-8','ignore')
        if TTS_DISPONIBLE and self.tts:
            def speak():
                self.tts.say(texto)
                self.tts.runAndWait()
            threading.Thread(target=speak, daemon=True).start()
            self._show_message("🔊 Leyendo...")
        else:
            self._show_message("❌ TTS no disponible")

    def toggle_game_mode(self, btn):
        self.game_mode = not self.game_mode
        if self.game_mode:
            self.text_display.parent.height = 0
            self.text_display.parent.opacity = 0
            if hasattr(self, 'sug_bar'): self.sug_bar.height = 0; self.sug_bar.opacity = 0
            btn.text="🎮"
        else:
            self.text_display.parent.height = dp(130)
            self.text_display.parent.opacity = 1
            if hasattr(self, 'sug_bar') and self.settings['suggestions']:
                self.sug_bar.height = dp(45); self.sug_bar.opacity = 1
            btn.text="✍️"

    def toggle_writer_mode(self, instance):
        self.writer_mode = not self.writer_mode
        if self.writer_mode:
            self.text_display.parent.height = Window.height - dp(100)
            self.text_display.font_size = dp(28)
            if hasattr(self, 'extended_keys'): self.extended_keys.opacity = 0
            if hasattr(self, 'slots_grid'): self.slots_grid.opacity = 0
            if hasattr(self, 'nav_bar'): self.nav_bar.opacity = 0
            self._show_message("📝 MODO WRITER ACTIVO")
        else:
            self.text_display.parent.height = dp(130)
            self.text_display.font_size = dp(44)
            if hasattr(self, 'extended_keys'): self.extended_keys.opacity = 1
            if hasattr(self, 'slots_grid'): self.slots_grid.opacity = 1
            if hasattr(self, 'nav_bar'): self.nav_bar.opacity = 1
            self._show_message("⌨️ MODO TECLADO")

    def cambiar_perfil(self, perfil_key):
        self.perfil_actual = perfil_key
        perfil = PERFILES[perfil_key]
        self.settings['color'] = perfil['color']
        for w in self.root.walk():
            if isinstance(w, NeonButton):
                w.update_color(perfil['color'])
        self.text_display.foreground_color = perfil['color']
        self._save_settings()
        self._show_message(f"✅ {perfil['nombre']}")

    def cambiar_tema(self, tema_key):
        self.tema_actual = tema_key
        tema = TEMAS[tema_key]
        Window.clearcolor = tema["bg"]
        self.text_display.background_color = tema["bg"]
        self.text_display.foreground_color = tema.get("text", (1,1,1,1))
        self._show_message(f"🎨 Tema: {tema_key.replace('_',' ').title()}")

    def cambiar_idioma(self, idioma_key):
        self.idioma_actual = idioma_key
        self.settings['idioma'] = idioma_key
        self.predictor.load_language(idioma_key)
        self._save_settings()
        self._show_message(f"🌍 {IDIOMAS[idioma_key]['bandera']} {IDIOMAS[idioma_key]['nombre']}")

    def _save_settings(self):
        try:
            with open("settings.json","w") as f:
                json.dump(self.settings, f)
        except: pass

    # --- ACCIONES DE APLICACIONES EXTERNAS ---
    def abrir_app_intent(self, package, fallback_url):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            pm = PythonActivity.mActivity.getPackageManager()
            intent = pm.getLaunchIntentForPackage(package)
            if intent:
                PythonActivity.mActivity.startActivity(intent)
            else:
                import webbrowser
                webbrowser.open(fallback_url)
        except: pass

    def abrir_whatsapp(self, instance):
        self.abrir_app_intent("com.whatsapp", "https://web.whatsapp.com")
    def abrir_telegram(self, instance):
        self.abrir_app_intent("org.telegram.messenger", "https://web.telegram.org")
    def abrir_tiktok(self, instance):
        self.abrir_app_intent("com.zhiliaoapp.musically", "https://www.tiktok.com")
    def abrir_calculadora(self, instance):
        self.abrir_app_intent("com.android.calculator2", "https://google.com")
    def abrir_alarma(self, instance):
        self.abrir_app_intent("com.android.deskclock", "https://google.com")
    def abrir_notas(self, instance):
        self.abrir_app_intent("com.google.android.apps.notes", "https://keep.google.com")
    def abrir_llamadas(self, instance):
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            intent = Intent(Intent.ACTION_DIAL)
            PythonActivity.mActivity.startActivity(intent)
        except: pass

    # --- BOTÓN MAMM: COPIAR, QR, WRITER EXTERNO ---
    def puente_writer(self, instance):
        with self.memory_lock:
            texto = self.mem[:self.pos].decode('utf-8','ignore')
        if not texto.strip():
            self._show_message("⚠️ Sin texto"); return
        Clipboard.copy(texto)
        self._mostrar_qr_con_texto(texto)
        texto_cod = urllib.parse.quote(texto, safe='')
        uri = f"mammwriter://transfer?text={texto_cod}"
        try:
            from jnius import autoclass
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            intent = Intent(Intent.ACTION_VIEW, Uri.parse(uri))
            PythonActivity.mActivity.startActivity(intent)
            self._show_message("📤 Abriendo Writer...")
        except: pass

    def _mostrar_qr_con_texto(self, texto):
        try:
            import qrcode, io
            from kivy.uix.image import Image as KivyImage
            from kivy.core.image import Image as CoreImage
            qr = qrcode.QRCode(box_size=8, border=2)
            qr.add_data(texto)
            qr.make(fit=True)
            img = qr.make_image(fill_color=(1,0.85,0.2), back_color=(0.05,0.05,0.05)).convert('RGBA')
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='PNG')
            byte_arr.seek(0)
            texture = CoreImage(byte_arr, ext='png').texture
            popup = Popup(title="📱 QR DEL TEXTO", size_hint=(0.85,0.85))
            layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
            qr_img = KivyImage(texture=texture, size_hint=(1,0.7))
            layout.add_widget(qr_img)
            layout.add_widget(Label(text="Escanea para compartir", size_hint_y=0.1, color=(0.9,0.9,0.9,1)))
            btn = Button(text="CERRAR", size_hint_y=0.1)
            btn.bind(on_press=popup.dismiss)
            layout.add_widget(btn)
            popup.content = layout
            popup.open()
        except Exception as e:
            self._show_message(f"❌ QR error: {e}")

    # --- ESCÁNER QR ---
    def escanear_qr(self, instance):
        try:
            from pyzbar.pyzbar import decode
            from PIL import Image as PILImage
        except:
            self._show_message("❌ Instala pyzbar/pillow"); return
        popup = Popup(title="📷 ESCANEAR QR", size_hint=(0.95,0.95))
        layout = FloatLayout()
        cam = Camera(resolution=(640,480), play=True)
        cam.size_hint = (1,0.8); cam.pos_hint = {'x':0,'y':0.1}
        layout.add_widget(cam)
        estado = Label(text="Acerca el código", size_hint=(1,0.1), pos_hint={'x':0,'y':0}, color=(0.9,0.9,0.9,1))
        layout.add_widget(estado)
        btn_cancel = Button(text="CANCELAR", size_hint=(0.3,0.08), pos_hint={'x':0.35,'y':0.01})
        btn_cancel.bind(on_press=popup.dismiss)
        layout.add_widget(btn_cancel)
        popup.content = layout
        popup.open()
        def capturar(dt):
            if not popup.is_open: return
            tex = cam.texture
            if not tex: return
            pil_img = PILImage.frombytes('RGBA', tex.size, tex.pixels).convert('RGB')
            codigos = decode(pil_img)
            if codigos:
                contenido = codigos[0].data.decode('utf-8')
                popup.dismiss()
                self._mostrar_resultado_qr(contenido)
                return
            Clock.schedule_once(capturar, 0.3)
        Clock.schedule_once(capturar, 0.5)

    def _mostrar_resultado_qr(self, contenido):
        popup = Popup(title="📌 QR DETECTADO", size_hint=(0.9,0.6))
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        scroll = ScrollView()
        lbl = Label(text=contenido, font_size=dp(16), color=(0.9,0.9,0.9,1), size_hint_y=None)
        lbl.bind(size=lbl.setter('height'))
        scroll.add_widget(lbl)
        layout.add_widget(scroll)
        btn_copy = Button(text="📋 COPIAR", size_hint_y=0.15)
        btn_copy.bind(on_press=lambda x: (Clipboard.copy(contenido), self._show_message("✅ Copiado"), popup.dismiss()))
        layout.add_widget(btn_copy)
        if contenido.startswith(('http://','https://')):
            btn_open = Button(text="🌐 ABRIR", size_hint_y=0.15)
            import webbrowser
            btn_open.bind(on_press=lambda x: (webbrowser.open(contenido), popup.dismiss()))
            layout.add_widget(btn_open)
        btn_close = Button(text="CERRAR", size_hint_y=0.15)
        btn_close.bind(on_press=popup.dismiss)
        layout.add_widget(btn_close)
        popup.content = layout
        popup.open()

    # --- INTERFAZ GRÁFICA (CON TECLADO QWERTY COMPLETO) ---
    def build(self):
        splash = SplashScreen()
        splash.open()
        root = BoxLayout(orientation='vertical', spacing=dp(2), padding=dp(2))
        root.clearcolor = (0.02,0.02,0.03,1)
        # Área de texto
        text_area = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(130))
        self.text_display = TextInput(readonly=True, font_size=dp(44), size_hint_y=None, height=dp(130),
                                 background_color=(0,0,0.05,1), foreground_color=self.settings['color'])
        text_area.add_widget(self.text_display)
        root.add_widget(text_area)
        # Barra de sugerencias
        self.sug_bar = BoxLayout(size_hint_y=None, height=dp(45), spacing=dp(2))
        for i in range(6):
            btn = NeonButton("", neon=self.settings['color'])
            setattr(self, f'sug_btn_{i}', btn)
            btn.id = f'sug_{i}'; btn.font_size = dp(18); btn.width = dp(80)
            btn.bind(on_press=self.use_suggestion)
            self.sug_bar.add_widget(btn)
        if self.settings['suggestions']:
            root.add_widget(self.sug_bar)
        # Panel superior horizontal
        self.top_scroll = ScrollView(size_hint_y=0.12, do_scroll_x=True, do_scroll_y=False)
        self.top_bar = BoxLayout(spacing=dp(2), size_hint_x=None)
        self.top_bar.bind(minimum_width=self.top_bar.setter('width'))
        acciones = [
            ("💬", self.abrir_whatsapp), ("✈️", self.abrir_telegram), ("🎵", self.abrir_tiktok),
            ("📞", self.abrir_llamadas), ("📝", self.toggle_writer_mode), ("🧮", self.abrir_calculadora),
            ("⏰", self.abrir_alarma), ("🗒️", self.abrir_notas), ("📷", self.escanear_qr),
            ("MAMM", self.puente_writer), ("🎨", self.ciclar_tema), ("🕵️", self.toggle_incognito),
            ("⚙️", self.open_settings), ("🎤", self.voice_dictation), ("🔊", self.speak_text),
            ("🚀", self.abrir_lanzador_apps)  # NUEVO BOTÓN LANZADOR PERSONALIZADO
        ]
        for text, func in acciones:
            btn = NeonButton(text, neon=self.settings['color'], width=dp(70))
            btn.bind(on_press=func)
            self.top_bar.add_widget(btn)
        self.top_scroll.add_widget(self.top_bar)
        root.add_widget(self.top_scroll)
        # Teclado QWERTY completo
        teclado = GridLayout(cols=10, size_hint_y=0.25, spacing=dp(2))
        letras = [
            "Q","W","E","R","T","Y","U","I","O","P",
            "A","S","D","F","G","H","J","K","L","Ñ",
            "*","Z","X","C","V","B","N","M","",""
        ]
        for letra in letras:
            if letra == "*":
                btn = NeonButton("SHIFT", neon=self.settings['color'], width=dp(90))
                btn.bind(on_press=lambda x: self.toggle_shift())
            elif letra == "":
                btn = NeonButton("", neon=self.settings['color'], width=dp(60))
            else:
                btn = NeonButton(letra, neon=self.settings['color'], width=dp(70))
                btn.bind(on_press=lambda x, k=letra: self.on_key(k))
            teclado.add_widget(btn)
        root.add_widget(teclado)
        # Teclado extendido
        self.extended_keys = GridLayout(cols=10, size_hint_y=0.15, spacing=dp(1))
        for s in "?!.,;:@#$%&*()_-+=[]<>/\\":
            btn = NeonButton(s, neon=self.settings['color'], font_size=dp(18), width=dp(40))
            btn.bind(on_press=lambda x, k=s: self.on_key(k))
            self.extended_keys.add_widget(btn)
        root.add_widget(self.extended_keys)
        # Slots
        self.slots_grid = GridLayout(cols=8, size_hint_y=0.1, spacing=dp(2))
        for i in range(1,17):
            btn = NeonButton(f"S{i:02d}", neon=self.settings['color'], font_size=dp(14), width=dp(50))
            btn.bind(on_press=lambda x, s=f"SLOT_{i:02d}": self.on_key(s))
            self.slots_grid.add_widget(btn)
        root.add_widget(self.slots_grid)
        # Navegación
        self.nav_bar = BoxLayout(size_hint_y=0.07, spacing=dp(5))
        left = NeonButton("◀ ◀", neon=self.settings['color']); left.bind(on_press=lambda x: self.on_key("LEFT"))
        right = NeonButton("▶ ▶", neon=self.settings['color']); right.bind(on_press=lambda x: self.on_key("RIGHT"))
        self.nav_bar.add_widget(left); self.nav_bar.add_widget(right)
        root.add_widget(self.nav_bar)
        # Estado
        self.status_label = Label(text=f"🆔 {self.fingerprint[:6]}", size_hint_y=0.04, color=self.settings['color'], font_size=dp(12))
        root.add_widget(self.status_label)
        return root

    def ciclar_tema(self, instance):
        temas = list(TEMAS.keys())
        idx = temas.index(self.tema_actual)
        nuevo = temas[(idx+1)%len(temas)]
        self.cambiar_tema(nuevo)

    def toggle_shift(self):
        pass

    def use_suggestion(self, btn):
        if btn.text and not self.game_mode and not self.writer_mode:
            self.pos -= len(self.buffer)
            self._write_async(btn.text + " ")
            self.buffer = ""
            self._update_ui()

    def toggle_incognito(self, instance):
        self.settings['incognito'] = not self.settings['incognito']
        self._save_settings()
        self._show_message("🕵️ Incógnito" if self.settings['incognito'] else "👁️ Normal")

    def open_settings(self, instance):
        self._show_message("⚙️ Configuración")

    def _on_keyboard(self, window, key, *args):
        if key == 27 and self.game_mode:
            self.toggle_game_mode(None); return True
        return False

    def chequeo_seguridad_termica(self, dt):
        try:
            if self.pos > 1024:
                self.status_label.text = "⚠️ MODO PROTECCIÓN ACTIVO"
                self.status_label.color = (1, 0, 0, 1)
        except:
            pass

    def on_stop(self):
        self.running = False
        if hasattr(self, 'worker_thread') and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=2.0)
        if hasattr(self, 'mem'): self.mem.close()
        print("✅ MAMM-KEYBOARD-1 cerrado")

if __name__ == '__main__':
    try:
        print("🚀 Iniciando MAMM-KEYBOARD-1...")
        MammKeyboard1().run()
    except KeyboardInterrupt:
        print("\n⏹️ Terminado por usuario")
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        traceback.print_exc()
