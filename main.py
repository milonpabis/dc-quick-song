from QuickMusic import QuickMusic, INTENTS
import os


if __name__ == "__main__":
    client = QuickMusic(intents=INTENTS)
    env = os.getenv("DISCORD_TOKEN")
    client.run(env)