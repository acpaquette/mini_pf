from minipf.controllers.default_controller import create_isd

if __name__ == "__main__":
    res = create_isd("/home/acpaquette/Desktop/EN0214547236M.LBL")
    with res as r:
        print(res)
