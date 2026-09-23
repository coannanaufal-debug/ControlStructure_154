# Program untuk mencetak pola angka sampai n

def print_pattern(n: int) -> None:
    """Mencetak baris dimana baris ke-i berisi angka i yang diulang sebanyak i kali.

    Contoh untuk n=5:
        1
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5
    """
    for i in range(1, n + 1):
        # Create a list with i repeated i times and join with spaces
        line = " ".join([str(i)] * i)
        print(line)

if __name__ == "__main__":
    try:
        n = int(input("Masukkan nilai n: "))
        if n <= 0:
            print("Silakan masukkan bilangan bulat positif.")
        else:
            print_pattern(n)
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")