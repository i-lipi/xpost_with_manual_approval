import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")

import os
import pandas as pd
import tweepy
from dotenv import load_dotenv
from crewai.flow.flow import Flow, start, listen
from self_evaluation_loop_flow.crews.shakespeare_crew.shakespeare_crew import ShakespeareanXPostCrew

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

if not consumer_key or not consumer_secret or not access_token or not access_secret:
    raise ValueError(" ERROR: Missing Twitter API keys. Check your .env file.")

# Authenticate with Tweepy Client 
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

#Excel File Path
EXCEL_FILE = r"C:\Users\Lipi Inampudi\OneDrive\Desktop\x_post_data.xlsx"

class ShakespeareXPostFlow(Flow):
    def __init__(self):
        super().__init__()
        try:
            self.df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
        except Exception as e:
            print(f"Error reading Excel file: {e}. Creating a new one...")
            self.df = pd.DataFrame(columns=["Topic", "Generated X Post", "Approval", "Posted"])

    @start()
    def generate_shakespeare_x_post(self):
        """Generates Shakespearean-style X posts for each topic in the Excel file."""
        generated_any = False  #Track if any tweets were generated

        for index, row in self.df.iterrows():
            if pd.isna(row["Generated X Post"]):  # Only generate if empty
                topic = row["Topic"]
                print(f"Generating X post for: {topic}")

                result = ShakespeareanXPostCrew().crew().kickoff(inputs={"topic": topic})

                # Save generated tweet
                self.df["Generated X Post"] = self.df["Generated X Post"].astype("string")
                self.df.at[index, "Generated X Post"] = str(result.raw)
                generated_any = True  # At least one tweet was generated

        self.save_excel()

        if generated_any:
            print("Tweets generated. Triggering 'complete' event...")
            return "complete"  # Move to post-to-twitter step
        else:
            print(" No new tweets generated. Skipping to posting...")
            self.post_to_twitter()  # Directly post tweets if none were generated

    @listen("complete")
    def post_to_twitter(self):
        """Posts approved X posts to Twitter."""
        print("`post_to_twitter()` function triggered!") 

        for index, row in self.df.iterrows():
            print(f" Checking Row {index}: {row['Topic']} | Approval: {row.get('Approval')} | Posted: {row.get('Posted')}")

            # "Approved" is properly read as a string
            if str(row.get("Approval")).strip().lower() == "approved" and pd.isna(row.get("Posted")):
                print(f" Attempting to post to Twitter: {row['Generated X Post']}")

                try:
                    response = client.create_tweet(text=row["Generated X Post"])
                    print(f" Tweet successfully posted! Tweet ID: {response.data['id']}")

                    # Mark as "Yes" in the "Posted" column
                    self.df.at[index, "Posted"] = "Yes"
                except tweepy.TweepyException as e:
                    print(f" Error posting tweet: {e}")
                    self.df.at[index, "Posted"] = "Failed"

        self.save_excel()

    def save_excel(self):
        """Safely writes data to Excel to avoid permission issues."""
        try:
            with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
                self.df.to_excel(writer, index=False)
            print("Excel file updated successfully.")
        except PermissionError:
            print("ERROR: Close the Excel file before running the script.")

def kickoff():
    flow = ShakespeareXPostFlow()
    flow.kickoff()

    flow.post_to_twitter()

if __name__ == "__main__":
    kickoff()
