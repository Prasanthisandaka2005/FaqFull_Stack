from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Existing languages
    question_hi = models.TextField(blank=True, null=True)  
    question_bn = models.TextField(blank=True, null=True)  
    question_fr = models.TextField(blank=True, null=True)  
    question_es = models.TextField(blank=True, null=True)  
    question_ta = models.TextField(blank=True, null=True)  
    question_te = models.TextField(blank=True, null=True) 

    answer_hi = models.TextField(blank=True, null=True)
    answer_bn = models.TextField(blank=True, null=True)
    answer_fr = models.TextField(blank=True, null=True)
    answer_es = models.TextField(blank=True, null=True)
    answer_ta = models.TextField(blank=True, null=True)
    answer_te = models.TextField(blank=True, null=True) 

    def translate_text(self, text, lang):
        """Translate text synchronously and handle None values."""
        if not text:
            return ""  

        try:
            result = translator.translate(text, dest=lang)
            return result.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text 

    def save(self, *args, **kwargs):
        """Automatically translate question & answer before saving."""
        translations = {
            "hi": ("question_hi", "answer_hi"),
            "bn": ("question_bn", "answer_bn"),
            "fr": ("question_fr", "answer_fr"),
            "es": ("question_es", "answer_es"),
            "ta": ("question_ta", "answer_ta"),
            "te": ("question_te", "answer_te"),
        }

        for lang, (q_field, a_field) in translations.items():
            if not getattr(self, q_field):
                setattr(self, q_field, self.translate_text(self.question, lang))
            if not getattr(self, a_field):
                setattr(self, a_field, self.translate_text(self.answer, lang))

        super().save(*args, **kwargs)

    def get_translated_faq(self, lang):
        """Retrieve the translated question & answer dynamically."""
        translations = {
            "hi": (self.question_hi, self.answer_hi),
            "bn": (self.question_bn, self.answer_bn),
            "fr": (self.question_fr, self.answer_fr),
            "es": (self.question_es, self.answer_es),
            "ta": (self.question_ta, self.answer_ta),
            "te": (self.question_te, self.answer_te),  
        }
        return translations.get(lang, (self.question, self.answer))  

    def __str__(self):
        return self.question
