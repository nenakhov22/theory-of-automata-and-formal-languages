from automata import State  # Импортируем нашли состояния (подключаем модуль с ними)
from automata import Automata  # Импортируем нашли автоматы (подключаем модуль с ними)


def main(string):
    # Создаем состояния, которые будут необходимы для работы автомата
    q1 = State('q1')
    q2 = State('q2')
    q3 = State('q3')
    q4 = State('q4')
    q5 = State('q5')
    q6 = State('q6')
    q7 = State('q7')  # Завершающее состояние

    begin_state, final_states = q1, [q7]

    # Настраиваем переходы для каждого состояния
    q1.add_transition('+', q2)
    q2.add_transition('b', q3)
    q3.add_transition('a', q4)
    q3.add_transition('b', q6)
    q4.add_transition('a', q4)
    q4.add_transition('b', q5)
    q5.add_transition('b', q5)
    q5.add_transition('b', q6)
    q5.add_transition('a', q4)
    q6.add_transition('+', q7)

    alphabet = '+abc'  # Наш допустимый алфавит

    # Создаем коллекцию автоматов
    automatas: list[Automata] = []

    found = False  # Отслеживаем, нашли ли мы хотя бы одну нужную нам цепочку цепочку

    # Начинаем обрабатываеть нашу строку
    for idx, symbol in enumerate(string):  # пробегаемся по строке. idx - индекс символа, symbol - сам символ
        automata = Automata(alphabet, begin_state, final_states, idx)  # создаем автомат для каждого символа в строке
        automatas.append(automata)  # Добавляем автомат в коллекцию
        # Проходимся по автоматам из коллекции
        i = 0
        while i < len(automatas):
            automata_answer = automatas[i](symbol)  # Получаем ответ автомата
            if automata_answer is False:  # Если у автомата только пустые состояния
                del automatas[i]
                i -= 1
            elif automata_answer is True:
                found = True
                yield f"{automatas[i].idx + 1}: {string[automatas[i].idx:idx + 1]}"
            i += 1
    if found is not True:  # Если цепочки не были найдены
        yield 'цепочки не найдены'
    return


if __name__ == '__main__':
    string = input("> ")  # Получаем строку, которую будем прогонять через автомат
    for i in main(string):
        print(i)
