data = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
def modifySong(songStr):
    songStr = data.lower()
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch, '')
    return songStr

print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)