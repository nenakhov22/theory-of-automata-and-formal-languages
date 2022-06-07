class State:  # Класс состояния
    def __init__(self, name: str = 'def name'):
        self.name = name  # Имя состояния
        self.__transitions: dict[str, list] = {}  # Указания для перехода в другие состояния

    def __repr__(self):  # Метод для удобного внутреннего отображения
        return f'<State {self.name}>'

    def __str__(self):  # Метод для удобного внешнего отображения
        return repr(self)

    def add_transition(self, symbols: str, state):  # Указания для перехода в другие состояния
        for symbol in symbols:
            if symbol not in self.__transitions:
                self.__transitions[symbol] = []
            self.__transitions[symbol].append(state)

    def __call__(self, symbol):  # Вызывается для получения нового состояния
        """
        Если можно перейти по символу в новое состояние, то возвращаем его,
        а если нет, то возвращаем None, что будет означать пустое состояние
        """
        return self.__transitions.get(symbol, [])


class Automata:  # Класс автомата
    def __init__(self, alphabet: str, begin_state: State, final_states: list[State], idx: int):
        """
        Метод, который инициализирует автомат
        """
        self.__alphabet = alphabet  # Алфавит, допускаемый автоматом
        self.__begin_state = begin_state  # Начальное состояние
        self.__current_states: set[State] = set()  # множество текущих состояний автомата
        self.__current_states.add(begin_state)
        self.__final_states = final_states  # Список завершающих состояний
        self.__idx = idx  # Индекс символа, на котором был создан автомат

    @property
    def idx(self):
        return self.__idx

    def __repr__(self):
        return f'<Auto {self.__idx}>'

    def __call__(self, symbol):  # метод, который будет вызываться для каждего символа из цепочки
        if symbol in self.__alphabet:  # Проверяем, есть ли символ в алфавите
            for state in self.__current_states.copy():  # Проходимся по всем текущим состояниям
                _ = state(symbol)  # Получаем состояние из текущего состояния
                self.__current_states.remove(state)  # удаляем проверенное состояние из множества
                for i in _:
                    if i is not None:  # Если не попадаем в пустое состояние,
                        self.__current_states.add(i)  # добавляем его в текущие состояния

            if len(self.__current_states) == 0:  # Если множество текущих состояние пустое,
                return False  # то цепочка уже не может быть правильной, возвращаем False
            for state in self.__current_states:  # Проходимся по всем текущим состояниям после итерации
                if state in self.__final_states:  # Если нашли финальное состояние
                    return True  # Возвращаем True, что будет соответствовать успешному завершению автомата
        return None
