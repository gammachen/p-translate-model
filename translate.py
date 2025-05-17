import os
import re
from transformers import MarianMTModel, MarianTokenizer
from typing import Optional

class LocalModelTranslator:
    def __init__(self, model_name: str = 'Helsinki-NLP/opus-mt-en-zh'):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self._setup_model_cache()
        self._load_model()

    def _setup_model_cache(self) -> None:
        """设置模型缓存目录"""
        self.model_cache_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'models'
        )
        os.makedirs(self.model_cache_dir, exist_ok=True)

    def _load_model(self) -> None:
        """加载预训练模型和分词器"""
        try:
            self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
            self.model = MarianMTModel.from_pretrained(self.model_name)
            print("本地模型加载成功")
        except Exception as e:
            print(f"加载本地模型失败: {e}")
            self.tokenizer = None
            self.model = None

    def translate(self, text: str) -> Optional[str]:
        """
        使用本地模型进行翻译
        
        :param text: 待翻译文本
        :return: 翻译结果或 None（失败时）
        """
        if not self.tokenizer or not self.model:
            print("模型未正确加载，无法翻译")
            return None

        try:
            # 编码输入文本
            batch = self.tokenizer([text], return_tensors="pt", padding="max_length", truncation=True, max_length=512)

            # 生成翻译结果
            translated = self.model.generate(
                **batch,
                num_beams=4,
                no_repeat_ngram_size=2,
                early_stopping=True,
                max_length=1024
            )

            # 解码输出
            tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
            result = tgt_text[0]

            # 去除重复中文词语
            pattern = r'([\u4e00-\u9fa5]+)(?:\s*\1)+'
            result = re.sub(pattern, r'\1', result)

            return result
        except Exception as e:
            print(f"翻译时出错: {e}")
            return None

if __name__ == "__main__":
    # 使用本地模型翻译
    local_translator = LocalModelTranslator()

    # 测试翻译
    texts_to_translate = [
        "Good morning, everyone! busywork",
        "busywork",
        "If you like adult comedy cartoons...",
        "Can I please say first of all..."
    ]

    for text in texts_to_translate:
        translation = local_translator.translate(text)
        print(f"\nOriginal Text:\n{text}")
        print(f"Translated Text:\n{translation}")