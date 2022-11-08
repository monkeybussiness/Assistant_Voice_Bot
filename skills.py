import pyttsx3
import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[2].id)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def weather():
    print('Сейчас погода!!!')
    speaker('Сейчас погода!!!')


def greetings():
    speaker('Никита, я тут! Тебе нужна моя помощь?')


def sleep():
    speaker('До скорых встреч!')


def song():
    playsound.playsound('1.mp3')


def developer():
    speaker(f"Всем привет меня зовут Джарвис."
            f" Мой создатель Никита Суслов. Я умею, подсказывать время. Подбрасывать монетку."
            f" Переходить в фазу сна."
            f"И многое другое но не сейчас")
