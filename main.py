def process_music_list(music_list):
    result = []
    i = 0
    while i < len(music_list):
        title = music_list[i].strip()
        remix = ""
        if i+4 < len(music_list) and music_list[i+4] == "":
            remix = music_list[i + 1].strip()
            i += 1
        author = music_list[i + 1].strip()
        result.append(f"{author} - {title} {remix}")
        i += 4
    return result

with open('yam.md') as music_file:
    music_text = music_file.read()
music_list = list(music_text.split("\n"))


result = process_music_list(music_list)
#print(result)
print("\n".join(result))
print(type(result))

with open('yam_result.md', 'w') as tmpfile:
    for ll in result:
        tmpfile.write(f'{ll}\n')
'''

music_list = [
    "Plasma",
    "Original Mix",
    "Colombo",
    "5:33",
    "",
    "Keep on Doing",
    "Stanton Warriors",
    "4:11",
    "",
    "Selections",
    "Original Mix",
    "Colombo",
    "4:32",
]



while i < len(music_list):
    title = music_list[i].strip()
    remix = ""
    if i+4 < len(music_list) and music_list[i+4] == "":
        remix = music_list[i + 1].strip()
        i += 1
    author = music_list[i + 1].strip()
    result.append(f"{author} - {title} {remix}")
    i += 4
    print(f"{author} - {title} {remix}")



'''

