[app]
title = MAMM KEYBOARD 1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini
version = 1.0.2
version.code = 3

# --- Requisitos: Se eliminó Cython de aquí para evitar conflictos con la instalación del sistema ---
requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

# --- Permisos (Limpiados de espacios extra para evitar errores de lectura) ---
android.permissions = INTERNET,VIBRATE,WAKE_LOCK,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE,FOREGROUND_SERVICE_DATA_SYNC,RECEIVE_BOOT_COMPLETED,MANAGE_EXTERNAL_STORAGE,REQUEST_INSTALL_PACKAGES,CALL_PHONE,READ_CONTACTS,CAMERA,RECORD_AUDIO

# --- Versiones de Android: Se eliminó android.sdk manual para evitar el WARNING del log ---
android.api = 34
android.minapi = 21
android.ndk = 25c
android.build_tools_version = 34.0.0

# --- Tipo de Foreground Service para Android 15 ---
android.manifest_extra = |
    <service android:name=".ServiceMamm" 
             android:foregroundServiceType="dataSync|shortTasks" 
             android:exported="false">
    </service>

p4a.bootstrap = sdl2
p4a.branch = develop

# --- Arquitecturas ---
android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True
android.gradle_dependencies = androidx.core:core:1.13.1,androidx.appcompat:appcompat:1.6.1,com.google.android.material:material:1.11.0

android.debug = True
android.release = False
android.release_artifact = apk

orientation = portrait
fullscreen = 0
window_soft_input_mode = adjustResize

# --- WakeLock para el Motor de Resonancia ---
android.wakelock = True

log_level = 2
logcat_filters = *:I python:D Kivy:D

android.allow_backup = True
android.supports_rtl = True
android.manifest.launch_mode = singleTop

# --- Rutas de recursos (Asegúrate de que existan estas carpetas) ---
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

android.default_locale = es_EC

p4a.optimize_python = 1
android.skip_update = False

[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
