[app]
title = MAMM KEYBOARD 1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini
version = 1.0.2
version.code = 3

requirements = python3,kivy==2.2.1,setuptools,urllib3<2.0.0,six,plyer,pyjnius,ujson,cython==3.0.11,openssl,requests,android,pyzbar,qrcode,Pillow,SpeechRecognition,pyttsx3

android.permissions = \
    INTERNET,\
    VIBRATE,\
    WAKE_LOCK,\
    SYSTEM_ALERT_WINDOW,\
    FOREGROUND_SERVICE,\
    FOREGROUND_SERVICE_DATA_SYNC,\
    RECEIVE_BOOT_COMPLETED,\
    MANAGE_EXTERNAL_STORAGE,\
    REQUEST_INSTALL_PACKAGES,\
    CALL_PHONE,\
    READ_CONTACTS,\
    CAMERA,\
    RECORD_AUDIO

android.api = 34
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0

android.manifest_extra = <service android:name=".ServiceMamm" android:foregroundServiceType="dataSync|shortTasks" android:exported="false"></service>

p4a.bootstrap = sdl2
p4a.branch = master

android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True

android.debug = True
android.release = False
android.release_artifact = apk

orientation = portrait
fullscreen = 0
window_soft_input_mode = adjustResize

android.wakelock = True

log_level = 2
logcat_filters = *:I python:D Kivy:D

android.allow_backup = True
android.supports_rtl = True
android.manifest.launch_mode = singleTop
android.manifest.theme = @style/Theme.AppCompat.NoActionBar

icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

android.default_locale = es_EC
android.extra_resources = app_name=%(title)s

p4a.whitelist =
p4a.blacklist =

p4a.optimize_python = 1
android.skip_update = False

[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
