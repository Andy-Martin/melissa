from GreyMatter import tell_time, general_conversations, weather, define_subject, business_news_reader, sleep, play_music


def brain(name, speech_text, city_name, city_code, music_path):
    def check_message(check):
        """
        This functiuon checks if the items in the list (specified in argument)
        are present in the user's input speech.
        """
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(['who', 'are', 'you']):
        general_conversations.who_are_you()

    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()

    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)

    elif check_message(['where', 'born']):
        general_conversations.where_born()

    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()

    elif check_message(['time']):
        tell_time.what_is_time()

    elif check_message(['how', 'weather']) or check_message(['hows', 'weather']) or check_message(['whats', 'weather']):
        weather.weather(city_name, city_code)

    elif check_message(['define']):
        define_subject.define_subject(speech_text)

    elif check_message(['business', 'news']):
        business_news_reader.news_reader()

    elif check_message(['sleep']) or check_message(['shutdown', 'melissa']):
        sleep.go_to_sleep()

    elif check_message(['play', 'music']) or check_message(['music']):
        play_music.play_random(music_path)

    elif check_message(['play']):
        play_music.play_specific_music(speech_text, music_path)

    else:
        general_conversations.undefined()
