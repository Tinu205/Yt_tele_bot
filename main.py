from youtube_transcript_api import YouTubeTranscriptApi
video_id = "r-GSGH2RxJs"
def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])  # Retrieve English transcript

        if transcript.is_generated:
            transcript.generate()

        return transcript.fetch()
    except Exception as e:
        error_message = f"Error retrieving transcript: {str(e)}"
        return None, error_message

def give_subs(video_id):
    transcript, error = get_video_transcript(video_id)

    if error:
        return error

    if transcript:
        subs = [line['text'] for line in transcript]
        full_transcript = '\n'.join(subs)  # Use '\n' for line breaks
        return full_transcript

# Example usage
if __name__ == "__main__":
    video_id = "YOUR_VIDEO_ID"
    subtitles = give_subs(video_id)
    if subtitles:
        print(subtitles)
    else:
        print("Error retrieving subtitles.")
give_subs(video_id)