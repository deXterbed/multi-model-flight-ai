def do_entry(message, history):
    """Add user message to chat history"""
    history += [{"role": "user", "content": message}]
    return "", history

def handle_voice_input(history):
    """Handle voice input and add to chat"""
    from voice_processor import voice_to_text

    voice_text = voice_to_text()
    if voice_text and voice_text not in ["No speech detected", "Could not understand audio", "Error with speech recognition:", "Error:"]:
        # Add voice input to chat
        history += [{"role": "user", "content": f"🎤 {voice_text}"}]
        return history, f"Voice recognized: {voice_text}"
    else:
        return history, f"Voice input failed: {voice_text}"
