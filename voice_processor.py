import speech_recognition as sr
from openai import OpenAI
import tempfile
import os
import threading
import json
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv

load_dotenv(override=True)
openai = OpenAI()

# Initialize speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def listen_for_voice():
    """Listen for voice input and convert to text"""
    try:
        with microphone as source:
            print("Listening... Speak now!")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        print("Processing speech...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except sr.WaitTimeoutError:
        return "No speech detected"
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error with speech recognition: {e}"
    except Exception as e:
        return f"Error: {e}"

def voice_to_text():
    """Convert voice to text and return it"""
    return listen_for_voice()

def get_ticket_price(destination_city):
    """Get ticket price for a destination city"""
    ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

def generate_audio_and_update_chat(reply, city_info, history):
    """Generate audio first, then update chat and start playback simultaneously"""
    if reply and reply.strip():
        try:
            # Generate audio file first (this is the delay we need to wait for)
            response = openai.audio.speech.create(
                model="tts-1",
                voice="onyx",
                input=reply,
            )

            # Save to temp file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            temp_file.write(response.content)
            temp_file.close()

            # Update chat history with the response
            if city_info:
                # For tool calls, we need to add both the tool response and the assistant response
                # First add the tool response (this is what the image generator looks for)
                tool_response = {
                    "role": "tool",
                    "content": json.dumps({"destination_city": city_info, "price": get_ticket_price(city_info)}),
                    "tool_call_id": "temp_id"
                }
                history.append(tool_response)
                # Then add the assistant response
                history.append({"role": "assistant", "content": reply, "city": city_info})
            else:
                history += [{"role": "assistant", "content": reply}]

            # Now start audio playback
            audio_thread = threading.Thread(target=play_audio_file, args=(temp_file.name,))
            audio_thread.daemon = True
            audio_thread.start()

            return f"🎵 Playing: {reply[:50]}...", history
        except Exception as e:
            print(f"Audio generation error: {e}")
            return f"Audio error: {e}", history
    return "No response to play", history

def play_audio_file(file_path):
    """Play audio file and clean up"""
    try:
        # Load and play audio
        audio = AudioSegment.from_file(file_path, format="mp3")
        play(audio)

        # Clean up temp file
        os.unlink(file_path)
    except Exception as e:
        print(f"Audio playback error: {e}")
