from pytube import YouTube


def downloader(self, url, res, directory, *args, **kwargs):
    """
    This function is used to get the address of a youtube video.

    param self: The object itself.
    type self: VideoDownloader

    param url: The url of the video on Youtube.
    type url: str

    param res: The video resulotion
    type res: str

    param directory: The download directory
    type directory: str
    """
    video_url = str(url)
    resulotion = str(res)
    directory = str(directory)

    video = YouTube(video_url)
    stream = video.streams.filter(res=resulotion).first()

    if stream:
        try:
            stream.download(directory)
            print('Video downloaded successfully')
            return True
        except Exception as e:
            print(f"An error occurred while downloading the video:\n{e}")
            return False
    else:
        print("Error! Couldn't find that resolution.")
        print(stream)
        return False


# Tests 
video_url = "https://www.youtube.com/watch?v=TIymoKXRTZg"
resulotion = "1080p"
directory = "D:/youtube/"

test = downloader(url=video_url, res=resulotion, directory=directory)
