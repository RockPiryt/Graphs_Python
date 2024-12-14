# Piority queue (Min heap)

# iteriation

class MinHeap:
    def __init__(self,capacity):
        self.storage = [0] * capacity #wszystkie jako 0
        self.capacity = capacity #wielkość kopca
        self.size = 0 #początkowa wielkość kopca


    #--------------------------------------------------------pobieranie indexów rodzica i dzieci
    def getParentIndex(self, index):
        return (index-1)//2 
    
    def getLeftChildIndex(self,index):
        return 2 * index + 1
    
    def getRightChildIndex(self,index):
        return 2 * index + 2
    
    #-------------------------------------------------------sprawdzenie posiadania rodzica/dzieci
    def hasParent(self,index):
        #index rodzica musi być większy lub równy 0 (moze być root)
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self,index):
        #index dziecka musi być mniejszy od aktualnej wielkosci kopca
        return self.getLeftChildIndex(index) < self.size
    
    def hasRighhtChild(self,index):
        #index dziecka musi być mniejszy od aktualnej wielkosci kopca
        return self.getRightChildIndex(index) < self.size
    
    #--------------------------------------------------------zwracanie wartości na konkretnym indexie rodzica, left i right
    def parent(self,index):
        #wyciagam z listy storage aktualna wartość na wybranym indexie
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]
    
    # -------------------------------------------------------pomocnicze funkcje
    def isFull(self):
        return self.size == self.capacity
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
    
    # ------------------------------------------------------iteracyjnie wkładania do stosu
    # wkładanie do stosu 
    def insertHeap(self,element):
        if (self.isFull()):
            raise("Kopiec pełny")
        #wstawienie elementu na ostatnim miejscu kopca
        self.storage[self.size] = element
        self.size += 1
        # przywrócenie własności kopca min
        self.heapifyUp()

    # przywracanie wlasnoci kopca min idać w góre (rodzic ma być mniejszy lub równy dzieciom)
    def heapifyUp(self):
        #index wstawianego ostatnio elementu
        index = self.size-1 
        #jeżeli obecny węzeł ma rodzica i rodzic jest większy od tego noda to zrób swap
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            #kontynuacja w górę swapowania jeżeli potrzeba
            index=self.getParentIndex(index)

     # ------------------------------------------------------iteracyjnie usuwanie ze stosu
    # usuwanie ze stosu 
    def removeFromHeap(self):
        # Gdy kopiec pusty
        if(self.size == 0):
            raise("Kopiec pusty")
        
        # Kopiec zawiera elementy
        # usuwany będzie root zawsze (bo to najmniejszy element w kopcu min)
        removedElement = self.storage[0]  
        # ustanowienie nowego root, nowym root staje się ostatni element w kopcu
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        # Przywracam własność kopca w dół
        self.heapifyDown()

        #zwrot co zostało usuniete
        return removedElement
    
    def heapifyDown(self):
        # zaczynam od root bo z tamtąd był usuwany element
        index = 0
        # muszę sprawdzić które dziecko lewe czy prawe a mniejsza wartość i wtedy zamienić z mniejszym dzieckiem 
        # musi mieć dziecko jak ma być przywracana własność (jak ma prawe to ma też lewe (musi byc kompletnym drzewem binarnym), dlatego sprawdzam tylko czy ma lewe)
        while(self.hasLeftChild(index)):
            #pobieram wartość lewego dziecka - narazie zakładam że lewe jest mniejsze
            smallerChildIndex = self.getLeftChildIndex(index)

            # sprawdzam czy prawe dziecko nie jest mniejsze od lewego
            if (self.hasRighhtChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex= self.getRightChildIndex(index)
            
            #jeśli root mniejszy od dzieci to ok
            if (self.storage[index] < self.storage[smallerChildIndex]):
                break
            else:
                #jeśli jest rodzic większy od dzieci to zamień miejscami
                self.swap(index,smallerChildIndex)
            # przywracanie własności ma iść do końca jeżeli potrzeba, więc ustawiam smallerChildIndex jako index do kolejnego sprawdzenia
            index = smallerChildIndex

if __name__ == "__main__":
    # Tworzymy kopiec - max 10 eleme
    min_heap = MinHeap(10)

    # Wstawiamy elementy do kopca
    min_heap.insertHeap(10)
    min_heap.insertHeap(5)
    min_heap.insertHeap(3)
    min_heap.insertHeap(2)
    min_heap.insertHeap(8)

    print("Kopiec po wstawieniu elementów:", min_heap.storage[:min_heap.size])

    # Usuwamy elementy z kopca i wyświetlamy
    print("Usunięty element:", min_heap.removeFromHeap())
    print("Kopiec po usunięciu elementu:", min_heap.storage[:min_heap.size])

    print("Usunięty element:", min_heap.removeFromHeap())
    print("Kopiec po usunięciu elementu:", min_heap.storage[:min_heap.size])
    





    


    


