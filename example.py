import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import slack_components as sc

load_dotenv('./.env')

app = App(token=os.environ['SLACK_BOT_TOKEN'])

test_message = sc.blocks.SectionBlock(
            text= sc.commons.TextObject(
                type="plain_text",
                text="This Component has been generated from the python Library !"
            ),
            accessory=sc.elements.Button(
                text= sc.commons.TextObject(
                    type="plain_text",
                    text="Cool !"
                ),
                action_id='button_click',
            )
        )

@app.message("example")
def message_hello(message, say):
    say(blocks=[
        test_message
    ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")

if __name__ == "__main__":
    SocketModeHandler(
        app, 
        os.environ["SLACK_APP_TOKEN"],
        trace_enabled=True
        ).start()
