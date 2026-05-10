[app]
title = MAMM KEYBOARD 1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini
version = 1.0.3
version.code = 4

# --- Requisitos (Cython estable para compatibilidad) ---
requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,cython==0.29.33,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

# --- Permisos (incluyendo BIND_INPUT_METHOD para teclado) ---
android.permissions = \
    BIND_INPUT_METHOD,\
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
    CAMERA,\
    RECORD_AUDIO

# --- Servicio de teclado ---
services = MAMMKeyboard:service.py

# --- Android 16 (API 36) ---
android.api = 36
android.minapi = 28
android.ndk_api = 28
android.sdk = 36
android.ndk = 25c

p4a.bootstrap = sdl2
p4a.branch = master

# --- Arquitectura exclusiva para Honor Magic 7 Lite ---
android.archs = arm64-v8a

android.enable_androidx = True
android.gradle_dependencies = \
    androidx.core:core:1.13.1,\
    androidx.appcompat:appcompat:1.6.1,\
    com.google.android.material:material:1.11.0

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
android.manifest.theme = @style/Theme.AppCompat.NoActionBar

# --- Icono y Splash Screen ---
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

android.default_locale = es_EC
android.extra_resources = app_name=%(title)s

p4a.whitelist =
p4a.blacklist =

p4a.optimize_python = 1
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
