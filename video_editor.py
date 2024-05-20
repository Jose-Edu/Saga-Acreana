import moviepy.editor as editor
from os import listdir


def main(): #wip

    files = listdir('video')

    for index, name in enumerate(files):
        n = name[:-4]
        files[index] = (
            n[:3],
            n[6:n.find(' - ', 6)].split(' x '),
            n[n.find(' - ', 6)+3:].split(' - ')
        )

    intro = editor.VideoFileClip('intro.mp4')
    
    for file in files:

        media_out = list(intro, intro)


'''    intro = editor.VideoFileClip('intro.mp4')

    media_out = list()
    media_out.append(intro)
    media_out.append(editor.VideoFileClip(f'video//{char}{part}.mp4'))
    media_out.append(intro)
    media_out = editor.concatenate_videoclips(media_out)
    media_out.write_videofile(f'output//{char}.mp4')'''


if __name__ == '__main__':
    main()
