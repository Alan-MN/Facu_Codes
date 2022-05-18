# Aluno: Alan da Mota Nascimento
# Mátricula: 2012130037
import math
import threading


def isprimo(numero: int) -> bool:

    if numero == 0 or numero == 1:
        return False
    if numero == 2:
        return True
    if numero > 2 and numero % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(numero))
    for x in range(3, 1 + max_divisor, 2):
        if numero % x == 0:
            return False
    return True


def mostraprimos(range_inicial: int, range_final: int):
    lista_primos = []
    for i in range(range_inicial, range_final):
        if isprimo(i):
            lista_primos.append(i)
    print(f'lista dos primos achados pela thread responsavel pelo intervalo {range_inicial} - {range_final}:\n{lista_primos}')

def main():
    thread1 = threading.Thread(target=mostraprimos, args=(0, 10000))
    thread2 = threading.Thread(target=mostraprimos, args=(10000, 20000))
    thread3 = threading.Thread(target=mostraprimos, args=(20000, 30000))
    thread4 = threading.Thread(target=mostraprimos, args=(30000, 40000))
    thread5 = threading.Thread(target=mostraprimos, args=(50000, 60000))
    thread6 = threading.Thread(target=mostraprimos, args=(60000, 70000))
    thread7 = threading.Thread(target=mostraprimos, args=(70000, 80000))
    thread8 = threading.Thread(target=mostraprimos, args=(80000, 90000))
    thread9 = threading.Thread(target=mostraprimos, args=(90000, 99999))

    thread1.run()
    thread2.run()
    thread3.run()
    thread4.run()
    thread5.run()
    thread6.run()
    thread7.run()
    thread8.run()
    thread9.run()

if __name__ == "__main__":
    main()