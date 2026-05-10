[app]

# ============================================================
# MAMM-KEYBOARD-1 - OBRA MAESTRA TECNOLÓGICA
# ARQUITECTO: MARCOS ABEL MENDIETA MOLINA
# COMPATIBLE: ANDROID 15 (API 35) | HONOR MAGIC 7 LITE
# CARACTERÍSTICAS: ESTACIÓN DE SERVICIO | FRECUENCIAS 60/62 Hz
# DISEÑO: AZUL MARINO OSCURO + LETRAS DORADAS
# ============================================================

title = MAMM-KEYBOARD-1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini,xml
version = 1.0.3
version.code = 4

# --- LIBRERÍAS EXACTAS (SIN FALTANTES, SIN ERRORES, TECNOLOGÍA ASEGURADA) ---
requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,cython==0.29.33,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

# --- PERMISOS TOTALES (TODO LO QUE NECESITAS + ANDROID 15 OBLIGATORIOS) ---
android.permissions = 
    BIND_INPUT_METHOD,
    INTERNET,
    VIBRATE,
    WAKE_LOCK,
    SYSTEM_ALERT_WINDOW,
    FOREGROUND_SERVICE,
    FOREGROUND_SERVICE_INPUT_METHOD,
    RECEIVE_BOOT_COMPLETED,
    MANAGE_EXTERNAL_STORAGE,
    REQUEST_INSTALL_PACKAGES,
    CALL_PHONE,
    READ_CONTACTS,
    CAMERA,
    RECORD_AUDIO,
    POST_NOTIFICATIONS,
    READ_MEDIA_AUDIO,
    READ_MEDIA_IMAGES,
    BLUETOOTH,
    BLUETOOTH_ADMIN,
    BLUETOOTH_CONNECT

# --- RUTAS DE RECURSOS (EXACTAS A TU ESTRUCTURA DE CARPETAS) ---
android.add_resources = android/res
android.add_src = org

# ==================================================
# 🛡️ IDENTIDAD OFICIAL: PARA QUE SEA APK RECONOCIDA
# ==================================================
android.manifest_application = 
    android:allowBackup="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:roundIcon="@mipmap/ic_launcher_round"
    android:supportsRtl="true"
    android:theme="@style/Theme.AppCompat.NoActionBar"
    android:extractNativeLibs="false"
    android:hasCode="true"
    android:largeHeap="true"

# ==================================================
# 🚀 ACTIVIDAD PRINCIPAL: ÍCONO EN EL MENÚ DEL TELÉFONO
# ==================================================
android.manifest_activities = 
    <activity
        android:name="org.kivy.android.PythonActivity"
        android:exported="true"
        android:launchMode="singleTop"
        android:configChanges="keyboard|keyboardHidden|orientation|screenSize|smallestScreenSize"
        android:windowSoftInputMode="adjustResize">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
    </activity>

# ==================================================
# ⌨️ DECLARACIÓN COMO TECLADO DEL SISTEMA (CERTIFICADO)
# ==================================================
android.manifest_placeholders = 
    <service 
        android:name=".MiTecladoServicio"
        android:exported="true"
        android:enabled="true"
        android:permission="android.permission.BIND_INPUT_METHOD"
        android:foregroundServiceType="inputMethod"
        android:stopWithTask="false">
        <intent-filter>
            <action android:name="android.view.InputMethod" />
            <category android:name="android.intent.category.DEFAULT" />
        </intent-filter>
        <meta-data
            android:name="android.view.im"
            android:resource="@xml/method" />
    </service>

android.meta_data = android.view.im=@xml/method

# ==================================================
# ⚠️ RECTIFICACIÓN EXACTA SEGÚN TU INDICACIÓN
# android.api = 35 | android.ndk = 26b
# ==================================================
android.api = 35
android.target_sdk_version = 35
android.minapi = 28
android.ndk_api = 28
android.sdk = 35
android.ndk = 26b
android.compile_sdk = 35

# --- MOTOR DE COMPILACIÓN OPTIMIZADO (VELOCIDAD Y SEGURIDAD) ---
p4a.bootstrap = sdl2
p4a.branch = master
p4a.optimize_python = 2
p4a.pyc_optimize = 2

# --- ARQUITECTURA EXACTA PARA TU HONOR MAGIC 7 LITE ---
android.archs = arm64-v8a
android.ndk_arch = arm64-v8a

# --- LIBRERÍAS ANDROID ACTUALIZADAS Y ESTABLES ---
android.enable_androidx = True
android.gradle_dependencies = \
    androidx.core:core:1.15.0,\
    androidx.appcompat:appcompat:1.7.0,\
    com.google.android.material:material:1.12.0,\
    androidx.lifecycle:lifecycle-service:2.8.6

android.debug = True
android.release = False
android.release_artifact = apk

# --- COMPORTAMIENTO DE PANTALLA Y VENTANA ---
orientation = portrait
fullscreen = 0
window_soft_input_mode = adjustResize|adjustPan
android.manifest.windowSoftInputMode = adjustResize|stateHidden

# ==================================================
# ⚡ MOTOR DE RESONANCIA SIEMPRE ACTIVO
# REGLAS: 60 Hz (REPOSO) | 62 Hz (ACTIVO) | 38.44 Hz (BORDE)
# ==================================================
android.wakelock = True
android.wakelock_timeout = -1
android.keep_screen_on = True

# --- DEPURACIÓN Y LOGS (LIMPIOS Y ÚTILES) ---
log_level = 2
logcat_filters = *:I python:D Kivy:D MammKeyboard:V

# --- SEGURIDAD Y ESTABILIDAD MÁXIMA ---
android.allow_backup = True
android.supports_rtl = True
android.manifest.launch_mode = singleTop
android.manifest.theme = @style/Theme.AppCompat.NoActionBar
android.manifest.debuggable = True
android.manifest.extractNativeLibs = False

# ==================================================
# 🎨 TU DISEÑO VISUAL: PANTALLA DE PRESENTACIÓN
# FONDO AZUL MARINO OSCURO - LETRAS DORADAS - 2.5 SEGUNDOS
# ==================================================
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

android.default_locale = es_EC
android.extra_resources = app_name=%(title)s

# --- COMPORTAMIENTO DE COMPILACIÓN ---
android.skip_update = False
android.accept_sdk_license = True
android.use_aapt2 = True

[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
parallel_jobs = 8
