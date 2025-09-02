#!/usr/bin/env python3
"""
Test script for voice functionality
"""
import speech_recognition as sr

def test_microphone():
    """Test if microphone is working"""
    try:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        print("Testing microphone access...")
        with microphone as source:
            print("Microphone accessed successfully!")
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ready to listen!")

        return True
    except Exception as e:
        print(f"Error accessing microphone: {e}")
        return False

def test_speech_recognition():
    """Test speech recognition with a simple phrase"""
    try:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        print("\nPlease say 'Hello World' when prompted...")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening... (say 'Hello World')")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        print("Processing speech...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")

        if "hello" in text.lower() or "world" in text.lower():
            print("✅ Speech recognition test passed!")
            return True
        else:
            print("❌ Speech recognition test failed - unexpected text")
            return False

    except sr.WaitTimeoutError:
        print("❌ No speech detected within timeout")
        return False
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return False
    except sr.RequestError as e:
        print(f"❌ Error with speech recognition service: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("Voice Functionality Test")
    print("=" * 30)

    # Test microphone access
    if test_microphone():
        print("\nMicrophone test: ✅ PASSED")

        # Test speech recognition
        if test_speech_recognition():
            print("\nOverall test: ✅ PASSED")
            print("Voice functionality is working correctly!")
        else:
            print("\nOverall test: ❌ FAILED")
            print("Speech recognition is not working properly.")
    else:
        print("\nOverall test: ❌ FAILED")
        print("Microphone access failed.")
