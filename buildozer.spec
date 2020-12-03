[app]
title = Hello
package.name = hello
package.domain = dev.obfusk.example
source.dir = .
source.include_exts = py
version = 0.0.1
requirements = kivy==2.0.0rc4
requirements.source.kivy = ../kivy
orientation = portrait
fullscreen = 0
android.api = 29
android.minapi = 21
android.ndk = 20b
#android.ndk_path =
#android.sdk_path =
android.accept_sdk_license = True
android.arch = arm64-v8a
p4a.fork = obfusk
p4a.branch = python3.9
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
