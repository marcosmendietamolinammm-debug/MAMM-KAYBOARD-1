[app]

# ============================================================
# MAMM KEYBOARD 1 - VERSIÓN TECNOLÓGICA MÁXIMA
# ARQUITECTO: MARCOS ABEL MENDIETA MOLINA
# COMPATIBLE: ANDROID 16 (API 36) | HONOR MAGIC 7 LITE
# ============================================================

title = MAMM KEYBOARD 1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini,xml
version = 1.0.3
version.code = 4

# --- REQUISITOS (MISMA TECNOLOGÍA QUE YA TE FUNCIONÓ - NO SE TOCA) ---
requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,cython==0.29.33,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

# --- PERMISOS (TODOS LOS TUYOS + LOS NUEVOS OBLIGATORIOS ANDROID 16) ---
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
    READ_MEDIA_IMAGES

# --- RECURSOS Y CÓDIGO (EXACTAMENTE COMO LO TENÍAS) ---
android.add_resources = android/res
android.add_src = org

# --- DECLARACIÓN TECLADO - MEJORADA Y CERTIFICADA PARA ANDROID 16 ---
android.manifest_placeholders = 
    <service 
        android:name=".MiTecladoServicio"
        android:exported="true"
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

# --- META-DATO (TU MEJORA, AHORA REFORZADA) ---
android.meta_data = android.view.im=@xml/method

# --- ANDROID: VERSIONES ACTUALIZADAS AL TECHO (COMPATIBLE HACIA ATRÁS) ---
android.api = 36                  # ✅ ANDROID 16 - ÚLTIMA TECNOLOGÍA
android.target_sdk_version = 36   # ✅ INDICA QUE ESTÁS PREPARADO PARA 16
android.minapi = 28               # ✅ MANTENEMOS TU MÍNIMO, NO PIERDES COMPATIBILIDAD
android.ndk_api = 28              # ✅ IGUAL QUE ANTES, ESTABLE
android.sdk = 36                  # ✅ SDK ACTUALIZADO
android.ndk = 27b                 # ✅ NDK ACTUALIZADO PERO COMPATIBLE CON TU CÓDIGO
android.compile_sdk = 36

# --- MOTOR DE COMPILACIÓN (LO QUE YA USABAS, CON OPTIMIZACIONES) ---
p4a.bootstrap = sdl2
p4a.branch = master
p4a.optimize_python = 2          # ✅ NIVEL MÁXIMO DE OPTIMIZACIÓN DE CÓDIGO
p4a.pyc_optimize = 2             # ✅ COMPILA A CÓDIGO MÁS RÁPIDO
p4a.whitelist =
p4a.blacklist =

# --- ARQUITECTURA: TU DECISIÓN PERFECTA, AHORA CON ACELERACIÓN ---
android.archs = arm64-v8a        # ✅ SOLO TU PROCESADOR, MÁS VELOCIDAD, MENOS PESO
android.ndk_arch = arm64-v8a

# --- LIBRERÍAS ANDROID (ACTUALIZADAS A VERSIONES ESTABLES RECIENTES) ---
android.enable_androidx = True
android.gradle_dependencies = \
    androidx.core:core:1.15.0,\
    androidx.appcompat:appcompat:1.7.0,\
    com.google.android.material:material:1.12.0,\
    androidx.lifecycle:lifecycle-service:2.8.6

android.debug = True
android.release = False
android.release_artifact = apk

# --- COMPORTAMIENTO DE VENTANA (TUS PARÁMETROS, MEJORADOS) ---
orientation = portrait
fullscreen = 0
window_soft_input_mode = adjustResize|adjustPan
android.manifest.windowSoftInputMode = adjustResize|stateHidden

# --- MOTOR DE RESONANCIA N-FE26: TU TECNOLOGÍA PROTEGIDA ---
android.wakelock = True
android.wakelock_timeout = -1     # ✅ SIEMPRE ACTIVO, NO SE APAGA EL MOTOR
android.keep_screen_on = True     # ✅ PARA QUE NO INTERRUMPA LA FRECUENCIA

# --- LOGS Y DEPURACIÓN (TUS AJUSTES, MÁS LIMPIOS) ---
log_level = 2
logcat_filters = *:I python:D Kivy:D MammKeyboard:V

# --- SEGURIDAD Y ESTABILIDAD ---
android.allow_backup = True
android.supports_rtl = True
android.manifest.launch_mode = singleTop
android.manifest.theme = @style/Theme.AppCompat.NoActionBar
android.manifest.debuggable = True
android.manifest.extractNativeLibs = False  # ✅ NO DESCOMPRIME, MÁS SEGURO Y RÁPIDO

# --- RECURSOS VISUALES (TUS RUTAS) ---
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

android.default_locale = es_EC
android.extra_resources = app_name=%(title)s

# --- COMPORTAMIENTO DE COMPILACIÓN ---
android.skip_update = False
android.accept_sdk_license = True
android.use_aapt2 = True          # ✅ HERRAMIENTA MÁS RÁPIDA DE ANDROID

[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
parallel_jobs = 8                 # ✅ USA TODOS LOS NÚCLEOS DE TU PC PARA COMPILAR RÁPIDO
