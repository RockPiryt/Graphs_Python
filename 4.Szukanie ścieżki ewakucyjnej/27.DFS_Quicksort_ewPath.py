import sys
#----------------------------------POBRANIE DANYCH WEJŚCIOWYCH
def read_input():
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

def is_sorted(arr):
    """Sprawdza, czy lista jest posortowana rosnąco."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

import sys

def read_inputStdin():
    """Wczytuje macierz sąsiedztwa oraz pozostałe dane wejściowe zgodnie z formatem."""
    try:
        input_lines = sys.stdin.read().strip().split('\n')

        # Sprawdzenie minimalnej liczby linii
        if len(input_lines) < 4:
            raise ValueError('BŁĄD')

        # Parsowanie pierwszej linii z n, k, m
        inputValues = list(map(int, input_lines[0].split()))
        if len(inputValues) != 3:
            raise ValueError('BŁĄD')
        n, k, m = inputValues

        # sprawdzenie czy n, k, m mają odpowiednie wartości
        if not (2 <= n <= 30 and 1 <= k <= 5 and 1 <= m <= 3):
            raise ValueError('BŁĄD')

        # Sprawdzenie liczby linii dla macierzy sąsiedztwa
        if len(input_lines) < n + 3:
            raise ValueError('BŁĄD')

        # Odczytanie macierzy sąsiedztwa
        adjacency_matrix = []
        for i in range(1, n + 1):
            row = [int(val) for val in input_lines[i].split()] 
            if len(row) != n:
                raise ValueError('BŁĄD')
            # Sprawdzamy, czy wszystkie wartości w wierszu są 0 lub 1
            for val in row:
                if val != 0 and val != 1:
                    raise ValueError('BŁĄD')
            adjacency_matrix.append(row)

        # Odczytanie listy wyjść ewakuacyjnych
        exits = [int(val) for val in input_lines[n + 1].split()] 
        if len(exits) != k:
            raise ValueError('BŁĄD')
        for val in exits:
            if val < 1 or val > n:
                raise ValueError('BŁĄD')
        # Sortowanie listy wyjść
        quick_sort(exits)

        # Odczytanie listy pomieszczeń zagrożonych
        dangers = [int(val) for val in input_lines[n + 2].split()]  
        if len(dangers) != m:
            raise ValueError('BŁĄD')
        for val in dangers:
            if val < 1 or val > n:
                raise ValueError('BŁĄD')
        # Sortowanie listy zagrożeń
        quick_sort(dangers)

        # Sprawdzenie, czy listy są posortowane rosnąco
        if not is_sorted(exits) or not is_sorted(dangers):
            raise ValueError('BŁĄD')

        # Zwracamy wyniki w odpowiedniej kolejności
        return n, k, m, adjacency_matrix, exits, dangers

    except Exception:
        print('BŁĄD')

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

#--------------------------------------IMPELENTACJA QUICKSORTA HOARE - wersja rosnąca i malejąca
def quick_sort(arr):
    """Sortuje listę rosnąco, [1,2,p=3,4,5] elementy mniejsze od pivota w lewej subaarray, elementy większe w prawej subarray"""

    def partition(arr, left, right):
        pivot_value = arr[(left + right) // 2]
        lt = left #lower than pivot
        gt = right #greater than pivot
        i = left #iterator

        while i <= gt:
            #Elementy mniejsze od pivota mają być w  left_subarray[1,2]
            if arr[i] < pivot_value:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            #elementy większe od pivota w w  rigth_subarray[2,1]
            elif arr[i] > pivot_value:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    def quick_sort_recursive(arr, left, right):
        if left >= right: #dopóki wskaźniki się nie miną
            return
        lt, gt = partition(arr, left, right)
        quick_sort_recursive(arr, left, lt - 1) #sortowanie lewej subarray
        quick_sort_recursive(arr, gt + 1, right) #sotowanie prawej subarray

    # Na poczatku cały subarray
    quick_sort_recursive(arr, 0, len(arr) - 1)

def quick_sort_desc(arr):
    """Sortuje listę malejąco, [5,4,p=3,2,1] elementy większe od pivota w lewej subaarray, elementy mniejsze w prawej subarray"""
    def partition(arr, left, right):
        pivot_value = arr[(left + right) // 2]
        lt = left  # Większe niż pivot
        gt = right  # Mniejsze niż pivot
        i = left  # Iterator

        while i <= gt:
            #Elementy większe od pivota mają być w  left_subarray[5,4]
            if arr[i] > pivot_value:  
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            #Elementy mniejsze od pivota mają być w  rigth_subarray[2,1]
            elif arr[i] < pivot_value: 
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    def quick_sort_recursive(arr, left, right):
        if left >= right:  # Dopóki wskaźniki się nie miną
            return
        lt, gt = partition(arr, left, right)
        quick_sort_recursive(arr, left, lt - 1)  # Sortowanie lewej sublisty
        quick_sort_recursive(arr, gt + 1, right)  # Sortowanie prawej sublisty

    # Na początku sortujemy cały zakres listy
    quick_sort_recursive(arr, 0, len(arr) - 1)


#-----------------------------------------GRAF KLASA
class Graph:
    def __init__(self, adjacency_list):
        """Inicjalizacja grafu na podstawie listy sąsiedztwa."""
        self.adjacency_list = adjacency_list
 
    
    def isPath_dfs_list(self, start, exits):
        """Funkcja do znajdowania ścieżki ew. za pomoca dfs"""

        n = len(self.adjacency_list)
        visited = [False] * (n + 1)
        stack = []
        
        parent = [-1] * (n + 1)# Tablica rodziców do śledzenia ścieżki
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
                quick_sort_desc(path) #odwrócenie listy
                return {'found': True, 'path': path}

            # Znajdź sąsiadów wierzchołka v
            neighbors = []
            for neighbor in self.adjacency_list[v - 1][1:]:
                if not visited[neighbor]:
                    neighbors.append(neighbor)
                    parent[neighbor] = v

            if neighbors:
                # Sortowanie sąsiadów
                quick_sort(neighbors)
                # Dodajemy najmniejszego sąsiada na stos
                next_node = neighbors[0]
                visited[next_node] = True
                stack.append(next_node)
            else:
                stack.pop()
        
        # Jeśli nie znaleziono ścieżki
        return {'found': False}
    
    
    def dfsFullList(self, start):
        n = len(self.adjacency_list)
        visited = [False] * (n + 1)
        stack = [] #wykorzystanie stosu do zarządzania ścieżką, którą eksplorujemy w danym momencie.
        order = []#Kolejność odwiedzin wierzchołków (finalna trasa przejścia dfs)

        visited[start] = True
        stack.append(start)
        order.append(start)

        while stack:
            v = stack[-1]  # Ostatni element ze stosu (aktualny wierzchołek)

            # Znajdź sąsiadów wierzchołka 
            neighbors = []
            for item in self.adjacency_list:
                if item[0] == v:  # Znajdujemy wierzchołek `v` w liście sąsiedztwa
                    neighbors = item[1:]  # Sąsiedzi to elementy od 1 dalej
                    break

            # Filtrujemy nieodwiedzone wierzchołki
            unvisited_neighbors = []
            for neighbor in neighbors:
                if not visited[neighbor]:
                    unvisited_neighbors.append(neighbor)

            if unvisited_neighbors:
                quick_sort(unvisited_neighbors)
                # Dodajemy najmniejszego sąsiada na stos
                next_node = unvisited_neighbors[0]
                visited[next_node] = True
                stack.append(next_node)
                order.append(next_node)  # Dodajemy do kolejności odwiedzin
            else:
                stack.pop()  # Usuwamy aktualny wierzchołek ze stosu, gdy brak sąsiadów

        return order
    
# # Wczytaj dane wejściowe
# n, k, m, adj_matrix, exits, dangers = read_input()
n, k, m, adj_matrix, exits, dangers = read_inputStdin()
print(f"dangers:{dangers}")

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


print("")
print("")
print("______________________SKONWERTOWANE WYNIKI______________________")
status = 'BEZPIECZNY'
paths = []
for danger_room in dangers:
    isPathlist = graph.isPath_dfs_list(danger_room, exits)
    if isPathlist['found']:
        paths.append(isPathlist['path'])
    else:
        paths.append(f'BRAK DROGI Z POMIESZCZENIA {danger_room}')
        status = 'NIEBEZPIECZNY'

print(status)
for path in paths:
    if isinstance(path, list):
        print(' '.join(map(str, path)))
    else:
        print(path)

# Jeśli status BEZPIECZNY, wykonujemy pełny DFS z pierwszego zagrożonego pom
if status == 'BEZPIECZNY':
    firstDanger=dangers[0]
    full_dfs= graph.dfsFullList(firstDanger)
    print(' '.join(map(str, full_dfs)))



#-------------------------------------testowe

# # Pełny dfs dla pierwszego zagrożonego pom
# firstDanger=dangers[0]
# order = graph.dfsFullList(firstDanger)
# print(f"pelny porzadek dfs - wykorzystanie listy sąsiedztwa: {order}")
# print(" ".join(map(str, order)))

# #  --------------------------------sprawdzenie ścieżki ucieczki dla każdego zagrozonego pom
# for v in dangers:
#     isPathlist = graph.isPath_dfs_list(v, exits)  # Przeszukiwanie dla list
#     paths=isPathlist["path"]
#     print(" ".join(map(str, paths)))

#     # paths2=isPathlist
#     # print(f"ścieżka ewakuacyjna dla {v}")
#     # print(paths2)

# # # #------------------------------------Pełny DFS dla pierwszego zagrożonego pomieszczenia
# # order, visited = graph.dfs_iter(2)
# # print(f"DFS startuje z pierwszego zagrożonego pom 2: {order}")



