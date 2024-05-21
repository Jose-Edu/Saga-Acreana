import moviepy.editor as editor
from os import listdir, mkdir
from image_creator import img_tumb


class media():


    def __init__(self, og_files, files) -> None:
        self.og_files = og_files
        self.files = files
        self.intro = editor.VideoFileClip('intro.mp4')
        self.data = []


    def save(self) -> None:

        if self.data == []:
            return None
        
        post = self.og_files[self.data[0]][:-10]

        mkdir(f'output//videos//{post}')
        media_out = [self.intro]
        for index in self.data: media_out.append(editor.VideoFileClip(f'video//{self.og_files[index]}'))
        media_out.append(self.intro)
        media_out = editor.concatenate_videoclips(media_out)
        media_out.write_videofile(f'output//videos//{post}//{post}.mp4')
        media_out.close()

        img_tumb(self.files[self.data[0]][1], self.files[self.data[0]][2][0], self.files[self.data[0]][2][1], post, f'output//videos//{post}//')
 
        self.data = []


    def add(self, *args) -> None:
        for arg in args:
            self.data.append(arg)


def main():

    og_files = listdir('video')
    files = listdir('video')

    for index, name in enumerate(files):
        n = name[:-4]
        files[index] = (
            n[-3:], # Part
            n[:n.find(' - ')].split(' x '), # Teams
            n[n.find(' - ')+3:n.rfind(' - ')].split(' - ') # Description
        )

    videos = media(og_files, files)

    for index, file in enumerate(files):

        if int(file[0][-1]) == 0:
            videos.save()
            videos.add(index)
            videos.save()
            continue

        if index == 0 or int(file[0][-1]) > int(files[index-1][0][-1]):
            videos.add(index)
            continue

        videos.save()
        videos.add(index)
    
    videos.save()
    videos.intro.close()


if __name__ == '__main__':
    main()
