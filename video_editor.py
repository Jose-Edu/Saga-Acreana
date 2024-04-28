import moviepy.editor as editor


chars = 'abcdefghijklmnopqrstuvwxyz'
intro = editor.VideoFileClip('intro.mp4')
end = False

for char in chars:
    if end == False:

        media_out = list()
        media_out.append(intro)

        for part in (1, 2):
            try:
                media_out.append(editor.VideoFileClip(f'video//{char}{part}.mp4'))
            except:
                if part == 1:
                    end = True
        if not end:
            media_out.append(intro)
            media_out = editor.concatenate_videoclips(media_out)
            media_out.write_videofile(f'output//{char}.mp4')
    else:
        break