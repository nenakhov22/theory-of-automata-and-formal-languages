from collections import deque


class Deque(deque):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(args) != 0:
            self.__last_el = args[0][-1]

    def append(self, x) -> None:
        super(Deque, self).append(x)
        self.__last_el = x

    def pop(self, i: int = ...):
        super(Deque, self).pop()
        if len(self) != 0:
            self.append(super(Deque, self).pop())
        else:
            self.__last_el = None

    def last(self):
        return self.__last_el


class State:
    def __init__(self, name):
        self.transitions = {}
        self.name = name

    def add_transition(self, symbol, in_stack, state, into_stack):
        self.transitions[(symbol, in_stack)] = (state, into_stack)

    def __repr__(self):
        return f'<State({self.name}>'

    def next(self, str, idx, stack: Deque):
        last_sym_in_stack = stack.last()
        gl_ans = []
        if idx < len(str):
            symbol = str[idx]

            ans = self.transitions.get((symbol, last_sym_in_stack))
            if ans is not None:
                n_stack = stack.copy()
                new_stack = ans[1]
                state = ans[0]

                _ = n_stack.pop()
                if new_stack != '\e':
                    for i in new_stack[::-1]:
                        n_stack.append(i)
                gl_ans.append((state, idx + 1, n_stack))
        ans = self.transitions.get(('\e', last_sym_in_stack))
        if ans is not None:
            new_stack = ans[1]
            state = ans[0]

            _ = stack.pop()
            if new_stack != '\e':
                for i in new_stack[::-1]:
                    stack.append(i)

            gl_ans.append((state, idx, stack))
        return gl_ans


q0 = State('q0')
q1 = State('q1')
q2 = State('q2')
f = State('f')

q0.add_transition('0', 'Z', q1, 'CCZ')
q0.add_transition('1', 'Z', q2, 'UUZ')
q0.add_transition('\e', 'Z', f, '\e')

q1.add_transition('0', 'C', q1, 'CCC')
q1.add_transition('1', 'C', q2, 'UUC')
q1.add_transition('\e', 'C', q2, 'C')

q2.add_transition('1', 'U', q2, 'UUU')
q2.add_transition('0', 'U', q2, '\e')
q2.add_transition('\e', 'Z', f, '\e')
q2.add_transition('0', 'C', q2, '\e')
_ = [(q0, 0, Deque('Z'))]

string = input()
while _:
    data = _.pop(0)
    state = data[0]
    idx = data[1]
    stack = data[2]
    ans = state.next(string, idx, stack)
    _.extend(ans)
    if len(_) == 0:
        print(f"Ошибка: в позиции {idx+1} неожидаемый символ {string[idx]}")
        break
    for i in ans:
        if i[0] is not f or i[1] != len(string):
            continue
        print('цепочка принадлежит языку')
        break
    else:
        continue
    break
