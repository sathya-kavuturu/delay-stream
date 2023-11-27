import subprocess

def download_youtube_stream(video_url, output_file):
    # Use youtube-dl to download the stream
    youtube_dl_command = ['yt-dlp', '-o', '-', video_url]
    youtube_dl_process = subprocess.Popen(youtube_dl_command, stdout=subprocess.PIPE)

    # Use ffmpeg to read from the standard input and copy the content to the specified output file
    ffmpeg_command = ['ffmpeg', '-i', '-', '-c', 'copy', output_file]
    ffmpeg_process = subprocess.Popen(ffmpeg_command, stdin=youtube_dl_process.stdout)

    # Wait for the processes to complete
    youtube_dl_process.wait()
    ffmpeg_process.wait()

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=vWnqj9WFzik"

    # Dynamically generate output file name based on video ID
    video_id = video_url.split("v=")[1]
    output_file = f"{video_id}_output.ts"

    download_youtube_stream(video_url, output_file)
