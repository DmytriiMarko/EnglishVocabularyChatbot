from config import mono_jar

keyboard_words = (
    "💵 Баланс",
    "⏩ Наступне слово",
    "⚙️ Налаштування",
    "✍️ Тест",
    "❓ Про бота",
    "📚 Мої слова"
)

levels = (
    ("A1", "LVLА1"),
    ("A2", "LVLА2"),
    ("B1", "LVLВ1"),
    ("B2", "LVLВ2"),
    ("C1", "LVLС1")
)

settings = (
    ("📈 Рівень", "SET1"),
    ("🔔 Сповіщення", "SET2"),
    ("👁️ Ховати переклад", "SET3")
)

spoiler = (
    ("Завжди", "HIDE1"),
    ("Ніколи", "HIDE0")
)

notification = (
    ("4 раз на день", "NOT4"),
    ("8 рази на день", "NOT8"),
    ("10 разів на день", "NOT10"),
    ("12 разів на день", "NOT12"),
    ("15 разів на день", "NOT15")
)

subscription = (
    ("💸 1 місяць - 50 грн", mono_jar + "?t={}&a=50"),
    ("💸 2 місяці - 80 грн", mono_jar + "?t={}&a=80"),
    ("💸 6 місяців - 220 грн", mono_jar + "?t={}&a=2250")
)

price_list = {
    50: 30,
    80: 60,
    220: 180
}


uk_dict = {
    'greeting': '✋ Привіт!\nЯ допоможу тобі вчити нові англійські слова! І ось яким чином: '
                '\n🔔 Надсилатиму тобі слова у сповіщеннях поки ти їх не вивчиш; '
                '\n💾 Зберігатиму слова, які ти вчиш та вивчені слова, щоб ти міг їх переглянути;'
                '\n🧑‍🏫 Перекладатиму і даватиму можливість вчити будь-які слова, які ти мені напишеш.'
                '\n\n✍️ Пиши @Helper з будь-яких питань.',
    'get_voice': '🎧 Озвучити',
    'word_translated': '🇬🇧 {} - {} 🇺🇦',
    'question_1': '📈 Вкажи якого рівня англійські слова ти хочеш вчити:',
    'question_2': '🔔 Скільки разів в день ти хочеш щоб я надсилав тобі слова у сповіщеннях? (оптимально 12):',
    'question_3': '👁️ Ховати переклад слів <span class="tg-spoiler">ось так</span>? Опція працює лише для слів які '
                  'мають приклади.',
    'conclusion': '💸 Тепер ти зможеш користуватись ботом безкоштовно 10 днів. Далі тобі слід буде передплатити '
                  'користування.\n\n🏁 Отож, поїхали! Просто натискай "⏩ Наступне слово" або напиши слово яке ти '
                  'хочеш вивчити.\n\n👁️ В налаштуваннях ти також можеш сховати переклад слів.',
    'settings': '⚙️ Налаштування\nМоя мова (інтерфейсу): 🇺🇦 Українська\nНавчальна мова: 🇬🇧 English\nРівень: ✨ {}'
                '\nСповіщення: 🔔 {} раз на день\nХовати переклад: 👁️ {}',
    'too_long_text': '⚠️ Вибач, обмеження на слово чи фразу 50 символів.',
    'confirmation': '\n\n- 🤔 Я надіслав тобі це слово лише разів: {} (рекомендовано 7). Справді вивчив?',
    'details': '📈 👼 {}: {} / {} ({}%).\n\n📚 Ти можеш подивитись слова які ти зараз вчиш (проходять у сповіщеннях),'
               ' а також слова які ти вже вивчив:',
    'subscribe': '💸 Твій акаунт активний до {} (ще днів: {}).\n\n'
                 '➕ Для продовження передплати користуйся кнопками нижче.\n\n'
                 '⚠️ Якщо сума платежу не заповнилась автоматично, введіть її вручну відповідно до обраного тарифу',
    'subscribe_out': '💸 Твоя передплата закінчилась\n\n'
                 '➕ Для продовження передплати користуйся кнопками нижче.\n\n'
                 '⚠️ Якщо сума платежу не заповнилась автоматично, введіть її вручну відповідно до обраного тарифу',
    'paid': 'Ви успішно продовжили підписку на {} днів',
    'incorrect': '⚠️ Вибач, але введене слово не є дійсним.',
    'words_not_found': '⚠️ Слова закінчились :)',
    'never': 'Ніколи',
    'always': 'Завжди',
    'learned': '👍 Знаю',
    'not_learned': '➕ Вчимо',
    'added_to_dict': '➕ Додано в словник!',
    'have_learned': '✔️ Вивчив',
    'have_learned_confirmed': '\n\n🎉 Вивчено!',
    'have_not_learned': '\n- 🕑 Продовжую вчити.',
    'learn_again': '🔄 Вчити знову',
    'get_active': '👨‍🏫 Активні слова',
    'get_learned': '🤖 Вивчені слова у боті',
    'test_eng': '🇬🇧 {} - ? 🇺🇦',
    'test_ukr': '🇺🇦 {} - ? 🇬🇧',
    'gb_flag': '🇬🇧',
    'ua_flag': '🇺🇦',
    'yes': '👍 Так',
    'no': '🙅‍♀️ Ні',
    'wrong': ' ❌',
    'your_dict': 'Ваш словник'
}