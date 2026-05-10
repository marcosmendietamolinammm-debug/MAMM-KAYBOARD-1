[app]

# (str) Title of your application
title = MAMM-KEYBOARD-1

# (str) Package name
package.name = mammkeyboard

# (str) Package domain (needed for android/ios packaging)
package.domain = com.mamm

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (list) Source files to exclude
source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,pillow,qrcode,pyzbar,plyer,urllib3,charset-normalizer,idna,requests,openssl,android,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

#
# OSX Specific
#
fullscreen = 0

#
# Android specific
#
fullscreen = 1
android.api = 34
android.minapi = 21
android.ndk = 25c
android.use_java8 = True
android.build_tools = 34.0.0   # ← Versión fija que evita problemas de licencias
android.gradle = 8.5

android.add_libs_armeabi_v7a =
android.add_libs_arm64_v8a =
android.add_libs_x86 =
android.add_libs_x86_64 =

android.permissions = INTERNET, CAMERA, VIBRATE, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.arch = 1
android.accept_sdk_license = True   # ← Confirma aceptación de licencias
android.use_androidx = True
android.package_format = apk

#
# iOS specific
#
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.debug = "iPhone Developer"
ios.codesign.release = "iPhone Distribution"

[buildozer]
log_level = 2
warn_on_root = 1
