from keras.src.backend.jax.core import switch


from SimpleProblemSolvingAgent import GraphProblem, best_first_graph_search, astar_search, hill_climbing, UndirectedGraph, simulated_annealing






def main():
    var = True
    while var:
        same = True
        while same:
            start = input("Please enter the origin city: ")
            end = input("Please enter the destination city: ")
            if start == end:
                print("The same city can't be both origin and destination. Please try again")
            else:
                same = False

        romania_map = UndirectedGraph(dict(
            Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
            Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
            Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
            Drobeta=dict(Mehadia=75),
            Eforie=dict(Hirsova=86),
            Fagaras=dict(Sibiu=99),
            Hirsova=dict(Urziceni=98),
            Iasi=dict(Vaslui=92, Neamt=87),
            Lugoj=dict(Timisoara=111, Mehadia=70),
            Oradea=dict(Zerind=71, Sibiu=151),
            Pitesti=dict(Rimnicu=97),
            Rimnicu=dict(Sibiu=80),
            Urziceni=dict(Vaslui=142)))
        romania_map.locations = dict(
            Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
            Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
            Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
            Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
            Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
            Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
            Vaslui=(509, 444), Zerind=(108, 531))

        problem = GraphProblem(start, end, romania_map)

        result = best_first_graph_search(problem, lambda n: problem.h(n))

        print("Greedy Best-First Search")
        path = result.path()
        for node in path:
            print(node.state, end=" -> " if node != path[-1] else "\n")

        total_cost = result.path_cost
        print("Total cost:", total_cost)


        result = astar_search(problem, problem.h)

        print("A* Search")
        path = result.path()
        for node in path:
            print(node.state, end=" -> " if node != path[-1] else "\n")


        total_cost = result.path_cost
        print("Total cost:", total_cost)

        print("Hill Climbing Search")

        result = hill_climbing(problem)

        path = result.path()

        for node in path:
            print(node.state, end=" -> " if node != path[-1] else "\n")

        print("Total cost:", total_cost)

        print("Simulated Annealing Search")

        result = simulated_annealing(problem)

        path = result.path()

        for node in path:
            print(node.state, end=" -> " if node != path[-1] else "\n")

        print("Total cost:", total_cost)

        if input("Would you like to find the best path between the other two cities?: ") != "yes":
            print("Thank You for Using Our App")
            var = False



if __name__ == "__main__":
    main()