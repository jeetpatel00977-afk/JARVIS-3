import datetime
import requests
import random
import webbrowser


# ============================================================
# WIKIPEDIA SEARCH
# ============================================================

def search_wikipedia(topic):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json",
        "utf8": 1,
        "srlimit": 1
    }

    headers = {
        "User-Agent": "JARVIS-3/1.0 (personal learning project)"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            print(
                f"JARVIS > Wikipedia connection error: "
                f"{response.status_code}"
            )
            return

        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            print(
                f"JARVIS > I couldn't find anything about '{topic}'."
            )
            return

        result = results[0]

        title = result["title"]

        print()
        print(f"JARVIS > I found: {title}")
        print("-" * 60)

        # Get the page summary
        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + title.replace(" ", "_")
        )

        summary_response = requests.get(
            summary_url,
            headers=headers,
            timeout=10
        )

        if summary_response.status_code == 200:
            summary_data = summary_response.json()

            extract = summary_data.get("extract")

            if extract:
                print(f"JARVIS > {extract}")
            else:
                print(
                    "JARVIS > I found the page, "
                    "but couldn't get its summary."
                )

        else:
            print(
                f"JARVIS > I found the page: {title}"
            )

        print("-" * 60)

    except requests.exceptions.RequestException as error:
        print(
            "JARVIS > I couldn't connect to Wikipedia."
        )
        print(f"JARVIS > Error: {error}")


# ============================================================
# MAIN JARVIS
# ============================================================

def jarvis():

    print("=" * 60)
    print("                 J.A.R.V.I.S. ONLINE")
    print("=" * 60)

    print("Hello, sir. All systems are ready.")
    print("Type 'help' to see what I can do.")
    print()

    while True:

        command = input("YOU > ").strip()

        if not command:
            continue

        command_lower = command.lower()


        # ====================================================
        # GREETINGS
        # ====================================================

        if any(word in command_lower for word in [
            "hello",
            "hi",
            "hey"
        ]):

            responses = [
                "Hello, sir. How can I assist you?",
                "Good to hear from you, sir.",
                "JARVIS online and ready.",
                "At your service, sir."
            ]

            print("JARVIS >", random.choice(responses))


        # ====================================================
        # TIME
        # ====================================================

        elif "time" in command_lower:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            print(
                f"JARVIS > The current time is {current_time}."
            )


        # ====================================================
        # DATE
        # ====================================================

        elif (
            "date" in command_lower
            or "today" in command_lower
        ):

            current_date = datetime.datetime.now().strftime(
                "%d %B %Y"
            )

            print(
                f"JARVIS > Today is {current_date}."
            )


        # ====================================================
        # IDENTITY
        # ====================================================

        elif (
            "who are you" in command_lower
            or "your name" in command_lower
        ):

            print(
                "JARVIS > I am JARVIS, your personal AI assistant."
            )


        # ====================================================
        # HOW ARE YOU
        # ====================================================

        elif "how are you" in command_lower:

            print(
                "JARVIS > All systems are operational, sir."
            )


        # ====================================================
        # STATUS
        # ====================================================

        elif "status" in command_lower:

            print("""
JARVIS > SYSTEM STATUS
------------------------------------------------------------

  Core System       : ONLINE
  Command System    : ONLINE
  Time System       : ONLINE
  Date System       : ONLINE
  Web Browser       : ONLINE
  Wikipedia Search  : ONLINE
  Voice System      : NOT INSTALLED
  AI Brain          : FUTURE UPGRADE

------------------------------------------------------------
""")


        # ====================================================
        # WIKIPEDIA SEARCH
        # ====================================================

        elif command_lower.startswith(
            "search wikipedia for "
        ):

            topic = command[21:].strip()

            if topic:

                print(
                    f"JARVIS > Searching Wikipedia for {topic}..."
                )

                search_wikipedia(topic)

            else:

                print(
                    "JARVIS > Please tell me what you want me to search for."
                )


        # ====================================================
        # SIMPLE SEARCH
        # Example: search ronaldo
        # ====================================================

        elif command_lower.startswith("search "):

            topic = command[7:].strip()

            if topic:

                print(
                    f"JARVIS > Searching Wikipedia for {topic}..."
                )

                search_wikipedia(topic)

            else:

                print(
                    "JARVIS > Please tell me what you want me to search for."
                )


        # ====================================================
        # GOOGLE
        # ====================================================

        elif "open google" in command_lower:

            print(
                "JARVIS > Opening Google, sir."
            )

            webbrowser.open(
                "https://www.google.com"
            )


        # ====================================================
        # YOUTUBE
        # ====================================================

        elif "open youtube" in command_lower:

            print(
                "JARVIS > Opening YouTube, sir."
            )

            webbrowser.open(
                "https://www.youtube.com"
            )


        # ====================================================
        # GITHUB
        # ====================================================

        elif "open github" in command_lower:

            print(
                "JARVIS > Opening GitHub, sir."
            )

            webbrowser.open(
                "https://github.com"
            )


        # ====================================================
        # HELP
        # ====================================================

        elif (
            "help" in command_lower
            or "what can you do" in command_lower
        ):

            print("""
JARVIS > CURRENT CAPABILITIES
------------------------------------------------------------

  1. Greetings
  2. Tell the time
  3. Tell the date
  4. Search Wikipedia
  5. Search using "search <topic>"
  6. Open Google
  7. Open YouTube
  8. Open GitHub
  9. Basic conversation
 10. System status
 11. Shutdown

Examples:

  hello
  what time is it
  what is today's date
  who are you
  search ronaldo
  search cristiano ronaldo
  search football
  open google
  open youtube
  open github
  status
  help
  exit

------------------------------------------------------------
""")


        # ====================================================
        # SHUTDOWN
        # ====================================================

        elif any(word in command_lower for word in [
            "exit",
            "quit",
            "shutdown"
        ]):

            print(
                "JARVIS > Shutting down. Goodbye, sir."
            )

            break


        # ====================================================
        # UNKNOWN COMMAND
        # ====================================================

        else:

            print(
                "JARVIS > I don't understand that command yet, sir."
            )


# ============================================================
# START JARVIS
# ============================================================

if __name__ == "__main__":
    jarvis()