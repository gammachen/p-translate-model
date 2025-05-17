import asyncio
from googletrans import Translator, LANGUAGES
import os


class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()
        # 设置环境变量，使用镜像站点
        os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

        # 设置模型缓存目录
        self.model_cache_dir = os.path.join(os.path.dirname(__file__), 'models')
        os.makedirs(self.model_cache_dir, exist_ok=True)

    async def translate_word(self, word, dest_language='zh-cn'):
        """
        翻译给定的单词或文本。
        
        :param word: 要翻译的单词或文本
        :param dest_language: 目标语言代码，默认为简体中文 ('zh-cn')
        :return: 翻译结果
        """
        translation = await self.translator.translate(word, dest=dest_language)
        print(f"Translated ({LANGUAGES[dest_language]}): {translation.text}")
        return translation.text

    async def main(self):
        # 示例1：翻译 "hello"
        word_to_translate = "hello"
        destination_language = "zh-cn"  # 目标语言代码，例如 'zh-cn' 表示简体中文
        translated_text = await self.translate_word(word_to_translate, destination_language)
        print(translated_text)

        # 示例2：翻译 "busywork"
        word_to_translate = "busywork"
        destination_language = "zh-cn"  # 目标语言代码，例如 'zh-cn' 表示简体中文
        translated_text = await self.translate_word(word_to_translate, destination_language)
        print(translated_text)

        # 示例3：翻译长文本1
        text_to_translate = (
            "If you like adult comedy cartoons, like South Park, then this is nearly a similar format "
            "about the small adventures of three teenage girls at Bromwell High. Keisha, Natella and "
            "Latrina have given exploding sweets and behaved like bitches, I think Keisha is a good leader. "
            "There are also small stories going on with the teachers of the school. There's the idiotic principal, "
            "Mr. Bip, the nervous Maths teacher and many others. The cast is also fantastic, Lenny Henry's "
            "Gina Yashere, EastEnders Chrissie Watts, Tracy-Ann Oberman, Smack The Pony's Doon Mackichan, "
            "Dead Ringers' Mark Perry and Blunder's Nina Conti. I didn't know this came from Canada, but it "
            "is very good. Very good!"
        )
        translated_text = await self.translate_word(text_to_translate)
        print(f"Original Text: {text_to_translate}")
        print(f"Translated Text: {translated_text}")

        # 示例4：翻译长文本2
        text_to_translate = (
            "Can I please say first of all, that I felt so strongly about this movie that I signed up to IMDb "
            "specifically to review it. And my review? This is easily the worst movie I have ever seen.<br /><br />"
            "The synopsis of the movie sounded interesting- Nazis, occult, time travel, etc., but the movies plot "
            "failed to properly bring all these elements together. Remember the episode of South Park that featured "
            "manatees writing Family Guy using 'idea balls'? Did these manatees also write Unholy? Its like the writer "
            "wanted to include all these different ideas, but had no idea how to link them all together, and then to "
            "make things make even less sense, included a Donnie Darko-esquire time travel theme to the ending, messing "
            "up the chronology.<br /><br />I could tell from early on that this was a bad movie. Special effects were too "
            "low budget for anything better than straight to DVD. The acting wasn't great, but in fairness I've seen worse. "
            "I will praise the Nazi paintings, they were creepy, but the evil Nazi butcher guy was just comic.<br /><br />"
            "I don't have a vendetta against this movie or anything, but to be honest, I'm not even into the horror genre. "
            "But this movie cannot be described as a thriller or a drama. If this story had been well told, this would have "
            "been a good movie. But it has been over hyped. Waaaaay over hyped."
        )
        translated_text = await self.translate_word(text_to_translate)
        print(f"Original Text: {text_to_translate}")
        print(f"Translated Text: {translated_text}")


if __name__ == "__main__":
    translator = GoogleTranslator()
    asyncio.run(translator.main())