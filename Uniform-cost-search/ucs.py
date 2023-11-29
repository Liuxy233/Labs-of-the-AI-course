import heapq
import sys

class PriorityQueue:

    def __init__(self):
        self.heap = [] #空堆
        self.count = 0 #计数器，跟踪队列中的元素

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.
        for index, (p, c, i) in enumerate(self.heap):
            assert type(i) == node, 'i must be node'
            if i.state == item.state:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class node:
    """define node"""

    def __init__(self, state, parent, path_cost, action,):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.action = action


class problem:
    """searching problem"""

    def __init__(self, initial_state, actions):
        self.initial_state = initial_state
        self.actions = actions

    def search_actions(self, state):
        """Search actions for the given state.
        Args:
            state: a string e.g. 'A'

        Returns:
            a list of action string list
            e.g. [['A', 'B', '2'], ['A', 'C', '3']]
        """
        ################################# Your code here ###########################ok
        Actions = []
        for a in self.actions:
            if a[0]==state:
                Actions.append(a)
        return Actions

    def solution(self, node):
        """Find the path & the cost from the beginning to the given node.

        Args:
            node: the node class defined above.

        Returns:
            ['Start', 'A', 'B', ....], Cost
        """
        ################################# Your code here ###########################
        path = []
        cost = 0
        current_node = node
        while current_node.parent != '':
            path.append(current_node.state)
            # cost += current_node.path_cost
            current_node = current_node.parent
        if current_node.parent == '':
            path.append(current_node.state)
        path.reverse()
        return path, node.path_cost


    def transition(self, state, action):
        """Find the next state from the state adopting the given action.

        Args:
            state: 'A'
            action: ['A', 'B', '2']

        Returns:
            string, representing the next state, e.g. 'B'
        """
        ################################# Your code here ###########################ok
        if state == action[0]:
            return action[1]
        else:
            raise Exception

    def goal_test(self, state):
        """Test if the state is goal

        Args:
            state: string, e.g. 'Goal' or 'A'

        Returns:
            a bool (True or False)
        """
        ################################# Your code here ###########################ok
        if state == 'Goal':
            return True
        else: 
            return False

    def step_cost(self, state1, action, state2):
        if (state1 == action[0]) and (state2 == action[1]):
            return int(action[2])
        else:
            print("Step error!")
            sys.exit()

    def child_node(self, node_begin, action):
        """Find the child node from the node adopting the given action

        Args:
            node_begin: the node class defined above.
            action: ['A', 'B', '2']

        Returns:
            a node as defined above
        """
        ################################# Your code here ###########################ok
        # node structure: state, parent, path_cost, action
        if node_begin.state==action[0]:
            new_node = node(action[1],node_begin,node_begin.path_cost+int(action[2]),'')
            return new_node
        else:
            raise Exception


def UCS(problem):
    """Using Uniform Cost Search to find a solution for the problem.

    Args:
        problem: problem class defined above.

    Returns:
        a list of strings representing the path, along with the path cost as an integer.
            e.g. ['A', 'B', '2'], 5
        if the path does not exist, return 'Unreachable'
    """
    node_test = node(problem.initial_state, '', 0, '') # state, parent, path_cost, action
    frontier = PriorityQueue()
    frontier.push(node_test, node_test.path_cost)
    state2node = {node_test.state: node_test}
    explored = []
    ################################# Your code here ###########################
    while not frontier.isEmpty():
        # 从frontier中取出成本最小的节点
        current_node = frontier.pop()
        # print(type(current_node))
        # 检查该节点是否为目标节点
        if problem.goal_test(current_node.state):
            return problem.solution(current_node)

        # 将当前节点加入到已探索的集合中
        explored.append(current_node.state)

        # 遍历该节点的所有后继节点
        for action in problem.search_actions(current_node.state):
            child = problem.child_node(current_node, action)
            if child.state not in explored:
                frontier.update(child, child.path_cost)

    return 'Unreachable', 'Unreachable'


if __name__ == '__main__':
    Actions = []
    while True:
        a = input().strip()
        if a != 'END':
            a = a.split()
            Actions += [a]
        else:
            break
    graph_problem = problem('Start', Actions)
    answer, path_cost = UCS(graph_problem)
    s = "->"
    if answer == 'Unreachable':
        print(answer)
    else:
        path = s.join(answer)
        print(path)
        print(path_cost)
