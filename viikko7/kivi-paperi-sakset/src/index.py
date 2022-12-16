from luo_peli import luo_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input("Anna vastaus: ")
        syotteet = ['a', 'b', 'c']
        if vastaus in syotteet:
            luo_peli(vastaus).pelaa()
        else:
            break

if __name__ == "__main__":
    main()
