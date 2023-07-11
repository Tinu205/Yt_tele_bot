from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])  # Retrieve English transcript

        return transcript.fetch()
    except Exception as e:
        error_message = f"Error retrieving transcript: {str(e)}"
        return None

def give_subs(video_id):
    transcript = get_video_transcript(video_id)
    if not transcript:
        return "Error retrieving transcript."
    subs = [line['text'] for line in transcript]
    full_transcript = '\n'.join(subs)  # Use '\n' for line breaks
    return full_transcript

def check_link(fulnk):
    try:
            video_id = fulnk.split("watch?v=")[1]
    except IndexError:
            try:
                video_id = fulnk.split("youtu.be/")[1]
            except IndexError:
                video_id = 0;

    return video_id