# https://github.com/mps-youtube/pafy
# pip install pafy
# pip install mopidy-youtube

import pafy

if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=D_Ij3fAps4s' # 따옴표 안에 유튜브 공유 주소를 넣음
    video = pafy.new(video_url)
    print(video.title, video.duration)

    best = video.getbest()
    best.download(quiet=False)
