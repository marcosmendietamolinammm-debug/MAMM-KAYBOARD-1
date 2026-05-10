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

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,pillow,qrcode,pyzbar,plyer,urllib3,charset-normalizer,idna,requests,openssl,android,pyjnius

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# (bool) Indicate whether the app should be in fullscreen or not.
fullscreen = 0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Whitlelist pattern to authorize for the application
#android.whitelist =

# (str) Android API level to compile against
android.api = 34

# (str) Minimum Android API level required
android.minapi = 21

# (str) Android SDK directory (if empty, buildozer will download it)
#android.sdk_path =

# (str) Android NDK directory (if empty, buildozer will download it)
#android.ndk_path =

# (str) Android NDK version to use
android.ndk = 25c

# (bool) Use Java 8 (recommended)
android.use_java8 = True

# (str) Java 8 directory (if empty, auto-detect)
#android.java8_path =

# (str) Android build-tools version to use
android.build_tools = 34.0.0

# (str) Gradle version to use
android.gradle = 8.5

# (list) Android Java compiler flags
#android.add_java_compiler_flags =

# (list) Android libraries to add (like for androidx)
android.add_libs_armeabi_v7a =
android.add_libs_arm64_v8a =
android.add_libs_x86 =
android.add_libs_x86_64 =

# (list) Android features to add
#android.add_features = android.hardware.camera,android.hardware.camera.autofocus

# (list) Permissions
android.permissions = INTERNET, CAMERA, VIBRATE, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target architecture (0 = armeabi-v7a, 1 = arm64-v8a)
android.arch = 1

# (bool) Sign the APK with keystore
# android.release = False

# (str) Key alias
# android.keyalias =

# (str) Key password
# android.keystore_password =

# (str) Key full path
# android.keystore =

# (list) Service to use
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) Android logcat filters
# android.logcat_filters = *:S python:D

# (bool) Android automatic SDK license acceptance (needed for CI)
android.accept_sdk_license = True

# (str) Android entry point to your app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom AndroidManifest.xml
#android.manifest.custom =

# (str) Path to a custom build.gradle
#android.gradle.custom =

# (bool) Use AndroidX
android.use_androidx = True

# (str) Android App Bundle (.aab) file generation
# android.release_artifact = aab

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (str) Android project URL
#android.url =

# (str) Android packaging format (apk or aab)
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

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, default is under app root
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app@demo:source.exclude_patterns]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug
