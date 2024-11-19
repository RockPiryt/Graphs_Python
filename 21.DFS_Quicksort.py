
#----------------------------------POBRANIE DANYCH WEJŚCIOWYCH
def read_adjacency_matrix():
    """Wczytuje macierz sąsiedztwa oraz pozostałe dane wejściowe zgodnie z formatem."""

    # Wczytaj pierwszą linię z trzema liczbami: n (liczba pomieszczeń), k (liczba wyjść ewakuacyjnych), m (liczba zagrożonych pomieszczeń)
    n, k, m = map(int, input().split())

    # Wczytaj macierz sąsiedztwa
    adj_matrix = []
    for i in range(n):
        row = list(map(int, input().split()))  # Wczytanie kolejnej linii jako listy liczb całkowitych
        adj_matrix.append(row)

    # Wczytaj numery wyjść ewakuacyjnych (k liczb rosnąco)
    exits = list(map(int, input().split()))

    # Wczytaj numery zagrożonych pomieszczeń (m liczb rosnąco)
    dangers = list(map(int, input().split()))

    # Zwróć wszystkie dane
    return n, k, m, adj_matrix, exits, dangers

#----------------------------------------------------ZMIANA MACIERZY NA LISTĘ SĄSIEDZTWA
def adjacency_matrix_to_list(matrix):
    adjacency_list = []
    num_vertices = len(matrix)

    for i in range(num_vertices):
        neighbors = []
        for j in range(num_vertices):
            if matrix[i][j] == 1:
                neighbors.append(j + 1)  # +1 to convert from 0-indexed to 1-indexed
        neighbors.sort()  # Sort the list of neighbors
        adjacency_list.append(neighbors)
    
    return adjacency_list

def print_adjacency_list(adjacency_list):
    for index in range(len(adjacency_list)):
        # Create a string of neighbors directly from the list
        neighbors_str = ' '.join(str(neighbor) for neighbor in adjacency_list[index])
        print(f"{index + 1} {neighbors_str}")

#--------------------------------------IMPELENTACJA QUICKSORTA
def swap(array, x, y):
    """Zamiana dwóch elementów w tablicy."""
    array[x], array[y] = array[y], array[x]

def quicksort(array):
    """Główna funkcja QuickSort jako wrapper."""
    quicksort_recursion(array, 0, len(array) - 1)

def quicksort_recursion(array, low, high):
    """Rekurencyjna funkcja sortująca."""
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_recursion(array, low, pivot_index - 1)  # Sortowanie przed pivotem
        quicksort_recursion(array, pivot_index + 1, high)  # Sortowanie za pivotem

def partition(array, low, high):
    """Funkcja dzieląca tablicę na podtablice na podstawie pivotu."""
    pivot_value = array[high]  # Wybieramy ostatni element jako pivot
    i = low
    for j in range(low, high):
        if array[j] <= pivot_value:  # Jeśli bieżący element jest <= pivot
            swap(array, i, j)  # Zamiana elementów
            i += 1
    swap(array, i, high)  # Zamiana pivotu na właściwą pozycję
    return i



