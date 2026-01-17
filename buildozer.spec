[app]
title = APK Python
package.name = apkpython
package.domain = org.edipratama

source.dir = .
source.include_exts = py
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# 🔒 PAKSA VERSI STABIL (JANGAN 36)
android.api = 33
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1
