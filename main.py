midi.use_raw_serial(8)
midi.play_tone(440, music.beat(BeatFraction.WHOLE))
midi.tone_on(440)
midi.tone_on(494)
basic.pause(100)
midi.tone_off(440)
midi.tone_off(494)
midi.play_drum(DrumSound.HAND_CLAP)