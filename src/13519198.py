import os

def topological_sort(file_name):
    # 1. Akses File
    file_sample = open(file_name, 'r')
    Lines = file_sample.readlines()

    container = []  
    # ⮚ List untuk isi dari file

    for line in Lines:
        container.append(line.strip().split(','))

    # 2. Reform Bentuk List
    reform_container = []   
    # ⮚ List dengan struktur elemen: [0] = elemen, [1] = list prerequisite | [ [ 'i' , [ 'j' , 'k'] ] , ... ]

    for element in container:    
        body = []
        # ⮚ temp var untuk menyimpan list prerequisite ([1])

        for i in range(len(element)):
            if (i == 0) :
                head = ''.join(character for character in element[i] if character.isalnum() or character=='_')
                # ⮚ temp var untuk menyimpan elemen ([0])
            else:
                body.append(''.join(character for character in element[i] if character.isalnum() or character=='_'))
                        
        reform_container.append([head,body])

    # 3. Seleksi dan Pop Elemen
    sorted_container = []
    # ⮚ List untuk hasil akhir, memiliki struktur elemen berupa himpunan elemen yang dapat dipilih | [ [ 'i' , 'j' ] , [ 'k' ] , ... ]

    while (len(reform_container) != 0):
    # ⮚ Lopp while dilakukan hingga semua elemen pada reform_container terpilih, dengan asumsi bahwa soal selalu dapat diselesaikan

        popped_element = []
        # ⮚ List untuk menyimpan elemen reform_container yang di-pop (untuk menghilangankan elemen yang sudah terdapat dalam solusi)
        element_name = []
        # ⮚ List untuk menyimpan nama elemen yang tidak memiliki prerequisite

        # 3.A. Mencari index elemen yang tidak memiliki prerequisite dan kemudian di-pop
        i = 0

        while (i < len(reform_container)):
            if (len(reform_container[i][1]) == 0):
                element_name.append(reform_container[i][0])
                popped_element.append(reform_container.pop(i))
                i = 0
            else:
                i += 1
               
        sorted_container.append(element_name)

        # 3.B. Menghapus dari list prerequisite elemen lain, elemen yang sudah berada dalam solusi 
        for l in range(len(element_name)):
            for i in range(len(reform_container)):
                for j in range(len(reform_container[i][1])):
                    if (reform_container[i][1][j] == element_name[l]):
                        reform_container[i][1].remove(element_name[l])
                        break
        
    # 4. Print Soal dan Solusi
    print("Persoalan:")
    for line in Lines:
        print(" ■ " + line.strip())

    print("\nSolusi:")
    for i in range(len(sorted_container)):
        print("Semester {} \t: {}".format(i + 1, ', '.join(c for c in sorted_container[i])))

if __name__ == '__main__':
    current_dirr = os.path.dirname(__file__)
    parent_dirr = os.path.split(current_dirr)[0]
    file_path = os.path.join(parent_dirr, 'test')
    
    for file_name in os.scandir(file_path):
        topological_sort(file_name)
        print()