# ============================================================
# BUILDOZER.SPEC EVOLUCIÓN 2026 - MAMM-KEYBOARD-1
# Honor Magic 7 Lite / Android 15 / Máximo Nivel Tecnológico
# ============================================================

[app]

# (str) Título de la aplicación
title = MAMM KEYBOARD 1

# (str) Package name
package.name = mammkeyboard1

# (str) Package domain
package.domain = org.mammkeyboard

# (str) Directorio del código fuente
source.dir = .

# (list) Extensiones de archivo a incluir
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini

# (str) Versión de la aplicación
version = 1.0.2
# (int) Código de versión (para Android)
version.code = 3

# ============================================================
# REQUISITOS (Piezas de compatibilidad exacta)
# ============================================================
requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,cython==3.0.11,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

# ============================================================
# PERMISOS ANDROID (Prioridad Operativa)
# ============================================================
android.permissions = \
    INTERNET,\
    VIBRATE,\
    WAKE_LOCK,\
    SYSTEM_ALERT_WINDOW,\
    FOREGROUND_SERVICE,\
    RECEIVE_BOOT_COMPLETED,\
    MANAGE_EXTERNAL_STORAGE,\
    REQUEST_INSTALL_PACKAGES,\
    CALL_PHONE,\
    READ_CONTACTS,\
    CAMERA

# ============================================================
# ANDROID 15 (API 35) - Configuración SDK/NDK
# ============================================================
android.api = 35
android.minapi = 21
android.sdk = 35
android.ndk = 25c

# ============================================================
# BOOTSTRAP Y RAMA DE PYTHON-FOR-ANDROID
# ============================================================
p4a.bootstrap = sdl2
p4a.branch = develop

# ============================================================
# ARQUITECTURAS (Máxima compatibilidad 64 y 32 bits)
# ============================================================
android.archs = arm64-v8a, armeabi-v7a

# ============================================================
# SERVICIOS EN SEGUNDO PLANO (Motor de Resonancia Persistente)
# ============================================================
# Descomenta la siguiente línea y crea service.py para que la "fórmula" se ejecute incluso con la pantalla apagada.
# android.services = monitor_servicio:service.py

# ============================================================
# DEPENDENCIAS GRADLE (AndroidX y Material Design)
# ============================================================
android.enable_androidx = True
android.gradle_dependencies = \
    androidx.core:core:1.13.1,\
    androidx.appcompat:appcompat:1.6.1,\
    com.google.android.material:material:1.11.0

# ============================================================
# MODO DE CONSTRUCCIÓN Y OPTIMIZACIONES
# ============================================================
android.debug = True
android.release = False
android.release_artifact = apk

# ============================================================
# INTERFAZ Y RENDIMIENTO
# ============================================================
orientation = portrait
fullscreen = 0
window_soft_input_mode = adjustResize
android.wakelock = True
p4a.optimize_python = 1

# ============================================================
# LOGS Y DEPURACIÓN
# ============================================================
log_level = 2
logcat_filters = *:I python:D Kivy:D

# ============================================================
# COMPATIBILIDAD GLOBAL
# ============================================================
android.allow_backup = True
android.supports_rtl = True
android.manifest.launch_mode = singleTop
android.manifest.theme = @style/Theme.AppCompat.NoActionBar
android.default_locale = es_EC
android.extra_resources = app_name=%(title)s

# ============================================================
# CONTROL AVANZADO DE DEPENDENCIAS
# ============================================================
p4a.whitelist = 
p4a.blacklist = 

# ============================================================
# [BUILDOZER]
# ============================================================
[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0

