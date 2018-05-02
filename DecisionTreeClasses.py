class Node:
    """ base class """
    def __init__(self, name, utility):
        """
        :param name: name of this node
        :param utility: utility of this node
        """
        self.name = name
        self.utility = utility

    def get_expected_utility(self):
        """ abstract method to be overridden in derived classes
        :returns expected utility of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


class ChanceNode(Node):

    def __init__(self, name, future_nodes, probs, utility):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_utility(self):
        """
        :return: expected utility of this chance node
        """
        exp_utility=self.utility  # expected utility initialized with the utility of visiting the current node
        i=0
        for node in self.futureNodes:
            exp_utility+=self.probs[i]*node.get_expected_utility()
            i+=1
        return exp_utility


class TerminalNode(Node):

    def __init__(self, name, utility):
        Node.__init__(self, name, utility)

    def get_expected_utility(self):
        """
        :return: utility of this chance node
        """
        return self.utility


class DecisionNode(Node):

    def __init__(self, name, future_nodes, utility):
        Node.__init__(self, name, utility)
        self.futureNode = future_nodes

    def get_expected_utility(self):
        """ returns the expected utility of future nodes"""
        utility_outcomes=dict()  # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            utility_outcomes[node.name]=node.get_expected_utility()
        return utility_outcomes
