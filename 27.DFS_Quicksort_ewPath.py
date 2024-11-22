
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
        neighbors = [i + 1]  # Start each list with the current vertex (1-indexed)
        for j in range(num_vertices):
            if matrix[i][j] == 1:
                neighbors.append(j + 1)  # Add the neighbor (1-indexed)
        adjacency_list.append(neighbors)
    
    return adjacency_list

#--------------------------------------IMPELENTACJA QUICKSORTA HOARE
def quick_sort_desc(array):
    def swap(A, i1, i2):
        A[i1], A[i2] = A[i2], A[i1]  

    def partition(array, lo, hi):
        mid_point = (lo + hi) // 2
        pivot = array[mid_point]
        i = lo - 1
        j = hi + 1  

        while True:
            # Przesuń i w prawo, dopóki nie znajdziesz wartości <= pivot
            while True:
                i += 1
                if array[i] <= pivot:
                    break
            # Przesuń j w lewo, dopóki nie znajdziesz wartości >= pivot
            while True:
                j -= 1
                if array[j] >= pivot:
                    break
            # Jeżeli wskaźniki się miną, zwróć indeks podziału
            if j <= i:
                return j
            swap(array, i, j)

    def recursive_quicksort(array, lo, hi):
        if lo >= hi:
            return 
        pivot_index = partition(array, lo, hi)  # Znajdź pivot i podziel tablicę
        recursive_quicksort(array, lo, pivot_index)  # Sortuj lewą część
        recursive_quicksort(array, pivot_index + 1, hi)  # Sortuj prawą część

    recursive_quicksort(array, 0, len(array) - 1) 
    
    return array


#-----------------------------------------GRAF KLASA
class Graph:
    def __init__(self, adjacency_list):
        """Inicjalizacja grafu na podstawie listy sąsiedztwa."""
        self.adjacency_list = adjacency_list

    
    def getNeighbours(self, vertex_index):
        """Zwraca sąsiadów wybranego wierzchołka na podstawie numeru wprowadzonego przez użytkownika."""
        try:
            
            # Pobranie listy sąsiadów
            # neighbors = self.adjacency_list[vertex_index][1:]
            neighbors = self.adjacency_list[vertex_index]
            
            # # Wyświetlenie sąsiadów (jeśli istnieją)
            # if neighbors:
            #     print(f"Sąsiedzi wierzchołka {vertex_index + 1} to    -----: {', '.join(map(str, neighbors))}")
            # else:
            #     print(f"Wierzchołek {vertex_index + 1} nie ma sąsiadów.")
            
            return neighbors

        except IndexError:
            print("BŁĄD: Nie można znaleźć sąsiadów dla podanego wierzchołka.")
            

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
    
    
    def dfs_iter(self, start):
        """Przeszukiwanie grafu w głąb (DFS) w iteracyjnej wersji."""

        n = len(self.adjacency_list)
        visited = [False] * n  # Wszystkie wierzchołki oznaczamy jako nieodwiedzone
        #print(f"visited: {visited}")
        stack = [start]  # Stos zaczyna się od wierzchołka startowego (0-based)
        #print(f"start:{start}")
        order = []  # Kolejność odwiedzania wierzchołków

        print("\nDFS:")

        while stack:
            # Pobieramy wierzchołek ze stosu
            node = stack.pop()
            #print(f"aktualny analizowany wierzcholek: {node+1}")#podpicie aby w printowaniu był prawidłowy numer wierzchołka
            node_neighbors = self.getNeighbours(node)
            #print(f"sasiedzi analizowanego wierzcholka: {node_neighbors}")
            if not visited[node]:  # Jeśli wierzchołek jeszcze nie został odwiedzony
                visited[node] = True  # Oznacz jako odwiedzony
                #print(f"visited: {visited}")
                order.append(node + 1)  # Dodajemy do porządku, ale jako 1-based
                #print(node + 1, end=" ")  # Wypisujemy jako 1-based
                #print(f"order: {order}")

                # Dodaj sąsiadów do stosu w odwrotnej kolejności
                reversed_neighbors = quick_sort_desc(node_neighbors)
                #print(f"reversed_neighbors: {reversed_neighbors}")
                updated_neighbors = [neighbor - 1 for neighbor in reversed_neighbors]
                #print(f"updated_neighbors: {updated_neighbors}")
                for neighbor in updated_neighbors:
                    #print(f"neighbor: {neighbor}")
                    neighbor_index = neighbor   # Przechodzimy na 0-based
                    if not visited[neighbor_index]:
                        stack.append(neighbor_index)

        return order, visited
    
    # Implementacja DFS dla znalezienia ścieżki do wyjścia
    def isPath_dfs_list(self, start, exits):
        # Liczba wierzchołków w grafie
        n = len(self.adjacency_list)
        
        # Tablica odwiedzonych wierzchołków
        visited = [False] * (n + 1)
        stack = []
        
        # Tablica rodziców do śledzenia ścieżki
        parent = [-1] * (n + 1)
        stack.append(start)
        visited[start] = True

        # Przeszukiwanie w głąb
        while stack:
            v = stack[-1]

            # Jeśli znaleziono wyjście
            if v in exits:
                path = []
                current = v
                while current != -1:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return {'found': True, 'path': path}

            # Znajdź sąsiadów wierzchołka v
            neighbors = []
            for neighbor in self.adjacency_list[v - 1][1:]:
                if not visited[neighbor]:
                    neighbors.append(neighbor)
                    parent[neighbor] = v

            if neighbors:
                # Sortowanie sąsiadów
                quick_sort(neighbors, 0, len(neighbors) - 1)
                # Dodajemy najmniejszego sąsiada na stos
                next_node = neighbors[0]
                visited[next_node] = True
                stack.append(next_node)
            else:
                stack.pop()
        
        # Jeśli nie znaleziono ścieżki
        return {'found': False}

def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot_index = (left + right) // 2
    pivot_value = arr[pivot_index]
    lt, gt = partition(arr, left, right, pivot_value)
    quick_sort(arr, left, lt - 1)
    quick_sort(arr, gt + 1, right)

def partition(arr, left, right, pivot_value):
    lt = left
    i = left
    gt = right

    while i <= gt:
        if arr[i] < pivot_value:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot_value:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt


# def isPath_dfs_list(adjacency_list, start, exits):
#     # Liczba wierzchołków w grafie
#     n = len(adjacency_list)
    
#     # Tablica odwiedzonych wierzchołków
#     visited = [False] * (n + 1)
#     stack = []
    
#     # Tablica rodziców do śledzenia ścieżki
#     parent = [-1] * (n + 1)
#     stack.append(start)
#     visited[start] = True

#     # Przeszukiwanie w głąb
#     while stack:
#         v = stack[-1]

#         # Jeśli znaleziono wyjście
#         if v in exits:
#             path = []
#             current = v
#             while current != -1:
#                 path.append(current)
#                 current = parent[current]
#             path.reverse()
#             return {'found': True, 'path': path}

#         # Znajdź sąsiadów wierzchołka v
#         neighbors = []
#         for neighbor in adjacency_list[v - 1][1:]:
#             if not visited[neighbor]:
#                 neighbors.append(neighbor)
#                 parent[neighbor] = v

#         if neighbors:
#             # Sortowanie sąsiadów
#             quick_sort(neighbors, 0, len(neighbors) - 1)
#             # Dodajemy najmniejszego sąsiada na stos
#             next_node = neighbors[0]
#             visited[next_node] = True
#             stack.append(next_node)
#         else:
#             stack.pop()
    
#     # Jeśli nie znaleziono ścieżki
#     return {'found': False}

 

# # Wczytaj dane wejściowe
n, k, m, adj_matrix, exits, dangers = read_adjacency_matrix()
print(f"dangers:{dangers}")
update_dangers= [v - 1 for v in dangers] #zmiejszenie indexowania o 1, zeby dla wierzchołka 2 był index 1
print(f"update_dangers:{update_dangers}")



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
graph_adj_list = adjacency_matrix_to_list(adj_matrix)
print("przekonwertowana lista", graph_adj_list)

graph = Graph(graph_adj_list)



#  --------------------------------sprawdzenie ścieżki ucieczki dla każdego zagrozonego pom
for v in dangers:
    isPathlist = graph.isPath_dfs_list(v, exits)  # Przeszukiwanie dla listy
    paths=isPathlist["path"]
    print(" ".join(map(str, paths)))



# # ---------------------------------------------------------MOJE WYJŚCIE

# start_neighbors = graph.getNeighbours(1)
# print("sasiedzi pkt startowego",start_neighbors)
# reversed_start_neighbors = quick_sort_desc(start_neighbors)
# print("odroceni sasiedzi pkt startowego",reversed_start_neighbors)
# #------------------------sprawdzenie sąsiadów wierzchołka na podstawie adjacency list------- Działa
# for v in update_dangers:
#     neighbors=graph.getNeighbours(v)
#     print(f"Sasiedzi {v+1} to : {neighbors} ")

#     #sprawdzenie ----------------------sortowania Quicksort malejąca dla sąsiadów wybranego vertexa -działa
#     sorted_des_neighbors=quick_sort_desc(neighbors)
#     print(f"posortowani malejąco sasiedzi wierzcholka{v+1} to: {sorted_des_neighbors}")

#     # # # Wykonanie DFS dla każdego wierzchołka
#     # order, visited = graph.dfs_iter(v)
#     # print(f"Odwiedzeni kolejność dla {v+1}: {order}")

# # #------------------------------------Pełny DFS dla pierwszego zagrożonego pomieszczenia
# # first_danger=update_dangers[0]
# # order, visited = graph.dfs_iter(first_danger)
# # print(f"DFS startuje z pierwszego zagrożonego pom {first_danger+1}: {order}")
    
# # # --------------------------------sprawdzenie ścieżki ucieczki dla pojedynczego pom - nie działa
# # start=dangers[0] # 3
# # print(f"pom zagrożone nr {start}")
# # end=exits[0]#1
# # # print(f"wyjscie ewakuacyjne w node {end}")

# start=2
# end=1
# graph.isPathBetweenVertex(start, end)
# # can_exit, path  = graph.isPathBetweenVertex(start, end)

# # print(f"Czy moze uciec? {can_exit}")
# # print(f"Sciezka ewakuacji:{path}")







