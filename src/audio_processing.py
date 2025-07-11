from spleeter.separator import Separator

def separate_stems(input_song_path, output_dir="output"):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_song_path, output_dir)
    return (f"{output_dir}/accompaniment.wav", f"{output_dir}/vocals.wav")


separate_stems("NightChanges.mp3")