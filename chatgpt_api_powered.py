import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "CHAT GPT POWERED API BOT"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply
    except Exception as e:
        raise Exception("Error occurred during prediction: {}".format(str(e)))

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="CUSTOMER ASSISTANCE BOT")

demo.launch(share=True)
