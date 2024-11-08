import re


def custom_sort(words):
    # Функція, що визначає порядок сортування слів
    def sort_key(word):
        # Українські літери мають пріоритет
        if re.match(r'[А-ЩЬЮЯЄІЇҐа-щьюяєіїґ]', word[0]):
            return (0, word.lower())
        else:
            return (1, word.lower())

    return sorted(words, key=sort_key)


def main():
    try:
        # Зчитуємо перше речення з файлу
        with open('text.txt', 'r', encoding='utf-8') as file:
            sentence = file.readline().strip()
            print("Зчитане речення:", sentence)

            # Видаляємо пунктуацію і ділимо на слова
            words = re.findall(r'\b\w+\b', sentence)
            print("Слова у реченні:", words)

            # Сортуємо слова з урахуванням українських і англійських слів
            sorted_words = custom_sort(words)
            print("Відсортовані слова:", sorted_words)
            print("Кількість слів:", len(words))

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")


if __name__ == "__main__":
    main()
    

