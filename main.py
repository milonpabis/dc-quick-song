from QuickMusic import os, QuickMusic, INTENTS


if __name__ == "__main__":
    client = QuickMusic(intents=INTENTS)
    env = os.environ["DISCORD_TOKEN"]
    print(env)
    #client.run(env)