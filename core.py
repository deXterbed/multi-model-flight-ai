import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

openai = OpenAI()

MODEL = "gpt-3.5-turbo"
system_message = "You are a helpful assistant for an Airline called FlightAI. "
system_message += "Give short, courteous answers, no more than 1 sentence. "
system_message += "Always be accurate. If you don't know the answer, say so."

ticket_prices = {"london": "$799", "paris": "$899", "tokyo": "$1400", "berlin": "$499"}

def get_ticket_price(destination_city):
    """Get ticket price for a destination city"""
    print(f"Tool get_ticket_price called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city. Call this whenever you need to know the ticket price, for example when a customer asks 'How much is a ticket to this city'",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}

tools = [{"type": "function", "function": price_function}]

def handle_tool_calls(message):
    """Handle all tool calls for ticket price queries. Returns (list of tool responses, first city for sync)."""
    responses = []
    first_city = None
    for tool_call in message.tool_calls:
        arguments = json.loads(tool_call.function.arguments)
        city = arguments.get("destination_city")
        price = get_ticket_price(city)
        if first_city is None:
            first_city = city
        responses.append({
            "role": "tool",
            "content": json.dumps({"destination_city": city, "price": price}),
            "tool_call_id": tool_call.id,
        })
    return responses, first_city

def chat(history):
    """Generate AI response without adding to history (for audio sync)"""
    # Validate and clean history
    cleaned_history = []
    for msg in history:
        if isinstance(msg, dict) and msg.get("content") is not None:
            cleaned_history.append(msg)
        elif isinstance(msg, dict) and msg.get("content") is None:
            cleaned_msg = msg.copy()
            cleaned_msg["content"] = ""
            cleaned_history.append(cleaned_msg)

    # Get the last user message
    last_user_message = None
    for msg in reversed(cleaned_history):
        if msg.get("role") == "user":
            last_user_message = msg.get("content")
            break

    if not last_user_message:
        return history, None, ""

    messages = (
        [{"role": "system", "content": system_message}]
        + cleaned_history
    )

    # Use faster model and parameters for instant response
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        temperature=0.3,  # More deterministic, faster
        max_tokens=100     # Shorter responses for speed
    )

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_responses, city = handle_tool_calls(message)

        assistant_message = {
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    }
                }
                for tc in message.tool_calls
            ]
        }
        messages.append(assistant_message)
        for tool_response in tool_responses:
            messages.append(tool_response)

        final_response = openai.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=80   # Very short for speed
        )
        reply = final_response.choices[0].message.content

        # Return response and city info, but don't add to history yet
        return history, None, reply, city
    else:
        reply = response.choices[0].message.content

        # Return response but don't add to history yet
        return history, None, reply, None