#-----------------------------------------GRAF KLASAS
class Graph:
    def __init__(self, adjacency_list):
        """Inicjalizacja grafu na podstawie listy sąsiedztwa."""
        self.adjacency_list = adjacency_list

    
    def getNeighbours(self, vertex_index):
        """Zwraca sąsiadów wybranego wierzchołka na podstawie numeru wprowadzonego przez użytkownika."""
        try:
            
            # Pobranie listy sąsiadów
            neighbors = self.adjacency_list[vertex_index][1:]
            
            # # Wyświetlenie sąsiadów (jeśli istnieją)
            # if neighbors:
            #     print(f"Sąsiedzi wierzchołka {vertex_index + 1} to    -----: {', '.join(map(str, neighbors))}")
            # else:
            #     print(f"Wierzchołek {vertex_index + 1} nie ma sąsiadów.")
            
            return neighbors

        except IndexError:
            print("BŁĄD: Nie można znaleźć sąsiadów dla podanego wierzchołka.")
            exit(1)

    def vertex_count(self):
        """Zwraca liczbę wierzchołków w grafie."""
        return len(self.adjacency_list)
    
    def count_edges(self):
        """Zlicza liczbę krawędzi w grafie."""
        edge_count = 0  
    
        for neighbors in self.adjacency_list:
            edge_count += len(neighbors) - 1  # Odejmujemy 1, aby pominąć numer wierzchołka
        
        return edge_count // 2  
    
    def get_degrees(self):
        '''Funkcja zwracająca ciąg stopni wierzchołków'''
        degrees = []
        for neighbors in self.adjacency_list:
            degrees.append(len(neighbors) - 1)  # Odejmujemy 1, aby pominąć numer wierzchołka
        return degrees
    
    def dfs_iterStepik(self, start):
        """Przeszukiwanie grafu w głąb (DFS) w iteracyjnej wersji."""

        n = len(self.adjacency_list)
        visited = [False] * n  # Wszystkie wierzchołki oznaczamy jako nieodwiedzone
        stack = [start]  # Stos zaczyna się od wierzchołka startowego (0-based)
        order = []  # Kolejność odwiedzania wierzchołków

        while stack:
            # Pobieramy wierzchołek ze stosu
            node = stack.pop()
            node_neighbors = self.getNeighbours(node)
            if not visited[node]:  # Jeśli wierzchołek jeszcze nie został odwiedzony
                visited[node] = True  # Oznacz jako odwiedzony
                order.append(node + 1)  # Dodajemy do porządku, ale jako 1-based

                # Dodaj sąsiadów do stosu w odwrotnej kolejności
                reversed_neighbors = sorted(node_neighbors, reverse=True)
                updated_neighbors = [neighbor - 1 for neighbor in reversed_neighbors] #odjęcie od każdego 1, zeby indexy sie zgadzaly
                for neighbor in updated_neighbors:
                    if not visited[neighbor]:
                        stack.append(neighbor)

        return order, visited
    def dfs_iter(self, start):
        """Przeszukiwanie grafu w głąb (DFS) w iteracyjnej wersji."""

        n = len(self.adjacency_list)
        visited = [False] * n  # Wszystkie wierzchołki oznaczamy jako nieodwiedzone
        print(f"visited: {visited}")
        stack = [start]  # Stos zaczyna się od wierzchołka startowego (0-based)
        print(f"start:{start}")
        order = []  # Kolejność odwiedzania wierzchołków

        print("\nDFS:")

        while stack:
            # Pobieramy wierzchołek ze stosu
            node = stack.pop()
            print(f"aktualny analizowany wierzcholek: {node}")
            node_neighbors = self.getNeighbours(node)
            print(f"sasiedzi analizowanego wierzcholka: {node_neighbors}")
            if not visited[node]:  # Jeśli wierzchołek jeszcze nie został odwiedzony
                visited[node] = True  # Oznacz jako odwiedzony
                print(f"visited: {visited}")
                order.append(node + 1)  # Dodajemy do porządku, ale jako 1-based
                print(node + 1, end=" ")  # Wypisujemy jako 1-based
                print(f"order: {order}")

                # Dodaj sąsiadów do stosu w odwrotnej kolejności
                reversed_neighbors = quicksort(node_neighbors)
                print(f"reversed_neighbors: {reversed_neighbors}")
                updated_neighbors = [neighbor - 1 for neighbor in reversed_neighbors]
                print(f"updated_neighbors: {updated_neighbors}")
                for neighbor in updated_neighbors:
                    print(f"neighbor: {neighbor}")
                    neighbor_index = neighbor   # Przechodzimy na 0-based
                    if not visited[neighbor_index]:
                        stack.append(neighbor_index)

        return order, visited
    
# # Wczytaj dane wejściowe
n, k, m, adj_matrix, exits, dangers = read_adjacency_matrix()

# Wypisz wczytane dane dla sprawdzenia
print("Liczba pomieszczeń:", n)
print("Liczba wyjść ewakuacyjnych:", k)
print("Liczba zagrożonych pomieszczeń:", m)

print("Pobrana Macierz sąsiedztwa:")
for row in adj_matrix:
    print(row)

print("Wyjścia ewakuacyjne:", exits)
print("Zagrożone pomieszczenia:", dangers)

# Convert the adjacency matrix to an adjacency list
adjacency_list = adjacency_matrix_to_list(adj_matrix)

# Print the adjacency list
print("Lista sasiedztwa:")
print_adjacency_list(adjacency_list)


# graph, start_vertex, error_flag = read_graph_and_vertex()

# if error_flag:
#     print(f"BŁĄD")
# else:
#     graph = Graph(graph)
#     # Wykonanie DFS
#     order, visited = graph.dfs_iter(start_vertex)

#     # Sprawdzenie spójności grafu — jeśli po wykonaniu DFS wszystkie wierzchołki są odwiedzone, graf jest spójny.
#     is_connected = True  

#     for v in visited:
#         if not v:  # Jeśli false na liście visited
#             is_connected = False
#             break  

#     if is_connected:
#         print("Porządek DFS:", " ".join(map(str, order)))
#         print("Graf jest spójny")
#     else:
#         print("Graf jest niespójny")

