import DecisionTreeClasses as Cls

# create the terminal nodes
T1 = Cls.TerminalNode('T1', 0.0)
T2 = Cls.TerminalNode('T2', 1.0)
T3 = Cls.TerminalNode('T3', 0.0)
T4 = Cls.TerminalNode('T4', 1.0)
T5 = Cls.TerminalNode('T5', 0.0)
T6 = Cls.TerminalNode('T6', 1.0)
T7 = Cls.TerminalNode('T7', 0.0)
T8 = Cls.TerminalNode('T8', 1.0)
T9 = Cls.TerminalNode('T9', 0.0)
T10 = Cls.TerminalNode('T10', 1.0)
T11 = Cls.TerminalNode('T11', 0.0)
T12 = Cls.TerminalNode('T12', 1.0)
T13 = Cls.TerminalNode('T13', 0.0)
T14 = Cls.TerminalNode('T14', 1.0)
T15 = Cls.TerminalNode('T15', 0.0)
T16 = Cls.TerminalNode('T16', 1.0)
T17 = Cls.TerminalNode('T17', 0.0)
T18 = Cls.TerminalNode('T18', 1.0)

# create C4
C4 = Cls.ChanceNode('C4', [T1, T2], [0.2184, 0.7816], 0)
# create C5
C5 = Cls.ChanceNode('C5', [T3, T4], [0.1586, 0.8414], 0)
# create C6
C6 = Cls.ChanceNode('C6', [T5, T6], [0.0900, 0.9100], 0)
# create C7
C7 = Cls.ChanceNode('C7', [T7, T8], [0.3219, 0.6781], 0)
# create C8
C8 = Cls.ChanceNode('C8', [T9, T10], [0.2326, 0.7674], 0)
# create C9
C9 = Cls.ChanceNode('C9', [T11, T12], [0.1300, 0.8700], 0)
# create C10
C10 = Cls.ChanceNode('C10', [T13, T14], [0.9883, 0.0117], 0)
# create C11
C11 = Cls.ChanceNode('C11', [T15, T16], [0.5282, 0.4718], 0)
# create C12
C12 = Cls.ChanceNode('C12', [T17, T18], [0.0, 1.0], 0)
# create C1
C1 = Cls.ChanceNode('C1', [C4, C5, C6], [0.4582, 0.1638, 0.3780], 0)
# create C2
C2 = Cls.ChanceNode('C2', [C7, C8, C9], [0.4582, 0.1638, 0.3780], 0)
# create C3
C3 = Cls.ChanceNode('C3', [C10, C11, C12], [0.4582, 0.1638, 0.3780], 0)

# create D1
D1 = Cls.DecisionNode('D1', [C1, C2, C3], 0)

# print the expect cost of D1
print(D1.get_expected_utility())
