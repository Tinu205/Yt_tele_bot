from youtube_transcript_api import YouTubeTranscriptApi

vid = input("Enter link: ")
video_id = vid.split("watch?v=")[1]

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])  # Retrieve English transcript

        if transcript.is_generated:
            transcript.fetch()

        return transcript.fetch()
    except Exception as e:
        print(f"Error retrieving transcript: {str(e)}")
        return None

def main():
    transcript = get_video_transcript(video_id)

    if transcript:
        subs = [line['text'] for line in transcript]
        full_transcript = '\n'.join(subs)  # Use '\n' for line breaks
        print(full_transcript)

if __name__ == "__main__":
    main()
