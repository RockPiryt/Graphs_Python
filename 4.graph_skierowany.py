def is_in_set(value, S):
    """Sprawdza, czy dana wartość znajduje się w zbiorze S."""
    return value in S

def create_adjacency_matrix(A, S):
    """Tworzy macierz sąsiedztwa dla grafu skierowanego na podstawie zbiorów A i S."""
    n = len(A)
    
    # Inicjalizuj pustą macierz sąsiedztwa zerami
    adj_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)  # Dodaj 0 do wiersza
        adj_matrix.append(row)  # Dodaj wiersz do macierzy

    # Wypełnij macierz sąsiedztwa
    for i in range(n):
        for j in range(n):
            # Unikaj pętli własnych
            if i != j:
                # Oblicz różnicę y - x
                diff = A[j] - A[i]
                
                # Jeśli różnica znajduje się w zbiorze S, oznacz jako krawędź
                if is_in_set(diff, S):
                    adj_matrix[i][j] = 1

    return adj_matrix

def display_adjacency_matrix(adj_matrix):
    """Wyświetla macierz sąsiedztwa."""
    n = len(adj_matrix)
    # Wyświetl macierz wiersz po wierszu
    for i in range(n):
        for j in range(n):
            if j == n - 1:
                # Jeśli to ostatni element w wierszu, nie dodawaj spacji
                print(adj_matrix[i][j], end="")
            else:
                # Dodaj spację po każdym elemencie oprócz ostatniego
                print(adj_matrix[i][j], end=" ")
        # Przejdź do nowego wiersza po zakończeniu wiersza
        print()

# Wejście: lista liczb A (pierwszy wiersz) oraz lista liczb S (drugi wiersz)
A = [int(x) for x in input("Podaj elementy zbioru A (oddzielone spacją): ").split()]
S = [int(x) for x in input("Podaj elementy zbioru S (oddzielone spacją): ").split()]

# Utwórz macierz sąsiedztwa
adj_matrix = create_adjacency_matrix(A, S)

# Wyświetl macierz sąsiedztwa
print("Macierz sąsiedztwa:")
display_adjacency_matrix(adj_matrix)
