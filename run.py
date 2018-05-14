import p0fmod
p0fmod.set_iface("eno1")
p0fmod.set_api_sock("/var/run/p0f.sock")
#p0fmod.en_daemon_mode()
p0fmod.start_p0f()
