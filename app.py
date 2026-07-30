Enter file contents here
import gradio as gr

def astrobot(question):
    return f"""🙏 Welcome to Vedic AstroBot

You asked:
{question}

This is the first version of AstroBot.

It will soon support:
✅ Panchang
✅ Horoscope
✅ Kundli
✅ Muhurta
✅ Vastu
✅ Numerology
✅ Festival Information

Thank you for using Vedic AstroBot!
"""

demo = gr.Interface(
    fn=astrobot,
    inputs=gr.Textbox(label="Ask your Vedic Astrology Question"),
    outputs=gr.Textbox(label="Answer"),
    title="🕉️ Vedic AstroBot",
    description="AI-powered Vedic Astrology Assistant"
)

demo.launch()
