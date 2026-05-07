[app]
title = MAMM KEYBOARD 1
package.name = mammkeyboard1
package.domain = org.mammkeyboard
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json,gif,mp3,wav,ogg,ini
version = 1.0.2
requirements = python3,kivy==2.2.1,setuptools,requests,android
android.permissions = INTERNET,VIBRATE,WAKE_LOCK,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED,MANAGE_EXTERNAL_STORAGE,REQUEST_INSTALL_PACKAGES,CALL_PHONE,READ_CONTACTS,CAMERA,RECORD_AUDIO
android.api = 35
android.minapi = 21
android.sdk = 35
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.debug = True
android.release = False
android.release_artifact = apk
orientation = portrait
fullscreen = 0
android.wakelock = True
log_level = 2
[buildozer]
build_dir = .buildozer
bin_dir = ./bin
log_level = 2
warn_on_root = 0
