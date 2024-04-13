import BanxicoAPI.Cetes as Cetes
from BanxicoAPI import Udi

if __name__ == "__main__":
    BM_TOKEN= ''
    cetes = Cetes.Cetes(BM_TOKEN)
    print(cetes.getIDSerie())
    print(cetes.get_CETES28_Today())
    print(cetes.get_CETES28_date("2023-04-12"))
    print(cetes.get_CETES28_date_range("2023-04-12", "2023-04-15"))
    print(cetes.get_CETES28_last_value())

    udi = Udi.Udi(BM_TOKEN)
    print(udi.get_UDI_Today())
    print(udi.get_UDI_date("2023-04-12"))
    print(udi.get_UDI_date_range("2023-04-12", "2023-04-15"))
    print(udi.get_UDI_last_value())