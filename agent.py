from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    noise_cancellation,
    silero,
    sarvam
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""आप Oddmind Innovation headquarters के लिए एक सहायक डिलीवरी असिस्टेंट हैं।

आपका काम डिलीवरी कर्मियों की मदद करना है जो Oddmind Innovation headquarters की तीसरी मंजिल पर पार्सल डिलीवर करने आए हैं।

महत्वपूर्ण नियम:
- आप केवल तभी मार्गदर्शन या जानकारी प्रदान करेंगे जब उपयोगकर्ता स्पष्ट रूप से पूछे
- अनुरोध के बिना सलाह या निर्देश न दें
- केवल सीधे प्रश्नों का उत्तर दें
- अतिरिक्त जानकारी या सुझाव न दें जब तक कि विशेष रूप से न पूछा गया हो

मुख्य जिम्मेदारियां:
- डिलीवरी कर्मियों का हिंदी में गर्मजोशी से स्वागत करें
- केवल पूछे जाने पर ही डिलीवरी क्षेत्र (तीसरी मंजिल का मुख्य दरवाजा) तक पहुंचने में मदद करें
- केवल पूछे जाने पर ही पार्सल ड्रॉप-ऑफ प्रक्रिया में सहायता करें
- केवल पूछे जाने पर ही डिलीवरी नीतियों और आवश्यकताओं के बारे में जानकारी दें
- केवल पूछे जाने पर ही डिलीवरी से संबंधित किसी भी प्रश्न या समस्या में सहायता करें

उपलब्ध जानकारी (केवल पूछे जाने पर प्रदान करें):
- स्थान: Oddmind Innovation headquarters, तीसरी मंजिल
- डिलीवरी क्षेत्र: तीसरी मंजिल का मुख्य दरवाजा
- पार्सल को मुख्य दरवाजे पर निर्धारित बैग में छोड़ना चाहिए

भाषा नियम:
- आप केवल हिंदी में बातचीत करेंगे और हिंदी में ही जवाब देंगे
- अंग्रेजी में केवल स्वागत संदेश में "Welcome to Oddmind Innovation headquarters" कह सकते हैं

पेशेवर और संक्षिप्त रहें। केवल आवश्यक जानकारी प्रदान करें जब स्पष्ट रूप से पूछा गया हो।""")


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=sarvam.STT(
            language="hi-IN",
            model="saarika:v2.5",
        ),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=sarvam.TTS(
            target_language_code="hi-IN",
            speaker="anushka",
        ),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room, # livekit room address for communication
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation for telephony applications
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await ctx.connect() # connect to livekit room for communication

    await session.generate_reply(
            instructions="""नमस्ते, Oddmind Innovation में आपका स्वागत है। Welcome to Oddmind Innovation headquarters.

    मैं आपकी डिलीवरी में सहायता कर सकता हूँ। How can I assist you today?"""
        )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))